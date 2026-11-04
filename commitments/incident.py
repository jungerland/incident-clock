"""Incident skill: tell it what happened, and it works out who to notify and by when.

The model proposes; code decides. The model reads each contract and proposes a
decision, the clock start, and the wording behind them. Code works out which
batches the vendor held, checks every quote and recipient against the contract,
takes the time limit from the commitment ledger, and does the deadline arithmetic.
Anything that fails a check goes to a person. Nothing is sent. Never reads the
answer key or the target summary.

Usage:
  python -m commitments.incident                   # Labelforge incident, latest v2 ledger
  python -m commitments.incident --runs 3
  python -m commitments.incident --transfer-log <csv> --only AHS

Output: runs/incidents/<timestamp>-<prompt>/run-NN.json, summary.md, drafts/
"""

import argparse
import csv
import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import anthropic

from commitments.checks import add_duration, contacts, duration_value
from commitments.quotes import is_verbatim, normalize

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "fixtures" / "exampleco"
INCIDENT_DIR = FIXTURES / "incident-labelforge"
PROMPTS = Path(__file__).parent / "prompts"
RUNS = ROOT / "runs"
MODEL = "claude-opus-5-5"
EFFORT = "high"
MAX_TOKENS = 64000
PT = ZoneInfo("America/Los_Angeles")
DEMO_NOW = "2026-11-02T16:00"
TABLE_ACTIONS = 4   # the rest go under the table, so a reviewer can skim it

CONTRACT_FILES = {
    "ANB": "awesome-national-bank-security-addendum.md",
    "ARG": "astounding-retail-group-xyzwire-dpa.md",
    "AHS": "amazing-health-system-baa.md",
}
CLOCK_VENDOR = "vendor_found_it"
CLOCK_TOLD = "exampleco_told"

FACTS_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "vendor": {"type": "string"},
        "vendor_found_at": {"type": "string"},
        "exampleco_told_at": {"type": "string"},
        "known": {"type": "string"},
        "not_yet_known": {"type": "string"},
    },
    "required": ["title", "vendor", "vendor_found_at", "exampleco_told_at", "known", "not_yet_known"],
    "additionalProperties": False,
}

CITATION = {
    "type": "object",
    "properties": {
        "section": {"type": "string"},
        "quote": {"type": "string"},
        "point": {"type": "string"},
    },
    "required": ["section", "quote", "point"],
    "additionalProperties": False,
}

ASSESSMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "notify": {"type": "string", "enum": ["yes", "no"]},
        "why": {"type": "string"},
        "evidence": {"type": "array", "items": CITATION},
        "notice_section": {"type": ["string", "null"]},
        "clock_start": {"anyOf": [{"type": "string", "enum": [CLOCK_VENDOR, CLOCK_TOLD]}, {"type": "null"}]},
        "clock_reason": {"type": ["string", "null"]},
        "also_do": {"type": "array", "items": CITATION},
        "legal_flags": {"type": "array", "items": CITATION},
        "vendor_report_section": {"type": ["string", "null"]},
        "open_questions": {"type": "array", "items": {"type": "string"}},
        "notice_draft": {
            "anyOf": [
                {
                    "type": "object",
                    "properties": {
                        "to": {"type": "array", "items": {"type": "string"}},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": ["to", "subject", "body"],
                    "additionalProperties": False,
                },
                {"type": "null"},
            ]
        },
    },
    "required": ["notify", "why", "evidence", "notice_section", "clock_start", "clock_reason", "also_do",
                 "legal_flags", "vendor_report_section", "open_questions", "notice_draft"],
    "additionalProperties": False,
}

FORMAT_RULES = f"""Output rules:
- `why` is one or two plain sentences a security lead can read at a glance.
- Every `quote` is copied word for word from the contract, from one clause, and `section` is that clause's number as written ("2.2", "D.2", "Schedule 2"). You may drop Markdown markup. `point` says in a few words what the quote shows or what to do.
- `evidence` is the wording behind the decision, including the definitions it rests on.
- `also_do` is what the contract requires now, one action per item, with `point` as the action.
- `legal_flags` is for legal to look at. Quote the term at issue.
- `notice_section` is the section of the ledger commitment that sets the time limit for notifying this customer, or null if no notice is owed. Do not state the deadline yourself: code calculates it.
- `clock_start` is what starts that limit under this contract: `{CLOCK_VENDOR}` if the vendor's own discovery of the incident starts it, `{CLOCK_TOLD}` if the clock starts only when ExampleCo or the contract party learned of it. Null if no notice is owed. `clock_reason` says why, in one sentence.
- `vendor_report_section` is the section of a ledger commitment limiting how quickly a vendor must report incidents to ExampleCo, or null if this contract has none.
- `open_questions` is what a person still has to find out or decide.
- `notice_draft` is null if no notice is owed. In `to`, list only email addresses and phone numbers, exactly as the contract gives them. Write `body` in plain text."""


# --- code decides: exposure, citations, recipients, deadlines ---------------

def load_batches(path: Path) -> list[dict]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def was_held(batch: dict, on: date) -> bool:
    """A batch counts if the vendor still held it on the day it found the incident."""
    return date.fromisoformat(batch["held_at_labelforge_until"].split()[0]) >= on


def exposure(batches: list[dict], on: date) -> dict[str, dict]:
    grouped: dict[str, dict] = {}
    for b in batches:
        group = grouped.setdefault(b["contract"], {"customer": b["exampleco_customer"], "held": [], "gone": []})
        group["held" if was_held(b, on) else "gone"].append(b)
    return grouped


def clause_number(quote: str, text: str) -> str | None:
    """Number of the numbered clause a quote sits in. None for tables and headings."""
    q = normalize(quote)
    for line in text.splitlines():
        if q in normalize(line):
            m = re.match(r"((?:[A-Z]\.)?\d+(?:\.\d+)*)\s", normalize(line))
            return m.group(1) if m else None
    return None


def bare_section(section: str) -> str:
    return section.lower().replace("§", "").replace("section", "").split(",")[-1].strip().rstrip(".")


def citation_ok(item: dict, text: str) -> bool:
    if not is_verbatim(item["quote"], text):
        return False
    number = clause_number(item["quote"], text)
    return number is None or bare_section(item["section"]).startswith(number.lower())


def split_citations(items: list[dict], text: str) -> tuple[list[dict], list[dict]]:
    good = [i for i in items if citation_ok(i, text)]
    return good, [i for i in items if i not in good]


def ledger_items(ledger: list[dict], section: str | None) -> list[dict]:
    if not section:
        return []
    wanted = bare_section(section)
    return [i for i in ledger if bare_section(i["section"]) == wanted]


def decide(raw: dict, facts: dict, ledger: list[dict], text: str, customer: str, contract: str,
           held: list[dict], gone: list[dict]) -> dict:
    """Turn the model's proposal into a row. Code sets the deadline and the status."""
    evidence, bad_evidence = split_citations(raw["evidence"], text)
    also_do, bad_also = split_citations(raw["also_do"], text)
    flags, bad_flags = split_citations(raw["legal_flags"], text)
    review = []
    if bad_evidence or bad_also or bad_flags:
        review.append(f"{len(bad_evidence + bad_also + bad_flags)} citation(s) failed the wording check and were dropped")
    if not evidence:
        review.append("no verified contract wording behind the decision")

    deadline = limit = None
    draft = raw["notice_draft"]
    if raw["notify"] == "yes":
        operative = [i for i in ledger_items(ledger, raw["notice_section"]) if i.get("operative_notice_deadline")]
        start = {CLOCK_VENDOR: facts["vendor_found_at"], CLOCK_TOLD: facts["exampleco_told_at"]}.get(raw["clock_start"])
        if not operative:
            review.append(f"section {raw['notice_section']} is not a governing notice term in the ledger")
        elif not start:
            review.append("no clock start proposed")
        else:
            limit = operative[0]["deadline"]["duration"]
            computed = add_duration(datetime.fromisoformat(start), limit)
            deadline = computed.isoformat() if computed else None
            if not computed:
                review.append(f"cannot read the duration {limit}")
        if not draft:
            review.append("notice owed but no draft")
        else:
            allowed = contacts(text)
            outside = [t for t in draft["to"] if not contacts(t) or not contacts(t) <= allowed]
            if outside:
                review.append(f"recipient not in the contract: {', '.join(outside)}")

    recurring = [{"section": i["section"], "every": i["deadline"]["duration"], "summary": i["summary"]}
                 for c in also_do for i in ledger_items(ledger, c["section"])
                 if i.get("deadline") and i["deadline"]["direction"] == "recurring"]
    recurring = list({r["section"] + r["every"]: r for r in recurring}.values())

    if review:
        status = "Needs a person: " + "; ".join(review)
    elif raw["notify"] == "no":
        status = "Logged with reason; counsel to confirm"
    elif flags:
        status = "Draft ready for counsel; flagged for legal"
    else:
        status = "Draft ready for counsel"

    return {
        "contract": contract,
        "customer": customer,
        "notify": raw["notify"],
        "why": raw["why"],
        "evidence": evidence,
        "notice_section": raw["notice_section"],
        "clock_start": raw["clock_start"],
        "clock_reason": raw["clock_reason"],
        "time_limit": limit,
        "deadline": deadline,
        "also_do": also_do,
        "recurring": recurring,
        "legal_flags": flags,
        "open_questions": raw["open_questions"],
        "notice_draft": draft,
        "vendor_report_section": raw["vendor_report_section"],
        "status": status,
        "needs_person": bool(review),
        "dropped_citations": bad_evidence + bad_also + bad_flags,
        "batches_held": [b["batch_id"] for b in held],
        "batches_gone": [b["batch_id"] for b in gone],
        "methods_held": sorted({b["deidentification_method"] for b in held}),
    }


def nothing_held(contract: str, customer: str, gone: list[dict]) -> dict:
    return {
        "contract": contract, "customer": customer, "notify": "no",
        "why": "The vendor no longer held any of this customer's data when the incident happened.",
        "evidence": [], "notice_section": None, "clock_start": None, "clock_reason": None, "time_limit": None,
        "deadline": None, "also_do": [], "recurring": [], "legal_flags": [], "open_questions": [],
        "notice_draft": None, "vendor_report_section": None,
        "status": "Logged with reason; counsel to confirm", "needs_person": False, "dropped_citations": [],
        "batches_held": [], "batches_gone": [b["batch_id"] for b in gone], "methods_held": [],
    }


def vendor_report_finding(rows: list[dict], facts: dict, ledgers: dict[str, list[dict]]) -> dict | None:
    """Did the vendor report slower than a contract says subcontractors must?"""
    found = datetime.fromisoformat(facts["vendor_found_at"])
    told = datetime.fromisoformat(facts["exampleco_told_at"])
    elapsed = (told - found).total_seconds() / 3600
    for row in rows:
        for item in ledger_items(ledgers.get(row["contract"], []), row["vendor_report_section"]):
            value = duration_value((item.get("deadline") or {}).get("duration"))
            if value and value[0] == "hours" and elapsed > value[1]:
                return {"contract": row["contract"], "customer": row["customer"], "section": item["section"],
                        "elapsed_hours": elapsed, "limit_hours": value[1], "vendor": facts["vendor"]}
    return None


# --- model proposes ---------------------------------------------------------

def call_model(client: anthropic.Anthropic, schema: dict, system: str, content: str, effort: str, label: str):
    with client.beta.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        output_config={"effort": effort, "format": {"type": "json_schema", "schema": schema}},
        system=system,
        messages=[{"role": "user", "content": content}],
    ) as stream:
        response = stream.get_final_message()
    if response.stop_reason == "refusal":
        raise RuntimeError(f"{label}: model refused ({response.stop_details})")
    if response.stop_reason == "max_tokens":
        raise RuntimeError(f"{label}: output truncated at max_tokens")
    usage = {"input_tokens": response.usage.input_tokens, "output_tokens": response.usage.output_tokens}
    return json.loads(next(b.text for b in response.content if b.type == "text")), usage, response.model


def read_incident(client: anthropic.Anthropic, report: str, now: datetime) -> tuple[dict, dict]:
    system = ("Read this incident report and record its facts. Times are local, America/Los_Angeles, as "
              "YYYY-MM-DDTHH:MM. Use only what the report says.")
    content = f"Current time: {now.isoformat(timespec='minutes')}\n\n<incident_report>\n{report}\n</incident_report>"
    facts, usage, _ = call_model(client, FACTS_SCHEMA, system, content, "low", "incident report")
    for field in ("vendor_found_at", "exampleco_told_at"):
        facts[field] = datetime.fromisoformat(facts[field]).replace(tzinfo=PT).isoformat()
    if facts["vendor_found_at"] > facts["exampleco_told_at"]:
        raise RuntimeError("Report says ExampleCo was told before the vendor found the incident. Check the report.")
    return facts, usage


def assess(client: anthropic.Anthropic, prompt: str, facts: dict, company: str, text: str, ledger: list[dict],
           held: list[dict], gone: list[dict], label: str) -> tuple[dict, dict, str]:
    ledger_view = [{k: i[k] for k in ("section", "type", "summary", "deadline", "secondary_deadline",
                                      "operative_notice_deadline", "recipient", "scope")} for i in ledger]
    content = "\n\n".join([
        prompt,
        f"<company_facts>\n{company}\n</company_facts>",
        f"<incident>\n{json.dumps(facts, indent=2)}\n</incident>",
        f"<batches_held_by_vendor>\n{json.dumps(held, indent=2)}\n</batches_held_by_vendor>",
        f"<batches_deleted_before_incident>\n{json.dumps(gone, indent=2)}\n</batches_deleted_before_incident>",
        f"<commitment_ledger>\n{json.dumps(ledger_view, indent=2)}\n</commitment_ledger>",
        f"<contract>\n{text}\n</contract>",
    ])
    return call_model(client, ASSESSMENT_SCHEMA, FORMAT_RULES, content, EFFORT, label)


# --- output -----------------------------------------------------------------

def pretty_time(iso: str) -> str:
    t = datetime.fromisoformat(iso)
    return t.strftime("%b %-d, %-I:%M %p").replace(":00 ", " ")


def time_left(iso: str, now: datetime) -> str:
    hours = (datetime.fromisoformat(iso) - now).total_seconds() / 3600
    if hours < 0:
        return f"OVERDUE by {abs(hours):.0f}h"
    return f"{hours:.0f}h left"


def human_duration(duration: str) -> str:
    unit, n = duration_value(duration)
    if unit == "hours" and n > 72 and n % 24 == 0:
        return f"{n // 24} days"
    return f"{n} {unit}"


def clock_words(row: dict, facts: dict) -> str:
    who = {CLOCK_VENDOR: f"{facts['vendor']} found it", CLOCK_TOLD: "ExampleCo was told"}[row["clock_start"]]
    return f"{human_duration(row['time_limit'])} from when {who} ({row['notice_section']})."


def action(c: dict) -> str:
    return f"{c['point'].rstrip('.')} ({c['section']})."


def render_summary(result: dict) -> str:
    facts, rows = result["facts"], result["rows"]
    now = datetime.fromisoformat(result["now"])
    notify = [r for r in rows if r["notify"] == "yes"]
    deadlines = sorted(r["deadline"] for r in notify if r["deadline"])
    headline = f"{facts['title']}. {len(notify)} to notify, {len(rows) - len(notify)} with no notice owed."
    if deadlines:
        headline += f" First deadline: {pretty_time(deadlines[0])} ({time_left(deadlines[0], now)})."

    lines = [f"# {facts['title']}", "", f"**{headline}**", "",
             f"All times Pacific. As of {pretty_time(result['now'])}. "
             f"Read from the report: {facts['vendor']} found it {pretty_time(facts['vendor_found_at'])}, "
             f"told ExampleCo {pretty_time(facts['exampleco_told_at'])}. Not yet known: {facts['not_yet_known']}", "",
             "| Customer | Notify? | Why | Deadline | Also do now | Status |", "|---|---|---|---|---|---|"]
    for r in rows:
        deadline = "n/a"
        if r["deadline"]:
            deadline = f"**{pretty_time(r['deadline'])}** ({time_left(r['deadline'], now)}). {clock_words(r, facts)}"
        elif r["notify"] == "yes":
            deadline = "**Not calculated**"
        also = " ".join(action(c) for c in r["also_do"][:TABLE_ACTIONS])
        lines.append(f"| {r['customer']} | **{r['notify'].title()}** | {r['why']} | {deadline} | {also} | {r['status']} |")
    lines.append("")

    if result.get("vendor_finding"):
        f = result["vendor_finding"]
        lines += [f"**Separate finding:** {f['vendor']} told ExampleCo {f['elapsed_hours']:.0f} hours after it found "
                  f"the incident. The {f['customer']} contract requires ExampleCo to make subcontractors report within "
                  f"{f['limit_hours']} hours ({f['section']}). Check whether {f['vendor']}'s contract says so.", ""]

    for r in rows:
        lines += [f"## {r['customer']}", ""]
        if r["also_do"][TABLE_ACTIONS:]:
            lines.append("**Also required**")
            lines += [f"- {action(c)}" for c in r["also_do"][TABLE_ACTIONS:]]
            lines.append("")
        for title, items in (("Contract wording behind the decision", r["evidence"]),
                             ("For legal", r["legal_flags"])):
            if items:
                lines.append(f"**{title}**")
                lines += [f"- {c['point']} ({c['section']}): \"{c['quote']}\"" for c in items]
                lines.append("")
        if r["recurring"]:
            lines.append("**Repeating duties**")
            lines += [f"- Every {human_duration(x['every'])} ({x['section']}): {x['summary']}" for x in r["recurring"]]
            lines.append("")
        if r["open_questions"]:
            lines.append("**Open questions**")
            lines += [f"- {q}" for q in r["open_questions"]]
            lines.append("")
        lines += [f"Batches held: {', '.join(r['batches_held']) or 'none'}. "
                  f"Deleted before the incident: {', '.join(r['batches_gone']) or 'none'}.", ""]
    return "\n".join(lines)


def write_drafts(out_dir: Path, rows: list[dict]) -> None:
    drafts = out_dir / "drafts"
    for r in rows:
        if r["notice_draft"]:
            drafts.mkdir(exist_ok=True)
            d = r["notice_draft"]
            (drafts / f"{r['contract']}.md").write_text(
                f"DRAFT FOR COUNSEL. NOT SENT.\n\nTo: {', '.join(d['to'])}\nSubject: {d['subject']}\n\n{d['body']}\n")


def run_once(client: anthropic.Anthropic, prompt: str, report: str, company: str, batches: list[dict],
             ledger: dict[str, list[dict]], now: datetime, only: list[str] | None) -> dict:
    facts, usage = read_incident(client, report, now)
    usages = [usage]
    found_on = datetime.fromisoformat(facts["vendor_found_at"]).date()
    groups = exposure(batches, found_on)
    ledgers = {c: [i for i in ledger.get(CONTRACT_FILES[c], [])] for c in groups}

    def one(contract: str) -> dict:
        group = groups[contract]
        if not group["held"]:
            return nothing_held(contract, group["customer"], group["gone"])
        text = (FIXTURES / "contracts" / CONTRACT_FILES[contract]).read_text()
        raw, used, served_by = assess(client, prompt, facts, company, text, ledgers[contract],
                                      group["held"], group["gone"], contract)
        usages.append(used)
        row = decide(raw, facts, ledgers[contract], text, group["customer"], contract, group["held"], group["gone"])
        row["served_by"] = served_by
        return row

    contracts = [c for c in groups if not only or c in only]
    with ThreadPoolExecutor(max_workers=len(contracts)) as pool:
        rows = list(pool.map(one, contracts))
    return {
        "now": now.isoformat(),
        "facts": facts,
        "rows": rows,
        "vendor_finding": vendor_report_finding(rows, facts, ledgers),
        "usage": {k: sum(u[k] for u in usages) for k in ("input_tokens", "output_tokens")},
    }


def latest_ledger() -> Path:
    candidates = sorted(RUNS.glob("*-v2/run-01.json"))
    if not candidates:
        raise RuntimeError("No v2 ledger found. Run commitments.extract first.")
    return candidates[-1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--prompt", default="incident-v2")
    parser.add_argument("--runs", type=int, default=1)
    parser.add_argument("--ledger", type=Path, help="default: run 1 of the latest v2 extraction")
    parser.add_argument("--report", type=Path, default=INCIDENT_DIR / "incident.md")
    parser.add_argument("--transfer-log", type=Path, default=INCIDENT_DIR / "labelforge-transfer-log.csv")
    parser.add_argument("--now", default=DEMO_NOW, help="local time, YYYY-MM-DDTHH:MM")
    parser.add_argument("--only", nargs="*", help="contract ids, such as AHS")
    parser.add_argument("--label", default="", help="added to the output folder name")
    args = parser.parse_args()

    ledger_path = (args.ledger or latest_ledger()).resolve()
    ledger: dict[str, list[dict]] = {}
    for item in json.loads(ledger_path.read_text())["commitments"]:
        ledger.setdefault(item["contract"], []).append(item)

    prompt = (PROMPTS / f"{args.prompt}.md").read_text()
    report = args.report.read_text()
    company = (FIXTURES / "company-facts.md").read_text()
    batches = load_batches(args.transfer_log)
    now = datetime.fromisoformat(args.now).replace(tzinfo=PT)

    stamp = datetime.now(PT).strftime("%Y%m%dT%H%M%S")
    out_dir = RUNS / "incidents" / f"{stamp}-{args.prompt}{'-' + args.label if args.label else ''}"
    out_dir.mkdir(parents=True)

    client = anthropic.Anthropic()
    for i in range(1, args.runs + 1):
        result = run_once(client, prompt, report, company, batches, ledger, now, args.only)
        record = {"prompt": args.prompt, "model": MODEL, "effort": EFFORT, "run": i,
                  "ledger": str(ledger_path.relative_to(ROOT)), "transfer_log": args.transfer_log.name, **result}
        (out_dir / f"run-{i:02d}.json").write_text(json.dumps(record, indent=2) + "\n")
        if i == 1:
            (out_dir / "summary.md").write_text(render_summary(record))
            write_drafts(out_dir, result["rows"])
        u = result["usage"]
        print(f"run {i}: " + ", ".join(f"{r['contract']} {r['notify']}" for r in result["rows"])
              + f", {u['input_tokens']} in / {u['output_tokens']} out")
    print(f"\nWrote {out_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

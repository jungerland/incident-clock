"""Deterministic scorer for the incident skill. No LLM.

Scores notify decisions and deadlines against expected.json (the target summary
in structured form) and runs a coded check for every trap the answer key marks
for the incident scenario. Notice wording is not judged: a person reads the drafts.

Usage:
  python -m evals.score_incident runs/incidents/<dir>
  python -m evals.score_incident runs/incidents/<dir> --flip runs/incidents/<flip dir>

The flip run uses a transfer log where the health system's data is a limited data
set. The health answer must change to yes, or the no was not read from the data.
Writes scores.json next to the runs.
"""

import argparse
import json
import re
from pathlib import Path
from statistics import mean

from commitments.checks import contacts
from commitments.incident import CLOCK_TOLD, CLOCK_VENDOR, bare_section

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "fixtures" / "exampleco"
KEY = FIXTURES / "answer-key.json"
EXPECTED = FIXTURES / "incident-labelforge" / "expected.json"


def cites(row: dict, section: str, fields: tuple[str, ...] = ("evidence", "also_do", "legal_flags")) -> bool:
    return any(bare_section(c["section"]).startswith(section) for f in fields for c in row[f])


def to_contacts(row: dict) -> set[str]:
    return contacts(" ".join((row["notice_draft"] or {}).get("to", [])))


def draft_mentions(row: dict, pattern: str) -> bool:
    return bool(row["notice_draft"] and re.search(pattern, row["notice_draft"]["body"], re.I))


def claimed_actions(row: dict) -> list[str]:
    """Sentences where a draft says something was already done. A person must confirm these."""
    body = (row["notice_draft"] or {}).get("body", "")
    pattern = r"[^.\n]*\b(?:we|labelforge|xyzwire|exampleco)\b (?:have|has|already) (?!not\b)[^.\n]*\."
    return [m.strip() for m in re.findall(pattern, body, re.I)]


def trap_checks(rows: dict[str, dict], expected: dict, flip: dict | None) -> dict[str, tuple[bool | None, str]]:
    anb, arg, ahs = rows["ANB"], rows["ARG"], rows["AHS"]
    right_time = lambda r, c: r["deadline"] == expected["rows"][c]["deadline"]
    return {
        "ANB-T1": (right_time(anb, "ANB") and anb["clock_start"] == CLOCK_VENDOR,
                   "12h runs from when the vendor found it"),
        "ANB-T2": (anb["notify"] == "yes" and cites(anb, "2.4"), "yes, citing the suspected-incident definition (2.4)"),
        "ANB-T3": (anb["notify"] == "yes" and cites(anb, "2.2"), "yes, citing de-identified data as Bank Data (2.2)"),
        "ANB-T4": (right_time(anb, "ANB") and bare_section(anb["notice_section"] or "") == "6.1",
                   "deadline comes from 6.1, not the 72h exhibit"),
        "ANB-T6": ({"cfc-thirdparty@anb.example", "12125550147"} <= to_contacts(anb)
                   and "dana.okafor@anb.example" not in to_contacts(anb),
                   "draft goes to the Cyber Fusion Center by email and phone, not the relationship manager"),
        "ANB-T7": (cites(anb, "6.4") and to_contacts(anb) <= {"cfc-thirdparty@anb.example", "12125550147"},
                   "says not to contact the bank's customers or regulators (6.4); draft goes to the bank only"),
        "ANB-T8": (cites(anb, "5.2"), "raises the 90-day notice for replacing a subcontractor (5.2)"),
        "ANB-T9": (any(x["every"] == "PT24H" for x in anb["recurring"]), "24h updates tracked as a repeating duty"),
        "ARG-T1": (right_time(arg, "ARG") and (cites(arg, "1.1") or cites(arg, "9.2")),
                   "24h, citing why ExampleCo's terms do not apply (1.1 or 9.2)"),
        "ARG-T2": (right_time(arg, "ARG") and arg["clock_start"] == CLOCK_TOLD,
                   "24h runs from when ExampleCo was told, not from the vendor's discovery"),
        "ARG-T3": (cites(arg, "5.1", ("legal_flags",)) and draft_mentions(arg, "labelforge"),
                   "flags the unapproved subprocessor for legal (5.1); draft names Labelforge"),
        "ARG-T4": (arg["notify"] == "yes" and cites(arg, "2.2"), "yes, citing derived data as Retailer Data (2.2)"),
        "ARG-T5": ({"secops@arg.example", "16145550182"} <= to_contacts(arg),
                   "draft goes to Retailer Security Operations by email and phone"),
        "AHS-T1": (ahs["notify"] == "no" and cites(ahs, "2.3"), "no, citing Safe Harbor data as outside the BAA (2.3)"),
        "AHS-T2": ((ahs["notify"] == "no" and ahs["methods_held"] == ["hipaa_safe_harbor"]
                    and bool(flip and flip["notify"] == "yes" and flip["deadline"])) if flip else None,
                   "no on Safe Harbor data, and yes with a deadline when the same data is a limited data set"),
        "AHS-T4": (ahs["notify"] == "no" and cites(ahs, "1.2"), "no, citing the ePHI limit on Security Incident (1.2)"),
    }


def score_run(run: dict, expected: dict, traps_expected: set[str], flip: dict | None) -> dict:
    rows = {r["contract"]: r for r in run["rows"]}
    traps = trap_checks(rows, expected, flip)
    if set(traps) != traps_expected:
        raise ValueError(f"Trap checks out of step with key: {set(traps) ^ traps_expected}")

    decisions = {c: rows[c]["notify"] == e["notify"] for c, e in expected["rows"].items()}
    with_deadline = {c: e for c, e in expected["rows"].items() if e["deadline"]}
    deadlines = {c: rows[c]["deadline"] == e["deadline"] for c, e in with_deadline.items()}
    finding = run.get("vendor_finding")
    want = expected["separate_finding"]
    return {
        "decisions": decisions,
        "deadlines": deadlines,
        "traps": {t: {"passed": ok, "check": what} for t, (ok, what) in traps.items()},
        "separate_finding_ok": bool(finding and finding["elapsed_hours"] == want["elapsed_hours"]
                                    and finding["limit_hours"] == want["limit_hours"]),
        "needs_person": [c for c, r in rows.items() if r["needs_person"]],
        "draft_claims": {c: claimed_actions(r) for c, r in rows.items() if claimed_actions(r)},
        "dropped_citations": sum(len(r["dropped_citations"]) for r in rows.values()),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path", type=Path)
    parser.add_argument("--flip", type=Path, help="folder of a run on the limited data set log")
    args = parser.parse_args()

    expected = json.loads(EXPECTED.read_text())
    key = json.loads(KEY.read_text())
    traps_expected = {t["id"] for c in key["contracts"] for t in c["traps"] if "incident" in t["scored_in"]}

    flip = None
    if args.flip:
        flip_run = json.loads(sorted(args.flip.glob("run-*.json"))[0].read_text())
        flip = next(r for r in flip_run["rows"] if r["contract"] == "AHS")

    files = sorted(args.path.glob("run-*.json"))
    scores = [score_run(json.loads(f.read_text()), expected, traps_expected, flip) for f in files]
    n = len(scores)

    print(f"\nScored {n} run(s).\n")
    print("NOTIFY DECISIONS")
    for c in expected["rows"]:
        print(f"  {c}  {sum(s['decisions'][c] for s in scores)}/{n} correct  (expected {expected['rows'][c]['notify']})")
    print("\nDEADLINES, calculated in code")
    for c in scores[0]["deadlines"]:
        print(f"  {c}  {sum(s['deadlines'][c] for s in scores)}/{n} correct  (expected {expected['rows'][c]['deadline']})")
    print(f"\nTRAPS ({len(traps_expected)} marked for the incident scenario)")
    for t, v in scores[0]["traps"].items():
        if v["passed"] is None:
            print(f"  {t:<7} not run    {v['check']}")
        else:
            print(f"  {t:<7} {sum(bool(s['traps'][t]['passed']) for s in scores)}/{n} passed   {v['check']}")
    print(f"\nSeparate finding (9h vs. 6h)  {sum(s['separate_finding_ok'] for s in scores)}/{n} correct")
    print(f"Sent to a person by a check   {sum(len(s['needs_person']) for s in scores)} row(s) across all runs")
    print(f"Citations dropped by a check  {sum(s['dropped_citations'] for s in scores)} across all runs")
    claims = [(c, q) for s in scores for c, qs in s["draft_claims"].items() for q in qs]
    print(f"Drafts saying an action was done  {len(claims)} across all runs")
    for c, q in claims:
        print(f"  {c}: {q[:120]}")
    if flip:
        print(f"\nFlip (limited data set)       AHS {flip['notify']}, section {flip['notice_section']}, "
              f"{flip['time_limit']}, deadline {flip['deadline']}")

    passed = [mean(bool(t["passed"]) for t in s["traps"].values() if t["passed"] is not None) for s in scores]
    print(f"\nTraps passed, mean            {mean(passed) * 100:.1f}%\n")
    out = args.path / "scores.json"
    out.write_text(json.dumps({"runs": n, "per_run": scores}, indent=2) + "\n")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()

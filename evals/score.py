"""Deterministic scorer for the commitments extractor. No LLM.

Compares extractor runs with the answer key and reports must_not_extract errors,
extraction traps, recall (overall and incident-relevant), precision, quote
accuracy, and field accuracy. Deviation wording is not judged: it goes to
deviations.md, beside the key's wording, for a person to read.

Usage:
  python -m evals.score runs/<dir>                 # every run-*.json in the dir
  python -m evals.score runs/<dir>/run-01.json ... # specific files

Writes scores.json and deviations.md next to the runs (or to --out).
"""

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from statistics import mean

from commitments.checks import contacts, duration_value
from commitments.quotes import is_verbatim, normalize

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "fixtures" / "exampleco"
KEY = FIXTURES / "answer-key.json"

SAME_SECTION_MIN = 0.5   # quote overlap needed to match a key item in the same section
ANY_SECTION_MIN = 0.8    # stricter overlap when the agent's section label does not match
RECIPIENT_MIN = 0.5      # word overlap for recipients with no email or phone to compare
STOPWORDS = {"a", "an", "the", "of", "to", "and", "or", "is", "are", "be", "for", "in", "on", "by",
             "with", "its", "their", "that", "this", "at", "as", "all", "every"}


# --- matching -------------------------------------------------------------

def norm_section(s: str) -> str:
    s = s.lower().replace("§", "").replace("section", "").split(",")[-1]
    return s.strip().rstrip(".")


def tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9][a-z0-9.\-']*[a-z0-9]|[a-z0-9]", normalize(text).lower())
            if t not in STOPWORDS}


def overlap(a: str, b: str) -> float:
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / min(len(ta), len(tb))


def match(item: dict, key_items: list[dict]) -> list[dict]:
    """Key items this extracted commitment covers.

    The best quote match, plus any key item whose whole quote sits inside this
    one, so a quote spanning two key items credits both.
    """
    section = norm_section(item["section"])
    quote = normalize(item["quote"])
    matched = [k for k in key_items if normalize(k["quote"]) in quote]

    same_section = [k for k in key_items if norm_section(k["section"]) == section]
    best = max(same_section, key=lambda k: overlap(item["quote"], k["quote"]), default=None)
    if not (best and overlap(item["quote"], best["quote"]) >= SAME_SECTION_MIN):
        best = max(key_items, key=lambda k: overlap(item["quote"], k["quote"]), default=None)
        if not (best and overlap(item["quote"], best["quote"]) >= ANY_SECTION_MIN):
            best = None
    if best and best not in matched:
        matched.append(best)
    return matched


# --- field checks ----------------------------------------------------------

def deadlines_of(item: dict) -> list[dict]:
    return [d for d in (item.get("deadline"), item.get("secondary_deadline")) if d]


def same_deadline(want: dict, got: dict) -> bool:
    return (duration_value(want["duration"]) == duration_value(got["duration"])
            and want["direction"] == got["direction"])


def deadline_ok(key_item: dict, items: list[dict]) -> bool:
    """Pools the deadlines of every item matched to this key item, so a commitment
    the agent split in two (24h updates, 30-day report) is not marked wrong."""
    wanted = [d for d in (key_item.get("deadline"), key_item.get("secondary_deadline")) if d]
    got = [d for i in items for d in deadlines_of(i)]
    return all(any(same_deadline(w, g) for g in got) for w in wanted)


def recipient_ok(key_item: dict, item: dict) -> bool:
    got = item.get("recipient")
    if not got:
        return False
    want = contacts(key_item["recipient"])
    if want:
        return want <= contacts(got)
    return overlap(key_item["recipient"], got) >= RECIPIENT_MIN


def norm_counterpart(s: str | None) -> str | None:
    if not s:
        return None
    s = s.lower()
    annex = re.search(r"annex[\s-]*(\d+)", s)
    if annex:
        return f"annex {annex.group(1)}"
    number = re.search(r"\d+(\.\d+)?", s)
    return number.group(0) if number else s.strip()


def counterpart_ok(key_item: dict, item: dict) -> bool:
    want = key_item["standard_counterpart"]
    if norm_counterpart(want) != norm_counterpart(item.get("standard_counterpart")):
        return False
    return not want or bool((item.get("deviation") or "").strip())


# --- must_not_extract and traps --------------------------------------------

def parse_must_not(text: str) -> tuple[str, tuple] | None:
    """'ENB breach notification deadline = 72 hours' -> ('ENB', duration value)."""
    m = re.fullmatch(r"(\w+) breach notification deadline = (.+)", text)
    return (m.group(1), duration_value(m.group(2))) if m else None


def operative(items: list[dict], duration: str) -> list[dict]:
    want = duration_value(duration)
    return [i for i in items if i.get("operative_notice_deadline")
            and any(duration_value(d["duration"]) == want for d in deadlines_of(i))]


def has_deadline(items: list[dict], duration: str, direction: str | None = None) -> bool:
    want = duration_value(duration)
    return any(duration_value(d["duration"]) == want and (direction is None or d["direction"] == direction)
               for i in items for d in deadlines_of(i))


def mentions(items: list[dict], fields: tuple[str, ...], pattern: str) -> bool:
    return any(re.search(pattern, i.get(f) or "", re.I) for i in items for f in fields)


def trap_checks(hits: dict[str, list[dict]], by_contract: dict[str, list[dict]]) -> dict[str, tuple[bool, str]]:
    """Coded check for each trap the key scores in extraction. id -> (passed, what was checked)."""
    h = lambda i: hits.get(i, [])
    enb, ehs = by_contract.get("ENB", []), by_contract.get("EHS", [])
    return {
        "ENB-T2": (mentions(h("ENB-6.1"), ("scope", "deviation"), r"suspect"),
                   "6.1 found, and its scope or deviation says suspected incidents count"),
        "ENB-T4": (bool(h("ENB-D.2")) and not operative(enb, "PT72H") and bool(operative(h("ENB-6.1"), "PT12H")),
                   "D.2 found, 72h not operative, 6.1's 12h operative"),
        "ENB-T5": (bool(h("ENB-5.3-FLOW")) and not operative(enb, "PT6H"),
                   "5.3 flow-down found, 6h not operative"),
        "ENB-T8": (has_deadline(h("ENB-5.2"), "P90D", "before")
                   and mentions(h("ENB-5.2"), ("recipient",), r"tprm|third-party risk")
                   and any(counterpart_ok({"standard_counterpart": "DPA-5.2"}, i) for i in h("ENB-5.2")),
                   "5.2 found with 90 days before, TPRM recipient, deviation from DPA 5.2"),
        "ENB-T9": (has_deadline(h("ENB-6.3-UPD"), "PT24H", "recurring"),
                   "6.3 updates recorded as recurring every 24h"),
        "ENB-T10": (any(counterpart_ok({"standard_counterpart": "DPA-6.2"}, i) for i in h("ENB-4.2")),
                    "4.2 found, flagged as a deviation from DPA 6.2"),
        "EHS-T3": (bool(operative(h("EHS-4.1"), "P10D")) and not operative(ehs, "P60D"),
                   "4.1's 10 days operative, 60 days not"),
    }


# --- scoring one run -------------------------------------------------------

def ratio(num: int, den: int) -> float | None:
    return num / den if den else None


def field_accuracy(required: list[dict], hits: dict, field: str, check) -> tuple[list[str], int]:
    """Wrong key ids among found items that define `field`, and how many were checked.

    A null standard_counterpart is an answer (the DPA has no match), so it is checked.
    """
    checked = [k for k in required if k["id"] in hits and field in k
               and (k[field] is not None or field == "standard_counterpart")]
    wrong = [k["id"] for k in checked if not any(check(k, i) for i in hits[k["id"]])]
    return wrong, len(checked)


def score_run(run: dict, contracts: list[dict], texts: dict[str, str]) -> dict:
    key_items = [k for c in contracts for k in c["commitments"]]
    required = [k for k in key_items if not k.get("optional")]
    incident = [k for k in required if k.get("incident_relevant")]
    id_by_file = {Path(c["file"]).name: c["id"] for c in contracts}
    key_by_file = {Path(c["file"]).name: c["commitments"] for c in contracts}

    hits: dict[str, list[dict]] = {}
    by_contract: dict[str, list[dict]] = {}
    extras, optional_found = [], set()
    matched_items = 0
    for item in run["commitments"]:
        by_contract.setdefault(id_by_file[item["contract"]], []).append(item)
        matched = match(item, key_by_file[item["contract"]])
        required_matches = [k for k in matched if not k.get("optional")]
        optional_found |= {k["id"] for k in matched if k.get("optional")}
        if not matched:
            extras.append({f: item[f] for f in ("contract", "section", "quote")})
        if required_matches:
            matched_items += 1
        for k in required_matches:
            hits.setdefault(k["id"], []).append(item)

    missed = [k["id"] for k in required if k["id"] not in hits]
    type_ok = lambda k, i: k.get("any_type_ok") or i["type"] == k["type"]
    wrong_type, type_n = field_accuracy(required, hits, "type", type_ok)
    with_deadline = [k for k in required if k["id"] in hits and k.get("deadline")]
    wrong_deadline = [k["id"] for k in with_deadline if not deadline_ok(k, hits[k["id"]])]
    deadline_n = len(with_deadline)
    wrong_recipient, recipient_n = field_accuracy(required, hits, "recipient", recipient_ok)
    wrong_counterpart, counterpart_n = field_accuracy(required, hits, "standard_counterpart", counterpart_ok)

    must_not = []
    for c in contracts:
        for t in c["traps"]:
            parsed = t.get("must_not_extract") and parse_must_not(t["must_not_extract"])
            if t.get("must_not_extract") and not parsed:
                raise ValueError(f"Cannot read must_not_extract on {t['id']}: {t['must_not_extract']}")
            if parsed:
                bad = [i for i in by_contract.get(parsed[0], []) if i.get("operative_notice_deadline")
                       and any(duration_value(d["duration"]) == parsed[1] for d in deadlines_of(i))]
                must_not.append({"trap": t["id"], "item": t["must_not_extract"], "clean": not bad,
                                 "produced_by": [i["section"] for i in bad]})

    traps = trap_checks(hits, by_contract)
    all_traps = [t for c in contracts for t in c["traps"]]
    extraction_ids = {t["id"] for t in all_traps if "extraction" in t["scored_in"]}
    if extraction_ids != set(traps):
        raise ValueError(f"Trap checks out of step with key: {extraction_ids ^ set(traps)}")

    proposed = run["commitments"] + run.get("rejected", [])
    not_verbatim = [{f: c[f] for f in ("contract", "section", "quote")} for c in proposed
                    if not is_verbatim(c["quote"], texts.get(c["contract"], ""))]

    return {
        "metrics": {
            "recall": ratio(len(hits), len(required)),
            "recall_incident": ratio(sum(1 for k in incident if k["id"] in hits), len(incident)),
            "precision": ratio(matched_items, matched_items + len(extras)),
            "quote_accuracy": ratio(len(proposed) - len(not_verbatim), len(proposed)),
            "type_accuracy": ratio(type_n - len(wrong_type), type_n),
            "deadline_accuracy": ratio(deadline_n - len(wrong_deadline), deadline_n),
            "recipient_accuracy": ratio(recipient_n - len(wrong_recipient), recipient_n),
            "counterpart_accuracy": ratio(counterpart_n - len(wrong_counterpart), counterpart_n),
        },
        "counts": {
            "required_found": len(hits), "required_total": len(required),
            "incident_found": sum(1 for k in incident if k["id"] in hits), "incident_total": len(incident),
            "agent_commitments": len(run["commitments"]), "rejected": len(run.get("rejected", [])),
            "extras": len(extras),
        },
        "must_not_extract": must_not,
        "traps": {tid: {"passed": ok, "check": what} for tid, (ok, what) in traps.items()},
        "traps_deferred": sorted(t["id"] for t in all_traps if t["id"] not in traps),
        "found": sorted(hits),
        "missed": missed,
        "extras": extras,
        "wrong_type": wrong_type,
        "wrong_deadline": wrong_deadline,
        "wrong_recipient": wrong_recipient,
        "wrong_counterpart": wrong_counterpart,
        "not_verbatim": not_verbatim,
        "optional_found": sorted(optional_found),
    }


# --- aggregation and report -----------------------------------------------

def summarize(values: list[float | None]) -> dict:
    vals = [v for v in values if v is not None]
    if not vals:
        return {"mean": None, "min": None, "max": None}
    return {"mean": round(mean(vals), 3), "min": round(min(vals), 3), "max": round(max(vals), 3)}


def pct(v: float | None) -> str:
    return "  n/a" if v is None else f"{v * 100:5.1f}%"


def report(per_run: list[dict], contracts: list[dict]) -> dict:
    n = len(per_run)
    key_items = [k for c in contracts for k in c["commitments"]]
    required = [k for k in key_items if not k.get("optional")]
    incident_ids = {k["id"] for k in required if k.get("incident_relevant")}
    found_counts = Counter(i for r in per_run for i in r["found"])
    metrics = {m: summarize([r["metrics"][m] for r in per_run]) for m in per_run[0]["metrics"]}

    print(f"\nScored {n} run(s) against {len(required)} required key commitments.\n")

    # Worst errors first: a wrong deadline read as true is worse than a miss.
    print(f"MUST-NOT-EXTRACT ({len(per_run[0]['must_not_extract'])} items)")
    for idx, m in enumerate(per_run[0]["must_not_extract"]):
        dirty = [r["must_not_extract"][idx] for r in per_run if not r["must_not_extract"][idx]["clean"]]
        status = "clean" if not dirty else f"PRODUCED in {len(dirty)}/{n} runs, section {dirty[0]['produced_by']}"
        print(f"  {m['trap']:<8} {m['item']:<46} {status}")

    print(f"\nEXTRACTION TRAPS ({len(per_run[0]['traps'])} scored here, "
          f"{len(per_run[0]['traps_deferred'])} deferred to the incident skill)")
    for tid, t in per_run[0]["traps"].items():
        passed = sum(1 for r in per_run if r["traps"][tid]["passed"])
        print(f"  {tid:<8} {passed}/{n} passed   {t['check']}")

    missed = [(k["id"], n - found_counts[k["id"]]) for k in required if found_counts[k["id"]] < n]
    missed.sort(key=lambda x: (x[0] not in incident_ids, -x[1]))
    print(f"\nMISSED ({len(missed)})")
    for cid, times in missed:
        tag = "incident" if cid in incident_ids else ""
        print(f"  {cid:<14} missed in {times}/{n} runs  {tag}")
    if not missed:
        print("  none")

    for label, field in (("WRONG DEADLINE", "wrong_deadline"), ("WRONG RECIPIENT", "wrong_recipient"),
                         ("WRONG COUNTERPART", "wrong_counterpart"), ("WRONG TYPE", "wrong_type")):
        counts = Counter(i for r in per_run for i in r[field])
        print(f"\n{label} ({len(counts)})")
        for cid, times in counts.most_common():
            print(f"  {cid:<14} {times}/{n} runs")
        if not counts:
            print("  none")

    extra_counts = Counter((e["contract"], e["section"], e["quote"]) for r in per_run for e in r["extras"])
    print(f"\nEXTRAS, not in key, for hand review ({len(extra_counts)} distinct)")
    for (contract, section, quote), times in extra_counts.most_common():
        print(f"  {times}/{n}  {contract} {section}: {quote[:90]}")
    if not extra_counts:
        print("  none")

    nv_counts = Counter((e["contract"], e["quote"]) for r in per_run for e in r["not_verbatim"])
    print(f"\nQUOTES REJECTED, not verbatim ({len(nv_counts)} distinct)")
    for (contract, quote), times in nv_counts.most_common():
        print(f"  {times}/{n}  {contract}: {quote[:90]}")
    if not nv_counts:
        print("  none")

    print(f"\n{'Metric':<24}{'Mean':>8}{'Min':>8}{'Max':>8}")
    for name, s in metrics.items():
        print(f"{name:<24}{pct(s['mean']):>8}{pct(s['min']):>8}{pct(s['max']):>8}")

    optional = Counter(i for r in per_run for i in r["optional_found"])
    if optional:
        print("\nOptional items found (no effect on score): "
              + ", ".join(f"{i} {c}/{n}" for i, c in sorted(optional.items())))
    print()

    return {
        "runs": n,
        "metrics": metrics,
        "hit_rate": {k["id"]: round(found_counts[k["id"]] / n, 3) for k in required},
        "per_run": per_run,
    }


def write_deviations(path: Path, run: dict, contracts: list[dict]) -> None:
    """The agent's deviation wording beside the key's, for a person to read."""
    lines = ["# Deviations: agent vs. key", "", f"From {run.get('prompt')} run {run.get('run')}.", ""]
    for c in contracts:
        name = Path(c["file"]).name
        items = [i for i in run["commitments"] if i["contract"] == name]
        keyed = [k for k in c["commitments"] if k.get("deviation")]
        if not keyed:
            continue
        lines += [f"## {c['id']}", ""]
        for k in keyed:
            got = [i.get("deviation") for i in items if k in match(i, c["commitments"])]
            lines += [f"**{k['id']}**", f"- Key: {k['deviation']}",
                      f"- Agent: {' / '.join(g or '(none)' for g in got) or '(commitment not found)'}", ""]
    path.write_text("\n".join(lines))


def load_key(path: Path) -> tuple[list[dict], dict[str, str]]:
    contracts = json.loads(path.read_text())["contracts"]
    return contracts, {Path(c["file"]).name: (path.parent / c["file"]).read_text() for c in contracts}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", type=Path, help="a runs/ directory or run-*.json files")
    parser.add_argument("--key", type=Path, default=KEY)
    parser.add_argument("--out", type=Path, help="default: scores.json in the first path's directory")
    args = parser.parse_args()

    files = []
    for p in args.paths:
        files += sorted(p.glob("run-*.json")) if p.is_dir() else [p]
    if not files:
        parser.error("no run-*.json files found")

    contracts, texts = load_key(args.key)
    runs = [json.loads(f.read_text()) for f in files]
    per_run = [{"file": str(f), "prompt": r.get("prompt"), **score_run(r, contracts, texts)}
               for f, r in zip(files, runs)]

    result = report(per_run, contracts)
    out = args.out or (args.paths[0] if args.paths[0].is_dir() else args.paths[0].parent) / "scores.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    write_deviations(out.with_name("deviations.md"), runs[0], contracts)
    print(f"Wrote {out} and {out.with_name('deviations.md').name}")


if __name__ == "__main__":
    main()

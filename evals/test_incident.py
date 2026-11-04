"""Checks the code that decides, using proposals written by hand. No model calls.

Usage: python -m evals.test_incident
"""

import copy
import json
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from commitments.checks import add_duration
from commitments.incident import (CLOCK_TOLD, CLOCK_VENDOR, CONTRACT_FILES, FIXTURES, INCIDENT_DIR, decide, exposure,
                                  load_batches, render_summary, vendor_report_finding)
from evals.score_incident import EXPECTED, KEY, claimed_actions, score_run

PT = ZoneInfo("America/Los_Angeles")
TEXT = {c: (FIXTURES / "contracts" / f).read_text() for c, f in CONTRACT_FILES.items()}
FACTS = {"title": "Labelforge credential breach", "vendor": "Labelforge",
         "vendor_found_at": "2026-11-02T06:00:00-08:00", "exampleco_told_at": "2026-11-02T15:00:00-08:00",
         "known": "x", "not_yet_known": "what was viewed"}
LEDGER = {
    "ANB": [
        {"section": "6.1", "summary": "12h", "operative_notice_deadline": True,
         "deadline": {"duration": "PT12H", "direction": "after", "anchor": "Discovery"}},
        {"section": "5.3", "summary": "6h flow-down", "operative_notice_deadline": False,
         "deadline": {"duration": "PT6H", "direction": "after", "anchor": "Discovery"}},
        {"section": "D.2", "summary": "72h", "operative_notice_deadline": False,
         "deadline": {"duration": "PT72H", "direction": "after", "anchor": "aware"}},
        {"section": "6.3", "summary": "updates", "operative_notice_deadline": False,
         "deadline": {"duration": "PT24H", "direction": "recurring", "anchor": "notice"}},
    ],
    "ARG": [{"section": "6.1", "summary": "24h", "operative_notice_deadline": True,
             "deadline": {"duration": "PT24H", "direction": "after", "anchor": "aware"}}],
    "AHS": [],
}


def quote(contract: str, section: str, start: str) -> dict:
    line = next(l for l in TEXT[contract].splitlines() if l.startswith(f"{section} {start}"))
    return {"section": section, "quote": line.split(" ", 1)[1], "point": f"point {section}"}


def bank() -> dict:
    return {"notify": "yes", "why": "w", "notice_section": "6.1", "clock_start": CLOCK_VENDOR, "clock_reason": "r",
            "evidence": [quote("ANB", "2.2", '"Bank Data"'), quote("ANB", "2.4", '"Security Incident"')],
            "also_do": [quote("ANB", "6.4", "Supplier shall not notify"), quote("ANB", "6.3", "Supplier's initial"),
                        quote("ANB", "5.2", "Supplier shall give")],
            "legal_flags": [], "vendor_report_section": "5.3", "open_questions": [],
            "notice_draft": {"to": ["cfc-thirdparty@anb.example", "+1 (212) 555-0147"], "subject": "s",
                             "body": "Labelforge found this at 6:00 AM"}}


def retail() -> dict:
    return {"notify": "yes", "why": "w", "notice_section": "6.1", "clock_start": CLOCK_TOLD, "clock_reason": "r",
            "evidence": [quote("ARG", "2.2", '"Retailer Data"'), quote("ARG", "1.1", "This VDPA")],
            "also_do": [], "legal_flags": [quote("ARG", "5.1", "Vendor shall not permit")],
            "vendor_report_section": None, "open_questions": [],
            "notice_draft": {"to": ["secops@arg.example", "+1 (614) 555-0182"], "subject": "s",
                             "body": "Subprocessor involved: Labelforge."}}


def health() -> dict:
    return {"notify": "no", "why": "w", "notice_section": None, "clock_start": None, "clock_reason": None,
            "evidence": [quote("AHS", "2.3", "Business Associate may"), quote("AHS", "1.2", '"Security Incident"')],
            "also_do": [], "legal_flags": [], "vendor_report_section": None, "open_questions": [], "notice_draft": None}


def row(raw: dict, contract: str, facts: dict = FACTS) -> dict:
    groups = exposure(load_batches(INCIDENT_DIR / "labelforge-transfer-log.csv"), date(2026, 11, 2))
    g = groups[contract]
    return decide(raw, facts, LEDGER[contract], TEXT[contract], g["customer"], contract, g["held"], g["gone"])


def perfect() -> dict:
    return {"now": "2026-11-02T16:00:00-08:00", "facts": FACTS, "usage": {},
            "rows": [row(bank(), "ANB"), row(retail(), "ARG"), row(health(), "AHS")]}


def expected_and_traps():
    expected = json.loads(EXPECTED.read_text())
    key = json.loads(KEY.read_text())
    return expected, {t["id"] for c in key["contracts"] for t in c["traps"] if "incident" in t["scored_in"]}


def test_deadlines_are_calculated_from_the_right_clock() -> None:
    assert row(bank(), "ANB")["deadline"] == "2026-11-02T18:00:00-08:00"
    assert row(retail(), "ARG")["deadline"] == "2026-11-03T15:00:00-08:00"
    wrong_clock = {**bank(), "clock_start": CLOCK_TOLD}
    assert row(wrong_clock, "ANB")["deadline"] == "2026-11-03T03:00:00-08:00"


def test_add_duration_handles_business_days_and_clock_change() -> None:
    friday = datetime(2026, 11, 6, 9, tzinfo=PT)
    assert add_duration(friday, "1 business day").day == 9
    assert add_duration(friday, "5 business days").day == 13
    before_change = datetime(2026, 10, 31, 12, tzinfo=PT)
    assert add_duration(before_change, "PT24H").hour == 11
    assert add_duration(before_change, "nonsense") is None


def test_exposure_ignores_batches_deleted_before_the_incident() -> None:
    groups = exposure(load_batches(INCIDENT_DIR / "labelforge-transfer-log.csv"), date(2026, 11, 2))
    assert [b["batch_id"] for b in groups["ARG"]["held"]] == ["LF-2026-0818"]
    assert [b["batch_id"] for b in groups["ARG"]["gone"]] == ["LF-2025-1103"]
    assert len(groups["ANB"]["held"]) == 3 and len(groups["AHS"]["held"]) == 2


def test_invented_quote_is_dropped_and_sent_to_a_person() -> None:
    raw = bank()
    raw["evidence"].append({"section": "6.1", "quote": "Supplier may notify Bank within 72 hours.", "point": "p"})
    r = row(raw, "ANB")
    assert r["needs_person"] and len(r["dropped_citations"]) == 1 and len(r["evidence"]) == 2


def test_real_quote_with_wrong_section_is_dropped() -> None:
    raw = bank()
    raw["evidence"][0]["section"] = "6.1"
    r = row(raw, "ANB")
    assert r["needs_person"] and len(r["dropped_citations"]) == 1


def test_section_with_subclause_is_accepted() -> None:
    raw = bank()
    raw["evidence"][0]["section"] = "2.2(c)"
    assert not row(raw, "ANB")["needs_person"]


def test_non_governing_notice_section_gets_no_deadline() -> None:
    for section in ("D.2", "5.3", "9.9"):
        r = row({**bank(), "notice_section": section}, "ANB")
        assert r["deadline"] is None and r["needs_person"], section


def test_recipient_not_in_contract_goes_to_a_person() -> None:
    raw = bank()
    raw["notice_draft"]["to"] = ["ciso@anb.example"]
    assert row(raw, "ANB")["needs_person"]


def test_missing_draft_or_clock_goes_to_a_person() -> None:
    assert row({**bank(), "notice_draft": None}, "ANB")["needs_person"]
    r = row({**bank(), "clock_start": None}, "ANB")
    assert r["needs_person"] and r["deadline"] is None


def test_decision_with_no_verified_wording_goes_to_a_person() -> None:
    assert row({**health(), "evidence": []}, "AHS")["needs_person"]


def test_recurring_duty_comes_from_the_ledger() -> None:
    assert [x["every"] for x in row(bank(), "ANB")["recurring"]] == ["PT24H"]


def test_vendor_finding_is_calculated() -> None:
    f = vendor_report_finding(perfect()["rows"], FACTS, LEDGER)
    assert f["elapsed_hours"] == 9 and f["limit_hours"] == 6 and f["section"] == "5.3"
    fast = {**FACTS, "exampleco_told_at": "2026-11-02T09:00:00-08:00"}
    assert vendor_report_finding(perfect()["rows"], fast, LEDGER) is None


def test_perfect_proposals_score_full_marks() -> None:
    expected, traps = expected_and_traps()
    run = perfect()
    run["vendor_finding"] = vendor_report_finding(run["rows"], FACTS, LEDGER)
    flip = {"notify": "yes", "deadline": "2026-11-12T06:00:00-08:00"}
    s = score_run(run, expected, traps, flip)
    assert all(s["decisions"].values()) and all(s["deadlines"].values()) and s["separate_finding_ok"]
    failed = [t for t, v in s["traps"].items() if not v["passed"]]
    assert not failed and len(s["traps"]) == 16, failed
    assert not s["needs_person"]


def test_wrong_answers_lose_the_right_traps() -> None:
    expected, traps = expected_and_traps()
    flip = {"notify": "yes", "deadline": "2026-11-12T06:00:00-08:00"}
    cases = [
        ("ANB", {"clock_start": CLOCK_TOLD}, {"ANB-T1", "ANB-T4"}),
        ("ARG", {"clock_start": CLOCK_VENDOR}, {"ARG-T1", "ARG-T2"}),
        ("ANB", {"notice_draft": {"to": ["dana.okafor@anb.example"], "subject": "s", "body": "b"}}, {"ANB-T6", "ANB-T7"}),
        ("ARG", {"legal_flags": []}, {"ARG-T3"}),
    ]
    for contract, change, should_fail in cases:
        run = copy.deepcopy(perfect())
        raw = {**(bank() if contract == "ANB" else retail()), **change}
        run["rows"] = [row(raw, contract) if r["contract"] == contract else r for r in run["rows"]]
        s = score_run(run, expected, traps, flip)
        failed = {t for t, v in s["traps"].items() if not v["passed"]}
        assert should_fail <= failed, (change, failed)


def test_health_yes_fails_the_opposite_answer_traps() -> None:
    expected, traps = expected_and_traps()
    run = perfect()
    wrong = {**health(), "notify": "yes", "notice_section": "4.1", "clock_start": CLOCK_TOLD}
    run["rows"][2] = row(wrong, "AHS")
    s = score_run(run, expected, traps, {"notify": "yes", "deadline": "x"})
    assert not s["decisions"]["AHS"] and not s["traps"]["AHS-T1"]["passed"]
    assert not s["traps"]["AHS-T2"]["passed"]


def test_flip_that_stays_no_fails_t2() -> None:
    expected, traps = expected_and_traps()
    s = score_run(perfect(), expected, traps, {"notify": "no", "deadline": None})
    assert not s["traps"]["AHS-T2"]["passed"]
    s = score_run(perfect(), expected, traps, None)
    assert s["traps"]["AHS-T2"]["passed"] is None


def test_draft_claiming_an_action_is_surfaced() -> None:
    claimed = {"notice_draft": {"body": "We have not confirmed access. We have instructed Labelforge to keep logs."}}
    assert claimed_actions(claimed) == ["We have instructed Labelforge to keep logs."]
    assert claimed_actions({"notice_draft": None}) == []


def test_table_shows_first_actions_and_moves_the_rest_below() -> None:
    run = perfect()
    r = run["rows"][0]
    r["also_do"] = [{"section": "6.2", "quote": "q", "point": f"action {i}"} for i in range(6)]
    table, below = render_summary(run).split("## Awesome National Bank")
    assert "action 3 (6.2)" in table and "action 4" not in table
    assert "action 4 (6.2)" in below and "action 5 (6.2)" in below


def test_summary_renders_the_table_and_overdue() -> None:
    run = perfect()
    run["vendor_finding"] = vendor_report_finding(run["rows"], FACTS, LEDGER)
    text = render_summary(run)
    assert "2 to notify, 1 with no notice owed" in text and "Nov 2, 6 PM" in text and "(2h left)" in text
    assert "Labelforge told ExampleCo 9 hours" in text and "12 hours from when Labelforge found it" in text
    late = render_summary({**run, "now": "2026-11-02T19:00:00-08:00"})
    assert "OVERDUE by 1h" in late


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_")]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"ok    {name}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {name}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    raise SystemExit(1 if failed else 0)

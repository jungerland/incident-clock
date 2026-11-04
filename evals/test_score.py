"""Checks that the scorer can tell right from wrong, using runs built from the key.

A run made from the key's own answers must score 100%. A run with planted errors
must lose exactly those points.

Usage: python -m evals.test_score
"""

import copy
import tempfile
from pathlib import Path

from commitments.extract import COMMITMENT_TYPES, contract_files, CONTRACTS
from commitments.quotes import is_verbatim
from evals.score import KEY, load_key, score_run

contracts, texts = load_key(KEY)


def perfect_run() -> dict:
    items = []
    for c in contracts:
        for k in c["commitments"]:
            items.append({
                "contract": Path(c["file"]).name,
                "section": k["section"],
                "type": k["type"],
                "quote": k["quote"],
                "summary": k["summary"],
                "deadline": k.get("deadline"),
                "secondary_deadline": k.get("secondary_deadline"),
                "operative_notice_deadline": bool(k["type"] == "breach_notification" and k.get("deadline")
                                                  and k.get("governing", True)),
                "recipient": k.get("recipient"),
                "scope": k.get("scope"),
                "standard_counterpart": k.get("standard_counterpart"),
                "deviation": k.get("deviation"),
            })
    return copy.deepcopy({"commitments": items, "rejected": []})


def find(run: dict, contract: str, section: str, fragment: str = "") -> dict:
    return next(i for i in run["commitments"]
                if i["contract"].startswith(contract) and i["section"] == section and fragment in i["quote"])


def test_perfect_run_scores_100() -> None:
    s = score_run(perfect_run(), contracts, texts)
    assert all(v == 1.0 for v in s["metrics"].values()), s["metrics"]
    assert not s["missed"] and not s["extras"]
    assert all(m["clean"] for m in s["must_not_extract"])
    assert len(s["must_not_extract"]) == 4
    failed = [t for t, v in s["traps"].items() if not v["passed"]]
    assert not failed and len(s["traps"]) == 7, failed
    assert len(s["traps_deferred"]) == 12


def test_key_quotes_are_verbatim() -> None:
    for c in contracts:
        for k in c["commitments"]:
            assert is_verbatim(k["quote"], texts[Path(c["file"]).name]), k["id"]


def test_key_counterparts_exist() -> None:
    ids = {k["id"] for c in contracts for k in c["commitments"]}
    dangling = [k["id"] for c in contracts for k in c["commitments"]
                if k.get("standard_counterpart") and k["standard_counterpart"] not in ids]
    assert not dangling, dangling


def test_key_types_are_in_schema() -> None:
    assert {k["type"] for c in contracts for k in c["commitments"]} <= set(COMMITMENT_TYPES)


def test_72_hours_as_bank_deadline_is_caught() -> None:
    run = perfect_run()
    find(run, "example-national-bank", "Exhibit D, D.2")["operative_notice_deadline"] = True
    s = score_run(run, contracts, texts)
    assert not next(m for m in s["must_not_extract"] if m["trap"] == "ENB-T4")["clean"]
    assert not s["traps"]["ENB-T4"]["passed"]


def test_6_hours_as_bank_deadline_is_caught() -> None:
    run = perfect_run()
    flow = find(run, "example-national-bank", "5.3")
    flow["deadline"] = {"duration": "PT6H", "direction": "after", "anchor": "Subcontractor's Discovery"}
    flow["operative_notice_deadline"] = True
    s = score_run(run, contracts, texts)
    assert not next(m for m in s["must_not_extract"] if m["trap"] == "ENB-T5")["clean"]
    assert not s["traps"]["ENB-T5"]["passed"]


def test_6_hours_recorded_as_flow_down_is_fine() -> None:
    run = perfect_run()
    find(run, "example-national-bank", "5.3")["deadline"] = {
        "duration": "PT6H", "direction": "after", "anchor": "Subcontractor's Discovery"}
    s = score_run(run, contracts, texts)
    assert next(m for m in s["must_not_extract"] if m["trap"] == "ENB-T5")["clean"]
    assert s["traps"]["ENB-T5"]["passed"]


def test_outside_deadlines_are_caught() -> None:
    run = perfect_run()
    retail = find(run, "example-retail", "6.1")
    retail["deadline"] = {"duration": "PT72H", "direction": "after", "anchor": "confirmation"}
    health = find(run, "example-health", "4.1")
    health["deadline"] = {"duration": "P60D", "direction": "after", "anchor": "Discovery"}
    s = score_run(run, contracts, texts)
    dirty = {m["trap"] for m in s["must_not_extract"] if not m["clean"]}
    assert dirty == {"ERG-T1", "EHS-T3"}, dirty
    assert {"ERG-6.1", "EHS-4.1"} <= set(s["wrong_deadline"])


def test_one_time_24h_update_fails_recurring_trap() -> None:
    run = perfect_run()
    find(run, "example-national-bank", "6.3", "status updates")["deadline"]["direction"] = "after"
    s = score_run(run, contracts, texts)
    assert not s["traps"]["ENB-T9"]["passed"]


def test_merged_quote_credits_both_key_items() -> None:
    run = perfect_run()
    first = find(run, "example-national-bank", "6.3", "initial notice")
    second = find(run, "example-national-bank", "6.3", "status updates")
    first["quote"] = f"{first['quote']} {second['quote']}"
    first["deadline"] = second["deadline"]
    first["secondary_deadline"] = second["secondary_deadline"]
    run["commitments"].remove(second)
    s = score_run(run, contracts, texts)
    assert "ENB-6.3-INIT" in s["found"] and "ENB-6.3-UPD" in s["found"]
    assert not s["extras"]


def test_split_commitment_keeps_both_deadlines() -> None:
    run = perfect_run()
    updates = find(run, "example-national-bank", "6.3", "status updates")
    report = {**updates, "quote": "shall deliver a written root-cause report within thirty (30) days after containment",
              "deadline": updates["secondary_deadline"], "secondary_deadline": None}
    updates["quote"] = "Supplier shall provide written status updates at least once every twenty-four (24) hours"
    updates["secondary_deadline"] = None
    run["commitments"].append(report)
    assert "ENB-6.3-UPD" not in score_run(run, contracts, texts)["wrong_deadline"]
    run["commitments"].remove(report)
    assert "ENB-6.3-UPD" in score_run(run, contracts, texts)["wrong_deadline"]


def test_missing_incident_commitment_lowers_both_recalls() -> None:
    run = perfect_run()
    run["commitments"].remove(find(run, "example-national-bank", "6.1"))
    s = score_run(run, contracts, texts)
    assert "ENB-6.1" in s["missed"]
    assert s["metrics"]["recall"] < 1 and s["metrics"]["recall_incident"] < 1
    assert not s["traps"]["ENB-T2"]["passed"]


def test_wrong_fields_are_reported() -> None:
    run = perfect_run()
    bank = find(run, "example-national-bank", "6.2")
    bank["recipient"] = "dana.okafor@enb.example"
    find(run, "example-national-bank", "4.2")["standard_counterpart"] = None
    find(run, "example-national-bank", "4.1")["type"] = "insurance"
    s = score_run(run, contracts, texts)
    assert s["wrong_recipient"] == ["ENB-6.2"]
    assert s["wrong_counterpart"] == ["ENB-4.2"]
    assert s["wrong_type"] == ["ENB-4.1"]
    assert not s["traps"]["ENB-T10"]["passed"]


def test_invented_quote_counts_against_quote_accuracy() -> None:
    run = perfect_run()
    fake = {**find(run, "example-national-bank", "6.1"), "quote": "Supplier shall notify Bank within 72 hours."}
    run["rejected"] = [fake]
    s = score_run(run, contracts, texts)
    assert s["metrics"]["quote_accuracy"] < 1
    assert s["not_verbatim"][0]["quote"] == fake["quote"]


def test_unknown_commitment_is_an_extra() -> None:
    run = perfect_run()
    extra = {**find(run, "example-national-bank", "6.1"), "section": "3.1", "deadline": None,
             "operative_notice_deadline": False,
             "quote": "Supplier shall maintain a written information security program that is consistent "
                      "with the NIST Cybersecurity Framework"}
    run["commitments"].append(extra)
    s = score_run(run, contracts, texts)
    assert len(s["extras"]) == 1 and s["metrics"]["precision"] < 1


def test_extractor_refuses_answer_key() -> None:
    assert contract_files(CONTRACTS)
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "answer-key.md").write_text("answers")
        try:
            contract_files(Path(d))
        except RuntimeError:
            return
    raise AssertionError("contract_files accepted an answer key")


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

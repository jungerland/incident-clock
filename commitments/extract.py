"""Extract commitments from contracts, one contract per call.

Gets commitments back in a fixed JSON structure and rejects any commitment whose
quote is not verbatim in the contract it came from. Customer contracts are read
alongside the standard DPA so the model can describe deviations, but quotes are
checked only against the contract being extracted. Never reads the answer key.

Usage:
  python -m commitments.extract                 # 1 run, v1 prompt
  python -m commitments.extract --runs 3 --prompt v1

Output: runs/<timestamp>-<prompt>/run-NN.json
"""

import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import anthropic

from commitments.quotes import is_verbatim

ROOT = Path(__file__).resolve().parent.parent
CONTRACTS = ROOT / "fixtures" / "exampleco" / "contracts"
BASELINE = "exampleco-standard-dpa.md"
PROMPTS = Path(__file__).parent / "prompts"
RUNS = ROOT / "runs"
MODEL = "claude-opus-5-5"
EFFORT = "high"
MAX_TOKENS = 64000

COMMITMENT_TYPES = [
    "breach_notification", "incident_updates", "incident_communications", "evidence_preservation",
    "incident_costs", "subprocessor_notice", "subprocessor_scope", "data_residency", "offshore_access",
    "ai_data_use", "testing_and_audit", "certification", "security_controls", "business_continuity",
    "insurance", "data_deletion",
]

# Output conventions, held fixed across prompt variants so the scorer can read
# every run the same way. The prompt file is the experimental variable.
FORMAT_RULES = """Output rules:
- `quote` is copied word for word from the contract. Do not paraphrase, merge sentences from different places, or add words. You may drop Markdown markup. Quote only the passage that states this commitment.
- `section` is the section number as written (for example "6.1", "D.2", or "Annex 2").
- `type` is the closest listed type. A term that decides which document governs takes the type of the duties it most affects.
- `summary` is one plain sentence.
- `deadline` is the commitment's main time limit, or null. `secondary_deadline` is a second time limit in the same commitment, or null.
- `duration` uses ISO 8601: PT12H is 12 hours, P30D is 30 days, P1Y is one year. Write business days out, as "5 business days", because ISO 8601 has no unit for them.
- `direction`: `after` means due within the period after the anchor. `before` means due at least that long before the anchor. `recurring` means repeating at that interval. `retain_for` means keep something for that long.
- `anchor` is the event that starts the period, read through the contract's definitions. If a defined term sets when the clock starts, say whose awareness or action counts.
- `operative_notice_deadline` is true only when this commitment sets the time limit that actually governs notifying this customer of an incident, after applying any term in the contract about which period controls. It is false for everything else, including periods imposed on someone other than the vendor and periods another term displaces.
- `recipient` is who must receive a notice or report, with the contact details the contract gives anywhere, including exhibits. Null when the commitment involves no recipient.
- `scope` is what the commitment covers, read through the contract's definitions, such as which incidents or data count. Null when there is nothing to add.
- `standard_counterpart` is the section number of the baseline DPA term this commitment corresponds to, such as "7.1" or "Annex 2". Null when the DPA has no matching term, or when you are extracting the DPA itself.
- `deviation` says how this commitment differs from that DPA term. Null when you are extracting the DPA itself. Write "No DPA equivalent." when the DPA has no matching term."""

DEADLINE_SCHEMA = {
    "anyOf": [
        {
            "type": "object",
            "properties": {
                "duration": {"type": "string"},
                "direction": {"type": "string", "enum": ["after", "before", "recurring", "retain_for"]},
                "anchor": {"type": "string"},
            },
            "required": ["duration", "direction", "anchor"],
            "additionalProperties": False,
        },
        {"type": "null"},
    ]
}

COMMITMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "commitments": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "section": {"type": "string"},
                    "type": {"type": "string", "enum": COMMITMENT_TYPES},
                    "quote": {"type": "string"},
                    "summary": {"type": "string"},
                    "deadline": DEADLINE_SCHEMA,
                    "secondary_deadline": DEADLINE_SCHEMA,
                    "operative_notice_deadline": {"type": "boolean"},
                    "recipient": {"type": ["string", "null"]},
                    "scope": {"type": ["string", "null"]},
                    "standard_counterpart": {"type": ["string", "null"]},
                    "deviation": {"type": ["string", "null"]},
                },
                "required": ["section", "type", "quote", "summary", "deadline", "secondary_deadline",
                             "operative_notice_deadline", "recipient", "scope", "standard_counterpart",
                             "deviation"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["commitments"],
    "additionalProperties": False,
}


def contract_files(contract_dir: Path) -> list[Path]:
    files = sorted(contract_dir.glob("*.md"))
    if any("answer-key" in f.name for f in files):
        raise RuntimeError("Extractor must not read the answer key")
    return files


def extract_contract(client: anthropic.Anthropic, prompt: str, path: Path, baseline: str) -> dict:
    text = path.read_text()
    parts = [prompt]
    if path.name != BASELINE:
        parts.append(f'<baseline_dpa file="{BASELINE}">\n{baseline}\n</baseline_dpa>')
    parts.append(f'<contract file="{path.name}">\n{text}\n</contract>')

    with client.beta.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        output_config={"effort": EFFORT, "format": {"type": "json_schema", "schema": COMMITMENT_SCHEMA}},
        system=FORMAT_RULES,
        messages=[{"role": "user", "content": "\n\n".join(parts)}],
    ) as stream:
        response = stream.get_final_message()

    if response.stop_reason == "refusal":
        raise RuntimeError(f"{path.name}: model refused ({response.stop_details})")
    if response.stop_reason == "max_tokens":
        raise RuntimeError(f"{path.name}: output truncated at max_tokens")

    raw = json.loads(next(b.text for b in response.content if b.type == "text"))
    accepted, rejected = [], []
    for item in raw["commitments"]:
        item = {"contract": path.name, **item}
        if is_verbatim(item["quote"], text):
            accepted.append(item)
        else:
            rejected.append({**item, "rejected_because": "quote not verbatim in contract"})
    usage = {"input_tokens": response.usage.input_tokens, "output_tokens": response.usage.output_tokens}
    return {"commitments": accepted, "rejected": rejected, "usage": usage, "served_by": response.model}


def run_once(client: anthropic.Anthropic, prompt: str, files: list[Path], baseline: str) -> dict:
    with ThreadPoolExecutor(max_workers=len(files)) as pool:
        results = list(pool.map(lambda f: extract_contract(client, prompt, f, baseline), files))
    return {
        "commitments": [c for r in results for c in r["commitments"]],
        "rejected": [c for r in results for c in r["rejected"]],
        "usage": {k: sum(r["usage"][k] for r in results) for k in ("input_tokens", "output_tokens")},
        "served_by": {f.name: r["served_by"] for f, r in zip(files, results)},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--prompt", default="v1", help="prompt file name in commitments/prompts/, without .md")
    parser.add_argument("--runs", type=int, default=1)
    parser.add_argument("--contracts", type=Path, default=CONTRACTS)
    args = parser.parse_args()

    prompt = (PROMPTS / f"{args.prompt}.md").read_text()
    files = contract_files(args.contracts)
    baseline = (args.contracts / BASELINE).read_text()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = RUNS / f"{stamp}-{args.prompt}"
    out_dir.mkdir(parents=True)

    client = anthropic.Anthropic()
    for i in range(1, args.runs + 1):
        result = run_once(client, prompt, files, baseline)
        record = {
            "prompt": args.prompt,
            "model": MODEL,
            "effort": EFFORT,
            "run": i,
            "created": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "contracts": [f.name for f in files],
            **result,
        }
        out = out_dir / f"run-{i:02d}.json"
        out.write_text(json.dumps(record, indent=2) + "\n")
        print(f"run {i}: {len(result['commitments'])} commitments, {len(result['rejected'])} rejected, "
              f"{result['usage']['input_tokens']} in / {result['usage']['output_tokens']} out -> {out.relative_to(ROOT)}")
    print(f"\nScore with: python -m evals.score {out_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

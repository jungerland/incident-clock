"""Build ui/index.html from MEMO.md and recorded incident runs. No model calls.

Usage: python -m ui.build
"""

import json
import re
from pathlib import Path

import markdown

from commitments.incident import INCIDENT_DIR, clock_words, pretty_time

ROOT = Path(__file__).resolve().parent.parent
RUN = ROOT / "runs" / "incidents" / "20261104T103134-incident-v2" / "run-03.json"
FLIP = ROOT / "runs" / "incidents" / "20261104T103135-incident-v2-flip" / "run-01.json"
ARTIFACT_LINK = re.compile(r"https://claude\.ai/artifact/\w+")

NOTE = ("This page replays recorded output: run 3 of 3 for the three customers, plus one run where the health "
        "system's data was changed to a limited data set. Why, the actions, flags and drafts are the agent's own "
        "wording. No model runs in this page and nothing is sent. Deadlines were calculated in code. The prototype "
        "doesn't record whether a notice went out, so a past deadline shows as overdue. All companies are fictional.")


def view(row: dict, facts: dict) -> dict:
    if row["deadline"]:
        row["deadline_words"] = pretty_time(row["deadline"])
        row["clock_words"] = clock_words(row, facts)
    return row


def main() -> None:
    run = json.loads(RUN.read_text())
    flip_run = json.loads(FLIP.read_text())
    facts = run["facts"]
    f = run["vendor_finding"]
    data = {
        "report": (INCIDENT_DIR / "incident.md").read_text().strip(),
        "rows": [view(r, facts) for r in run["rows"]],
        "flip": view(flip_run["rows"][0], flip_run["facts"]),
        "finding": (f"{f['vendor']} told ExampleCo {f['elapsed_hours']:.0f} hours after it found the incident. The "
                    f"{f['customer']} contract requires ExampleCo to make subcontractors report within "
                    f"{f['limit_hours']} hours ({f['section']}). Check whether {f['vendor']}'s contract says so."),
        "note": NOTE,
    }

    memo = ARTIFACT_LINK.sub("#demo", (ROOT / "MEMO.md").read_text())
    memo_html = markdown.markdown(memo, extensions=["tables", "sane_lists"])
    memo_html = memo_html.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")

    template = (Path(__file__).parent / "template.html").read_text()
    page = template.replace("<!--MEMO-->", memo_html).replace(
        "<!--DATA-->", json.dumps(data).replace("</", "<\\/"))
    out = Path(__file__).parent / "index.html"
    out.write_text(page)
    print(f"Wrote {out.relative_to(ROOT)}, {len(page) // 1024} KB")


if __name__ == "__main__":
    main()

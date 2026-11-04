# Incident Clock: what your contracts require, and by when

A prototype for the first hours after a vendor breach, when the question is who to notify and by when. You describe what happened. Incident Clock reads each customer contract, decides who is owed notice, works out each deadline, and drafts each notice for counsel. Nothing goes to customers without human review.

**[Try the demo](https://claude.ai/artifact/3q22aFqYC36LqojnzfnSYK)** · **[Read the product memo](MEMO.md)**

All companies and contracts are fictional. I designed the agent and the test, and built both with Claude Code.

## The problem

From my online research, Vanta's Customer Commitments shows which customers require notice and how long each notice window is. I worked from public docs, not the product. A person still has to answer three questions:

- **Does this contract apply to this data?** The same de-identified data can be covered by one contract and excluded by another.
- **When did the clock start?** In the test, starting every clock when the company heard about the breach puts one deadline 9 hours too late.
- **Which time limit applies?** One contract has 12-hour, 72-hour and 6-hour terms, and only the 12-hour term is the deadline for notifying the bank.

## The test

A data-labeling vendor finds a login with a stolen credential at 6:00 AM PT and tells the company at 3:00 PM PT. It's now 4:00 PM.

| Customer | Notify? | Deadline | Why |
|---|---|---|---|
| Bank | Yes | Nov 2, 6:00 PM (2 hours left) | The clock started when the vendor found the breach, not when the company heard. |
| Retailer | Yes | Nov 3, 3:00 PM (23 hours left) | This contract came with an acquisition, so 24 hours applies, not the usual 72. |
| Health system | No | n/a | The vendor held only de-identified data, which this contract excludes. Counsel to confirm. |

I wrote the expected answers before writing any agent code, including 19 traps: places where the obvious reading of a contract is wrong. In each of 3 runs, it:

- Got 3 of 3 notify decisions and 2 of 2 deadlines right
- Handled 19 of 19 traps
- Found 71 of 71 required contract commitments, with exact quotes

Cost was about 27 cents per contract to read and 15 cents per customer per incident, at list price on the most capable model.

## Decisions I made

- **The model reads, code decides.** Filtering by data type doesn't settle whether tokenized data counts as bank data. The contract's definition does, and that takes reading it. Code does the deadline arithmetic and checks every quote and recipient against the contract. Anything that fails a check goes to human review.
- **"No" needs the same evidence as "yes."** A wrong no is the costliest mistake, because nobody gets told. To test that, I changed the log so the health data counted as protected, and the answer changed to yes.
- **Draft for counsel, never send.** A notice is a legal statement, so a person reviews each one. I wouldn't send notices automatically at any stage.
- **Use a cheaper model only where code can check the work.** Sonnet reads contracts at under half the cost, because code can verify each quote. Decisions stay on Opus, because no code check can catch a confident wrong no.
- **Left out on purpose:** checking draft contracts before signing, which Vanta already offers, and a fourth and fifth customer, which added reading time without a new kind of judgment.

## What failed, and what's unproven

- **A false sentence in a draft.** My first version wrote "we have instructed that all logs be preserved," which the incident report never said. No check caught it; I found it by reading the drafts. After I changed the instructions, none of the 7 later drafts made that claim.
- **The cheapest model wasn't good enough.** Haiku cost about 1 cent per contract but missed a required commitment in 1 of 3 runs.
- **This shows it passes its own test, not how it does on new contracts.** I wrote the contracts and the expected answers, there's no separate test set, and I adjusted the instructions twice after seeing results. No lawyer has reviewed the legal readings.
- **The hardest part may be the input.** My test uses a clean log of what the vendor held, and most companies may not have one.

## What I'd do next

1. Replay past incidents on real contracts and compare with what counsel decided. This replaces my fictional test with a real one.
2. Offer it for incident drills, where a wrong answer costs nothing.
3. Use it on live vendor breaches, with drafts for counsel.

I'd measure success by the percentage of required notices sent before their deadline, and watch how many no decisions counsel reverses. That number must stay near zero.

<details>
<summary>Run it yourself</summary>

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

.venv/bin/python -m commitments.extract              # read the contracts, write the commitments
.venv/bin/python -m evals.score runs/<dir>           # score them
.venv/bin/python -m commitments.incident             # run the Labelforge incident
.venv/bin/python -m evals.score_incident runs/incidents/<dir> --flip runs/incidents/<flip dir>
.venv/bin/python -m ui.build                         # rebuild the page from recorded runs

.venv/bin/python -m evals.test_score                 # scorer and guardrail tests, no model calls
.venv/bin/python -m evals.test_incident
```

The flip run uses the limited data set log:

```
.venv/bin/python -m commitments.incident --label flip --only AHS \
  --transfer-log fixtures/exampleco/incident-labelforge/labelforge-transfer-log-limited-data-set.csv
```

Model calls need Anthropic credentials, from `ant auth login` or `ANTHROPIC_API_KEY`.

</details>

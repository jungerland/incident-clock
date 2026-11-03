# ExampleCo contract fixtures

Test contracts for the commitments agent, with an answer key for each contract.

- `contracts/` holds the contracts. `exampleco-standard-dpa.md` is ExampleCo's own standard terms, the baseline every customer contract is compared against. Each other file is a customer contract, written in that customer's voice on the customer's own template.
- `answer-key.json` lists, for each contract, every commitment a correct agent should extract (with an exact quote from the contract), how it differs from the DPA, and the traps planted in the contract. Each trap names the correct reading and the wrong one.

All company and vendor names are fictional placeholders: Example National Bank, Labelforge (the data-labeling vendor in the incident story), Model Provider A, Helpdesk Platform. AWS is the only real company named.

## Status

| Contract | Customer | Business unit | Status |
|---|---|---|---|
| `exampleco-standard-dpa.md` | ExampleCo standard terms | all | drafted |
| `example-national-bank-security-addendum.md` | Large US bank, 12-hour notice | Commercial Cloud | drafted |
| (planned) | Example Defense Systems, 72-hour notice plus 90-day evidence preservation | Commercial Cloud | |
| (planned) | Example Health System BAA, 10-day notice, not exposed | Healthcare and Life Sciences | |
| (planned) | Example Retail Group, XYZwire contract (24 hours) and ExampleCo contract (72 hours) | XYZwire | |
| (planned) | Labelforge transfer log | | |
| `incident-labelforge/target-summary.md` | Incident scenario: target output and answer key | | drafted |

The EU bank was dropped (2026-11-03): it repeated the bank's role in the demo.

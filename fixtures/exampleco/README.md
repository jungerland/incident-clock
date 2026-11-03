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
| (planned) | Defense prime, 72-hour notice plus 90-day evidence preservation | Public Sector | |
| (planned) | Health system BAA, 10-day notice | Healthcare and Life Sciences | |
| (planned) | EU bank, "without undue delay" | ExampleCo EU | |
| (planned) | XYZwire customer, 24 hours vs. ExampleCo's 72 hours | XYZwire | |
| (planned) | Incident scenario and its answer key | | |

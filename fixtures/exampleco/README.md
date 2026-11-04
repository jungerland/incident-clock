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
| `example-health-system-baa.md` | Example Health System BAA, 10-day notice, not exposed | Healthcare and Life Sciences | drafted |
| `example-retail-group-xyzwire-dpa.md` | Example Retail Group, XYZwire contract from before the acquisition, 24-hour notice | XYZwire | drafted |
| `incident-labelforge/labelforge-transfer-log.csv` | Labelforge transfer log | | drafted |
| `incident-labelforge/target-summary.md` | Incident scenario: target output and answer key | | drafted |

## Labelforge transfer log

`incident-labelforge/labelforge-transfer-log.csv` is ExampleCo's record of what it sent to Labelforge, its data-labeling vendor. Staff at ExampleCo's customers rate the outputs of the AI agents they run on ExampleCo's platform. Every few months ExampleCo exports a set of those rated examples (one row in the log, called a batch), strips identifiers, and sends it to Labelforge. Labelforge's annotators label each example (correct, wrong, why), and ExampleCo uses the labels to improve that customer's agents. The `exampleco_customer` column names the ExampleCo customer the data came from.

The incident agent uses the log to decide which customers had data at Labelforge and in what form. The contracts then decide whether that form counts.

- `deidentification_method`: `tokenized` (names and account numbers replaced with tokens), `hashed_identifiers` (IP addresses and user IDs hashed), or `hipaa_safe_harbor` (HIPAA's 18 identifiers removed).
- `contains_direct_identifiers` is `no` for every row. That doesn't settle exposure: the bank and retail contracts count de-identified and derived data as their data.
- `held_at_labelforge_until`: when Labelforge deletes the batch. Only batches still held on Nov 2, 2026 were exposed. One retail batch was deleted in May 2026; a later one is still held.

Dropped on 2026-11-03 to keep the demo explainable in a short memo: the EU bank (repeated the bank's role) and the defense prime (needed too much backstory; its evidence-keeping duty is already in the bank contract).

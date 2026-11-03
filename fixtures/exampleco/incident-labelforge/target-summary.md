# Target output: Labelforge incident

This is the summary the agent should produce for the main demo story. It is written before the agent exists, so it doubles as the answer key for the incident scenario. The remaining contracts get written to produce exactly these four rows.

All times Eastern.

---

## What the agent is told

> Labelforge, our data-labeling vendor, emailed us at 3:00 PM today (Nov 2). Someone logged into their annotation platform with a stolen employee credential. Their security team spotted it at 6:00 AM. They don't yet know what was viewed or downloaded.

The agent also has the Labelforge transfer log: which customers' data ExampleCo sent to Labelforge, and in what form. (Fixture still to write.)

**Now:** Nov 2, 4:00 PM.

---

## Summary the reviewer sees

**Labelforge credential breach. 3 customers to notify, 1 not exposed. First deadline in 2 hours.**

| # | Customer | Notify? | Why | Deadline | Also do now | Status |
|---|---|---|---|---|---|---|
| 1 | Example National Bank (Commercial Cloud) | **Yes** | Labelforge held de-identified feedback samples from the bank. The bank's contract counts de-identified data as bank data (2.2) and covers suspected incidents (2.4). | **Nov 2, 6:00 PM** (2h left). The clock started when Labelforge found the breach, not when we heard (2.3). | Phone and email the bank's Cyber Fusion Center, not the relationship manager (6.2). Written updates every 24 hours until contained (6.3). Do not contact the bank's customers or regulators (6.4). | Draft ready for counsel |
| 2 | Example Retail Group (XYZwire) | **Yes, within 24 hours** | Labelforge held samples from XYZwire's anomaly product. The XYZwire contract promises 24 hours; the customer's ExampleCo contract says 72. The XYZwire contract governs XYZwire data. | **Nov 3, 3:00 PM** | Flag for legal: Labelforge was never disclosed as a subprocessor under the XYZwire contract. | Draft ready; conflict flagged |
| 3 | Example Defense Systems (Commercial Cloud) | **Yes** | Labelforge held samples from the prime's supply-chain agents. The prime's contract covers all "Prime Information," not only controlled defense information. | **Nov 5, 3:00 PM** (72 hours from our discovery) | Ask Labelforge today to preserve images of affected systems for 90 days. No report to the Defense Department: no controlled defense information was involved. | Draft ready; preservation request drafted |
| 4 | Example Health System (Healthcare and Life Sciences) | **No** | Labelforge held only samples de-identified under HIPAA's Safe Harbor method. The BAA's notice duties cover protected health information only, and de-identified data is not protected health information. | n/a | Counsel to confirm. Optional courtesy note. | Logged with reason |

**Separate finding:** Labelforge told us 9 hours after it found the breach. The bank contract requires ExampleCo to make subcontractors report within 6 hours (5.3). Check whether Labelforge's contract says so.

Deadlines are calculated in code from the contract terms and the discovery times, not by the model. Every "Why" links to the exact contract wording.

**Eval line (placeholder until the agent runs):** across 4 customer contracts and the standard DPA, X of 48+ commitments found with exact quotes, Y of Z traps handled, 4 of 4 notify decisions correct.

**Scale note:** ExampleCo has about 650 negotiated contracts. This demo runs 4.

---

## Why these four

Each row shows a different kind of judgment:

| Row | What it proves |
|---|---|
| Bank | Reads definitions, not just the notice clause. Gets the clock start right when it differs from contract to contract. |
| XYZwire customer | Spots conflicting terms from an acquisition and picks the one that governs. |
| Defense prime | Notice is not the only duty. Some contracts require action now (keeping evidence) and some duties don't apply (the Defense Department report). |
| Health system | Says no, with a reason. Same facts as the bank, opposite answer, because the contract wording differs. |

## What the remaining contracts must contain

- **Example Retail Group, XYZwire contract:** 24 hours from XYZwire becoming aware (awareness by XYZwire, not its vendors). A subprocessor list without Labelforge. A data definition broad enough to cover feedback samples.
- **Example Retail Group, ExampleCo contract:** on the standard DPA with 72 hours, so the conflict is real.
- **Example Defense Systems:** the prime's own template. 72 hours from the supplier's discovery. "Prime Information" defined broadly. 90-day image preservation. A separate Defense Department reporting clause limited to controlled defense information.
- **Example Health System BAA:** 10 days for breaches of unsecured protected health information, and security incident reporting limited to electronic protected health information. HIPAA's definitions, so de-identified data falls outside.
- **Labelforge transfer log:** one row per customer with data type and form (de-identified, Safe Harbor, none).

# Target output: Labelforge incident

This is the summary the agent should produce for the main demo story. It is written before the agent exists, so it doubles as the answer key for the incident scenario. The remaining contracts get written to produce exactly these three rows.

All times Eastern.

---

## What the agent is told

> Labelforge, our data-labeling vendor, emailed us at 3:00 PM today (Nov 2). Someone logged into their annotation platform with a stolen employee credential. Their security team spotted it at 6:00 AM. They don't yet know what was viewed or downloaded.

The agent also has the Labelforge transfer log: which customers' data ExampleCo sent to Labelforge, and in what form (`labelforge-transfer-log.csv`, one row per batch).

**Now:** Nov 2, 4:00 PM.

---

## Summary the reviewer sees

**Labelforge credential breach. 2 customers to notify, 1 not exposed. First deadline in 2 hours.**

| # | ExampleCo Customer | Notify? | Why | Deadline | Also do now | Status |
|---|---|---|---|---|---|---|
| 1 | Awesome National Bank | **Yes** | Labelforge held de-identified feedback samples from the bank. The bank's contract counts de-identified data as bank data (2.2) and covers suspected incidents (2.4). | **Nov 2, 6:00 PM** (2h left). The clock started when Labelforge found the breach, not when we heard (2.3). | Phone and email the bank's Cyber Fusion Center, not the relationship manager (6.2). Written updates every 24 hours until contained (6.3). Keep all evidence for 1 year (6.5). Do not contact the bank's customers or regulators (6.4). | Draft ready for counsel |
| 2 | Astounding Retail Group | **Yes, within 24 hours** | This customer came with the XYZwire acquisition. Its contract was never moved to our standard terms and promises 24 hours, not our usual 72. | **Nov 3, 3:00 PM** | Flag for legal: Labelforge was never disclosed as a subprocessor under this contract. | Draft ready; deviation flagged |
| 3 | Amazing Health System | **No** | Labelforge held only samples de-identified under HIPAA's Safe Harbor method. The BAA's notice duties cover protected health information only, and de-identified data is not protected health information. | n/a | Counsel to confirm. Optional courtesy note. | Logged with reason |

**Separate finding:** Labelforge told us 9 hours after it found the breach. The bank contract requires ExampleCo to make subcontractors report within 6 hours (5.3). Check whether Labelforge's contract says so.

Deadlines are calculated in code from the contract terms and the discovery times, not by the model. Every "Why" links to the exact contract wording.

**Eval line (placeholder until the agent runs):** across 3 customer contracts and the standard DPA, X of Y commitments found with exact quotes, A of B traps handled, 3 of 3 notify decisions correct.

**Scale note:** ExampleCo has about 650 negotiated contracts. This demo runs 3. The same method applies to other contract families, such as Defense Department flow-down terms.

---

## Why these three

Each row shows a different kind of judgment:

| Row | What it proves |
|---|---|
| Bank | Reads definitions, not just the notice clause. Gets the clock start right when it differs from contract to contract. |
| Retail customer | Finds terms that differ from the standard, even in contracts that came with an acquisition and were never migrated. |
| Health system | Says no, with a reason. Same facts as the bank, opposite answer, because the contract wording differs. |

## What the remaining fixtures must contain

- **Astounding Retail Group, XYZwire contract:** signed with XYZwire before the acquisition. 24 hours from XYZwire becoming aware (awareness by XYZwire, not its vendors, so the clock starts at 3:00 PM when ExampleCo heard). A subprocessor list without Labelforge. A data definition broad enough to cover feedback samples.
- **Amazing Health System BAA:** 10 days for breaches of unsecured protected health information, and security incident reporting limited to electronic protected health information. HIPAA's definitions, so de-identified data falls outside.
- **Labelforge transfer log:** one row per customer with data type and form. Bank: de-identified feedback samples. Retail: feedback samples from XYZwire's anomaly product, which began using ExampleCo's labeling pipeline after the acquisition. Health system: Safe Harbor de-identified samples only.

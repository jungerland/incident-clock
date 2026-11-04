# Labelforge annotation platform accessed with stolen employee credential

**Labelforge annotation platform accessed with stolen employee credential. 1 to notify, 0 with no notice owed. First deadline: Nov 9, 3 PM (167h left).**

All times Pacific. As of Nov 2, 4 PM. Read from the report: Labelforge found it Nov 2, 6 AM, told ExampleCo Nov 2, 3 PM. Not yet known: What data was viewed or downloaded.

| Customer | Notify? | Why | Deadline | Also do now | Status |
|---|---|---|---|---|---|
| Amazing Health System | **Yes** | Both batches Labelforge held are limited data sets, and Section 2.4 makes those PHI. A successful login with a stolen credential to the system holding them is a Security Incident that must be reported to AHS within 5 business days under Section 4.2, even though it is not yet known what data was viewed or downloaded. | **Nov 9, 3 PM** (167h left). 5 business days from when ExampleCo was told (4.2). | After counsel review, send the written Security Incident report to privacy-office@ahs.example with a copy to iso@ahs.example (4.4). Get Labelforge's access logs now and decide quickly whether this is a Breach. If it is, a separate Breach report is due within 10 calendar days of Discovery (4.1). Start collecting affected-individual identities, the PHI involved, the dates and the mitigation steps for both batches (2,700 and 3,100 records) (4.5). Assess whether the intruder's access is an impermissible disclosure that needs a 4.3 report within 10 days of awareness (4.3). | Draft ready for counsel; flagged for legal |

## Amazing Health System

**Also required**
- Pull Labelforge's written subcontractor BAA and use it to require cooperation, logs and reporting (5.1).
- Run and document Security Rule incident response: identify, mitigate and record the incident and its outcome (3.1).
- Keep incident records and vendor communications so they can be produced to HHS (6.2).
- Leave notice to individuals, regulators and media to AHS. Do not contact them directly, and track possible reimbursement costs (4.6).
- If ExampleCo ends or changes the Labelforge relationship, require return or destruction of AHS PHI. Any replacement vendor must meet 3.2 (US only), 3.3 (HITRUST r2) and 5.1 (7.1).

**Contract wording behind the decision**
- Both batches are limited data sets, so they are PHI. (2.4): "A limited data set under 45 C.F.R. § 164.514(e) is PHI for all purposes of this BAA."
- The carve-out covers only safe-harbor de-identification. These batches kept service dates and ZIP codes, so it does not apply. (2.3): "Information de-identified in accordance with this Section 2.3 is not PHI and is not subject to this BAA."
- Covers attempted or successful unauthorized access to ePHI held by a Subcontractor such as Labelforge. (1.2): ""Security Incident" has the meaning given in 45 C.F.R. § 164.304, limited to incidents involving ePHI that Business Associate or its Subcontractors create, receive, maintain or transmit for Covered Entity."
- Labelforge maintains AHS PHI on ExampleCo's behalf, so it is a Subcontractor. (1.3): ""Subcontractor" has the meaning given in 45 C.F.R. § 160.103."
- A report is owed now. Confirmed exfiltration is not required. (4.2): "Business Associate shall report to Covered Entity any Security Incident within five (5) business days after Business Associate becomes aware of it."
- The exception does not apply. The stolen-credential login succeeded. (4.2): "This Section 4.2 serves as notice of, and no further report is required for, unsuccessful attempts such as pings, port scans and blocked log-in attempts that do not result in unauthorized access to ePHI."
- Whether this is a Breach of Unsecured PHI turns on the HIPAA definitions and is still undetermined. (1.1): "Terms used but not defined in this BAA have the meanings given in the HIPAA Rules (45 C.F.R. Parts 160 and 164), including "Breach," "Discovery," "Protected Health Information" ("PHI"), "Electronic Protected Health Information" ("ePHI") and "Unsecured Protected Health Information.""

**For legal**
- ExampleCo sent limited data sets (PHI under 2.4) to Labelforge to "improve the claims-triage agent feature". The BAA ties improvement use to safe-harbor data, and 2.1 limits PHI use to what is "necessary to perform the Underlying Agreements". The disclosure itself may be impermissible and reportable under 4.3. (2.3): "Business Associate may de-identify PHI only in accordance with the safe harbor method at 45 C.F.R. § 164.514(b)(2), and may use the de-identified information only to provide and improve the services under the Underlying Agreements."
- Keeping service dates and ZIP codes in labeling feedback may exceed minimum necessary. (2.2): "Business Associate shall limit its uses and disclosures of PHI to the minimum necessary."

**Open questions**
- What data did the intruder view or download, and over what period was the credential used?
- Is this a Breach of Unsecured PHI after a HIPAA risk assessment? Were the batches encrypted or otherwise secured?
- Is Labelforge an agent of ExampleCo under federal common law? If so, HIPAA Discovery may date from Labelforge's 6:00 AM detection rather than ExampleCo's 3:00 PM notice.
- Does a 4.1 Breach report or the 4.2 Security Incident report govern if both apply, given the BAA has no precedence term?
- Is there a signed subcontractor BAA with Labelforge as Section 5.1 requires?
- Does Labelforge store, process or access AHS PHI only in the US (3.2)? Where was the compromised employee and the login source?
- Does Labelforge hold HITRUST r2 certification for the annotation platform (3.3)?
- Should the scheduled 2026-11-29 removal of batch LF-2026-0602 be paused so the investigation can proceed?
- Do the Underlying Agreements authorize using AHS PHI to improve the claims-triage feature?

Batches held: LF-2026-0602, LF-2026-0915. Deleted before the incident: none.

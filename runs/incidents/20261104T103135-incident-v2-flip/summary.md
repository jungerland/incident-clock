# Labelforge annotation platform accessed with stolen employee credential

**Labelforge annotation platform accessed with stolen employee credential. 1 to notify, 0 with no notice owed. First deadline: Nov 9, 3 PM (167h left).**

All times Pacific. As of Nov 2, 4 PM. Read from the report: Labelforge found it Nov 2, 6 AM, told ExampleCo Nov 2, 3 PM. Not yet known: What data was viewed or downloaded.

| Customer | Notify? | Why | Deadline | Also do now | Status |
|---|---|---|---|---|---|
| Amazing Health System | **Yes** | Labelforge, acting as ExampleCo's subcontractor, held two AHS limited data sets, and this BAA treats limited data sets as PHI for every purpose. Someone logged into Labelforge's platform with a stolen credential, which is a successful unauthorized access and therefore a reportable Security Incident under Section 4.2. Whether it is also a Breach depends on what was viewed or downloaded, and that is not yet known. | **Nov 9, 3 PM** (167h left). 5 business days from when ExampleCo was told (4.2). | Have Labelforge disable the stolen credential and preserve its access and download logs now. The Breach risk assessment and any later Breach report depend on that evidence (4.1). Send the written Security Incident report to privacy-office@ahs.example with a copy to iso@ahs.example within the 4.2 window, after counsel reviews it (4.4). Run the HIPAA breach risk assessment now. Treat Discovery as possibly 6:00 AM Nov 2, when Labelforge spotted the login (4.1). Once Labelforge confirms whether AHS batches were viewed or downloaded, file the 4.3 report within 10 days of learning it (4.3). | Draft ready for counsel; flagged for legal |

## Amazing Health System

**Also required**
- Gather the 4.5 elements: affected individuals, which needs AHS help because names were removed; PHI involved; Breach and Discovery dates; mitigation steps (4.5).
- Send follow-up updates to the same addresses as facts develop. The contract sets no update cadence, so agree one with AHS (4.2).
- Pull Labelforge's written subcontractor BAA and confirm it carries the reporting, US-only and HITRUST terms (5.1).
- Keep a complete incident record, including timeline, communications and the risk assessment, in case HHS reviews it (6.2).
- If ExampleCo ends or narrows its use of Labelforge, require return or destruction of both batches with certification. Do this only after evidence is preserved (7.1).
- Any replacement labeling vendor must sign a written flow-down agreement before receiving AHS PHI, including the US-only (3.2) and HITRUST (3.3) terms (5.1).
- Leave notice to individuals, regulators and media to AHS. Track the reimbursable costs if a Breach is confirmed (4.6).

**Contract wording behind the decision**
- Both batches are limited data sets, so they are PHI for reporting purposes. (2.4): "A limited data set under 45 C.F.R. § 164.514(e) is PHI for all purposes of this BAA."
- Only safe-harbor data is excluded. These batches kept service dates and ZIP codes, so they are not safe harbor. (2.3): "Information de-identified in accordance with this Section 2.3 is not PHI and is not subject to this BAA."
- The definition reaches incidents at Subcontractors that maintain ePHI for AHS. (1.2): ""Security Incident" has the meaning given in 45 C.F.R. § 164.304, limited to incidents involving ePHI that Business Associate or its Subcontractors create, receive, maintain or transmit for Covered Entity."
- Labelforge maintains AHS PHI on ExampleCo's behalf, so it is a Subcontractor. (1.3): ""Subcontractor" has the meaning given in 45 C.F.R. § 160.103."
- Report is owed. The clock runs from ExampleCo's awareness. (4.2): "Business Associate shall report to Covered Entity any Security Incident within five (5) business days after Business Associate becomes aware of it."
- The standing-notice carve-out does not apply. This login succeeded and was not blocked. (4.2): "This Section 4.2 serves as notice of, and no further report is required for, unsuccessful attempts such as pings, port scans and blocked log-in attempts that do not result in unauthorized access to ePHI."
- A separate Breach report applies if the risk assessment finds a Breach. (4.1): "Business Associate shall report to Covered Entity any Breach of Unsecured PHI without unreasonable delay and in no event later than ten (10) calendar days after Discovery."
- Viewing or downloading by the intruder would be an impermissible disclosure. (4.3): "Business Associate shall report to Covered Entity any use or disclosure of PHI not provided for by this BAA within ten (10) calendar days after becoming aware of it."

**For legal**
- The batch records list 'limited_data_set' as their de-identification method. Check whether ExampleCo handled these batches as de-identified, outside the BAA, when it sent them to Labelforge. (2.3): "Business Associate may de-identify PHI only in accordance with the safe harbor method at 45 C.F.R. § 164.514(b)(2)"
- Service dates and ZIP codes were sent to a labeling vendor for reviewer-feedback work. Assess whether that was the minimum necessary. (2.2): "Business Associate shall limit its uses and disclosures of PHI to the minimum necessary."
- Discovery under HIPAA may be imputed from Labelforge's 6:00 AM detection if Labelforge is ExampleCo's agent. The contract also does not say how 4.1 and 4.2 interact. (4.1): "in no event later than ten (10) calendar days after Discovery"
- ExampleCo has potential cost exposure for a Breach caused by its Subcontractor. Consider recovery from Labelforge. (4.6): "Business Associate shall reimburse Covered Entity's reasonable costs of notifying individuals, regulators and the media of a Breach caused by Business Associate or its Subcontractors."

**Open questions**
- Were either of the AHS batches (LF-2026-0602, LF-2026-0915) viewed or downloaded, and could the stolen credential reach them?
- When did the unauthorized access begin, and how long did it last?
- Does the HIPAA risk assessment show a low probability of compromise, or is this a Breach of Unsecured PHI under 4.1?
- Did Labelforge sign a written subcontractor BAA under 5.1, and does it include reporting deadlines, US-only handling and HITRUST terms?
- Was the login made from outside the United States, and does Labelforge store or access the data only in the US (3.2)?
- Does Labelforge's annotation platform hold HITRUST r2 certification (3.3)?
- Is Labelforge ExampleCo's agent under federal agency law, which would set Discovery at 6:00 AM Nov 2?
- Can AHS identify affected individuals from record context, since names and record numbers were removed?
- Was any other AHS data on the platform beyond the two batches listed?
- Will ExampleCo continue, suspend or end the Labelforge relationship?

Batches held: LF-2026-0602, LF-2026-0915. Deleted before the incident: none.

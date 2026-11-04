# Labelforge annotation platform accessed with stolen employee credential

**Labelforge annotation platform accessed with stolen employee credential. 2 to notify, 1 with no notice owed. First deadline: Nov 2, 6 PM (2h left).**

All times Eastern. As of Nov 2, 4 PM. Read from the report: Labelforge found it Nov 2, 6 AM, told ExampleCo Nov 2, 3 PM. Not yet known: What data was viewed or downloaded.

| Customer | Notify? | Why | Deadline | Also do now | Status |
|---|---|---|---|---|---|
| Example National Bank | **Yes** | Labelforge is an Approved Subcontractor holding Bank Data; tokenized data is expressly Bank Data. Unauthorized access to a Subcontractor system holding Bank Data is a Security Incident even before any data access is confirmed, so ExampleCo must notify the Bank's Cyber Fusion Center within 12 hours of Labelforge's own discovery. | **Nov 2, 6 PM** (2h left). PT12H from when Labelforge found it (6.1). | Call +1 (212) 555-0147 and email cfc-thirdparty@enb.example; both are required (6.2). Do not rely on Dana Okafor or a status/trust page for notice (6.2). Do not send incident notice to the relationship manager (Exhibit C). Include Discovery time, Labelforge platform, and data categories in the initial notice (6.3). Schedule written updates to the CFC at least every 24 hours until containment (6.3). Plan the root-cause report; get Labelforge's findings (6.3). Do not contact Bank customers, regulators, law enforcement or media without Bank's written consent (6.4). Tell the Bank before any legally required third-party notice (6.4). Issue a preservation instruction to Labelforge and internal teams (6.5). Ensure Labelforge can provide evidence access on request (6.5). Prepare for a possible post-incident audit (8.4). Track costs; potential reimbursement exposure (6.6). Check Labelforge's contract for the 6-hour flow-down and enforce it (5.3). If replacing Labelforge, give TPRM 90 days' prior notice first (5.2). Be ready to have Labelforge return and destroy the batches if Bank requests (11.1). | Draft ready for counsel; flagged for legal |
| Example Retail Group | **Yes** | A stolen credential was used on Labelforge's annotation platform while it held 6,300 hashed log and trace records from ERG's checkout services. This contract counts logs, traces and derived data as Retailer Data, and counts reasonably suspected access at a third-party processor as a Data Incident. XYZwire must notify ERG Security Operations within 24 hours of becoming aware. | **Nov 3, 3 PM** (23h left). PT24H from when ExampleCo was told (6.1). | Give notice by both email and phone to Retailer Security Operations. (6.2). Do not rely on account or procurement contacts for notice. (6.2). Name Labelforge, describe batch LF-2026-0818, and list the steps actually taken. (6.3). Send supplements as Labelforge learns what was viewed or downloaded. (6.3). Get ERG's written approval before telling ERG's customers, other ExampleCo customers, regulators or anyone else, unless the law requires it. (6.4). Preserve Labelforge logs and evidence, cooperate with ERG's investigation, and expect to bear reasonable costs. (6.5). Prepare for an incident audit by ERG within 10 days of its notice. (8.1). Do not send further ERG data to Labelforge unless ERG gives written consent. (5.1). Any replacement labeling vendor needs a written consent request 30 days ahead, and silence is not consent. (5.2). Confirm or put in place written VDPA-level terms with Labelforge or any successor vendor. (5.3). Handle this under the VDPA, not ExampleCo's standard DPA and its 72-hour confirmed-breach notice. (9.2). | Draft ready for counsel; flagged for legal |
| Example Health System | **No** | Both Example Health System batches at Labelforge were de-identified under the HIPAA Safe Harbor method, and Section 2.3 of the BAA says such information is not PHI and is not subject to the BAA. The BAA's reporting duties cover only PHI or ePHI, so no report is owed for this incident on the facts given. | n/a |  | Logged with reason; counsel to confirm |

**Separate finding:** Labelforge told ExampleCo 9 hours after it found the incident. The Example National Bank contract requires ExampleCo to make subcontractors report within 6 hours (5.3). Check whether Labelforge's contract says so.

## Example National Bank

**Contract wording behind the decision**
- Tokenized feedback batches are Bank Data (2.2): "any data derived from any of the foregoing, including model outputs, embeddings, annotations, and data that has been aggregated, de-identified, pseudonymized or tokenized"
- Covers data Labelforge holds, in any form (2.2): ""Bank Data" means all data and information, in any form, that Supplier or any Subcontractor receives, accesses, creates or processes in connection with the Agreement"
- Stolen-credential login to Labelforge's platform counts now, even though data access is unknown (2.4): "unauthorized access to any system of Supplier or any Subcontractor that stores, processes or transmits Bank Data, whether or not unauthorized access to Bank Data has been confirmed"
- Suspected incidents count (2.4): ""Security Incident" means any actual or reasonably suspected"
- Labelforge is a Subcontractor (2.5): ""Subcontractor" means any third party, including any Supplier Affiliate, that Supplier engages to perform any part of the Services or that has access to Bank Data."
- Labelforge is the Approved Subcontractor holding these feedback samples (Schedule 2): "Only de-identified feedback samples that Bank submits through the Services' feedback feature, for improving Bank's own agents."
- Notice duty and time limit (6.1): "Supplier shall notify Bank of any Security Incident as soon as possible and in no event later than twelve (12) hours after Discovery."
- Labelforge's detection starts the clock (2.3): ""Discovery" means the earliest time at which Supplier or any Subcontractor knew, or by exercising reasonable diligence would have known, of a Security Incident."
- ExampleCo standard DPA terms do not displace these duties (1.2): "This Addendum controls over any conflicting term of the Agreement, any order form, and any data processing addendum, privacy policy, or other document published or provided by Supplier."

**For legal**
- Labelforge took 9 hours to tell ExampleCo; check whether the 6-hour flow-down exists. If it does not, ExampleCo may be in breach. (5.3): "Supplier shall require each Subcontractor to notify Supplier of any Security Incident within six (6) hours after the Subcontractor's Discovery."
- A login with a stolen credential raises whether MFA was enforced on Labelforge's platform (3.3): "Supplier shall require multi-factor authentication for all remote access to systems that store, process or transmit Bank Data."
- Tokenization may be pseudonymization, not de-identification; free-text agent output and analyst comments may contain identifiers. Possible out-of-scope transfer. (Schedule 2): "Bank Data in identifiable form is not permitted."
- Confirm whether the attacker or the compromised employee's access was from outside the US (4.2): "Supplier shall not permit any Supplier Personnel located outside the United States to access Bank Data"
- Possible cost exposure if individuals are affected; consider recovery from Labelforge (6.6): "including costs of notifying affected individuals and providing them with twenty-four (24) months of credit monitoring"
- ExampleCo bears liability for Labelforge's breach and late reporting (5.4): "Supplier remains fully liable to Bank for the acts and omissions of its Subcontractors."

**Repeating duties**
- Every PT24H (6.3): Supplier must give written status updates at least every 24 hours until the incident is contained.

**Open questions**
- What data, if any, was viewed or downloaded, and from which batches?
- Has the incident been contained, and when? Containment starts the root-cause and evidence-retention periods.
- Does ExampleCo's contract with Labelforge contain the 6-hour reporting flow-down and Addendum-equivalent terms?
- Was MFA enforced on the compromised Labelforge account?
- Do agent output text or analyst comments contain identifying information despite tokenization? Does Labelforge hold any token mapping?
- Do any records relate to ENB Securities LLC customers, which would trigger Exhibit D?
- Where were the attacker and the compromised employee located?
- Has anyone at ExampleCo already told Dana Okafor, posted on a status or trust page, or contacted law enforcement or regulators?
- Should ExampleCo suspend Labelforge's access or replace Labelforge, given the 90-day notice requirement?

Batches held: LF-2026-0714, LF-2026-0908, LF-2026-1020. Deleted before the incident: none.

## Example Retail Group

**Contract wording behind the decision**
- Hashed log lines and trace snippets are covered. Hashing does not take them out of scope. (2.2): ""Retailer Data" means all data that Retailer, its employees or its customers provide to Vendor or that Vendor collects from Retailer's systems, including telemetry, logs, traces and metrics, and all data derived from any of it."
- A login with a stolen credential to a platform holding Retailer Data is at least a reasonably suspected incident. (2.3): ""Data Incident" means any actual or reasonably suspected unauthorized access to, or acquisition, disclosure or loss of, Retailer Data, including while held by a Subprocessor."
- Labelforge processed batch LF-2026-0818 on XYZwire's behalf, so it is a Subprocessor. (2.4): ""Subprocessor" means any third party, including any Vendor Affiliate, that processes Retailer Data on Vendor's behalf."
- Notice is owed, with the clock running from Vendor's awareness. (6.1): "Vendor shall notify Retailer of a Data Incident without undue delay and no later than twenty-four (24) hours after Vendor becomes aware of it."

**For legal**
- Labelforge is not in Appendix B or Amendment No. 1. Both batches (Nov 2025 and Aug 2026) appear to have been sent without consent. (5.1): "Vendor shall not permit any Subprocessor other than those listed in Appendix B to process Retailer Data without Retailer's prior written consent."
- The amendment approves only ExampleCo, Inc., not Labelforge. The notice will have to disclose Labelforge under 6.3. (Appendix B): "ExampleCo, Inc. (Vendor Affiliate) | Platform hosting and AI features for the Services | United States"
- Unknown whether Labelforge is bound in writing to VDPA-level terms. (5.3): "Vendor shall bind each Subprocessor in writing to obligations at least as protective as this VDPA"
- Labelforge's storage location is unknown. (3.3): "Vendor shall store Retailer Data only in the United States or Canada."
- Unknown whether Labelforge encrypted the batch at rest. (4.2): "Vendor shall encrypt Retailer Data at rest and in transit using industry-standard encryption."
- Check whether ERG gave written instructions covering third-party annotation. (3.1): "Vendor shall process Retailer Data only to provide the services described in the Subscription Agreement (the "Services") and on Retailer's written instructions."

**Open questions**
- Did the unauthorized session access, view or download batch LF-2026-0818?
- Did ERG ever give written consent to Labelforge outside Amendment No. 1?
- Is there a written agreement binding Labelforge to VDPA-level obligations?
- Where does Labelforge store the data, and was it encrypted at rest?
- Were the hashes of IP addresses and user IDs salted or keyed, or could they be reversed?
- What steps have Labelforge and XYZwire actually taken (credential revoked, sessions killed, logs preserved)? These must go into the notice.
- Should the 24-hour clock be measured conservatively from Labelforge's 6:00 AM detection, given the Subprocessor wording in 2.3?
- Who at XYZwire will make the required phone call to +1 (614) 555-0182?
- Should ExampleCo stop using Labelforge for ERG data, demand deletion of LF-2026-0818 now, and seek ERG's consent for any replacement vendor?

Batches held: LF-2026-0818. Deleted before the incident: LF-2025-1103.

## Example Health System

**Contract wording behind the decision**
- Safe Harbor is the permitted method. Both batches used it, and their stated purpose is to improve EHS's claims-triage agent feature. (2.3): "Business Associate may de-identify PHI only in accordance with the safe harbor method at 45 C.F.R. § 164.514(b)(2), and may use the de-identified information only to provide and improve the services under the Underlying Agreements."
- The batches held at Labelforge fall outside the BAA entirely. (2.3): "Information de-identified in accordance with this Section 2.3 is not PHI and is not subject to this BAA."
- A Security Incident requires ePHI. No ePHI was held, so the 4.2 report is not triggered. (1.2): ""Security Incident" has the meaning given in 45 C.F.R. § 164.304, limited to incidents involving ePHI that Business Associate or its Subcontractors create, receive, maintain or transmit for Covered Entity."
- A Breach report requires Unsecured PHI, which is absent here. (4.1): "Business Associate shall report to Covered Entity any Breach of Unsecured PHI without unreasonable delay and in no event later than ten (10) calendar days after Discovery."
- This report also requires PHI, so it is not triggered. (4.3): "Business Associate shall report to Covered Entity any use or disclosure of PHI not provided for by this BAA within ten (10) calendar days after becoming aware of it."
- PHI takes its HIPAA meaning, which excludes properly de-identified information. (1.1): "Terms used but not defined in this BAA have the meanings given in the HIPAA Rules (45 C.F.R. Parts 160 and 164), including "Breach," "Discovery," "Protected Health Information" ("PHI"), "Electronic Protected Health Information" ("ePHI") and "Unsecured Protected Health Information.""

**For legal**
- Confirm that sending Safe Harbor data to Labelforge for annotation fits this use limit. The stated purpose (improving EHS's claims-triage agent) appears to fit. The BAA itself does not exclude the data, but keep any onward use within this purpose. (2.3): "may use the de-identified information only to provide and improve the services under the Underlying Agreements"
- If Labelforge has ever received EHS PHI (not only Safe Harbor data), confirm a written flow-down agreement exists. That would include the US-only (3.2) and HITRUST (3.3) terms. (5.1): "Business Associate shall ensure that each Subcontractor that creates, receives, maintains or transmits PHI on its behalf agrees in writing to the same restrictions and conditions that apply to Business Associate under this BAA."

**Open questions**
- Confirm that Labelforge's annotation platform held no EHS data other than batches LF-2026-0602 and LF-2026-0915, such as identifiable or limited-data-set records from any other ExampleCo or XYZwire workflow. If any PHI was there, reports under 4.1, 4.2 or 4.3 would be owed to privacy-office@ehs.example with a copy to iso@ehs.example. The 4.2 clock would run 5 business days from ExampleCo's awareness.
- Confirm with ExampleCo Privacy that the free-text reviewer feedback was fully scrubbed of all 18 identifiers. Also confirm ExampleCo had no actual knowledge that the remaining information could identify individuals, which Safe Harbor requires.
- Find out from Labelforge what data the stolen credential was used to view or download, and whether the account could reach other customers' or other ExampleCo data.
- Decide whether to tell EHS voluntarily as a relationship courtesy, even though the BAA requires no report.
- Decide whether to keep batch LF-2026-0915 at Labelforge until 2027-03-14, or ask for earlier deletion given the compromise.

Batches held: LF-2026-0602, LF-2026-0915. Deleted before the incident: none.

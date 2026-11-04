# Labelforge annotation platform accessed with stolen employee credential

**Labelforge annotation platform accessed with stolen employee credential. 2 to notify, 1 with no notice owed. First deadline: Nov 2, 6 PM (2h left).**

All times Pacific. As of Nov 2, 4 PM. Read from the report: Labelforge found it Nov 2, 6 AM, told ExampleCo Nov 2, 3 PM. Not yet known: What data was viewed or downloaded.

| Customer | Notify? | Why | Deadline | Also do now | Status |
|---|---|---|---|---|---|
| Awesome National Bank | **Yes** | Labelforge is an Approved Subcontractor holding tokenized ANB feedback data. That data is Bank Data, and unauthorized access to a Subcontractor system holding Bank Data is a Security Incident even without confirmed access to the data. Notice to the Bank Cyber Fusion Center is owed within 12 hours of Discovery, and Discovery counts from Labelforge's own detection. | **Nov 2, 6 PM** (2h left). 12 hours from when Labelforge found it (6.1). | Call the CFC 24x7 line +1 (212) 555-0147 and email cfc-thirdparty@anb.example now. Both are required, and most of the 12 hours were used before ExampleCo was told (6.2). Do not rely on Dana Okafor or a trust or status page for notice (6.2). Include the Discovery time, Labelforge's annotation platform, and the feedback data categories in the initial notice (6.3). Do not contact Bank customers, regulators, law enforcement or the media without Bank's written consent. Make sure Labelforge does not either (6.4). | Draft ready for counsel; flagged for legal |
| Astounding Retail Group | **Yes** | A stolen credential was used to log into Labelforge's annotation platform while Labelforge held 6,300 records of Astounding Retail Group checkout logs and traces. Under this VDPA, hashed logs and traces are still Retailer Data, and a reasonably suspected unauthorized access to them at a Subprocessor is a Data Incident that must be reported within 24 hours. | **Nov 3, 3 PM** (23h left). 24 hours from when ExampleCo was told (6.1). | Send the counsel-approved notice by email to secops@arg.example and also call +1 (614) 555-0182 before 24 hours pass from 3:00 PM Nov 2 (6.2). Do not route notice through account managers or procurement; only Security Operations counts (6.2). Hold all external statements about this incident, including to other customers, press or regulators, unless ARG approves in writing or the law requires it (6.4). Make sure the notice names Labelforge, describes batch LF-2026-0818 and lists the steps taken (6.3). | Draft ready for counsel; flagged for legal |
| Amazing Health System | **No** | Both Labelforge batches were de-identified by the HIPAA safe harbor method, and under Section 2.3 that data is not PHI and is not subject to the BAA. Every reporting duty in Section 4 (Breach, Security Incident, impermissible use or disclosure) applies only to PHI or ePHI, so no report is owed unless the de-identification turns out to be defective or Labelforge held other AHS data. | n/a | Keep any response handling of the batches, such as forensic copies, retrieval or moving them to another vendor, within the purpose of improving AHS's services (2.3). If the vendor relationship changes and any replacement or forensic vendor would receive AHS PHI, get its written flow-down agreement first (5.1). | Logged with reason; counsel to confirm |

**Separate finding:** Labelforge told ExampleCo 9 hours after it found the incident. The Awesome National Bank contract requires ExampleCo to make subcontractors report within 6 hours (5.3). Check whether Labelforge's contract says so.

## Awesome National Bank

**Also required**
- Instruct Labelforge in writing to preserve all logs, images and forensic evidence, and preserve ExampleCo's own (6.5).
- Schedule written updates to the CFC at least every 24 hours until containment, and require Labelforge to supply the inputs (6.3).
- Prepare for a possible Bank audit on 5 business days' notice (8.4).
- Plan a root-cause report within 30 days of containment, and require Labelforge's cooperation (6.3).
- Make sure Labelforge can give Bank's forensic investigator access to the evidence (6.5).
- Replacing Labelforge with another annotation vendor needs 90 days' notice to tprm-notices@anb.example, with a copy to the Bank Legal Department. Pausing new batches needs no notice (5.2).
- If Bank asks, or if ExampleCo ends the Labelforge relationship, coordinate return and destruction of the ANB batches at Labelforge (11.1).

**Contract wording behind the decision**
- Tokenized analyst feedback batches are Bank Data. (2.2): "any data derived from any of the foregoing, including model outputs, embeddings, annotations, and data that has been aggregated, de-identified, pseudonymized or tokenized"
- Labelforge is a Subcontractor. (2.5): "any third party, including any Supplier Affiliate, that Supplier engages to perform any part of the Services or that has access to Bank Data"
- Labelforge is an Approved Subcontractor for exactly this kind of data. (Schedule 2): "Only de-identified feedback samples that Bank submits through the Services' feedback feature, for improving Bank's own agents."
- A login with a stolen credential to Labelforge's annotation platform is a Security Incident even though data access is unconfirmed. (2.4): "unauthorized access to any system of Supplier or any Subcontractor that stores, processes or transmits Bank Data, whether or not unauthorized access to Bank Data has been confirmed"
- Suspected incidents count. (2.4): ""Security Incident" means any actual or reasonably suspected"
- Labelforge's detection is Discovery. (2.3): "the earliest time at which Supplier or any Subcontractor knew, or by exercising reasonable diligence would have known, of a Security Incident"
- Notice duty and time limit. (6.1): "Supplier shall notify Bank of any Security Incident as soon as possible and in no event later than twelve (12) hours after Discovery."

**For legal**
- Labelforge detected the login at 6:00 AM but did not tell ExampleCo until 3:00 PM, which is 9 hours and past the 6-hour flow-down standard. Check whether the flow-down was imposed and whether Labelforge breached it. (5.3): "Supplier shall require each Subcontractor to notify Supplier of any Security Incident within six (6) hours after the Subcontractor's Discovery."
- ExampleCo bears liability to Bank for Labelforge's late reporting and for the credential compromise, including any resulting delay in the 12-hour Bank notice. (5.4): "Supplier remains fully liable to Bank for the acts and omissions of its Subcontractors."
- Potential cost exposure. Review recovery rights against Labelforge. (6.6): "Supplier shall reimburse Bank's reasonable costs of investigating and responding to a Security Incident caused by Supplier or any Subcontractor, including costs of notifying affected individuals and providing them with twenty-four (24) months of credit monitoring."

**Repeating duties**
- Every 24 hours (6.3): Supplier must give written status updates at least every 24 hours until the incident is contained.

**Open questions**
- Has anyone at ExampleCo already called and emailed the CFC, and who will do it now?
- Were any ANB batches, or other ANB data, viewed or downloaded? When did the unauthorized access begin, and is it contained?
- Should Discovery be treated as earlier than 6:00 AM? Section 2.3 includes when Labelforge 'would have known' with reasonable diligence.
- Does ExampleCo's contract with Labelforge include the 6-hour reporting term and protections at least as strong as the Addendum, as required by 5.3?
- Was MFA required for the compromised Labelforge account, as Section 3.3 requires for remote access to systems handling Bank Data?
- Do the free-text analyst comments or agent output text contain un-tokenized identifiers? Schedule 2 bars identifiable Bank Data at Labelforge.
- Were these batches submitted by Bank through the Services' feedback feature, as Schedule 2 requires?
- Does any batch include customer information of ANB Securities LLC, which would bring in Exhibit D?
- Was the person who logged in, or any Labelforge personnel involved, located outside the US (Section 4.2)?
- Does any law require notice to a third party, which under 6.4 would first need to be raised with Bank?
- Should ExampleCo pause sending new batches to Labelforge or replace it? Replacement triggers the 5.2 90-day notice.

Batches held: LF-2026-0714, LF-2026-0908, LF-2026-1020. Deleted before the incident: none.

## Astounding Retail Group

**Also required**
- Get Labelforge's access logs and session details for the compromised credential now so ExampleCo can support ARG's investigation, and track incident costs (6.5).
- Set up a channel for Labelforge findings and send ARG supplemental notices as facts on viewed or downloaded data emerge (6.3).
- Prepare for a possible incident audit by ARG within 10 days of its notice (8.1).
- Have the current SOC 2 Type II report ready in case ARG requests it (4.3).
- If ExampleCo replaces Labelforge with another annotation vendor, first get ARG's written consent at least 30 days ahead; silence is not consent (5.2).
- Any continuing or replacement annotation vendor must be bound in writing to VDPA-level terms; XYZwire stays liable for Labelforge (5.3).

**Contract wording behind the decision**
- Checkout log lines and trace snippets are Retailer Data, and hashing does not take them out of scope. (2.2): ""Retailer Data" means all data that Retailer, its employees or its customers provide to Vendor or that Vendor collects from Retailer's systems, including telemetry, logs, traces and metrics, and all data derived from any of it."
- A suspected incident counts, so notice is owed even though no data access has been confirmed. (2.3): ""Data Incident" means any actual or reasonably suspected unauthorized access to, or acquisition, disclosure or loss of, Retailer Data, including while held by a Subprocessor."
- Labelforge annotates the ARG batch to improve XYZwire's detectors, so it is a Subprocessor. (2.4): ""Subprocessor" means any third party, including any Vendor Affiliate, that processes Retailer Data on Vendor's behalf."
- Sets the notice duty and the 24-hour limit. (6.1): "Vendor shall notify Retailer of a Data Incident without undue delay and no later than twenty-four (24) hours after Vendor becomes aware of it."
- ExampleCo's standard terms, such as 72-hour notice for confirmed breaches only, do not govern. (1.1): "This VDPA prevails over the Subscription Agreement and over any data processing terms, policies or online terms of Vendor or its Affiliates."
- ExampleCo's standard DPA does not displace the VDPA's 24-hour, suspected-incident standard. (9.2): "Any acquirer's standard terms do not apply to Retailer Data unless Retailer agrees in writing."

**For legal**
- Labelforge is not in Appendix B or Amendment No. 1, yet ARG batches were sent to it on 2025-11-03 and 2026-08-18; no consent appears in the contract. (5.1): "Vendor shall not permit any Subprocessor other than those listed in Appendix B to process Retailer Data without Retailer's prior written consent."
- Even if ExampleCo sent the data to Labelforge, the Amendment approves only ExampleCo, not its onward vendors. (Appendix B): "ExampleCo, Inc. (Vendor Affiliate) | Platform hosting and AI features for the Services | United States"
- The notice must name Labelforge, which will disclose the unapproved Subprocessor; legal should review the wording. (6.3): "Vendor's notice shall describe the Data Incident, the Retailer Data involved, any Subprocessor involved, and the steps Vendor has taken."

**Repeating duties**
- Every 365 days (4.3): Vendor must obtain an annual SOC 2 Type II report covering the Services.

**Open questions**
- Did the stolen credential's session reach batch LF-2026-0818, and was any of it viewed or downloaded?
- When did the unauthorized access begin? Only the 6:00 AM detection time is known.
- Did ARG give written consent to Labelforge anywhere outside this document?
- Did XYZwire or ExampleCo contract with Labelforge, and is Labelforge bound in writing to VDPA-level terms (5.3)?
- Where does Labelforge store the data? Section 3.3 allows only the US or Canada.
- Did Labelforge encrypt the data at rest (4.2)?
- Were the IP and user ID hashes salted or keyed, or could they be reversed?
- Was batch LF-2025-1103 fully deleted at Labelforge, including backups?
- Does any law require notice to third parties, which 6.4 permits without ARG's approval?
- Did anyone at ExampleCo or XYZwire learn of the incident before the 3:00 PM email?
- Will ExampleCo keep using Labelforge for ARG data or pull the batch back?

Batches held: LF-2026-0818. Deleted before the incident: LF-2025-1103.

## Amazing Health System

**Contract wording behind the decision**
- Safe harbor is the permitted method. Both batches used it, and their stated purpose is improving AHS's claims-triage agent. (2.3): "Business Associate may de-identify PHI only in accordance with the safe harbor method at 45 C.F.R. § 164.514(b)(2), and may use the de-identified information only to provide and improve the services under the Underlying Agreements."
- The batches fall outside the BAA entirely. (2.3): "Information de-identified in accordance with this Section 2.3 is not PHI and is not subject to this BAA."
- A Security Incident must involve ePHI, and none was held. (1.2): ""Security Incident" has the meaning given in 45 C.F.R. § 164.304, limited to incidents involving ePHI that Business Associate or its Subcontractors create, receive, maintain or transmit for Covered Entity."
- The Breach duty is limited to Unsecured PHI. (4.1): "Business Associate shall report to Covered Entity any Breach of Unsecured PHI without unreasonable delay and in no event later than ten (10) calendar days after Discovery."
- The impermissible-disclosure duty is also limited to PHI. (4.3): "Business Associate shall report to Covered Entity any use or disclosure of PHI not provided for by this BAA within ten (10) calendar days after becoming aware of it."
- The BAA's scope depends on PHI being present. (Preamble): "It applies to all agreements under which Business Associate creates, receives, maintains or transmits Protected Health Information for or on behalf of Covered Entity (the "Underlying Agreements")."

**Open questions**
- Confirm the safe harbor de-identification actually holds for these batches. Reviewer feedback is free text that may contain names, dates, record numbers or other identifiers. Also confirm ExampleCo had no actual knowledge that the remaining information could identify individuals. If either fails, the data is PHI and the no-notice decision reverses.
- If the data does turn out to be PHI, decide when the clock starts. The Section 4.2 report runs 5 business days from ExampleCo's awareness, which was Nov 2, 3:00 PM PT. The Section 4.1 Breach clock runs 10 days from Discovery, which could be imputed to 6:00 AM if Labelforge is treated as ExampleCo's agent.
- Confirm Labelforge held no other AHS data on the annotation platform beyond these two batches, such as raw PHI, re-identification codes or linking keys, including anything sent by XYZwire.
- Find out from Labelforge what data the intruder viewed or downloaded.
- Decide whether to tell AHS voluntarily as a relationship courtesy, even though the BAA does not require it.

Batches held: LF-2026-0602, LF-2026-0915. Deleted before the incident: none.

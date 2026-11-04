# AWESOME NATIONAL BANK, N.A.
# THIRD-PARTY INFORMATION SECURITY ADDENDUM

**Bank Contract No. ANB-TPRM-2025-0418**
**Supplier:** ExampleCo, Inc. (Commercial Cloud)
**Effective Date:** April 1, 2025

This Third-Party Information Security Addendum ("Addendum") is entered into by Awesome National Bank, N.A., on behalf of itself and its Affiliates ("Bank"), and ExampleCo, Inc. ("Supplier"), and amends the Master Services Agreement between Bank and Supplier dated April 1, 2025 (the "Agreement").

---

## 1. Purpose and Precedence

1.1 This Addendum sets out the minimum information security requirements that apply to Supplier's performance under the Agreement.

1.2 This Addendum controls over any conflicting term of the Agreement, any order form, and any data processing addendum, privacy policy, or other document published or provided by Supplier. Terms incorporated by reference to a Supplier website, including any Supplier trust or security site, do not bind Bank and do not modify this Addendum.

## 2. Definitions

2.1 "Affiliate" means any entity that controls, is controlled by, or is under common control with Awesome National Bank, N.A., including ANB Securities LLC.

2.2 "Bank Data" means all data and information, in any form, that Supplier or any Subcontractor receives, accesses, creates or processes in connection with the Agreement, including (a) data provided by or on behalf of Bank or its customers; (b) metadata, logs and configuration data relating to Bank's use of the Services; and (c) any data derived from any of the foregoing, including model outputs, embeddings, annotations, and data that has been aggregated, de-identified, pseudonymized or tokenized.

2.3 "Discovery" means the earliest time at which Supplier or any Subcontractor knew, or by exercising reasonable diligence would have known, of a Security Incident.

2.4 "Security Incident" means any actual or reasonably suspected (a) unauthorized access to, or acquisition, use, disclosure, alteration or destruction of, Bank Data; or (b) unauthorized access to any system of Supplier or any Subcontractor that stores, processes or transmits Bank Data, whether or not unauthorized access to Bank Data has been confirmed.

2.5 "Subcontractor" means any third party, including any Supplier Affiliate, that Supplier engages to perform any part of the Services or that has access to Bank Data.

2.6 "Supplier Personnel" means employees, contractors and agents of Supplier and of any Subcontractor.

## 3. Information Security Program

3.1 Supplier shall maintain a written information security program that is consistent with the NIST Cybersecurity Framework and the FFIEC Information Technology Examination Handbook.

3.2 Supplier shall encrypt Bank Data at rest using AES-256 or stronger and in transit using TLS 1.2 or higher.

3.3 Supplier shall require multi-factor authentication for all remote access to systems that store, process or transmit Bank Data.

3.4 Supplier shall complete a criminal background check on all Supplier Personnel before granting them access to Bank Data, to the extent permitted by law.

3.5 Supplier shall maintain throughout the term of the Agreement a current SOC 2 Type II report covering the Services.

## 4. Data Location and Offshore Access

4.1 Supplier shall store and process Bank Data only within the United States.

4.2 Supplier shall not permit any Supplier Personnel located outside the United States to access Bank Data, including for support or maintenance, without Bank's prior written approval.

## 5. Subcontractors

5.1 Supplier may permit only the Subcontractors listed in Schedule 2 ("Approved Subcontractors") to access Bank Data, and each only within the scope stated for it in Schedule 2.

5.2 Supplier shall give Bank's Third-Party Risk Management office at least ninety (90) days' prior written notice, delivered as provided in Exhibit C, before adding or replacing any Subcontractor or expanding an Approved Subcontractor's scope. Bank may object within thirty (30) days after receiving the notice. If Bank objects, Supplier shall not engage the Subcontractor for the Services provided to Bank, or Bank may terminate the affected Services without penalty and receive a pro-rata refund of prepaid fees.

5.3 Supplier shall impose on each Subcontractor written obligations at least as protective of Bank Data as this Addendum. Supplier shall require each Subcontractor to notify Supplier of any Security Incident within six (6) hours after the Subcontractor's Discovery.

5.4 Supplier remains fully liable to Bank for the acts and omissions of its Subcontractors.

## 6. Security Incidents

6.1 Supplier shall notify Bank of any Security Incident as soon as possible and in no event later than twelve (12) hours after Discovery.

6.2 Supplier shall give notice under Section 6.1 by telephone and by email to Bank's Cyber Fusion Center as provided in Exhibit C. Notice provided only to Bank's relationship manager, or through a Supplier status page or trust site, does not satisfy Section 6.1.

6.3 Supplier's initial notice shall include all information then known about the Security Incident, including the date and time of Discovery, the systems and Subcontractors involved, and the categories of Bank Data affected or potentially affected. Supplier shall provide written status updates at least once every twenty-four (24) hours until the Security Incident is contained, and shall deliver a written root-cause report within thirty (30) days after containment.

6.4 Supplier shall not notify any Bank customer, regulator, law enforcement agency or the media of a Security Incident involving Bank Data without Bank's prior written consent, unless required by law. Where law requires such notice, Supplier shall inform Bank before giving it, to the extent legally permitted.

6.5 Supplier shall preserve all logs, images and other forensic evidence relating to a Security Incident for at least one (1) year after containment, and shall give Bank and its designated forensic investigator access to that evidence on request.

6.6 Supplier shall reimburse Bank's reasonable costs of investigating and responding to a Security Incident caused by Supplier or any Subcontractor, including costs of notifying affected individuals and providing them with twenty-four (24) months of credit monitoring.

6.7 Supplier's obligations to ANB Securities LLC are supplemented by Exhibit D.

6.8 Where this Addendum, the Agreement, any exhibit or schedule, or applicable law specifies more than one period for the same notice, the shortest period applies.

## 7. Artificial Intelligence and Bank Data

7.1 Supplier shall not use Bank Data to train, fine-tune, evaluate or improve any artificial intelligence or machine learning model, other than a model used solely to provide the Services to Bank.

7.2 Supplier shall not permit any person to review, label or annotate Bank Data for the purpose of developing or improving any model, except as expressly permitted for an Approved Subcontractor in Schedule 2.

7.3 Supplier shall identify in Schedule 2 every third-party model provider that receives Bank Data, and shall ensure that no model provider retains Bank Data after returning a response.

## 8. Testing and Audit

8.1 Supplier shall engage an independent third party to perform a penetration test of the Services at least once every twelve (12) months, and shall deliver an executive summary of the results to Bank within thirty (30) days after Bank's request.

8.2 Supplier shall remediate vulnerabilities rated Critical within fifteen (15) days, and vulnerabilities rated High within thirty (30) days, after identification.

8.3 Supplier shall deliver its SOC 2 Type II report to Bank within thirty (30) days after the report is issued, and a bridge letter on request.

8.4 Bank, its auditors and its regulators may audit Supplier's compliance with this Addendum once in any twelve (12) month period on thirty (30) days' written notice, and at any time after a Security Incident on five (5) business days' written notice. Nothing in this Addendum limits the access of any regulator with authority over Bank.

## 9. Business Continuity

9.1 Supplier shall maintain a business continuity and disaster recovery plan for the Services with a recovery time objective of no more than four (4) hours and a recovery point objective of no more than one (1) hour.

9.2 Supplier shall test the plan at least annually, provide Bank a summary of the results, and participate in Bank's annual operational resilience exercise on sixty (60) days' written notice.

## 10. Insurance

10.1 Supplier shall maintain cyber liability insurance with limits of no less than twenty-five million dollars ($25,000,000) per claim throughout the term of the Agreement and for two (2) years after.

## 11. Return and Destruction of Bank Data

11.1 Within thirty (30) days after termination of the Agreement or Bank's written request, Supplier shall return Bank Data to Bank in the format Bank reasonably requests and then securely destroy all Bank Data, including in backups, held by Supplier and its Subcontractors.

11.2 Within ten (10) business days after destruction, Supplier shall deliver a certificate of destruction signed by an officer of Supplier.

## 12. Survival

12.1 Sections 6, 10 and 11 survive termination of the Agreement for as long as Supplier or any Subcontractor holds Bank Data.

---

## Schedule 2: Approved Subcontractors

| Subcontractor | Service | Permitted scope | Location |
|---|---|---|---|
| Amazon Web Services, Inc. | Infrastructure hosting | All Bank Data, US regions only | United States |
| Model Provider A, Inc. | Large-model inference for AI agent features | Prompts and outputs only; zero retention | United States |
| Labelforge, Inc. | Human annotation of feedback samples | Only de-identified feedback samples that Bank submits through the Services' feedback feature, for improving Bank's own agents. Bank Data in identifiable form is not permitted. | United States; US-based annotators only |
| Helpdesk Platform, Inc. | Support ticketing | Contact details of Bank users only | United States |

---

## Exhibit C: Notices

**Security Incident notices (Section 6.1):** Bank Cyber Fusion Center
- Telephone (24x7): +1 (212) 555-0147
- Email: cfc-thirdparty@anb.example

**Subcontractor notices (Section 5.2):** Third-Party Risk Management office
- Email: tprm-notices@anb.example
- With a copy to: Awesome National Bank, N.A., Legal Department, 100 Example Plaza, New York, NY 10001

**Relationship manager:** Dana Okafor, dana.okafor@anb.example (for routine matters only)

---

## Exhibit D: ANB Securities LLC

D.1 This Exhibit applies to Supplier's processing of customer information of ANB Securities LLC, a broker-dealer registered with the U.S. Securities and Exchange Commission.

D.2 Supplier shall notify ANB Securities LLC as soon as possible, but no later than seventy-two (72) hours after becoming aware of a breach in security resulting in unauthorized access to a customer information system maintained by Supplier.

D.3 This Exhibit supplements, and does not replace, Section 6 of the Addendum.

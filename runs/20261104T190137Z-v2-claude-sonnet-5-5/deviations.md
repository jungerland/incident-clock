# Deviations: agent vs. key

From v2 run 1.

## ANB

**ANB-3.2**
- Key: none (matches standard)
- Agent: The encryption standards match Annex 2. Here the duty covers all Bank Data, a broader category than Customer Data.

**ANB-3.4**
- Key: No DPA equivalent.
- Agent: No DPA equivalent. The DPA requires only written confidentiality obligations for personnel (Section 3.1).

**ANB-3.5**
- Key: Narrower than standard (SOC 2 only, no ISO 27001 requirement).
- Agent: The DPA also commits to ISO/IEC 27001 certification or an equivalent. Here only SOC 2 Type II is required and ISO 27001 is not mentioned.

**ANB-4.1**
- Key: Stricter: covers processing as well as storage, and is fixed to the US rather than a customer-chosen region.
- Agent: The DPA stores data at rest in the customer-selected region and allows access from elsewhere. Here both storage and processing are limited to the US.

**ANB-4.2**
- Key: Conflicts with standard: the Manila support center may not touch Bank Data.
- Agent: The DPA permits access from outside the hosting region, including from Manila, for support, maintenance and security. Here offshore access is prohibited without prior written Bank approval.

**ANB-5.1**
- Key: Stricter: closed list with per-vendor scope instead of general authorization.
- Agent: The DPA gives general authorization to engage Subprocessors. Here only listed Subcontractors are permitted, each limited to its stated scope.

**ANB-5.2**
- Key: Stricter: 90 days vs. 30; direct written notice vs. Trust Center; also covers replacements and scope expansions.
- Agent: The DPA requires 30 days' notice by Trust Center update and email. Here notice must be 90 days, written, and sent to the TPRM office with a copy to Legal. The DPA's urgent-replacement exception (5.4) has no counterpart.

**ANB-5.2-OBJ**
- Key: Stricter: objection is a veto, not just a termination right; refund included.
- Agent: The DPA allows objection within 15 days on reasonable data protection grounds, with termination as the sole remedy after 30 days of failed resolution. Here the objection window is 30 days, no grounds are required, and the Subcontractor is barred for Bank or Bank may terminate with a pro-rata refund.

**ANB-5.3-FLOW**
- Key: No DPA equivalent.
- Agent: No DPA equivalent. The DPA sets no Subprocessor-to-ExampleCo notice period.

**ANB-6.1**
- Key: Much stricter: 12h vs. 72h; clock starts at earliest awareness (including the subcontractor's) rather than ExampleCo's confirmation; covers suspected incidents and all Bank Data, not just personal data.
- Agent: The DPA gives 72 hours after ExampleCo confirms a Personal Data Breach. Here the limit is 12 hours from Discovery, which includes constructive knowledge and Subcontractor knowledge, and covers suspected incidents and unconfirmed access.

**ANB-6.2**
- Key: Different recipient and two required channels.
- Agent: The DPA sends notice to a customer-designated security contact or the account owner. Here notice goes by phone and email to the Bank's Cyber Fusion Center, and other channels do not satisfy the duty.

**ANB-6.3-UPD**
- Key: Stricter: fixed 24h update cadence and a 30-day root-cause report; standard has neither.
- Agent: The DPA says only that further information will be provided as it becomes available, with no fixed interval. Here updates are written and due at least every 24 hours. / No DPA equivalent.

**ANB-6.4**
- Key: No DPA equivalent.
- Agent: No DPA equivalent. The DPA has no restriction on third-party communications.

**ANB-6.5**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-6.6**
- Key: Opposite direction: standard disclaims fault; Bank shifts response costs to ExampleCo.
- Agent: No DPA equivalent. The DPA has no cost reimbursement term, and Section 7.4 says notification is not an admission of fault.

**ANB-7.1**
- Key: Stricter: covers evaluate and improve, any model (not just shared foundation models), and derived data.
- Agent: The DPA bars only training or fine-tuning of foundation models offered to other customers, and lets ExampleCo use Usage Data to improve the Services (8.2). Here the ban covers any AI/ML model and evaluation or improvement, and de-identified data counts as Bank Data.

**ANB-7.2**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-7.3**
- Key: Stricter: no abuse-monitoring exception.
- Agent: The DPA lists model providers as Subprocessors on the Trust Center. Here they must be listed in Schedule 2, and Trust Center listings do not bind the Bank. / The DPA only requires model providers not to retain prompts or outputs beyond the time needed to respond, with an exception for abuse monitoring. Here there is no abuse-monitoring exception, and the duty covers all Bank Data.

**ANB-8.1**
- Key: Stricter: direct delivery with a 30-day deadline instead of Trust Center availability.
- Agent: The DPA also requires an annual independent penetration test, but it makes the summary available on the Trust Center. Here the summary is delivered directly to the Bank within 30 days of request.

**ANB-8.2**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-8.3**
- Key: Stricter: proactive delivery with a deadline instead of Trust Center access.
- Agent: The DPA makes the report available through the Trust Center, subject to Trust Center NDA terms. Here it is delivered to the Bank within 30 days of issuance, and a bridge letter is available on request.

**ANB-8.4**
- Key: Stricter: no regulator precondition, shorter notice, extra post-incident audit right.
- Agent: The DPA treats its reports as satisfying audit rights and allows one on-site audit per 12 months only where a supervisory authority requires it, on 60 days' notice. Here the audit right is unconditional, with 30 days' notice (5 business days after an incident), and extends to the Bank's auditors and regulators.

**ANB-9.1**
- Key: Standard Annex 2 has a plan but no RTO or RPO.
- Agent: Annex 2 requires a BC/DR plan but sets no recovery objectives. Here the RTO is 4 hours and the RPO is 1 hour.

**ANB-11.1**
- Key: Stricter: 30 days vs. 90; includes backups and subcontractors; also triggered by request, not just termination.
- Agent: The DPA deletes Customer Personal Data within 90 days after termination, with backups overwritten within a further 35 days, and has no return duty. Here the period is 30 days, can be triggered by request before termination, requires return first, and covers backups and Subcontractors with no extra backup period.

**ANB-11.2**
- Key: Stricter: automatic, officer-signed, with a deadline.
- Agent: The DPA gives written certification only upon request. Here a certificate signed by an officer is due automatically within 10 business days after destruction.

## ARG

**ARG-3.2**
- Key: Stricter: any model, and covers improving as well as training.
- Agent: The baseline bars only training or fine-tuning of foundation models made available to other customers, and allows use of aggregated Usage Data to improve the Services. This contract bars training or improving any ML model, with a narrow Retailer-only exception, and has no Usage Data carve-out.

**ARG-3.3**
- Key: Fixed to US or Canada rather than a customer-chosen region.
- Agent: The baseline stores data in the hosting region the customer selects. This contract fixes storage to the US or Canada. It has no equivalent of the baseline's 6.2 permission to access data from outside the region, such as Manila.

**ARG-4.1**
- Key: No DPA equivalent.
- Agent: The baseline commits to its own Annex 2 measures, which Vendor may update. This contract sets an external benchmark (CIS IG2) and has no unilateral update right.

**ARG-4.3**
- Key: Stricter: direct delivery with a 15-day deadline instead of Trust Center access.
- Agent: The baseline makes the report available through the Trust Center under NDA terms with no delivery deadline. This contract requires delivery to Retailer within 15 days of request. It does not mention ISO/IEC 27001 certification (baseline 4.2) or an annual penetration test (baseline 9.2).

**ARG-5.1**
- Key: Stricter: closed list and prior consent instead of general authorization.
- Agent: The baseline gives general authorization to engage Subprocessors and publishes a list. This contract requires prior written consent for any Subprocessor not listed in Appendix B and expressly treats Vendor Affiliates as Subprocessors.

**ARG-5.2**
- Key: Stricter: consent required, not notice with a right to object.
- Agent: The baseline gives 30 days' notice via the Trust Center with a 15-day objection right and termination as the sole remedy. This contract requires an affirmative written consent request, silence is not consent, and there is no urgent-replacement exception.

**ARG-5.3**
- Key: Adds a written flow-down requirement.
- Agent: The baseline says ExampleCo remains responsible for Subprocessors' performance of the DPA obligations. This contract adds an express written flow-down requirement and liability for all Subprocessor acts and omissions.

**ARG-6.1**
- Key: Stricter: 24h vs. 72h; awareness rather than confirmation; suspected incidents and all retailer data, not just personal data.
- Agent: The baseline gives 72 hours after ExampleCo confirms a Personal Data Breach. This contract gives 24 hours after awareness, covers reasonably suspected incidents and incidents at Subprocessors, and has no confirmation threshold or exclusion for unsuccessful attempts.

**ARG-6.2**
- Key: Different recipient and two required channels.
- Agent: The baseline sends notice to the security contact designated in the admin console, or else the account owner. This contract requires both email and phone to named Security Operations contacts and rejects notice to account or procurement contacts.

**ARG-6.3**
- Key: Adds a requirement to name the subprocessor, which exposes the undisclosed Labelforge use.
- Agent: Similar to the baseline, but this contract additionally requires identifying any Subprocessor involved, has no 'to the extent then known' qualifier, and sets no deadline for supplements.

**ARG-6.4**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ARG-6.5**
- Key: Opposite direction: standard disclaims fault.
- Agent: No DPA equivalent. / No DPA equivalent.

**ARG-7.1**
- Key: Stricter: 30 days vs. 90; confirmation automatic.
- Agent: The baseline gives 90 days plus 35 days for backups and provides certification only on request. This contract gives 30 days, states no backup extension, and requires written confirmation without a request.

**ARG-8.1**
- Key: Stricter: no regulator precondition, shorter notice, post-incident audit right.
- Agent: The baseline treats reports as satisfying audit rights, with one on-site audit only where a supervisory authority requires it, on 60 days' notice, at Customer's expense. This contract grants a direct annual audit on 30 days' notice and an additional post-incident audit, with no regulator trigger and no stated limits on hours or costs.

## AHS

**AHS-2.3**
- Key: Narrower: Safe Harbor method only, use limited to these services.
- Agent: The DPA lets ExampleCo use aggregated or de-identified Usage Data to operate, secure and improve the Services. The BAA requires the HIPAA safe harbor method and limits use to providing and improving services under the Underlying Agreements, which excludes securing the services. / The DPA excludes Usage Data, defined as aggregated or de-identified data that does not identify Customer or any person, from Customer Personal Data. The BAA excludes only information de-identified by the safe harbor method.

**AHS-3.2**
- Key: Conflicts with standard: the Manila support center may not access PHI.
- Agent: The DPA stores data in the customer-selected region and allows access from outside it, including from Manila, Philippines. The BAA prohibits any storage, processing or access outside the United States. It names no exception for Subcontractors, so the ban appears to apply to them as well (inference).

**AHS-3.3**
- Key: Adds HITRUST r2.
- Agent: The DPA requires a SOC 2 Type II report and ISO/IEC 27001 certification for the Services. The BAA requires HITRUST r2 for PHI systems and does not mention SOC 2 or ISO 27001.

**AHS-4.1**
- Key: Longer than the DPA's 72 hours but stricter than HIPAA's 60 days; limited to PHI.
- Agent: The DPA requires notice within 72 hours after ExampleCo confirms a Personal Data Breach. The BAA allows 10 calendar days after Discovery, which is longer, and covers Breaches of Unsecured PHI rather than confirmed breaches of Customer Personal Data.

**AHS-4.2**
- Key: No DPA equivalent.
- Agent: The DPA has no separate security-incident reporting term and notifies only on a confirmed Personal Data Breach, within 72 hours. The BAA covers any Security Incident, including attempted ones, within 5 business days of awareness rather than confirmation.

**AHS-4.3**
- Key: No DPA equivalent.
- Agent: The DPA has no equivalent for non-breach impermissible uses. It notifies only a confirmed Personal Data Breach, within 72 hours. The BAA gives 10 calendar days from awareness.

**AHS-4.4**
- Key: Different recipients.
- Agent: The DPA sends notice to the security contact designated in the admin console, or else the account owner. The BAA names two fixed email addresses and requires written reports with a copy to the Information Security Office.

**AHS-4.6**
- Key: Opposite direction: standard disclaims fault.
- Agent: No DPA equivalent.

**AHS-5.1**
- Key: Adds a written flow-down requirement for PHI.
- Agent: The DPA makes ExampleCo responsible for its Subprocessors' performance. The BAA requires written flow-down of the same restrictions. The BAA has no Subprocessor notice or objection mechanism like DPA 5.2 to 5.4, so any such rights are not stated in it.

**AHS-7.1**
- Key: Stricter: 30 days vs. 90.
- Agent: The DPA deletes Customer Personal Data within 90 days, with a further 35 days for backups. The BAA requires return or destruction within 30 days, with no separate backup period and no deletion certification term (DPA 10.2).

# Deviations: agent vs. key

From v1 run 1.

## ENB

**ENB-3.2**
- Key: none (matches standard)
- Agent: Same encryption standard, but it is a fixed contractual obligation covering the broader Bank Data definition, rather than only Customer Data.

**ENB-3.4**
- Key: No DPA equivalent.
- Agent: The DPA requires only written confidentiality obligations for personnel. It has no background check requirement.

**ENB-3.5**
- Key: Narrower than standard (SOC 2 only, no ISO 27001 requirement).
- Agent: The DPA requires SOC 2 Type II and ISO 27001, or substantially equivalent successor standards. Here a current SOC 2 Type II is required with no substitution allowed, and ISO 27001 is not required.

**ENB-4.1**
- Key: Stricter: covers processing as well as storage, and is fixed to the US rather than a customer-chosen region.
- Agent: The DPA covers only storage at rest in the customer-selected region. Here both storage and processing are restricted to the US.

**ENB-4.2**
- Key: Conflicts with standard: the Manila support center may not touch Bank Data.
- Agent: The DPA permits access from outside the hosting region, including from the Manila support center, under the SCCs. Here offshore access is prohibited without Bank's prior written approval.

**ENB-5.1**
- Key: Stricter: closed list with per-vendor scope instead of general authorization.
- Agent: The DPA grants general authorization using the Trust Center list. Here there is a closed list with per-subcontractor scope limits.

**ENB-5.2**
- Key: Stricter: 90 days vs. 30; direct written notice vs. Trust Center; also covers replacements and scope expansions.
- Agent: The DPA gives 30 days' notice through a Trust Center update and email to subscribers, and DPA 5.4 allows urgent replacement without prior notice. Here 90 days' direct written notice is required, it also covers scope expansions, and there is no urgent-replacement exception.

**ENB-5.2-OBJ**
- Key: Stricter: objection is a veto, not just a termination right; refund included.
- Agent: The DPA allows objection within 15 days only on reasonable data protection grounds, with termination as the sole remedy after 30 days. Here Bank has 30 days, needs no stated grounds, and Supplier must not engage the Subcontractor; Bank may alternatively terminate without penalty and get a refund.

**ENB-5.3-FLOW**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ENB-6.1**
- Key: Much stricter: 12h vs. 72h; clock starts at earliest awareness (including the subcontractor's) rather than ExampleCo's confirmation; covers suspected incidents and all Bank Data, not just personal data.
- Agent: The DPA allows 72 hours after ExampleCo confirms a Personal Data Breach. Here the limit is 12 hours from actual or constructive knowledge by Supplier or any Subcontractor, and it covers suspected incidents and system intrusions.

**ENB-6.2**
- Key: Different recipient and two required channels.
- Agent: The DPA sends notice to the security contact in the admin console, or to the account owner. Here notice must be by phone and email to a fixed Bank address, and status pages and trust sites are excluded.

**ENB-6.3-UPD**
- Key: Stricter: fixed 24h update cadence and a 30-day root-cause report; standard has neither.
- Agent: The DPA requires further information only as it becomes available. Here written updates are required at least every 24 hours. / The DPA has no root-cause report requirement.

**ENB-6.4**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ENB-6.5**
- Key: No DPA equivalent.
- Agent: No DPA equivalent. / No DPA equivalent.

**ENB-6.6**
- Key: Opposite direction: standard disclaims fault; Bank shifts response costs to ExampleCo.
- Agent: No DPA equivalent. DPA 7.4 says notification is not an acknowledgment of fault, and the DPA has no cost reimbursement.

**ENB-7.1**
- Key: Stricter: covers evaluate and improve, any model (not just shared foundation models), and derived data.
- Agent: The DPA bars only training or fine-tuning of foundation models offered to other customers, and DPA 8.2 lets ExampleCo use aggregated Usage Data to improve the Services. Here any model use (including evaluation and improvement) is barred except Bank-only models, and aggregated or de-identified data counts as Bank Data.

**ENB-7.2**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ENB-7.3**
- Key: Stricter: no abuse-monitoring exception.
- Agent: The DPA lists model providers on the Trust Center. Here they must appear in the contractual Schedule 2. / The DPA allows retention for abuse monitoring and only requires ExampleCo to impose the requirement on providers. Here zero retention must be ensured, with no abuse-monitoring exception.

**ENB-8.1**
- Key: Stricter: direct delivery with a 30-day deadline instead of Trust Center availability.
- Agent: The DPA makes the summary available through the Trust Center. Here it must be delivered directly to Bank within 30 days of request.

**ENB-8.2**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ENB-8.3**
- Key: Stricter: proactive delivery with a deadline instead of Trust Center access.
- Agent: The DPA makes the report available on the Trust Center subject to NDA terms. Here it must be delivered proactively within 30 days, plus bridge letters, and Trust Center terms do not bind Bank.

**ENB-8.4**
- Key: Stricter: no regulator precondition, shorter notice, extra post-incident audit right.
- Agent: The DPA treats reports as satisfying audit rights and allows an on-site audit only when a supervisory authority requires it, with 60 days' notice, at Customer's expense. Here audits are allowed annually on 30 days' notice and after incidents on 5 business days' notice, with no cost-shifting.

**ENB-9.1**
- Key: Standard Annex 2 has a plan but no RTO or RPO.
- Agent: The DPA requires a BC/DR plan with no RTO or RPO targets.

**ENB-11.1**
- Key: Stricter: 30 days vs. 90; includes backups and subcontractors; also triggered by request, not just termination.
- Agent: The DPA allows 90 days for deletion plus 35 more days for backups, with no return and no deletion on request. Here return and full destruction, including backups, are due within 30 days and can be triggered on request.

**ENB-11.2**
- Key: Stricter: automatic, officer-signed, with a deadline.
- Agent: The DPA provides certification only on written request, with no deadline. Here an officer-signed certificate is automatic within 10 business days.

## ERG

**ERG-3.2**
- Key: Stricter: any model, and covers improving as well as training.
- Agent: The baseline bars only training or fine-tuning of foundation models offered to other customers, and 8.2 permits use of Usage Data to improve the Services. The VDPA bars any training or improvement of any model except Retailer-only models, and because derived data is Retailer Data, the Usage Data carve-out is effectively unavailable.

**ERG-3.3**
- Key: Fixed to US or Canada rather than a customer-chosen region.
- Agent: The baseline stores data in the customer-selected region and 6.2 allows access from outside that region, including from Manila. The VDPA fixes storage to the US or Canada. It does not expressly restrict remote access, but Appendix B approves ExampleCo only with a United States location, and the VDPA prevails over DPA 6.2.

**ERG-4.1**
- Key: No DPA equivalent.
- Agent: The baseline points to vendor-defined Annex 2 measures that the vendor may update unilaterally. The VDPA sets an external benchmark (CIS Controls IG2) with no unilateral change right.

**ERG-4.3**
- Key: Stricter: direct delivery with a 15-day deadline instead of Trust Center access.
- Agent: The baseline requires SOC 2 Type II and ISO 27001, or substantially equivalent successor standards. The VDPA requires an annual SOC 2 Type II only, with no successor-standard substitution. / The baseline makes the report available via the Trust Center subject to Trust Center NDA terms. The VDPA requires direct delivery within 15 days, with no NDA condition, and does not treat reports as satisfying audit rights (contrast DPA 9.3).

**ERG-5.1**
- Key: Stricter: closed list and prior consent instead of general authorization.
- Agent: The baseline grants general authorization with a list on the Trust Center. The VDPA uses a closed list and requires prior written consent for anything else.

**ERG-5.2**
- Key: Stricter: consent required, not notice with a right to object.
- Agent: The baseline gives 30 days' notice by Trust Center update and email to subscribers. The customer may object within 15 days (5.3), with termination as the sole remedy, and urgent replacement without prior notice is allowed (5.4). The VDPA requires an affirmative written consent request, treats silence as no consent, and has no urgent-replacement exception.

**ERG-5.3**
- Key: Adds a written flow-down requirement.
- Agent: The baseline has no express written flow-down requirement. The VDPA requires written terms at least as protective as the VDPA, so ExampleCo's standard 72-hour, confirmation-based terms would not suffice. / The baseline makes the vendor responsible only for Subprocessors' performance of DPA obligations. The VDPA imposes liability for all Subprocessor acts and omissions.

**ERG-6.1**
- Key: Stricter: 24h vs. 72h; awareness rather than confirmation; suspected incidents and all retailer data, not just personal data.
- Agent: The baseline gives 72 hours after ExampleCo confirms a Personal Data Breach and excludes unconfirmed or unsuccessful events. The VDPA gives 24 hours from awareness, covers suspected incidents, all Retailer Data and Subprocessor-held data, and prevails over ExampleCo's terms under Section 1.1.

**ERG-6.2**
- Key: Different recipient and two required channels.
- Agent: The baseline sends notice to the security contact designated in the admin console, or else the account owner. The VDPA fixes dual-channel delivery (email and phone) to SecOps and expressly excludes account or procurement contacts.

**ERG-6.3**
- Key: Adds a requirement to name the subprocessor, which exposes the undisclosed Labelforge use.
- Agent: The baseline requires content only to the extent then known and does not require identification of Subprocessors. The VDPA adds Subprocessor identification and has no 'to the extent known' qualifier. / This is substantially similar to the baseline's commitment to provide further information as it becomes available.

**ERG-6.4**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ERG-6.5**
- Key: Opposite direction: standard disclaims fault.
- Agent: No DPA equivalent. / No DPA equivalent. The baseline 7.4 instead states that breach notification is not an acknowledgment of fault or liability.

**ERG-7.1**
- Key: Stricter: 30 days vs. 90; confirmation automatic.
- Agent: The baseline allows 90 days for deletion plus a further 35 days for backups to be overwritten, and covers only personal data. The VDPA requires deletion of all Retailer Data within 30 days, with no backup extension. / The baseline provides certification only on the customer's written request. The VDPA requires written confirmation automatically.

**ERG-8.1**
- Key: Stricter: no regulator precondition, shorter notice, post-incident audit right.
- Agent: The baseline treats SOC 2 and pen-test reports as satisfying audit rights and allows an on-site audit only where a supervisory authority requires one, on 60 days' notice, during business hours, at customer expense. The VDPA gives a direct annual audit right on 30 days' notice with no regulator trigger or cost allocation to Retailer. / The baseline has no incident-triggered audit right. The VDPA allows an expedited audit on 10 days' notice after a Data Incident.

## EHS

**EHS-2.3**
- Key: Narrower: Safe Harbor method only, use limited to these services.
- Agent: DPA 8.2 lets ExampleCo use aggregated or de-identified Usage Data to operate, secure and improve the Services, with no prescribed de-identification method. The BAA requires the HIPAA safe harbor method and limits use to providing and improving the services under the Underlying Agreements. It does not address AI model training (DPA 8.1) or model provider retention (DPA 8.3).

**EHS-3.2**
- Key: Conflicts with standard: the Manila support center may not access PHI.
- Agent: The DPA stores data at rest in the hosting region Customer selects. The BAA imposes a fixed United States-only requirement covering both storage and processing. / DPA 6.2 permits access from outside the hosting region for support, maintenance and security, including from the Manila, Philippines support center, under the Annex 3 transfer mechanism. The BAA prohibits all access to PHI from outside the United States, which rules out the Manila support model for PHI.

**EHS-3.3**
- Key: Adds HITRUST r2.
- Agent: The DPA commits to a SOC 2 Type II report and ISO/IEC 27001, or substantially equivalent successor standards. The BAA requires HITRUST r2 certification specifically, which is not part of the DPA commitment.

**EHS-4.1**
- Key: Longer than the DPA's 72 hours but stricter than HIPAA's 60 days; limited to PHI.
- Agent: The DPA gives 72 hours after ExampleCo confirms a Personal Data Breach. The BAA gives a longer 10 calendar days, but the clock starts at Discovery, which includes constructive knowledge of any workforce member or agent, rather than at confirmation. Breach also covers all Unsecured PHI under the HIPAA presumption, not only confirmed security breaches. Where the Breach involves ePHI, the 5-business-day Security Incident report in Section 4.2 may fall due first.

**EHS-4.2**
- Key: No DPA equivalent.
- Agent: The DPA requires notice only of confirmed Personal Data Breaches and excludes unsuccessful attempts. The BAA requires a report of every Security Incident, including attempted incidents and incidents not confirmed as breaches. The deadline is 5 business days from awareness rather than 72 hours from confirmation.

**EHS-4.3**
- Key: No DPA equivalent.
- Agent: The DPA has no duty to report non-security impermissible uses or disclosures. It notifies only confirmed security breaches within 72 hours of confirmation. The BAA adds this separate 10-calendar-day reporting duty, which runs from awareness.

**EHS-4.4**
- Key: Different recipients.
- Agent: The DPA sends notice to the security contact designated in the administration console, or else to the account owner. The BAA fixes two contractual email addresses and requires written reports to both.

**EHS-4.6**
- Key: Opposite direction: standard disclaims fault.
- Agent: No DPA equivalent.

**EHS-5.1**
- Key: Adds a written flow-down requirement for PHI.
- Agent: The DPA keeps ExampleCo responsible for Subprocessor performance and provides 30-day notice, objection and urgent-replacement mechanics (5.1–5.4). The BAA instead requires a written flow-down of all BAA terms, including US-only storage and access and HITRUST obligations. It has no subcontractor notice or objection mechanism.

**EHS-7.1**
- Key: Stricter: 30 days vs. 90.
- Agent: The DPA deletes data within 90 days after termination, with backups overwritten within a further 35 days, and provides a deletion certificate on request. The BAA requires return or destruction of all PHI within 30 days and makes no separate allowance for backups.

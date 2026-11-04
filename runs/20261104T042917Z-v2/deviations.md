# Deviations: agent vs. key

From v2 run 1.

## ANB

**ANB-3.2**
- Key: none (matches standard)
- Agent: The encryption standard is substantively the same as the DPA, but it applies to all Bank Data rather than Customer Data.

**ANB-3.4**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-3.5**
- Key: Narrower than standard (SOC 2 only, no ISO 27001 requirement).
- Agent: The Addendum requires a current SOC 2 Type II report throughout the term. It does not require ISO/IEC 27001, and it does not allow substitution of successor standards.

**ANB-4.1**
- Key: Stricter: covers processing as well as storage, and is fixed to the US rather than a customer-chosen region.
- Agent: The DPA limits only storage at rest, to a customer-selected region. The Addendum confines both storage and processing to the US.

**ANB-4.2**
- Key: Conflicts with standard: the Manila support center may not touch Bank Data.
- Agent: The DPA permits access from outside the hosting region, including from the Manila support center. The Addendum prohibits offshore access without Bank's prior written approval.

**ANB-5.1**
- Key: Stricter: closed list with per-vendor scope instead of general authorization.
- Agent: The DPA gives general authorization based on the Trust Center list. The Addendum uses a closed list with per-subcontractor scope limits, and Supplier Affiliates are also covered.

**ANB-5.2**
- Key: Stricter: 90 days vs. 30; direct written notice vs. Trust Center; also covers replacements and scope expansions.
- Agent: The DPA requires 30 days' notice via a Trust Center update and email to subscribers. The Addendum requires 90 days' direct written notice to TPRM with a copy to Legal, and it also covers scope expansions. It contains no counterpart to the DPA 5.4 urgent-replacement exception.

**ANB-5.2-OBJ**
- Key: Stricter: objection is a veto, not just a termination right; refund included.
- Agent: The DPA gives 15 days, requires reasonable data protection grounds and makes termination the sole remedy. The Addendum gives 30 days with no grounds required. Supplier must not engage the objected Subcontractor for Bank, or Bank may terminate without penalty and receive a pro-rata refund.

**ANB-5.3-FLOW**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-6.1**
- Key: Much stricter: 12h vs. 72h; clock starts at earliest awareness (including the subcontractor's) rather than ExampleCo's confirmation; covers suspected incidents and all Bank Data, not just personal data.
- Agent: The DPA allows 72 hours, counted from ExampleCo's confirmation of a breach of Customer Personal Data, and excludes unsuccessful attempts. The Addendum allows 12 hours, counted from the earliest actual or constructive knowledge of Supplier or any Subcontractor. It covers suspected incidents and system intrusions involving any Bank Data.

**ANB-6.2**
- Key: Different recipient and two required channels.
- Agent: The DPA sends notice to the security contact designated in the console, or else the account owner. The Addendum requires both telephone and email to the Cyber Fusion Center and excludes relationship-manager-only notice and status page or trust site notice.

**ANB-6.3-UPD**
- Key: Stricter: fixed 24h update cadence and a 30-day root-cause report; standard has neither.
- Agent: The DPA requires further information only as it becomes available. The Addendum requires fixed written updates every 24 hours until containment. / No DPA equivalent.

**ANB-6.4**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-6.5**
- Key: No DPA equivalent.
- Agent: No DPA equivalent. / No DPA equivalent.

**ANB-6.6**
- Key: Opposite direction: standard disclaims fault; Bank shifts response costs to ExampleCo.
- Agent: No DPA equivalent.

**ANB-7.1**
- Key: Stricter: covers evaluate and improve, any model (not just shared foundation models), and derived data.
- Agent: The DPA bars only training or fine-tuning of foundation models made available to other customers, and it allows Usage Data to improve the Services. The Addendum bars training, fine-tuning, evaluation and improvement of any model other than a Bank-only model. Because de-identified data is Bank Data, DPA 8.2 Usage Data use is restricted (inference).

**ANB-7.2**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-7.3**
- Key: Stricter: no abuse-monitoring exception.
- Agent: The DPA lists model providers on the Trust Center. The Addendum requires listing in contractual Schedule 2, which also makes them subject to the 5.2 notice and objection process. / The DPA only 'requires' providers not to retain data and allows an abuse-monitoring exception. The Addendum makes Supplier ensure zero retention and has no exception.

**ANB-8.1**
- Key: Stricter: direct delivery with a 30-day deadline instead of Trust Center availability.
- Agent: The frequency is substantively the same as the DPA's annual testing. / The DPA makes the summary available through the Trust Center. The Addendum requires direct delivery within 30 days of request.

**ANB-8.2**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-8.3**
- Key: Stricter: proactive delivery with a deadline instead of Trust Center access.
- Agent: The DPA makes the report available on the Trust Center, subject to Trust Center NDA terms, which under 1.2 do not bind Bank. The Addendum requires proactive delivery within 30 days. / The DPA has no bridge letter obligation.

**ANB-8.4**
- Key: Stricter: no regulator precondition, shorter notice, extra post-incident audit right.
- Agent: The DPA treats reports as satisfying audit rights and allows an on-site audit only when a supervisory authority requires it, on 60 days' notice and at Customer's expense. The Addendum gives a routine annual audit right to Bank, its auditors and its regulators on 30 days' notice and does not shift the cost to Bank. / The DPA has no post-incident audit right. This audit falls outside the annual limit and requires only 5 business days' notice.

**ANB-9.1**
- Key: Standard Annex 2 has a plan but no RTO or RPO.
- Agent: The DPA requires a BC/DR plan but sets no RTO or RPO. The Addendum sets a 4-hour RTO and a 1-hour RPO.

**ANB-11.1**
- Key: Stricter: 30 days vs. 90; includes backups and subcontractors; also triggered by request, not just termination.
- Agent: The DPA has no data return obligation. / The DPA allows 90 days for deletion, plus a further 35 days for backup overwrite, and is triggered only by termination. The Addendum requires destruction, including backups and Subcontractor copies, within 30 days, triggered by termination or Bank request.

**ANB-11.2**
- Key: Stricter: automatic, officer-signed, with a deadline.
- Agent: The DPA provides a certification only on written request, with no deadline or signatory requirement. The Addendum requires automatic delivery within 10 business days, signed by an officer.

## ARG

**ARG-3.2**
- Key: Stricter: any model, and covers improving as well as training.
- Agent: The DPA bars training or fine-tuning only of foundation models made available to other customers, and under 8.2 allows Usage Data to improve the Services. The VDPA bars training or improving any model unless it serves only Retailer, and the bar reaches derived and aggregated data.

**ARG-3.3**
- Key: Fixed to US or Canada rather than a customer-chosen region.
- Agent: The DPA stores data in whatever region Customer selects. The VDPA fixes storage to the US or Canada. The VDPA does not expressly address remote access, while DPA 6.2 permits access from outside the region, including from Manila. Inference: offshore access is not expressly authorized, and Appendix B lists only US locations for Subprocessors.

**ARG-4.1**
- Key: No DPA equivalent.
- Agent: The DPA refers to its own Annex 2 measures, which ExampleCo may update unilaterally. The VDPA sets an external benchmark, CIS IG2, and gives Vendor no unilateral right to update its measures.

**ARG-4.3**
- Key: Stricter: direct delivery with a 15-day deadline instead of Trust Center access.
- Agent: The DPA requires SOC 2 Type II and ISO/IEC 27001, or equivalent successor standards. The VDPA requires an annual SOC 2 Type II report only, with no ISO 27001 requirement. / The DPA makes the report available through the Trust Center subject to NDA terms, with no delivery deadline. The VDPA requires delivery to Retailer within 15 days of request and states no NDA condition. The VDPA has no equivalent of the DPA 9.2 annual penetration test.

**ARG-5.1**
- Key: Stricter: closed list and prior consent instead of general authorization.
- Agent: The DPA grants general authorization and points to a Trust Center list. The VDPA requires specific prior written consent for any Subprocessor not on Appendix B.

**ARG-5.2**
- Key: Stricter: consent required, not notice with a right to object.
- Agent: The DPA requires 30 days' notice through a Trust Center update and email to subscribers. Under the DPA, Customer must object within 15 days, its sole remedy is termination (5.3), and urgent replacement is allowed without notice (5.4). The VDPA requires an affirmative written consent request, treats silence as no consent, and has no urgent-replacement exception.

**ARG-5.3**
- Key: Adds a written flow-down requirement.
- Agent: No DPA equivalent. / The DPA makes ExampleCo responsible for Subprocessors' performance of DPA obligations. The VDPA makes Vendor liable for all of their acts and omissions.

**ARG-6.1**
- Key: Stricter: 24h vs. 72h; awareness rather than confirmation; suspected incidents and all retailer data, not just personal data.
- Agent: The DPA allows 72 hours, starting after ExampleCo confirms a personal data breach. The VDPA requires notice within 24 hours of Vendor's awareness and covers suspected incidents. Section 1.1 makes this period prevail over any Affiliate DPA.

**ARG-6.2**
- Key: Different recipient and two required channels.
- Agent: The DPA sends notice to the console security contact, or to the account owner as a fallback. The VDPA fixes both the email and telephone channels and expressly says notice to account or procurement contacts is not valid.

**ARG-6.3**
- Key: Adds a requirement to name the subprocessor, which exposes the undisclosed Labelforge use.
- Agent: The DPA requires content only "to the extent then known" and does not require identifying a Subprocessor. The VDPA requires the notice to identify any Subprocessor involved. / Substantially similar to the DPA's commitment to provide further information as it becomes available.

**ARG-6.4**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ARG-6.5**
- Key: Opposite direction: standard disclaims fault.
- Agent: No DPA equivalent. The VDPA also has no counterpart to DPA 7.4, under which notice is not an acknowledgment of fault. / No DPA equivalent.

**ARG-7.1**
- Key: Stricter: 30 days vs. 90; confirmation automatic.
- Agent: The DPA allows 90 days after termination, plus a further 35 days for backups to be overwritten. The VDPA requires deletion of all Retailer Data within 30 days, with no backup extension. / The DPA certifies deletion only on Customer's written request. The VDPA requires written confirmation without any request.

**ARG-8.1**
- Key: Stricter: no regulator precondition, shorter notice, post-incident audit right.
- Agent: The DPA treats reports as satisfying audit rights. It allows an on-site audit only where a supervisory authority requires one, on 60 days' notice and at Customer's expense. The VDPA gives an annual audit right with no regulator trigger, on 30 days' notice, and does not shift costs to Retailer. / The DPA has no expedited post-incident audit right.

## AHS

**AHS-2.3**
- Key: Narrower: Safe Harbor method only, use limited to these services.
- Agent: The DPA lets ExampleCo use aggregated or de-identified Usage Data to operate, secure and improve the Services, with no prescribed de-identification method. The BAA requires the safe harbor method only (not expert determination) and limits use to providing and improving the services under the Underlying Agreements. Operating and securing are not separately listed. / The DPA excludes Usage Data, meaning aggregated or de-identified data that does not identify Customer or any person, with no method requirement. The BAA excludes only data de-identified by HIPAA safe harbor. The BAA does not exclude merely aggregated data.

**AHS-3.2**
- Key: Conflicts with standard: the Manila support center may not access PHI.
- Agent: The DPA stores data at rest in the hosting region Customer selects. The BAA imposes a fixed United States-only requirement covering processing as well as storage. / The DPA permits personnel and Subprocessors to access data from outside the hosting region, including the Manila, Philippines support center, under the Annex 3 transfer mechanism. The BAA prohibits any access to PHI from outside the United States. Inference: Manila-based support could not access PHI.

**AHS-3.3**
- Key: Adds HITRUST r2.
- Agent: The DPA commits to SOC 2 Type II and ISO/IEC 27001, or substantially equivalent successor standards. The BAA requires HITRUST r2 specifically and has no successor-standard substitution.

**AHS-4.1**
- Key: Longer than the DPA's 72 hours but stricter than HIPAA's 60 days; limited to PHI.
- Agent: The DPA allows 72 hours after ExampleCo confirms a breach. The BAA allows 10 calendar days, which is longer. However, the clock starts at HIPAA Discovery, including constructive knowledge through reasonable diligence, rather than confirmation, so it can start much earlier. The BAA also covers non-electronic PHI.

**AHS-4.2**
- Key: No DPA equivalent.
- Agent: The DPA has a single 72-hour deadline after a breach is confirmed. The BAA adds a separate 5-business-day report for any Security Incident from awareness, with no confirmation or compromise threshold.

**AHS-4.3**
- Key: No DPA equivalent.
- Agent: The DPA requires notice only of confirmed Personal Data Breaches, within 72 hours. The BAA separately requires reporting of any impermissible use or disclosure within 10 calendar days of awareness, with no security-breach or confirmation threshold.

**AHS-4.4**
- Key: Different recipients.
- Agent: The DPA sends notice to the security contact designated in the administration console, or else the account owner. The BAA fixes two contractual email addresses and requires written reports, so console contacts alone would not satisfy it.

**AHS-4.6**
- Key: Opposite direction: standard disclaims fault.
- Agent: No DPA equivalent.

**AHS-5.1**
- Key: Adds a written flow-down requirement for PHI.
- Agent: The DPA makes ExampleCo responsible for Subprocessors' performance, gives general authorization, and requires 30 days' notice with an objection right. The BAA requires written flow-down of identical restrictions but contains no subcontractor notice, list or objection mechanism.

**AHS-7.1**
- Key: Stricter: 30 days vs. 90.
- Agent: The DPA deletes within 90 days after termination, with backups overwritten within a further 35 days, and offers no return option. The BAA requires return or destruction of all PHI within 30 days, with no separate backup period. The BAA has no counterpart to the DPA 10.2 deletion certification.

# Deviations: agent vs. key

From v2 run 1.

## ANB

**ANB-3.2**
- Key: none (matches standard)
- Agent: Same TLS 1.2 floor as Annex 2; at rest the standard is AES-256 or stronger, applied to Bank Data.

**ANB-3.4**
- Key: No DPA equivalent.
- Agent: DPA requires only written confidentiality obligations for authorized personnel; this adds a background check before access, to the extent law permits.

**ANB-3.5**
- Key: Narrower than standard (SOC 2 only, no ISO 27001 requirement).
- Agent: DPA requires both a SOC 2 Type II report and ISO/IEC 27001 certification; this requires only the SOC 2 Type II report, maintained for the full term.

**ANB-4.1**
- Key: Stricter: covers processing as well as storage, and is fixed to the US rather than a customer-chosen region.
- Agent: DPA stores Customer Personal Data at rest in the hosting region the customer selects; this requires storage and processing only within the United States.

**ANB-4.2**
- Key: Conflicts with standard: the Manila support center may not touch Bank Data.
- Agent: DPA allows access from outside the hosting region for support, maintenance and security, including from Manila, under the Annex 3 transfer terms; this bars offshore access without Bank's prior written approval.

**ANB-5.1**
- Key: Stricter: closed list with per-vendor scope instead of general authorization.
- Agent: DPA grants general authorization to engage Subprocessors listed on the Trust Center; this allows only Schedule 2 subcontractors, each limited to its stated scope.

**ANB-5.2**
- Key: Stricter: 90 days vs. 30; direct written notice vs. Trust Center; also covers replacements and scope expansions.
- Agent: DPA requires 30 days' notice of new Subprocessors by Trust Center update and email; this requires 90 days' prior written notice to Bank's TPRM office, and also covers scope expansions.

**ANB-5.2-OBJ**
- Key: Stricter: objection is a veto, not just a termination right; refund included.
- Agent: DPA gives the customer 15 days to object on reasonable data protection grounds; this gives Bank 30 days after receiving notice and states no grounds. / DPA makes termination of affected Services the customer's sole and exclusive remedy after 30 unresolved days; this states no sole-remedy limit and adds a pro-rata refund of prepaid fees.

**ANB-5.3-FLOW**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-6.1**
- Key: Much stricter: 12h vs. 72h; clock starts at earliest awareness (including the subcontractor's) rather than ExampleCo's confirmation; covers suspected incidents and all Bank Data, not just personal data.
- Agent: DPA requires notice within 72 hours after ExampleCo confirms a Personal Data Breach; this requires notice within 12 hours after Discovery of any actual or reasonably suspected Security Incident, even if unconfirmed.

**ANB-6.2**
- Key: Different recipient and two required channels.
- Agent: DPA sends notice to the admin-console security contact or the account owner; this requires telephone and email to Bank's Cyber Fusion Center. / DPA 7.2 does not exclude other channels such as a status page or trust site; this expressly excludes relationship-manager notice, status pages and trust sites.

**ANB-6.3-UPD**
- Key: Stricter: fixed 24h update cadence and a 30-day root-cause report; standard has neither.
- Agent: DPA promises further information as it becomes available, with no fixed interval; this sets a 24-hour update cycle until containment. / DPA has no root-cause report requirement; this requires a written root-cause report within 30 days after containment.

**ANB-6.4**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-6.5**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-6.6**
- Key: Opposite direction: standard disclaims fault; Bank shifts response costs to ExampleCo.
- Agent: No DPA equivalent.

**ANB-7.1**
- Key: Stricter: covers evaluate and improve, any model (not just shared foundation models), and derived data.
- Agent: DPA bars training only foundation models made available to other customers and does not restrict Usage Data; this bars use of all Bank Data for training, evaluation or improvement, except for models used solely for Bank.

**ANB-7.2**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-7.3**
- Key: Stricter: no abuse-monitoring exception.
- Agent: DPA lists AI model providers as Subprocessors on the Trust Center; this requires listing every third-party model provider that receives Bank Data in Schedule 2. / DPA requires model providers not to retain prompts or outputs beyond the time needed to respond, except for abuse monitoring; this allows no retention after the response and states no abuse-monitoring exception.

**ANB-8.1**
- Key: Stricter: direct delivery with a 30-day deadline instead of Trust Center availability.
- Agent: DPA requires an annual penetration test with an executive summary posted on the Trust Center; this requires the same annual test. / DPA posts the executive summary on the Trust Center; this requires delivery to Bank within 30 days after Bank requests it.

**ANB-8.2**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ANB-8.3**
- Key: Stricter: proactive delivery with a deadline instead of Trust Center access.
- Agent: DPA makes the report available through the Trust Center subject to non-disclosure terms; this requires delivery to Bank within 30 days after issue, plus a bridge letter on request.

**ANB-8.4**
- Key: Stricter: no regulator precondition, shorter notice, extra post-incident audit right.
- Agent: DPA allows one on-site audit per 12 months on 60 days' notice, during business hours, at the customer's expense, and treats reports as satisfying audit rights; this allows audit by Bank, its auditors and regulators on 30 days' notice, and after a Security Incident on 5 business days' notice, with no business-hours or cost terms.

**ANB-9.1**
- Key: Standard Annex 2 has a plan but no RTO or RPO.
- Agent: Annex 2 says ExampleCo maintains a BCDR plan and tests it annually; this adds a 4-hour recovery time objective and 1-hour recovery point objective.

**ANB-11.1**
- Key: Stricter: 30 days vs. 90; includes backups and subcontractors; also triggered by request, not just termination.
- Agent: DPA has no return-of-data duty and gives 90 days after termination to delete from the Services; this requires return of Bank Data within 30 days. / DPA allows backups to be overwritten within a further 35 days; this requires destruction of backups, and inference suggests within the same 30-day period.

**ANB-11.2**
- Key: Stricter: automatic, officer-signed, with a deadline.
- Agent: DPA gives written deletion certification only on the customer's request; this requires an officer-signed certificate within 10 business days after destruction.

## ARG

**ARG-3.2**
- Key: Stricter: any model, and covers improving as well as training.
- Agent: Baseline 8.1 bars training only foundation models made available to other customers; this bars training or improving any machine learning model, with an exception only for Retailer-only models.

**ARG-3.3**
- Key: Fixed to US or Canada rather than a customer-chosen region.
- Agent: Baseline 6.1 stores data in the hosting region the customer selects; this fixes storage to the United States or Canada. Baseline 6.2 offshore access has no equivalent here.

**ARG-4.1**
- Key: No DPA equivalent.
- Agent: Baseline 4.1 ties security to the measures in Annex 2 and allows unilateral updates; this requires a fixed external standard (CIS IG2) with no unilateral update right stated.

**ARG-4.3**
- Key: Stricter: direct delivery with a 15-day deadline instead of Trust Center access.
- Agent: Baseline 4.2 requires a SOC 2 Type II report and ISO/IEC 27001 certification and 9.1 makes the report available through the Trust Center; this requires only SOC 2 Type II, delivered within 15 days of request and no ISO certification.

**ARG-5.1**
- Key: Stricter: closed list and prior consent instead of general authorization.
- Agent: Baseline 5.1 grants general authorization to engage Subprocessors; this requires Retailer's prior written consent for any Subprocessor not listed in Appendix B.

**ARG-5.2**
- Key: Stricter: consent required, not notice with a right to object.
- Agent: Baseline 5.2 gives notice of a new Subprocessor with an objection right; this requires a consent request and treats Retailer's silence as non-consent.

**ARG-5.3**
- Key: Adds a written flow-down requirement.
- Agent: No DPA equivalent. / Baseline 5.5 makes ExampleCo responsible for Subprocessors' performance of DPA obligations; this makes Vendor liable for Subprocessors' acts and omissions in general.

**ARG-6.1**
- Key: Stricter: 24h vs. 72h; awareness rather than confirmation; suspected incidents and all retailer data, not just personal data.
- Agent: Baseline 7.1 requires notice within 72 hours after ExampleCo confirms a breach; this requires notice within 24 hours after Vendor becomes aware of a Data Incident, including reasonably suspected ones.

**ARG-6.2**
- Key: Different recipient and two required channels.
- Agent: Baseline 7.2 sends notice to the security contact designated in the console or else the account owner; this fixes an email and telephone contact for Retailer Security Operations. / Baseline 7.2 falls back to the account owner when no security contact is designated; this excludes account and procurement contacts from satisfying the notice duty.

**ARG-6.3**
- Key: Adds a requirement to name the subprocessor, which exposes the undisclosed Labelforge use.
- Agent: Baseline 7.3 describes only what is known and omits Subprocessor involvement; this requires the notice to describe any Subprocessor involved. / Baseline 7.3 says ExampleCo will provide further information as it becomes available; this is substantively similar and is listed here as the supplement duty.

**ARG-6.4**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**ARG-6.5**
- Key: Opposite direction: standard disclaims fault.
- Agent: No DPA equivalent. / No DPA equivalent.

**ARG-7.1**
- Key: Stricter: 30 days vs. 90; confirmation automatic.
- Agent: Baseline 10.1 allows 90 days after termination or expiry and a further 35 days for backups; this requires deletion of all Retailer Data within 30 days with no backup carve-out. / Baseline 10.2 requires certification of deletion only on customer request; this requires written confirmation of deletion without a request, within the same 30-day period.

**ARG-8.1**
- Key: Stricter: no regulator precondition, shorter notice, post-incident audit right.
- Agent: Baseline 9.3 limits audits to one on-site audit per 12 months only where a supervisor requires it, on 60 days' notice; this grants an annual audit right on 30 days' notice without a supervisor trigger. / Baseline 9.3 has no post-incident audit right; this allows an audit within 10 days after notice following a Data Incident.

## AHS

**AHS-2.3**
- Key: Narrower: Safe Harbor method only, use limited to these services.
- Agent: BAA allows de-identification only by HIPAA safe harbor and use only to provide and improve the services; DPA 8.2 allows use of Usage Data to operate, secure and improve the Services. / BAA expressly excludes de-identified information from its coverage; DPA 1.6 defines Usage Data as aggregated or de-identified data and does not expressly exclude it from the DPA.

**AHS-3.2**
- Key: Conflicts with standard: the Manila support center may not access PHI.
- Agent: BAA bars storage, processing and access outside the United States; DPA 6.1 keeps data at rest in the selected hosting region and DPA 6.2 permits access from outside it, including Manila.

**AHS-3.3**
- Key: Adds HITRUST r2.
- Agent: BAA requires HITRUST r2 certification; DPA 4.2 requires SOC 2 Type II and ISO/IEC 27001 and does not mention HITRUST.

**AHS-4.1**
- Key: Longer than the DPA's 72 hours but stricter than HIPAA's 60 days; limited to PHI.
- Agent: BAA sets 10 calendar days from Discovery rather than 72 hours after ExampleCo confirms a Personal Data Breach. Inference, not stated in the contract: HIPAA Discovery generally runs from when the breach is known or should reasonably have been known.

**AHS-4.2**
- Key: No DPA equivalent.
- Agent: No DPA equivalent. DPA 7.1 covers only confirmed Personal Data Breaches, with notice within 72 hours.

**AHS-4.3**
- Key: No DPA equivalent.
- Agent: No DPA equivalent.

**AHS-4.4**
- Key: Different recipients.
- Agent: BAA sends reports to the Privacy Office with a copy to the Information Security Office; DPA 7.2 sends notice to the security contact designated in the Services administration console, or to the account owner if none.

**AHS-4.6**
- Key: Opposite direction: standard disclaims fault.
- Agent: No DPA equivalent.

**AHS-5.1**
- Key: Adds a written flow-down requirement for PHI.
- Agent: BAA requires a written flow-down of the same restrictions; DPA 5.5 makes ExampleCo responsible for Subprocessors' performance but has no written flow-down requirement.

**AHS-7.1**
- Key: Stricter: 30 days vs. 90.
- Agent: BAA requires return or destruction of all PHI within 30 days; DPA 10.1 allows 90 days after termination, with backups overwritten within a further 35 days.

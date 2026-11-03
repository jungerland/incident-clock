# ExampleCo (Mid-Market Edition): Demo Company Profile, Version 2

Re-evaluated November 3, 2026. This version replaces version 1 (an AI customer-servicing platform for financial services), which is section 5 of `vanta-commitments-exampleco-research.md`. The enterprise edition is in `exampleco-enterprise-profile.md`. Supporting research is in `vanta-commitments-exampleco-research.md`.

**How to read this:** cited facts link to their sources. Everything about the fictional company itself (its size, customers, frameworks, contracts and scenarios) is my inference, designed to fit those facts.

---

## Why version 1 was re-evaluated

Version 1 started from ExampleCo's original customer-success positioning and moved it toward financial-services buyers. It never tested whether a customer-facing product was the best choice. This version scores industries from scratch, ignoring that positioning.

## Industry re-evaluation (mid-market, roughly 150–400 employees)

Scoring criteria, all judgments mine:
- **Vanta push:** how many of Vanta's push segments the company falls into.
- **Commitments value:** how many and how varied the negotiated security terms would be at this size.
- **Mid-market fit:** whether it looks like a company in Vanta's strongest segment.
- **Contrast with enterprise:** whether it gives the demo toggle a clearly different story.

| Candidate | Vanta push | Commitments value | Mid-market fit | Contrast with enterprise edition | Verdict |
|---|---|---|---|---|---|
| Customer-success / CX SaaS (original ExampleCo) | Low | Low: mostly sells to tech companies on its own paper | High | Medium | Rejected |
| AI customer servicing for financial services (version 1) | AI, financial services, EU | High | High | High | Strong, but customer servicing is rarely a bank's most critical vendor function |
| **AI fraud and AML platform for banks and fintechs** | **AI, financial services, EU** | **Highest for a single industry** (see below) | **High** | **High: one industry, deep rules vs. many industries, broad rules** | **Chosen** |
| Defense tech (like Nominal) | Government | Medium-high, but defense terms are standardized by DFARS flow-down clauses | Medium | Low: enterprise edition already has a Public Sector unit | Runner-up |
| AI-native horizontal app (e.g. AI agents for legal or ops) | AI | Medium: AI addenda, but buyers' rules vary less | High | Medium | Not chosen |
| Health tech | Healthcare | Medium: BAAs are fairly templated | Medium | Medium | Not chosen: about 3–4% of Vanta's detected customers ([Bloomberry](https://bloomberry.com/data/vanta/)) |
| HR / payroll SaaS | Low | Medium-high: SSNs and bank accounts | High | Medium | Not chosen |

### Why fraud and AML wins
- **It falls into two of Vanta's push segments.** Vanta has a fintech solution built around DORA and names fintech customers BVNK, MoonPay, Ramp and Taptap Send ([Vanta Fintech](https://www.vanta.com/solutions/fintech)). It also claims 60% of the Forbes AI 50 as customers ([Vanta, Apr 29, 2026](https://www.vanta.com/resources/vanta-crosses-300m-in-arr-as-growth-accelerates)).
- **Banks have to take fraud and AML vendors seriously.** Fraud detection and transaction monitoring are hard for a bank to replace. Under DORA, a service that supports a "critical or important function" needs an exit strategy and extra contract terms ([AFM](https://www.afm.nl/en/sector/themas/belangrijke-europese-wet--en-regelgeving/dora/derde-aanbieders)). Whether a given fraud or AML service counts as critical is each bank's call. That it usually does is my inference.
- **It brings rules that most SaaS vendors never face:**
  - **Bank incident notice.** A bank service provider must notify each affected bank "as soon as possible" after an incident that disrupts covered services for four or more hours. The bank then has 36 hours to notify its regulator ([OCC 12 CFR 53.4](https://www.ecfr.gov/current/title-12/part-53/section-53.4); [Federal Register, Nov 23, 2021](https://www.federalregister.gov/documents/2021/11/23/2021-25510/computer-security-incident-notification-requirements-for-banking-organizations-and-their-bank)).
  - **Model risk.** Revised interagency guidance issued in April 2026 replaces SR 11-7. It says "vendor and third-party models are subject to the same model risk management principles as internally developed models." Generative and agentic AI are outside its formal scope but "should follow a banking organization's established risk management and governance practices" ([KPMG summary, Apr 2026](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/model-risk-management-revised-interagency-guidance-reg-alert.pdf)). The guidance itself doesn't specify contract terms. Banks writing model documentation, change notice and validation access into vendor contracts is my inference.
  - **SAR confidentiality.** A suspicious activity report (SAR), and any information that would reveal one exists, "are confidential, and may not be disclosed except as specified" ([FinCEN](https://bsaefiling.fincen.gov/docs/FinCENSARElectronicFilingRequirements.pdf)). That makes AI subprocessors and offshore support very sensitive.
  - **New York and AI.** NYDFS guidance covers contractual limits on vendors using data for AI model training ([NYDFS, Oct 21, 2025](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20251021-guidance-managing-risks-third-party)).
- **It mirrors the incident question in Vanta's lead Commitments testimonial.** Perforce's CISO: "who do we need to notify, and by when?" ([Vanta, Feb 25, 2026](https://www.vanta.com/resources/introducing-customer-commitments)).

---

## Company profile

| Attribute | ExampleCo (Mid-Market Edition) |
|---|---|
| **Product** | ExampleCo Sentinel, an AI fraud and AML platform. It scores payments in real time with machine-learning models (ACH, wires, cards, RTP/FedNow, SEPA Instant). It also handles transaction monitoring and alert case management, and offers an AI investigator copilot that summarizes cases and drafts SAR narratives. |
| **Customers** | About 190: 120 US community and regional banks and credit unions, 45 fintechs and banking-as-a-service sponsor banks, and 25 EU e-money and payment institutions (Ireland, Netherlands, Lithuania). About 70 are on contracts the customer drafted or heavily negotiated, mostly banks. |
| **Deployment** | Shared multi-tenant AWS in US and EU regions; dedicated single-tenant setups for the 10 largest banks. |
| **Employees** | About 260. The GRC team of 5 is led by a Head of GRC who reports to the CISO. A Head of Model Governance answers bank model-validation requests. |
| **Stage / scale** | Series C (2026), about $55M ARR. |
| **Frameworks held** | SOC 2 Type II, including the Processing Integrity criterion because fraud scores must be accurate; ISO 27001; PCI DSS as a service provider; ISO 42001 in progress. A GDPR program. DORA appears as obligations passed down from EU customers. |
| **Customer data stored** | Transaction data (amounts, counterparties, account numbers, tokenized card numbers); customer identity details (names, dates of birth, addresses, partial tax IDs); device and behavioral signals; alerts, cases and investigator notes; SAR drafts and other SAR-revealing information; model features and scores; AI copilot prompts and outputs. |
| **Key subprocessors** | AWS, a large-model provider for the copilot, a device-intelligence data provider, a support platform. |
| **People in the demo** | Head of GRC; Head of Model Governance; General Counsel; CISO. |

**Rough scale of the problem (inference):** Vanta says a single contract "can contain 50+ commitments" ([Vanta What's New](https://www.vanta.com/whats-new)). At about 70 negotiated contracts, that's 3,500 or more commitments for a GRC team of 5.

---

## Commitments to seed in the demo

| Commitment type | How it varies across ExampleCo's contracts | Real-world basis |
|---|---|---|
| Incident notification | Baseline "as soon as possible" for disruptions of 4+ hours; negotiated 4h or 12h for large banks; 24h for any suspected data exposure; 72h for EU customers | [OCC 12 CFR 53.4](https://www.ecfr.gov/current/title-12/part-53/section-53.4); [NYDFS](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20251021-guidance-managing-risks-third-party) |
| Model change notice | 30 or 60 days before material changes to a model; release notes plus updated model documentation | [Revised model risk guidance (KPMG summary)](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/model-risk-management-revised-interagency-guidance-reg-alert.pdf), with contract terms as my inference |
| Model validation support | Annual documentation package; quarterly performance and drift reports; access for the bank's independent validator | Same as above |
| SAR data handling | SAR-revealing data never sent to subprocessors; US-only storage and access; no offshore support access | [FinCEN SAR confidentiality](https://bsaefiling.fincen.gov/docs/FinCENSARElectronicFilingRequirements.pdf) |
| AI use of customer data | No training of shared models on one bank's data without consent; disclosure of which model providers are used | [NYDFS](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20251021-guidance-managing-risks-third-party) |
| Subprocessor notice | 30 days' notice with a right to object (fintechs); 60 days plus prior approval (banks); DORA notice of subcontracting changes (EU) | [AFM on DORA Art. 30](https://www.afm.nl/en/sector/themas/belangrijke-europese-wet--en-regelgeving/dora/derde-aanbieders) |
| Resilience and exit | Exit plan and transition help; business-continuity test participation; threat-led penetration test (TLPT) cooperation for EU customers where the service is critical | [AFM](https://www.afm.nl/en/sector/themas/belangrijke-europese-wet--en-regelgeving/dora/derde-aanbieders) |
| Testing and audit | Annual pen-test summary vs. full report under NDA; on-site audit rights; SOC 2 report delivered within 30 days of issue | Inference, based on common practice |
| Data deletion | 30 or 90 days after termination, with a certificate; records held longer where banks must keep them | [NYDFS](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20251021-guidance-managing-risks-third-party) |

---

## Demo stories

**1. New model and new AI provider (main story).** ExampleCo plans to ship fraud model version 4 and move the copilot to a second large-model provider. The agent:
- finds the 41 contracts that require advance notice of model changes, grouped into 30-day and 60-day windows;
- flags 9 bank contracts where SAR-revealing data in copilot prompts would break the rule against sending it to subprocessors;
- lists the EU customers who need a DORA subcontracting notice;
- drafts the notices and assembles the model documentation packet.

The Head of Model Governance and the Head of GRC see one shared view.

**2. Outage triggers the bank notification rule.** A 5-hour slowdown hits real-time scoring. The agent works out which banks are owed notice under the 4-hour federal rule, and which contracts set a shorter, negotiated window. It ranks them by deadline and pulls each bank's designated point of contact from the contract.

**3. Redline check.** A regional bank's draft contract asks for 4-hour notice of any incident and quarterly model validation access. The agent compares this with ExampleCo's incident-response tests and its model-governance calendar, flags the terms ExampleCo can't meet, and suggests fallback wording.

---

## Toggle comparison

| | ExampleCo (Mid-Market) | ExampleCo Enterprise |
|---|---|---|
| Industry | AI fraud and AML for banks and fintechs (one industry, deep rules) | Horizontal data and AI platform for regulated enterprises (many industries) |
| Employees | ~260 | ~2,600 |
| Stage / ARR | Series C, ~$55M | Pre-IPO Series F, ~$420M |
| Negotiated contracts | ~70 | ~650 across 5 business units |
| Frameworks | SOC 2 Type II (with Processing Integrity), ISO 27001, PCI DSS, ISO 42001 (in progress) | 12+ including FedRAMP Moderate, CMMC L2, HITRUST, PCI DSS, C5 |
| Unusual commitments | Model change notice, SAR confidentiality, 4-hour bank incident rule | DFARS 72h reporting with 90-day evidence preservation, residency that differs by business unit, inherited contracts from an acquisition |
| Main story | A model and AI-provider change triggers notices | Incident triage across business units and an acquired company |
| Strategic message to Vanta | Commitments helps a team of 5 handle bank-grade obligations | Commitments helps win enterprise accounts from Drata |

---

## Naming note

This fictional company was renamed from Acme to ExampleCo. Vanta publishes a real case study for **Acme Technology**, a 5–10 person Singapore fintech that builds bank integrations and holds ISO 27001 ([Vanta customer story](https://www.vanta.com/customers/acme-technology)). Because the mid-market edition is also a fintech vendor, reviewers at Vanta could have confused the two.

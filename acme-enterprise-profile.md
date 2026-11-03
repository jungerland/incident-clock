# Acme Enterprise: Demo Company Profile

Prepared November 3, 2026. This is a separate company from Acme (Mid-Market Edition, version 2) in `acme-midmarket-profile.md`, so the demo can switch between the two. Supporting research and full citations are in `vanta-commitments-acme-research.md`.

**How to read this:** cited facts link to their sources. Everything about the fictional company itself (its size, customers, frameworks, contracts and scenarios) is my inference, designed to fit those facts.

---

## Industry choice: an enterprise data and AI platform

Acme's current customer-success positioning had no influence on this choice. I scored candidate industries on two questions: how many of Vanta's push areas the company falls into, and how much Customer Commitments would be worth to it.

| Candidate industry | Vanta push areas covered | Contract-term variety (inference) | Verdict |
|---|---|---|---|
| **Horizontal data and AI platform selling to regulated industries** | Enterprise, AI, government, financial services, healthcare, EU | Highest: each buyer industry brings its own rules (DORA, NYDFS, SEC Reg S-P, DFARS, HIPAA), all in one contract set | **Chosen** |
| Fintech / banking software vendor | Financial services, EU, often AI | High, but limited to one rule family | Strong second; used by the mid-market edition (AI fraud and AML) |
| Defense / government contractor software | Government | Strict but more standardized through contract clauses (FAR/DFARS) | Narrow |
| Health tech | Healthcare | BAAs are heavy but fairly templated | Smallest Vanta segment (about 3–4% of detected customers) |

Why this industry is the most valuable for Vanta:
- **It falls into every push area at once.** Vanta is pushing into enterprise ([Vanta, Nov 18, 2025](https://www.vanta.com/resources/introducing-vantas-agentic-trust-platform)), AI ([Vanta, Apr 29, 2026](https://www.vanta.com/resources/vanta-crosses-300m-in-arr-as-growth-accelerates)), government ([Vanta, Apr 28, 2026](https://www.vanta.com/resources/from-pilot-to-moderate-lessons-from-vantas-fedramp-20x-journey)) and EU regulation ([Vanta DORA](https://www.vanta.com/products/dora)). One company that sells to all of those buyers exercises every part of the product. This is inference.
- **It matches Vanta's named enterprise and Commitments customers.** Vanta names Snowflake (data cloud) and Samsara as enterprise customers ([Vanta, Apr 29, 2026](https://www.vanta.com/resources/vanta-crosses-300m-in-arr-as-growth-accelerates)). Perforce, its lead Commitments customer, is a software company with 2,000+ employees, six frameworks and 14 audits ([Perforce case study](https://www.vanta.com/customers/perforce)).
- **It targets Vanta's competitive gap.** YipitData's spend panel shows Drata ahead of Vanta in enterprise, 45 to 31 ([YipitData, May 13, 2026](https://www.yipitdata.com/resources/vanta-vs-drata-compliance-software-2026)).
- **It uses the most of the platform (inference).** A company like this would plausibly buy Compliance, Trust Center, Questionnaires, Customer Commitments, Organizations Center and VantaGov. That makes it the largest kind of contract Vanta can win.

---

## Company profile

| Attribute | Acme Enterprise |
|---|---|
| **Product** | Acme Data Cloud, a governed data platform with an AI agent builder on top. Enterprises use it to bring in, store and analyze operational data, then build AI agents that work on it (fraud review, claims triage, clinical operations, supply chain). |
| **Deployment options** | Shared commercial cloud on AWS, Azure and GCP; an EU sovereign region; a GovCloud environment; and bring-your-own-cloud, where the platform runs in the customer's own account. |
| **Business units** (each a separate Vanta organization, joined in Organizations Center) | 1. Commercial Cloud. 2. Acme Public Sector (federal and defense). 3. Healthcare and Life Sciences. 4. Acme EU (Dublin and Frankfurt entities). 5. Pipewire, an observability startup acquired in 2025 that still runs on its own systems and contracts. |
| **Employees** | About 2,600. Security has about 90 people, GRC 14 (a VP of GRC plus GRC leads for each business unit), and legal 30, including a Deputy GC for commercial contracts. |
| **Stage / scale** | Late-stage and pre-IPO: Series F in 2025, about $420M ARR, IPO targeted for 2027, so SOX readiness is under way. |
| **Customers** | About 2,100. Around 650 are on contracts the customer drafted or heavily negotiated. These include about 120 financial institutions (US and EU), 45 federal agencies and defense prime contractors, 90 health systems and pharma companies, and 300 of the Fortune 1000. |
| **Frameworks held** | SOC 2 Type II for each business unit; SOC 1 Type II; ISO 27001, 27017, 27018 and 27701; ISO 42001; FedRAMP Moderate (Public Sector); CMMC Level 2 (Public Sector); HIPAA and HITRUST r2 (Healthcare); PCI DSS as a service provider; C5 (Germany); NIS 2. DORA appears as obligations passed down from EU bank customers. |
| **Customer data stored** | Customer-loaded enterprise datasets, which can include health records (PHI), tokenized card data, controlled unclassified defense information (CUI), consumers' financial data (NPI) and EU personal data. Also customers' employee identities, AI model prompts and outputs, models fine-tuned on customer data, encryption keys the customer manages, and audit logs. |
| **Key subprocessors** | AWS, Azure, GCP, two large-model providers, a support platform, a data-labeling vendor, and an offshore support center. |
| **People in the demo** | CISO; VP of GRC; GRC leads for each business unit; Deputy GC who runs the redlining of contract terms; incident commander. |

**Rough scale of the problem (inference):** Vanta says a single contract "can contain 50+ commitments" ([Vanta What's New](https://www.vanta.com/whats-new)). At about 650 negotiated contracts, Acme Enterprise would be tracking more than 30,000 commitments across five business units.

---

## Commitments to seed in the demo

Each one comes from a real rule or common contract term. The variation between customers is what makes the demo interesting.

| Commitment type | How it varies across Acme's contracts | Real-world basis |
|---|---|---|
| Breach notification | 12h or 24h (large banks); 72h (SEC-regulated firms); 72h to DoD, passed through prime contractors; 10 days under a negotiated BAA, against HIPAA's 60-day limit; "without undue delay" (EU) | [SEC Reg S-P](https://www.sec.gov/rules/final/2024/34-100155.pdf); [DFARS 252.204-7012](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.); [Ballard Spahr on HIPAA](https://www.ballardspahr.com/insights/alerts-and-articles/2024/01/hipaa-breach-notifications-a-question-of-timing) |
| Forensic evidence preservation | Keep images of affected systems for at least 90 days for defense customers | [DFARS 252.204-7012](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.) |
| Subprocessor notice | 30, 60 or 90 days' notice; some with a right to object or terminate; some requiring listed approval of any offshore access | [NYDFS, Oct 21, 2025](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20251021-guidance-managing-risks-third-party) |
| Data residency | EU-only for EU banks; US-only with US-person access for federal and defense customers | [AFM on DORA Art. 30](https://www.afm.nl/en/sector/themas/belangrijke-europese-wet--en-regelgeving/dora/derde-aanbieders); [DFARS 252.204-7012](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.) |
| AI use of customer data | No training on customer data; no fine-tuning without written consent; disclosure of which model providers are used | [NYDFS, Oct 21, 2025](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20251021-guidance-managing-risks-third-party) |
| Testing and audit | Annual pen-test summary vs. full report under NDA; on-site audit rights; DORA threat-led penetration test (TLPT) cooperation; business-continuity test participation | [AFM on DORA Art. 30](https://www.afm.nl/en/sector/themas/belangrijke-europese-wet--en-regelgeving/dora/derde-aanbieders) |
| Data deletion | 30 or 90 days after termination, with a certificate of destruction; exit assistance for DORA customers | [NYDFS](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20251021-guidance-managing-risks-third-party); [AFM](https://www.afm.nl/en/sector/themas/belangrijke-europese-wet--en-regelgeving/dora/derde-aanbieders) |
| Certification maintenance | Keep SOC 2, ISO 27001, FedRAMP Moderate or HITRUST active; deliver reports within set windows | Inference, based on common practice |

---

## Demo stories

**1. Incident at a shared subprocessor (main story).** A data-labeling vendor reports that someone accessed its systems using stolen credentials. The agent:
- finds which business units and customers had data with that vendor, including Pipewire contracts that were never migrated;
- ranks notification deadlines, earliest first: bank customers at 12h and 24h, then the defense 72h path, then BAA customers at 10 days;
- flags the defense contracts that require 90-day evidence preservation;
- drafts customer notices for each business unit and shows the combined view in Organizations Center.

This story directly answers the question Perforce's CISO says comes first in an incident: "who do we need to notify, and by when?" ([Vanta, Feb 25, 2026](https://www.vanta.com/resources/introducing-customer-commitments)).

**2. Redline checked against reality (deal-desk story).** A top-10 bank's draft contract asks for 6-hour breach notice and an EU-only AI model provider. The agent compares the draft with Acme's current incident-response tests and its list of subprocessors. It flags two terms Acme cannot meet today and suggests fallback wording. Vanta says the product can analyze a draft contract against a company's live compliance program ([Vanta Help Center](https://help.vanta.com/en/articles/13931299-managing-customer-commitments)).

**3. Combining an acquired company (Organizations Center story).** The agent loads Pipewire's 140 contracts, maps their commitments onto Acme's standard commitment types, and highlights conflicts. One example is Pipewire promising 24h breach notice to a shared customer whose Acme contract says 72h.

---

## Toggle comparison

| | Acme (Mid-Market) | Acme Enterprise |
|---|---|---|
| Industry | AI fraud and AML for banks and fintechs (one industry, deep rules) | Horizontal data and AI platform for regulated enterprises (many industries) |
| Employees | ~260 | ~2,600 |
| Stage / ARR | Series C, ~$55M | Pre-IPO Series F, ~$420M |
| Negotiated contracts | ~70 | ~650 across 5 business units |
| Frameworks | SOC 2 Type II (with Processing Integrity), ISO 27001, PCI DSS, ISO 42001 (in progress) | 12+ including FedRAMP Moderate, CMMC L2, HITRUST, PCI DSS, C5 |
| Unusual commitments | Model change notice, SAR confidentiality, 4-hour bank incident rule | DFARS 72h reporting with 90-day evidence preservation, residency that differs by business unit, inherited contracts from an acquisition |
| Main story | A model and AI-provider change triggers notices | Incident triage across business units and an acquired company |
| Strategic message to Vanta | Commitments helps a team of 5 handle bank-grade obligations | Commitments helps win enterprise accounts from Drata |

Before building the demo, check that every framework listed above is available in Vanta. I couldn't load Vanta's framework catalog page to confirm SOC 1, 27017, 27018 and 27701. I did confirm FedRAMP, CMMC, HITRUST, DORA, NIS 2, ISO 42001 and C5 in the earlier research.


Naming caution: Vanta has a real customer story for "Acme Technology," a small Singapore fintech ([Vanta](https://www.vanta.com/customers/acme-technology)). Consider a distinct product name or a short note saying Acme is fictional.

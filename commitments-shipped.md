# What Vanta Customer Commitments Ships Today

Researched 2026-11-03. Sources are Vanta's own pages. [DOC] = help center or changelog. [MKT] = marketing only. Some changelog entries came from a summary, not verbatim text; verify before quoting in an interview.

## Timeline

| Date (2026) | Feature |
|---|---|
| Feb 25 | Launch ("Introducing Customer Commitments"), add-on, gated access |
| Mar | Structured commitments, auto-tracking |
| Apr | REST API for contracts, auto account assignment, standard commitments |
| May | Onboarding flow, SharePoint ingestion (before: Ironclad only) |
| Jun 21 | Alpha: contract gap analysis (draft or executed contract) |
| Jun 28 | Agent support, read-only |
| Jul | Custom commitment types, MCP support, Salesforce ingestion, analysis against GRC program |
| Aug | Agent-led custom type creation; analysis "available to all customers for purchase" |

## What it does [DOC]

- **Extraction:** 6 structured types (audit rights, data deletion/return, data residency/use, frameworks/certifications, security incident and breach notices, subprocessor change notices) plus ~31 unstructured types (one free-text summary each). Citations to the source contract.
- **Inventory:** commitments tied to a contract and a customer account. Standard vs. non-standard terms, compared against your default terms.
- **Draft preview:** upload a draft to see what it would commit you to, without adding it to the inventory.
- **Contract analysis:** each commitment checked against controls, policies, knowledge base, tests, documents. Output: Covered / Gap / Unclear, consequence High / Medium / Low, "Have you accepted this before?" Point-in-time; rerun replaces results.
- **Review:** acknowledge, or flag for redline; the agent can suggest redline wording; agent memory keeps acknowledgment reasons.
- **Ingestion:** Ironclad, Salesforce, SharePoint, manual PDF, API. Google Drive on the roadmap.
- **Notifications:** upload summaries, weekly digest, unassigned-account emails. That's all.

## Confirmed by online research (2026-11-03)

- **Incident lookup:** a manual filter on the commitment inventory. You filter by event type and affected data to see which customers require notice, their notification windows (such as 24 or 72 hours), and their contacts.
- **Deadlines:** each customer's notification window is extracted, but I found no deadline computed from discovery time.
- **Tracking notified customers:** unconfirmed.

## Not documented (marketing promises only, or absent)

- **Deadline tracking.** The window is listed (24h, 72h), but no clock or due date computed from discovery time. [MKT] promises "who needs to be notified, by when."
- **Incident workflow.** A person filters by hand. Nothing takes incident facts and works out which contracts are triggered (suspected vs. confirmed, which data is in the affected system), drafts notices, or tracks whether each notice went out. A customer quote (Perforce) asks to "plug into our incident response workflows."
- **Operating data.** Analysis checks design coverage (is there a control or policy?), not whether the company actually does it. [MKT] claims "continuous assurance."
- **Real alerts.** [MKT] "24/7 monitoring and proactive alerts"; no alert types in the docs.

## Perforce (the customer quote)

Launch blog, 2026-02-25, verbatim:

> "When an incident happens, the first question is always: who do we need to notify, and by when? To manually dig through our top customer contracts during a crisis is not sustainable. Customer Commitments simplifies that completely by making those obligations clear and actionable upfront—it's exactly the kind of structure we need to plug into our incident response workflows." (Aaron Kiemele, CISO, Perforce)

Perforce case study (https://www.vanta.com/customers/perforce): DevOps platform, Minneapolis, 2,000+ employees, Vanta customer since 2024. 20+ products, multiple business units, six frameworks (ISO 27001/27018, SOC 2, TISAX, NIST CSF, ISO 42001), plans to consolidate 14 audits in Vanta. Uses Trust Center, Questionnaire Automation, Vendor Risk, Risk Management, Custom Frameworks, Access Reviews. The case study does not mention Customer Commitments; the blog quote reads as a need, not a confirmed deployment.

## Sources

- https://www.vanta.com/products/customer-commitments
- https://help.vanta.com/en/articles/13931299-managing-customer-commitments
- https://www.vanta.com/resources/introducing-customer-commitments
- https://www.vanta.com/whats-new
- https://help.vanta.com/en/articles/11345422-product-updates
- https://community.vanta.com/x/vanta-product-updates/msg_mLH6bpA3XpPn/vanta-now-supports-sharepoint-integration-for-auto

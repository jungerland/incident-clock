**PRODUCT MEMO**

# Notice Clock: an incident notification agent

When a vendor is breached, the first question is who to notify and by when. Vanta's Customer Commitments lists each customer's notification window. A person still has to decide which contracts apply, work out when each clock started, and write each notice. I built an agent that does that work. You tell it what happened. It reads each contract, decides who is owed notice, calculates each deadline in code, and drafts each notice for counsel. In a test with three fictional customers and one vendor breach, it got all 3 notify decisions and both deadlines right in each of 3 runs.

**The test incident:** Labelforge, a data-labeling vendor, finds a login with a stolen credential at 6:00 AM on Nov 2 and tells the fictional company, ExampleCo, at 3:00 PM. It doesn't yet know what was viewed. The time now is 4:00 PM Eastern.

| Customer | Notify? | Why | Deadline | Also do now |
| --- | --- | --- | --- | --- |
| Example National Bank | **Yes** | Labelforge held tokenized feedback samples. The contract counts tokenized and de-identified data as bank data (2.2) and covers suspected incidents (2.4). | **Nov 2, 6:00 PM** (2 hours left). The clock started when Labelforge found the breach, not when ExampleCo heard (2.3). | Phone and email the Cyber Fusion Center, not the relationship manager (6.2). Send written updates every 24 hours (6.3). Don't contact the bank's customers or regulators (6.4). |
| Example Retail Group | **Yes** | This contract came with an acquisition and never moved to ExampleCo's standard terms (9.2). Derived logs and traces count as retailer data (2.2). | **Nov 3, 3:00 PM** (23 hours left). 24 hours, not ExampleCo's usual 72, from when ExampleCo heard (6.1). | Email and phone Security Operations (6.2). For legal: Labelforge was never approved under this contract (5.1), and the notice must name it (6.3). |
| Example Health System | **No** | Labelforge held only data de-identified by HIPAA's Safe Harbor method. This contract says that data is not protected health information and is not subject to the contract (2.3). | n/a | Counsel to confirm. |

I shortened the wording in this table by hand. The numbers in parentheses are contract sections. Tokenized means names and account numbers were replaced with tokens. Safe Harbor means 18 kinds of identifier were removed. The [demo](https://claude.ai/artifact/3q22aFqYC36LqojnzfnSYK) shows the agent's unedited output, the contract wording behind each decision, and the draft notices.

## The problem

Aaron Kiemele, Perforce's CISO, describes the problem in Vanta's launch post: "When an incident happens, the first question is always: who do we need to notify, and by when?" He calls Customer Commitments "exactly the kind of structure we need to plug into our incident response workflows."

Vanta's sales team told me what ships today: "During an incident, you can filter by event type and affected data to see which customers require notice, their contractual notification windows (such as 24 or 72 hours), and notification contacts." I couldn't find a deadline calculated from discovery time, and the sales team wasn't sure whether notified customers are tracked.

A list of windows would show 12 hours, 24 hours and 10 days for these customers. It leaves three questions open, and these are the ones that decide the outcome:

- **Does this contract apply to this data?** De-identified data is covered by the bank's contract and outside the health system's.
- **When did the clock start?** The bank's clock started at 6:00 AM, when the vendor found the breach. The retailer's started at 3:00 PM, when ExampleCo heard. A person who starts both at 3:00 PM plans for a bank deadline 9 hours too late.
- **Which term governs?** The bank's contract also has a 72-hour term in an exhibit and a 6-hour term for subcontractors. Neither is the deadline for notifying the bank.

## What I built

A working prototype with an eval. Try the [demo](https://claude.ai/artifact/3q22aFqYC36LqojnzfnSYK), or see the [code and full results](https://github.com/jungerland/vanta-commitments).

It runs in two steps. The first reads each contract once and extracts its commitments, each with a quote and how it differs from the company's standard terms. The second runs when an incident happens and uses that list, the contract text, and a log of what was sent to the vendor.

I wrote the expected answers before writing any agent code, including 19 traps: places in the contracts where the obvious reading is wrong. Across the 3 customer contracts and the standard terms, in each of 3 runs:

- 71 of 71 required commitments found with exact quotes
- 19 of 19 traps handled
- 3 of 3 notify decisions and 2 of 2 deadlines correct

Of 416 quotes the model proposed, one wasn't word for word in the contract, and code rejected it. Cost at list price on the most capable model was about 27 cents per contract to extract and 15 cents per customer per incident.

The agent also flagged something I hadn't put in my expected answers, in 2 of 3 runs. The bank's contract allows Labelforge only de-identified data, the log shows tokenized data, and the contract lists those as different things. That may be a transfer the bank never allowed.

## Product decisions

1. **Start from the incident, not a filter.** The person says what happened in plain words. The agent works out which contracts are affected, because that's the slow part during an incident.
2. **The model reads, code decides.** The model is good at judgment: does tokenized feedback count as bank data? It's the wrong place for the final say. Code works out which data the vendor held, checks every quote and recipient against the contract, takes the time limit from the extracted commitment, and does the deadline arithmetic. Anything that fails a check goes to human review.
3. **"No" needs the same evidence as "yes."** A wrong no is the costliest mistake here, because nobody gets told. So the health system's no cites contract wording and depends on how the data was de-identified. To test that, I changed the log to say a limited data set, which this contract treats as protected. The answer changed to yes.
4. **Draft for counsel, never send.** A notice is a legal statement. My first version wrote "we have instructed that all logs be preserved" in the bank's draft, which the incident report never said. No check caught it. I found it by reading the drafts. The instructions now tell the agent to leave a placeholder for steps taken, and none of the 7 later drafts made that claim. A code check can't catch every false sentence, so human review of each notice stays.
5. **Read definitions from the contract at incident time.** Extraction was steady on deadlines and recipients, but varied between runs on definitions and subprocessor tables. Those are the parts that decide hard cases, so the incident step reads the contract itself.

## What I deprioritized, and why

- **Checking draft contracts before signing.** Vanta already ships a draft preview and contract analysis. Incident response is where I found the biggest gap.
- **More contract types.** I cut a fourth and fifth customer because they added reading time without adding a new kind of judgment.

## What I'd build next

1. **Tracking sent and overdue notices.** The prototype shows time left and marks a passed deadline as overdue, but it can't record that a notice went out. It also needs to track repeating duties, like the bank's 24-hour updates.
2. **A vendor replacement check.** Pulling a breached vendor can set off its own notices. The bank's contract requires 90 days' notice with no emergency exception. The agent raises this today, but nothing tracks it.
3. **Learning from counsel's edits.** Each changed decision is a case where someone confirmed the right answer, and it should become a test.

## How I'd measure it

- **North star:** the percentage of required notices sent before their contractual deadline.
- **Guardrail:** the number of no decisions that counsel reverses. This must stay near zero as the agent handles more of the work.
- **Numbers the team can move week to week:**
  - **Time to first draft:** minutes from reporting an incident to a draft ready for counsel.
  - **Decisions kept:** how often counsel keeps the agent's decision and deadline unchanged.
  - **Human review rate:** how often a code check sends a row to human review.
- **Business:** Commitments adoption and retention. I'd compare renewal for two groups: customers who have run an incident or drill through the agent, and customers who haven't.

## How I'd roll it out

1. **Replay past incidents.** Run the agent on customers' real contracts and past incidents, and compare it with what their counsel decided. This replaces my fictional test with a real one.
2. **Incident drills.** Offer it for tabletop exercises, where a wrong answer costs nothing and teams see their real deadlines.
3. **Live incidents, with drafts for counsel.** Start with vendor breaches. Every decision shows its contract wording.

I wouldn't send notices automatically at any stage.

## Open questions

- Where does the "what did this vendor hold" answer come from? My test uses a clean log. Most companies may not have one, and that could be the hardest part of the product.
- Who makes the call during an incident: GRC, security or legal? That decides whose queue this belongs in.
- Does Commitments track which customers were notified? The sales team wasn't sure.
- In my test where the health data was protected, the agent chose the 5-business-day Security Incident term, not the 10-day breach term I expected. Its reasoning holds together, but a lawyer should check it. It's one run.

## Caveats

The contracts, the log and the expected answers are fictional. I designed them and the agent, and built both with Claude Code, so the test may share my blind spots. There's no separate test set. I adjusted the instructions twice to fit results I'd seen: once to catch a term extraction missed, and once to stop the false statement in Decision 4. These results show the agent passes its own test, not how it will do on new contracts. No lawyer has reviewed the legal readings. The agent also extracted terms my expected answers left out, so I don't report a precision number. Of the ones I read, most were real contract terms. Vanta's behavior comes from its public pages and a sales chat, not from using the product.

## Sources

- [Vanta, Introducing Customer Commitments, Feb 25, 2026](https://www.vanta.com/resources/introducing-customer-commitments)
- [Vanta Help Center, Managing customer commitments](https://help.vanta.com/en/articles/13931299-managing-customer-commitments)
- Vanta sales chat, Nov 3, 2026

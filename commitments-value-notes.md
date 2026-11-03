# Understanding Customer Commitments

Notes from a side conversation about what makes Vanta's Customer Commitments product valuable, and how that affects Acme's profile in the demo.

---

## Question 1

> Please elaborate on this point: "Customer Commitments gets its value from something else: how many tough, negotiated contracts a company signs with demanding buyers."

### Answer

What makes Customer Commitments valuable is less how big a company is and more how many different promises it has made to customers, and how costly breaking one would be. This is my inference from how the product works, but Vanta's own materials back it up.

#### What the product actually saves

Customer Commitments reads contracts, pulls out the security obligations, tracks them, and warns you when something triggers them, such as an incident, a subprocessor change, or a pen-test request. It can also check a draft contract against what your security program can actually deliver. So the value comes from three things:

- Time saved hunting through contracts.
- Penalties or lost trust avoided, for example missing a 24-hour breach notice.
- Deals closed faster because you know what you can safely agree to.

#### Four things that drive that value

1. **How many contracts differ from your standard terms.** If every customer signs your standard data processing agreement (DPA), one answer covers all of them, and a spreadsheet works. Vanta built the product around this: you define your "standard commitments," and it flags where customers deviate ([Vanta Help Center](https://help.vanta.com/en/articles/13931299-managing-customer-commitments)).
2. **How many commitments each contract holds.** Vanta says one contract can contain "50+ commitments" ([Vanta What's New](https://www.vanta.com/whats-new)).
3. **How often events trigger them.** Incidents, new subprocessors, annual pen tests, audits and renewals each force someone to ask, "which customers do we owe what, and by when?"
4. **How costly a miss is.** Short notice windows, audit rights, termination rights and regulator involvement turn a forgotten clause into a business risk.

A rough way to think about it (my own framing, not Vanta's):

> value ≈ contracts that deviate × commitments per contract × how often they're triggered × cost of a miss

#### Why "negotiated" and "demanding buyers" matter

Large and regulated buyers usually make vendors sign their own security addenda, not the vendor's standard terms. That is the main reason contracts end up different from each other. Some buyers have no choice:

- EU banks must include certain contract terms under DORA Article 30 ([AFM](https://www.afm.nl/en/sector/themas/belangrijke-europese-wet--en-regelgeving/dora/derde-aanbieders)).
- New York regulators (NYDFS) list terms they expect in vendor contracts ([NYDFS, Oct 21, 2025](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20251021-guidance-managing-risks-third-party)).
- SEC-regulated firms must require 72-hour breach notice from service providers ([SEC final rule, 2024](https://www.sec.gov/rules/final/2024/34-100155.pdf)).

A bank's contract is therefore longer, stricter and different from the next bank's.

#### Why company size is a weak stand-in

- A 75-person vendor selling to the military and aerospace companies can carry heavier obligations than a 3,000-person company selling self-serve on its own terms. Vanta's Nominal case study says more than 75% of Nominal's customers require or track compliance metrics ([Vanta, Nominal case study](https://www.vanta.com/customers/nominal)).
- Perforce's CISO talks about digging through "our top customer contracts" during an incident. The pain comes from those negotiated accounts, not from headcount ([Vanta, Feb 25, 2026](https://www.vanta.com/resources/introducing-customer-commitments)).

Size still matters in one way. A company needs someone who owns GRC and the budget for a paid add-on. A large enterprise vendor that also sells to demanding buyers gets the most value of all, because it has many negotiated contracts and many triggering events. That's why the enterprise version of Acme is a strong option too.

---

## Question 2

> The following two statements seem to relate to the points you just made. Is that correct? If so, what does paper mean in this context?
>
> "Software or AI vendors that sign contracts on their customers' paper with banks and other financial institutions,"
>
> "A mid-size vendor selling to big banks can carry more unusual terms than a large company signing mostly its own standard paper"

### Answer

Yes, both statements make the same point. A vendor that signs its customers' contracts ends up with many different, unusual obligations to track. A vendor that mostly uses its own contract has few.

#### What "paper" means

"Paper" is contracting slang for whose template a deal starts from, meaning who wrote the first draft.

- **Your own paper:** the vendor's standard contract, such as its master subscription agreement, data processing agreement (DPA) and security terms. The customer may redline it, but your terms are the baseline, so most customers end up on similar terms.
- **Customer's paper:** the buyer's own vendor agreement, security addendum and DPA. The vendor has to accept or negotiate against the buyer's terms, so each big customer brings its own set of obligations.

Big buyers, especially banks, usually insist on their own paper. Part of the reason is regulation: rules like DORA and New York's NYDFS guidance expect certain terms in vendor contracts, and banks put those terms in their templates.

#### How this connects to Customer Commitments

- **On your own paper:** commitments are mostly the same across customers, so one lookup answers almost every question.
- **On customers' paper:** each contract can differ on breach-notice windows, subprocessor notice, audit rights, data location and deletion timelines. That variation is what makes tracking hard and Customer Commitments valuable. Vanta's product reflects this: you set your "standard commitments," and it flags where each customer's contract departs from them ([Vanta Help Center](https://help.vanta.com/en/articles/13931299-managing-customer-commitments)).

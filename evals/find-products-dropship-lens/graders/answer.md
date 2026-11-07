---
type: llm
---

The data (Amazon pet-supplies Best Sellers, TikTok "cat toy", Trends over 12 months): automatic laser toy (6,400 TikTok units), interactive rolling ball "USB Rechargeable" (5,200 units), cat window perch (3,800 units, a suction-cup seat), cardboard scratcher (2,100 units, bulky; 31,200 Amazon reviews on the chart leader), catnip toys (1,400), tunnel (900), handheld USB laser pointer (60 units, 22,300 Amazon reviews). Non-cat rows (dog toys, litter, treats, a grooming glove) are not cat toys.

PASS if all of these hold:
- the answer reads the ideas through a dropship / cold-traffic lens for this user (named as such, or plainly applied), with the profile repeated as bands (under USD 1k, dropship, first time), not the exact USD 500;
- it weighs TikTok units (impulse, felt want) over Amazon search demand for this user, and says at least once that Amazon search demand (deep Best Sellers reviews or high search interest) is not counted for them, counts against cold traffic, or is not a lead for them (never that it favours them);
- it applies at least two of these lens checks to specific ideas, each tied to a title or number: a "USB Rechargeable" lithium battery shown as a neutral risk note (never a policy fail: no named ad platform prohibits it), weight / bulk / fragility, demo-ability (visible on video in seconds, as a judgement), or MOQ-1 supplier availability (offering an AliExpress check; an offer carries no price, since the owner's rule puts cost only at the approval);
- each idea gets a for-you reading next to the market's for/against, using the fixed labels (a strong fit / a fit, with one fix / a long shot / not this one), and a gate that can't be judged from the titles (single units, profit) is said to be not read, not checked yet or unclear, rather than guessed; the lens's profit floor worked from read data (for example "any price above about USD 8.55 can cover USD 8 of ads and the card fee", from the prices read and the stated ad-cost assumption) is allowed and is not a guess; the handheld USB laser pointer (60 TikTok units) reads "a long shot" (thin demand on their channel) or "not this one" (at USD 7.99 even a free product can't cover USD 8 of ads plus fees, and no listing of it sells at a higher price), never "a fit, with one fix";
- non-cat rows are left out; it ends on a next step with no Apify cost (validate two ideas, or the AliExpress check);
- no hype words, no doom words, no comment on the profile itself; it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step.

FAIL if the rechargeable ball is set aside or failed for its battery alone, if the ideas are ranked only by Amazon demand with no lens, if no lens filter is applied to any idea, if the exact USD 500 is repeated, or if there is no next step, or it closes on a "This run cost…" (or "This research cost…") line, or puts an Apify cost on its next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

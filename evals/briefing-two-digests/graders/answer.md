---
type: llm
---

The account: two MarketMage watches and one unrelated task (my-instagram-scrape). The notebook (read with the user's `MarketMage notebook: on`): profile $1k–5k, own stock, some experience, store and Amazon, brand; the heated eye mask is at the launching stage, with a stop rule agreed on 15 Oct to check on 2026-10-22 (test spend band USD 250–500 of ads, or 7 days: add-to-cart under 2% → stop; click-through over 1.5% with add-to-cart under 2% = curiosity, not intent; no sale → stop). The Catalog Matcher watch on glowrest.com found 3 new undercuts on the user's products: Cordless Heated Eye Mask 29.99 vs 27.99 (6.7%), Eye Mask Travel Case 12.99 vs 11.99 (7.7%), Heated Neck Wrap 39.99 vs 24.99 (37.5%, a "Final Sale" item that is out of stock there). The launch-week digest: a leader's price drop (Lunara 32.99 → 27.99), the user's own ASIN B0MYMASK01 entered the top 10 on "heated eye mask" (#14 → #9) and the top 3 on "cordless eye mask" (#6 → #3), a new 2-star review on the user's mask about a tight, non-adjustable strap, and GlowRest's rating 4.3 → 4.1.

The account's two schedules were due to run on 25 Oct (daily) and 26 Oct (weekly) and their tasks' last runs are 23 Oct and 20 Oct, so a line naming both watches as not having run since then (missed or late runs, with things to check) is correct reporting, not an invented change.

PASS if all of these hold:
- it gives no cost commentary on the reads (no "reading the digests is free" line, no notebook-read price, no closing cost line; saying a scheduled briefing only reads and starts no paid run is fine);
- it puts the due stop rule first: names the 22 Oct check, quotes the rule with its numbers (the USD 250–500 test spend band or 7 days, 2% add-to-cart, 1.5% click-through as curiosity), and asks what the test showed or applies the rule, without deciding for the user against the rule;
- the rest is turned into at most 5 numbered decisions in total, each with one recommended move and a reason tied to a number, and no Apify cost on the moves;
- the undercuts get split moves (grouped in one decision, or with the mask's undercut grouped with the Amazon leader's price drop): match or close the gap on the small ones (6.7% and 7.7%, or a conditional match tied to margin or sales), and hold on the Heated Neck Wrap because the gap is large (37.5%), it is a final sale / clearance, or it is out of stock there;
- the user's own rank gains are credited with their numbers, and the 2-star strap review is turned into a move (for example answer it, or fix the strap);
- the unrelated my-instagram-scrape task is not named or reported;
- it names the stage (launching) or the heated eye mask idea in a welcome-back line;
- it invents no changes beyond those above, and it ends on one next move.

FAIL if it lists changes without recommended moves, gives more than 5 decisions, buries or omits the due stop rule, recommends matching the 37.5% final-sale price, reports the non-cw task, invents changes, or claims to have run a paid check without a yes.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

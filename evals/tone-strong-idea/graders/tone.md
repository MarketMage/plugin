---
type: llm
---

PASS if all of these hold:
- it is warm where the numbers support it (for example "the data strongly favours this", "you've found a real opening"), and each warm statement is tied to a number;
- it gives the user specific credit tied to a number, for example that they were right about dry eyes (the rising search "heated eye mask for dry eyes", +900%) or that their USD 29.99 sits inside the market's price band;
- it names the biggest risk as an early sign to watch with today's number (for example ads on page 1 rising from 4 in 48, or new sellers entering), not as a generic warning, and offers a watch that would catch that sign, without an Apify cost, as an offer (it does not claim to have created one) (in the short default answer, the early sign and its watch may instead wait behind the one line offering the full detail, when that line names them: either passes);
- it ends on a concrete next move with no Apify cost, not on the verdict;
- it uses no hype beyond the data ("definitely", "guaranteed", "can't miss", "goldmine", "huge potential") and no doom or pre-owned failure ("most products fail", "be careful", "unfortunately");
- it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step.

Since 0.4.22 the verdict here is Promising, with one fix (the launch ad cost decides it: the Launch ads row is neutral), and the answer states a verdict confidence (medium or low, it hangs on the ad cost) and the data's confidence: saying plainly how sure it is, and that the ad cost decides it, is the rule, not caution; warmth is still expected on what the data backs (demand, an open page 1, the user's dry-eyes hunch).

FAIL if it is flat or cautious despite the data (for example leading with risks or caveats), if it praises the person rather than tying credit to data, if it names no early sign or no watch and has no offer line naming them, or if it uses hype or doom words.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

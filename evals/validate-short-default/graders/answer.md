---
type: llm
---

The check's data favours the idea on every row but Launch ads (neutral). Since 0.4.22 two rows read the money: the Margin row, before ads (at USD 29.99 a sale pays out USD 20.87 after Amazon's fees; minus the USD 4.80 factory median and freight of 15 to 30% of it, an assumption, it leaves about USD 14.63 to 15.35, about 49%: favours), and the Launch ads row (that break-even ad cost per sale, about USD 14 to 15, against USD 8 to 12 of launch ads a sale, an assumption: after USD 12 a sale keeps about USD 2.63, under 25% of the price, and the ad cost that keeps 25% is about USD 7: neutral). A neutral Launch ads row caps the market verdict at **Promising, with one fix**, the fix being the ad cost per sale (it works under about USD 7 a sale and loses money over about USD 14), with a verdict confidence one step down for it (medium; low when the reply also names a thin source, such as few matching factory offers, which is fine). Since 0.4.23 the owner's short default for this first answer is a scorecard: a headline (a badge emoji, the product, the label), one bold sentence of why (with the counts in words), at most five signal chips (each a badge emoji and a few words with a number), the deciding number (the break-even ad cost per sale and the healthy ad cost), both confidences on one line, one "Check first" line, then ONE line offering the rest, then the Next step line last. The signal table and the other full-detail parts wait for the full detail.

PASS if all of these hold:
- it opens with the scorecard's headline ("Promising, with one fix", or Maybe, with a badge), then the why and both confidences;
- it shows the signal chips (at most five) with their numbers, and the deciding number;
- before the Next step line there is one line offering the rest of the answer (for example "Want the full detail: every signal, the other versions and the early sign to watch?"; the profile's offer may be its second half);
- the full-detail parts are NOT written out anywhere: no signal table, no "What it means" section, no list of related versions, no paragraph on the early sign and its watch (the one "Check first" line is fine), and no "What this can't see" line;
- between the "Check first" line and the last line there is nothing but: that offer line, at most one line on what lowered a confidence, at most one short exclusion or mismatch line, at most one question for the user's landed cost, and at most the notebook's ask; no other notes or caveats (no fee assumptions, no "Before listing" step, no supplier offer ranges);
- its last line is a next step ("Next step: …"), which may say it is free and how long it takes, and there is no closing cost line ("This research cost…"). Up to two "After that" items inside that same Next step line are the approved shape since 0.4.22.

FAIL if any full-detail part (including the signal table) is written out, if there is no offer line for the rest, if other notes or caveats sit before the last line, or if the reply does not end on a next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

Since 0.4.23 (the scorecard), the first answer's Next step line says the move's cost when it has one: a free step says it is free (with its time), and a MarketMage read may carry its one estimate ("about $0.14"); that is the approved shape and does not count as an Apify cost on the next step. A closing "This run cost…" line still fails. Money may be written with $ rather than USD.

---
type: llm
---

The check's data favours the idea (Strong for the market). The answer's default shape is short: the first screen (verdict line first, one plain line, what must stay true, the next step), the signal table, then one line offering the rest, and the Next step line last.

PASS if all of these hold:
- it opens with the verdict line ("For the market: Strong", or Go) with its confidence and counts, then one plain line with numbers;
- it shows the signal table (or one line per signal) with the numbers;
- it has exactly one line offering the rest of the answer (for example "Want the full detail: what it means, the early sign and its watch, what this can't see?"), placed after the table and before the last line;
- the full-detail parts are NOT written out: no "What it means" section, no list of related versions (a single next move on the first screen is fine), no paragraph on the early sign and its watch, and no "What this can't see" line;
- its last line is a next step ("Next step: …") with no Apify cost, and there is no closing cost line ("This research cost…");
- the whole reply, not counting the table, is about 350 words or fewer, with no block of notes or caveats under the table (an exclusion or mismatch line, and one line on what lowered the confidence with what would raise it, are fine).

FAIL if any full-detail section is written out in full, if there is no offer line for the rest, if there are several offer or follow-up lines (the profile's one offer line, the notebook's one-line ask and a one-line question for their landed cost are allowed), or if the reply does not end on a next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

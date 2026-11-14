---
type: llm
---

The data: searches up about 45% over 5 years; the top 10 sell at least 14,000 units a month; a page-1 review median of about 310 with 14 of 48 under 100 reviews; top-3 seller share about 0.22; 4 ads in 48; at the USD 44.99 median a sale pays out about USD 32.74 after Amazon's fees (USD 12.25), and the factory median is USD 4.50. With freight at 15 to 30% of the unit cost (an assumption, about USD 0.68 to 1.35), the Margin row, before ads, is about USD 26.89 to 27.56 a sale (about 60%: favours). That is the break-even ad cost per sale; the Launch ads row judges it against USD 8 to 12 of launch ads (an assumption): after USD 12 a sale still keeps about USD 14.89 (about 33%), and the healthy ad cost (break-even less 25% of the price) is about USD 15.64, over 12, so Launch ads favours and caps nothing; nothing assumed decides the verdict.

PASS if all of these hold:
- the market verdict is **Strong** (or Go), with its counts;
- the margin is worked after Amazon's fees with a freight or duty allowance (labelled an assumption) or a clear note that freight is still to add, and the launch ads (USD 8 and/or 12 a sale, labelled an assumption) are set against what a sale leaves; figures within about USD 1 or 3 percentage points of those above are fine;
- the break-even ad cost per sale (about USD 26 to 27.5) is stated, in those or equivalent words ("ads can cost up to about USD 26 a sale before it loses money");
- it gives two confidences: one for the verdict, which is **high**, and one for the data (complete, or every source came back), in compact or plain words;
- it ends on one Next step line, with at most two "After that" items in it, and no Apify cost on it (beyond the move's own one estimate, allowed since 0.4.23).

FAIL if the verdict is Promising, Not this version, Maybe or No; if launch ads are never mentioned; if the break-even ad cost is missing; if only one confidence is given or the verdict confidence is medium or low; or if it ends on a menu of moves or puts an Apify cost on the next step (beyond the move's own one estimate, allowed since 0.4.23).

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

Since 0.4.23 (the scorecard), the first answer's Next step line says the move's cost when it has one: a free step says it is free (with its time), and a MarketMage read may carry its one estimate ("about $0.14"); that is the approved shape and does not count as an Apify cost on the next step. A closing "This run cost…" line still fails. Money may be written with $ rather than USD.

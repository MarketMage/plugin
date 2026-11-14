---
type: llm
---

The data: searches up about 96% over 5 years; the top 10 sell at least 14,000 units a month; review median about 310 with 14 of 48 under 100; top-3 seller share about 0.22; 4 ads in 48; the user's USD 28.99 inside the USD 22.99 to 34.99 band. At USD 28.99 a sale pays out USD 20.28 after Amazon's fees (USD 8.71); minus the USD 6.10 factory median, USD 14.18 (49%). Freight at 15 to 30% of the unit cost (an assumption) is about USD 0.92 to 1.83, so the Margin row, before ads, is about USD 12.35 to 13.26 a sale (about 43 to 46%: favours). The Launch ads row judges that break-even ad cost per sale (about USD 12.35) against USD 8 to 12 of launch ads a sale (an assumption): after USD 12 a sale keeps about USD 0.35, under 25% of the price, and the ad cost that keeps 25% (the healthy ad cost) is about USD 5.10, so Launch ads is neutral: the ad cost decides it, which caps the verdict at Promising, with one fix.

PASS if all of these hold:
- the market verdict is **Promising, with one fix** (or Maybe), and its fix is about the ad cost per sale (keeping it under about USD 4 to 6 a sale, or the price per click that gives that), not a cheaper supplier;
- the deciding numbers are on the first screen: the break-even ad cost per sale, about USD 12 to 13.5 ("it loses money once ads cost more than about USD 12 a sale"), and the healthy ad cost, about USD 4 to 6 ("it works if ads cost under about USD 5 a sale");
- the margin before ads (about 43 to 49%, or about USD 12.35 to 14.18 a sale) is reported as the margin, favouring or healthy, not as against (since 0.4.23 the first answer is a scorecard: a Profit chip with a watch badge ⚠️ that gives about $12 before ads and the after-ads range is the approved shape, since that chip combines the margin with the launch ad cost; money may be written with $ rather than USD);
- the ad cost per sale (USD 8 and/or 12) and any freight allowance, click price or conversion rate are labelled as assumptions, never as measured;
- two confidences are given: the verdict's, which is **medium** (or "fairly sure", with the reason that it depends on what ads cost), and the data's, complete (or every source came back);
- one Next step line, last, whose move is a step that measures the ad cost (for example looking up the suggested bid or cost per click for "heated eye mask" in the Amazon ad console, free, about 5 minutes), with what result means what; at most two "After that" items in that line; no Apify cost on it (beyond the move's own one estimate, allowed since 0.4.23).

FAIL if the verdict is Strong (or Go) or Not this version; if there is no break-even ad cost; if the margin is called against (or "hurts") because of the ads; if the verdict confidence is high; if a click price or conversion rate is presented as measured; or if the next step is a paid MarketMage read while the ad cost is what decides the verdict.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

Since 0.4.23 (the scorecard), the first answer's Next step line says the move's cost when it has one: a free step says it is free (with its time), and a MarketMage read may carry its one estimate ("about $0.14"); that is the approved shape and does not count as an Apify cost on the next step. A closing "This run cost…" line still fails. Money may be written with $ rather than USD.

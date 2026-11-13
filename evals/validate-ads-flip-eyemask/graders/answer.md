---
type: llm
---

The data: searches up about 96% over 5 years; the top 10 sell at least 14,000 units a month; review median about 310 with 14 of 48 under 100; top-3 seller share about 0.22; 4 ads in 48; the user's USD 28.99 inside the USD 22.99 to 34.99 band. At USD 28.99 a sale pays out USD 20.28 after Amazon's fees (USD 8.71); minus the USD 6.10 factory median, USD 14.18 (49%, before freight and ads). Freight at 15 to 30% of the unit cost (an assumption) is about USD 0.92 to 1.83, so what a sale leaves before ads, the break-even ad cost per sale, is about USD 12.35 to 13.26. After USD 8 to 12 of launch ads a sale it leaves about USD 0.35 to 5.26 (under 25% of the price), so the margin reads against after ads; the ad cost that keeps a 25% margin is about USD 5.

PASS if all of these hold:
- the market verdict is **Promising, with one fix** (or Maybe), and its fix is about the ad cost per sale (keeping it under about USD 4 to 6 a sale, or the price per click that gives that), not a cheaper supplier;
- the break-even ad cost per sale is stated, about USD 12 to 13.5 (for example "it loses money once ads cost more than about USD 12 a sale"), and the margin before ads (about 49%, or USD 14.18, or with freight about USD 12.35 to 13.26) appears as context;
- the ad cost per sale (USD 8 and/or 12) and any freight allowance, click price or conversion rate are labelled as assumptions, never as measured;
- two confidences are given: the verdict's, which is **medium** (or "fairly sure", with the reason that it depends on what ads cost), and the data's, complete (or every source came back);
- one Next step line, last, whose move is a step that measures the ad cost (for example looking up the suggested bid or cost per click for "heated eye mask" in the Amazon ad console, free, about 5 minutes), with what result means what; at most two "After that" items in that line; no Apify cost on it.

FAIL if the verdict is Strong (or Go) or Not this version; if the margin is scored only after fees; if there is no break-even ad cost; if the verdict confidence is high; if a click price or conversion rate is presented as measured; or if the next step is a paid MarketMage read while the ad cost is what decides the verdict.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

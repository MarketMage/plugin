---
type: llm
---

The market data favours this idea on every row but Launch ads (neutral) (demand +95.6% over 5 years, a top-10 sales floor of about 14,000 units a month, median 310 reviews, top-3 share 0.22, 4 ads in 48). Since 0.4.22 two rows read the money: the Margin row, before ads (at USD 29.99 a sale pays out USD 20.87 after Amazon's fees; minus the USD 4.80 factory median and freight of 15 to 30% of it, an assumption, it leaves about USD 14.63 to 15.35, about 49%: favours), and the Launch ads row (that break-even ad cost per sale, about USD 14 to 15, against USD 8 to 12 of launch ads a sale, an assumption: after USD 12 a sale keeps about USD 2.63, under 25% of the price, and the ad cost that keeps 25% is about USD 7: neutral). A neutral Launch ads row caps the market verdict at **Promising, with one fix**, the fix being the ad cost per sale (it works under about USD 7 a sale and loses money over about USD 14), with a verdict confidence one step down for it (medium; low when the reply also names a thin source, such as few matching factory offers, which is fine). The supplier rows give a median unit price of about USD 4.80 at a median MOQ of 200 (a first order of about USD 960), well inside a USD 5k-25k band; several leaders are rated under 4.2 or carry a 1-star share near 9%.

PASS if all of these hold:
- the answer leads with a "For you" verdict that is positive (a strong fit, or a fit with one named fix), then "For the market: Promising, with one fix" (or Maybe), its fix the ad cost per sale, with its counts;
- the For you block names an own-stock / FBA (and possibly brand) reading and includes a fit check with numbers: the first order (units × unit cost, about USD 960 or similar) against the USD 5k-25k band, and the FBA fees or margin after fees;
- it treats the leaders' quality gap or rising related searches as room for a brand, with a number;
- the profile is repeated as bands (USD 5k-25k, FBA, some experience, brand), not the exact USD 8,000;
- the facts table and market verdict are the same kind as for any seller (no number changed by the profile);
- no comment on the profile itself; it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step (beyond the move's own one estimate, allowed since 0.4.23).

FAIL if "For you" is "not this one", if there is no fit check with the first-order number, if the exact USD 8,000 is repeated, or if the market verdict differs from Promising, with one fix.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

Since 0.4.23 (the scorecard), the first answer's Next step line says the move's cost when it has one: a free step says it is free (with its time), and a MarketMage read may carry its one estimate ("about $0.14"); that is the approved shape and does not count as an Apify cost on the next step. A closing "This run cost…" line still fails. Money may be written with $ rather than USD.

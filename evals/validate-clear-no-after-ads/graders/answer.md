---
type: llm
---

The data is against this idea on most signals: searches down about 85% over 5 years, a review median about 4,800 with 1 of 48 under 100, top-3 seller share about 0.64, 14 ads in 48 priced low: four against, which settles Not this version whatever the money rows read. At USD 9.99 a sale pays out about USD 8.49 after the referral fee alone (about USD 5.18 after the FBA fee too, if the leaders were read), and the factory median is about USD 0.35; so what a sale leaves before ads (the Margin row, favours on its share of the price), the break-even ad cost per sale, is about USD 8 before the FBA fee or about USD 4.5 to 5 after it. The Launch ads row judges that against USD 8 to 12 of launch ads a sale: neutral on the referral fee alone, against after the FBA fee. Either reading (with or without the leaders' FBA fee) is fine.

PASS if all of these hold:
- the market verdict is **Not this version** (or No), with its counts, and it names a related version drawn from the data;
- it states the break-even ad cost per sale, or in plain words what a sale leaves before ads set against the launch ad cost (for example "a sale leaves about USD 4.70 before ads, less than the USD 8 a sale ads usually cost at launch");
- it gives two confidences, the verdict's and the data's (for a verdict settled after the first reads, "the data read is enough to settle it" or "data: complete" counts as the data's); the verdict confidence is **not** lowered because of the ad cost (the verdict holds whatever ads cost); a verdict confidence of high, or one lowered only for a missing source, passes;
- it ends on one Next step line (a check of the related version, or the free stop "nothing to buy; keep the USD …" with the related version offered on the same line, which is the plugin's approved free-stop shape and not a menu), with at most two "After that" items in it and no Apify cost (beyond the move's own one estimate, allowed since 0.4.23).

FAIL if the verdict is Strong, Promising, Go or Maybe; if there is no break-even ad cost or before-ads figure; if only one confidence is given, or the verdict confidence is said to hang on the ad cost; or if it ends on the verdict or a menu.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

Since 0.4.23 (the scorecard), the first answer's Next step line says the move's cost when it has one: a free step says it is free (with its time), and a MarketMage read may carry its one estimate ("about $0.14"); that is the approved shape and does not count as an Apify cost on the next step. A closing "This run cost…" line still fails. Money may be written with $ rather than USD.

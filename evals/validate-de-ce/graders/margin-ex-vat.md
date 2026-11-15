---
type: llm
---

The amazon.de leaders' rows now carry Amazon's European fees (amazon-product-scraper 0.1.15). The leaders at his 19,99 € (B0NACHT001, B0NACHT008, lighting) give `afterFeesExVatRange` 10,88 to 11,88 €: 19,99 € less 19% VAT is 16,80 €, less Amazon's fees of 4,92 to 5,92 € (a referral range, because lighting spans the home products and DIY rates, plus a 3,32 € FBA fee). Less his 4,10 € landed cost that leaves about 6,78 to 7,78 € a unit, about 40 to 46% of the net price. Those rows have `confidence: "low"`; their `basis` says lithium battery and dangerous-goods fees are not included. Two leaders in Baby Products have `vatRate: null` (a reduced rate is possible there).

PASS if all of these hold:
- it works his margin after Amazon's fees with VAT taken out first: a payout figure (or range) from the data near 10,88 to 11,88 € (or fees near 4,92 to 5,92 €) and a margin near 6,78 to 7,78 € or 40 to 46% of the net price (a single figure or either end of that range is fine; the score at the lower end);
- it says the fees are a rough or low-confidence estimate, or names why (the category spans two fee rates), in a few words;
- it names at least one fee the estimate leaves out that bears on this product (lithium battery or dangerous-goods fees, or the digital services fee), or another `notModelled` or "not included" item from the data;
- it does not use the VAT-inclusive `afterFees` (14,07 to 15,07 €) as what a sale leaves, and states no Amazon fee figure that isn't in the data.

FAIL if the margin is before Amazon's fees with the fees called unmodelled or unknown, if `afterFees` with VAT still in it is treated as the payout, if no confidence or caveat is given on the fees, or if a fee or rate appears that the data doesn't hold.

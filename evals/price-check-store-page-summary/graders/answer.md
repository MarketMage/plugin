---
type: llm
---

The run's status message: "examplepottery.com Speckled Stoneware Mug, 12 oz: USD 24.99 (was USD 29.99, 17% off); in stock; 6 variants, USD 19.99 to 34.99, 4 in stock."

PASS if all of these hold:
- the reply gives USD 24.99 as the price and says it is in stock;
- it mentions the sale (was USD 29.99, or 17% off) or the variant range (USD 19.99 to 34.99), or both;
- every price it gives is one of USD 24.99, 29.99, 19.99 or 34.99 (no other price for this mug, no price for a named variant such as "Sage" or "16 oz", and no other store's price);
- it ends on a next step and puts no Apify cost on it.

FAIL if the price or stock is missing or wrong, if it names a price that isn't in the message, or if it says the page couldn't be read.

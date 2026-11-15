---
type: llm
---

The data's `lowestPrice` is USD 189.99 at Best Buy with `lowestPriceCondition: "unknown"`; `lowestNewPrice` is USD 279.99 at Target.

PASS if the reply gives USD 279.99 at Target as the lowest new price (the headline), and shows the USD 189.99 Best Buy offer as of unstated or unknown condition (to check), not as the lowest new price.
FAIL if it presents USD 189.99 as the lowest new price, or leaves the USD 189.99 offer out without mentioning it.

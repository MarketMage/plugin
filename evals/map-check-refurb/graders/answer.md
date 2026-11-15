---
type: llm
---

The record's `mapViolations` holds 1ShopDirect on Walmart at USD 259.00 (new); `mapUnconfirmed` holds Best Buy at USD 189.99 (condition unknown, plain title).

PASS if the reply reports both as MAP violations: 1ShopDirect on Walmart at USD 259.00, and Best Buy at USD 189.99 marked as condition not stated (or unconfirmed condition).
FAIL if it omits either offer, does not count the Best Buy offer as a violation, or presents the Best Buy offer as confirmed new without saying its condition isn't stated.

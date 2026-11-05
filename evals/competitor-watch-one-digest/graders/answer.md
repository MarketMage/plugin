---
type: llm
---

The account already has one watch, `cw-price-competitors` (daily, 2 store pages and 1 Amazon ASIN, a few cents a month), and its export schedule `cw-export-price-competitors`.

PASS if the reply proposes **one** watch (a single Watch Digest task and schedule, one digest per run) that covers both stores' prices and new products, their promotions, and their ads, gives that watch's monthly cost as one figure, and states the total monthly cost of the user's watches with this one added (a figure that includes the existing competitor-prices watch, said as a total across their watches), and creates nothing yet.
FAIL if it plans separate tasks for prices, promotions and ads without offering them as one digest, gives no total across the user's watches, or says it has created the watch.

---
type: llm
---

The account already has one watch, `cw-price-competitors` (daily, 2 store pages and 1 Amazon ASIN, a few cents a month), and its export schedule `cw-export-price-competitors`.

PASS if the reply proposes **one** watch (a single Watch Digest task and schedule, one digest per run) that covers both stores' prices and new products, their promotions, and their ads, gives that watch's monthly cost (the user asked to see what it costs, so a first-run figure, a Max cost per run and a breakdown are fine), and creates nothing yet. A total across their watches may appear in a line about Apify's free plan's USD 5 a month, or be absent: either passes.
FAIL if it plans separate tasks for prices, promotions and ads without offering them as one digest, gives no monthly cost for the new watch, or says it has created the watch.

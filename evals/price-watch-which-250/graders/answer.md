---
type: llm
---

The facts: a capped whole-store watch reads the Shopify store's product feed, which lists the most recently published products first, so a cap of 250 reads the 250 newest. A new launch is published at the top, so launches are seen. Older products past the 250th are not watched for price, stock or sales. On a capped read, removed products are not reported. A store that blocks its feed is read from its sitemap, which is not newest first. Raising the cap to the store's size (about 600) covers the whole catalogue at a little more cost.

PASS if the reply says the 250 are the store's most recently published (newest) products, says new launches are seen (they appear at the top of the feed), says older products past the cap are not watched, and offers the whole catalogue (a cap near 600 or above) as the alternative. Mentioning removals or the sitemap case is welcome but not required.
FAIL if it says the 250 are chosen at random, by best sellers, alphabetically or by price, says it doesn't know which 250 are read, says launches past the cap are missed (without the sitemap exception), says a product the store re-publishes always shows as new (one an earlier run read is compared with its last reading; only one never read shows as new), or creates a task or schedule.

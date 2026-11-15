---
type: llm
---

The account: three MarketMage watches for two client labels and one unrelated task. Acme: `cw-price-acme-competitors` (Watch Digest, weekly) and `cw-map-acme-headphones` (Barcode Price Checker, weekly). Bondi Paws: `cw-promo-bondi-rivals` (Watch Digest, weekly). Each task ran on 28 Sep, 5, 12, 19 and 26 Oct and 2 Nov 2026. October has 4 runs of each. Per October run: Acme's digest 0.0055 plus its watcher runs 0.03 and 0.012 and its delivery run 0.001 (0.0485 a run, 0.194 for October); Acme's MAP task 0.26 a run (1.04); Bondi's digest 0.0075 plus its promotions watcher 0.018 and delivery 0.001 (0.0265 a run, 0.106). So Acme about USD 1.23 (1.234), Bondi Paws about USD 0.11, total about USD 1.34. Each run's charge is its `chargedEventCounts` × its `pricingInfo` event prices; the runs' `usageTotalUsd` is Apify's platform usage, not the charge (summing it would give Acme about 0.28 and Bondi about 0.04).

PASS if all of these hold:
- it gives one figure per client (Acme, Bondi Paws or Bondi), within USD 0.03 of 1.23 for Acme and 0.11 for Bondi, and a total within USD 0.03 of 1.34;
- the October figures leave out the 28 September and 2 November runs (a figure of about 1.54 for Acme, or 0.13 for Bondi, means they were counted);
- the Watch Digest figures include the watcher and delivery runs, not only the digest runs' own 0.0055 and 0.0075 (an Acme price-watch figure near 0.02, or a Bondi figure near 0.03, means they were missed);
- it is laid out per client, as a table or list ready for an invoice, with the total;
- the unrelated my-instagram-scrape task is not counted in any figure (a line saying it was left out is fine);
- the figures come from the charged events, not `usageTotalUsd` (an Acme figure near 0.28 or a Bondi figure near 0.04 means the usage figures were summed).

FAIL if it counts runs outside October, prices runs from `usageTotalUsd`, leaves out the watcher runs, mixes the two clients' costs, invents runs or charges, or adds the unrelated task's runs to a figure. Extra offers (an AUD column, a client brief) and a pointer to Apify's usage page are fine.

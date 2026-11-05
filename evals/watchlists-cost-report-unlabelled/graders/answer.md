---
type: llm
---

The account has three MarketMage watches and one unrelated task. Only one watch carries a client label in its title: `cw-price-acme-competitors`, titled "Acme: competitor prices". `cw-price-competitors` ("Competitor prices") and `cw-rank-eye-mask` ("Eye mask ranks") have no label. Each watch ran weekly on 5, 12, 19 and 26 Oct 2026 (and on 28 Sep and 2 Nov, outside October).

Charges (each run's `chargedEventCounts` × its `pricingInfo` prices):
- Acme: a normal run is the digest 0.0055 + store watcher 0.03 + Amazon watcher 0.012 + delivery 0.001 = 0.0485. The 19 Oct digest run TIMED-OUT before writing `RUN_SUMMARY` and charged 0.0005; its store and Amazon watcher runs (0.03 and 0.012) still ran and are found with `get-actor-run-list` in that run's time window (their `INPUT` has `monitorName` "digest-acme-competitors"). October: 3 × 0.0485 + 0.0425 = 0.188, about USD 0.19. Missing the 19 Oct watcher runs gives about 0.146.
- No label: `cw-price-competitors` 0.0205 a run (0.082) and `cw-rank-eye-mask` 0.01475 a run (0.059): about USD 0.14.
- Total about USD 0.33.

PASS if all of these hold:
- the unlabelled watches are grouped as "No label", "unlabelled" or similar (or listed per watch without a client), never as a client named from the short name (no client called "Competitors", "Competitor", "Eye", "Eye mask" or "Rank");
- it offers (or asks) to assign the unlabelled watches to a client, or asks which client they belong to;
- Acme's October figure is within USD 0.01 of 0.19, so it includes the 19 Oct watcher runs; or, if it gives about 0.15 instead, it says plainly that the 19 Oct run's watcher runs are missing or that the figure is an estimate, and does not call it exact;
- the No label figure is within USD 0.01 of 0.14 (or the two watches' figures, about 0.08 and 0.06, are given), and the total is within USD 0.02 of 0.33 (or of 0.29 with the 19 Oct shortfall stated);
- it mentions the 19 Oct run that timed out (or stopped, or failed);
- the unrelated my-instagram-scrape task is not counted.

FAIL if it invents a client from a short name, splits the unlabelled watches' cost among clients, counts runs outside October, prices runs from `usageTotalUsd` (an Acme figure near 0.12 means it did), or calls a total exact while leaving out the 19 Oct watcher runs.

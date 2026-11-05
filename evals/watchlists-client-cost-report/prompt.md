---
description: "W17 / A21 (c09, adversarial review 2026-11-03). An agency asks what each client cost in October, for invoices. The watchlists skill groups the cw- watches by client label (acme, bondi), keeps only the runs that started in October (not 28 Sep or 2 Nov), adds each Watch Digest run's watcher and delivery runs (from RUN_SUMMARY) to the digest run's own charge, prices every run from its chargedEventCounts × its pricingInfo event prices (not usageTotalUsd), adds the MAP task's own runs, and gives a per-client table with a total: Acme about USD 1.23, Bondi Paws about USD 0.11, total about USD 1.34."
max_turns: 40
allowed_tools: [Read, Skill]
runs: 1
---

I run an agency and invoice clients for monitoring. What did each client's MarketMage watches cost me in October 2026? I need exact figures for the invoices.

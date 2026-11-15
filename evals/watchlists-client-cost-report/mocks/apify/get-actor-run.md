---
type: agent
---

You are the Apify `get-actor-run` tool. Reply with exactly one JSON object for the call's `runId`, and nothing else. Every run below is SUCCEEDED; `<mmdd>` is one of 1102, 1026, 1019, 1012, 1005, 0928, and the run started on that date (2026; 0928 is 28 September) at the time given.

Every run is pay-per-event: include `"chargedEventCounts"` and `"pricingInfo": {"pricingModel": "PAY_PER_EVENT", "pricingPerEvent": {"actorChargeEvents": {<event>: {"eventTitle": <title>, "eventPriceUsd": <price>}, …}}}` with the event prices listed for that run, and the `usageTotalUsd` given (Apify's platform usage for the run, which is not what the run charged). Also `finishedAt`, a few minutes after `startedAt`.

- `run-acme-<mmdd>`: `{"runId": "<runId>", "actorName": "cleanpull/watch-digest", "status": "SUCCEEDED", "startedAt": "2026-<mm>-<dd>T02:00:00Z", "defaultKeyValueStoreId": "kv-acme-<mmdd>", "defaultDatasetId": "ds-acme-<mmdd>", "chargedEventCounts": {"digest": 1, "item-watched": 2}, "usageTotalUsd": 0.0021}`; prices `digest` 0.005, `item-watched` 0.00025.
- `run-acme-stores-<mmdd>`: actor `cleanpull/any-store-product-monitor`, started 02:00:20Z, `chargedEventCounts` `{"product": 12, "product-checked": 24}`, prices `product` 0.0015, `product-checked` 0.0005, `"usageTotalUsd": 0.0108`.
- `run-acme-amazon-<mmdd>`: actor `cleanpull/amazon-product-scraper`, started 02:00:20Z, `chargedEventCounts` `{"product": 4}`, price `product` 0.003, `"usageTotalUsd": 0.0154`.
- `run-acme-alert-<mmdd>`: actor `cleanpull/alerts-sender`, started 02:04:00Z, `chargedEventCounts` `{"alert-delivered": 1}`, price 0.001, `"usageTotalUsd": 0.0004`.
- `run-map-<mmdd>`: actor `cleanpull/barcode-price-checker`, started 02:15:00Z, `chargedEventCounts` `{"product-result": 20, "google-request": 50}`, prices `product-result` 0.003, `google-request` 0.004, `"usageTotalUsd": 0.041`.
- `run-bondi-<mmdd>`: actor `cleanpull/watch-digest`, started 02:30:00Z, `defaultKeyValueStoreId` `kv-bondi-<mmdd>`, `chargedEventCounts` `{"digest": 1, "item-watched": 10}`, prices as the Acme digest, `"usageTotalUsd": 0.0019`.
- `run-bondi-promo-<mmdd>`: actor `cleanpull/promotions-monitor`, started 02:30:20Z, `chargedEventCounts` `{"promotion": 3, "page-checked": 12}`, prices `promotion` 0.002, `page-checked` 0.001, `"usageTotalUsd": 0.0067`.
- `run-bondi-alert-<mmdd>`: actor `cleanpull/alerts-sender`, started 02:33:00Z, `chargedEventCounts` `{"alert-delivered": 1}`, price 0.001, `"usageTotalUsd": 0.0004`.
- Any other: `{"error": "Run not found"}`.

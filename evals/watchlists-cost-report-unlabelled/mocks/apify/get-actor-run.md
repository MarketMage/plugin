---
type: agent
---

You are the Apify `get-actor-run` tool. Reply with exactly one JSON object for the call's `runId`, and nothing else. `<mmdd>` is one of 1102, 1026, 1019, 1012, 1005, 0928 (2026; 0928 is 28 September). Every run is pay-per-event: include `"chargedEventCounts"`, `"pricingInfo": {"pricingModel": "PAY_PER_EVENT", "pricingPerEvent": {"actorChargeEvents": {<event>: {"eventPriceUsd": <price>}, …}}}` with the prices given, `startedAt`, `finishedAt`, `defaultKeyValueStoreId` `kv-<runId>` unless given, and the `usageTotalUsd` given (Apify's platform usage, not the charge). Digest prices: `digest` 0.005, `item-watched` 0.00025.

- `run-acme-<mmdd>`: actor `cleanpull/watch-digest`, SUCCEEDED, 12:00:00Z to 12:04:00Z, `defaultKeyValueStoreId` `kv-acme-<mmdd>`, `chargedEventCounts` `{"digest": 1, "item-watched": 2}`, `usageTotalUsd` 0.0021. **Except `run-acme-1019`:** status `TIMED-OUT`, `statusMessage` "Run timed out", 12:00:00Z to 12:10:00Z, `chargedEventCounts` `{"item-watched": 2}`, `usageTotalUsd` 0.0031.
- `run-acme-stores-<mmdd>`: actor `cleanpull/any-store-product-monitor`, SUCCEEDED, 12:00:20Z to 12:02:30Z, `chargedEventCounts` `{"product": 12, "product-checked": 24}`, prices `product` 0.0015, `product-checked` 0.0005, `usageTotalUsd` 0.0108.
- `run-acme-amazon-<mmdd>`: actor `cleanpull/amazon-product-scraper`, SUCCEEDED, 12:00:20Z to 12:02:00Z, `chargedEventCounts` `{"product": 4}`, price `product` 0.003, `usageTotalUsd` 0.0154.
- `run-acme-alert-<mmdd>` (not for 1019): actor `cleanpull/alerts-sender`, SUCCEEDED, 12:03:30Z to 12:03:40Z, `chargedEventCounts` `{"alert-delivered": 1}`, price 0.001, `usageTotalUsd` 0.0004.
- `run-comp-<mmdd>`: actor `cleanpull/watch-digest`, SUCCEEDED, 12:30:00Z to 12:33:00Z, `defaultKeyValueStoreId` `kv-comp-<mmdd>`, `chargedEventCounts` `{"digest": 1, "item-watched": 2}`, `usageTotalUsd` 0.0018.
- `run-comp-stores-<mmdd>`: actor `cleanpull/any-store-product-monitor`, SUCCEEDED, 12:30:20Z to 12:32:00Z, `chargedEventCounts` `{"product": 10}`, price `product` 0.0015, `usageTotalUsd` 0.0071.
- `run-eye-<mmdd>`: actor `cleanpull/watch-digest`, SUCCEEDED, 13:00:00Z to 13:03:00Z, `defaultKeyValueStoreId` `kv-eye-<mmdd>`, `chargedEventCounts` `{"digest": 1, "item-watched": 3}`, `usageTotalUsd` 0.0017.
- `run-eye-ranks-<mmdd>`: actor `cleanpull/amazon-keyword-rank-tracker`, SUCCEEDED, 13:00:20Z to 13:02:00Z, `chargedEventCounts` `{"search-page": 3, "rank": 3}`, prices `search-page` 0.002, `rank` 0.001, `usageTotalUsd` 0.0062.
- Any other: `{"error": "Run not found"}`.

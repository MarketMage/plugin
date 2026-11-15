---
type: agent
---

You are the Apify `get-actor-run-list` tool. Reply with only a JSON object `{"total", "count", "offset", "limit", "desc", "items"}`; `limit` is at most 10. Each item: `{"id", "actId", "status", "startedAt", "finishedAt", "defaultKeyValueStoreId", "defaultDatasetId"}` (no charge figures: those come from `get-actor-run`). `defaultKeyValueStoreId` is `kv-<id>`. Dates are 2026; `<mmdd>` is one of 1102, 1026, 1019, 1012, 1005, 0928. Sort by `startedAt` (newest first with `desc: true`) and page with `offset`.

- `actorId` `cleanpull/any-store-product-monitor` or `cleanpull~any-store-product-monitor`: 12 SUCCEEDED runs, `run-acme-stores-<mmdd>` (started 12:00:20Z, finished 12:02:30Z) and `run-comp-stores-<mmdd>` (started 12:30:20Z, finished 12:32:00Z) on each of the six dates.
- `actorId` `cleanpull/amazon-product-scraper` or `cleanpull~amazon-product-scraper`: 6 SUCCEEDED runs `run-acme-amazon-<mmdd>` (started 12:00:20Z, finished 12:02:00Z).
- `actorId` `cleanpull/amazon-keyword-rank-tracker` or with `~`: 6 SUCCEEDED runs `run-eye-ranks-<mmdd>` (started 13:00:20Z).
- `actorId` `cleanpull/alerts-sender` or with `~`: 5 SUCCEEDED runs `run-acme-alert-<mmdd>` for every date but 1019 (started 12:03:30Z).
- `actorId` `cleanpull/google-sheets-sync` or with `~`: none.
- Anything else, or no `actorId`: `{"total": 0, "count": 0, "offset": 0, "limit": 10, "items": []}`.

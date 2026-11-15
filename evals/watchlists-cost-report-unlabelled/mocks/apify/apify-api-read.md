---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state. Use `total`, `count`, `offset`, `limit` and `items` for lists; a list read with an `offset` past its items returns `items: []`. `<mmdd>` is one of 1102, 1026, 1019, 1012, 1005, 0928 (2026; 0928 is 28 September).

- `/v2/actor-tasks`: four tasks.
  - `{"id": "tskACME", "name": "cw-price-acme-competitors", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: Acme: competitor prices"}`
  - `{"id": "tskCOMP", "name": "cw-price-competitors", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: competitor prices"}`
  - `{"id": "tskEYE", "name": "cw-rank-eye-mask", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: eye mask ranks"}`
  - `{"id": "tskOTHER", "name": "my-instagram-scrape", "actId": "abc"}`
- `/v2/schedules`: four schedules, each `isEnabled: true`, timezone `America/New_York`, weekly on Mondays: `cw-price-acme-competitors` (task tskACME), `cw-price-competitors` (tskCOMP), `cw-rank-eye-mask` (tskEYE), `my-instagram-scrape` (hourly, tskOTHER).
- `/v2/actor-tasks/tskACME/runs` (newest first): six runs `run-acme-<mmdd>` started at 12:00:00Z on 2026-11-02, 10-26, 10-19, 10-12, 10-05 and 09-28, `defaultKeyValueStoreId` `kv-acme-<mmdd>`. All SUCCEEDED (finished 12:04:00Z) except `run-acme-1019`: status `TIMED-OUT`, finished 12:10:00Z. Each lists a `usageTotalUsd` (Apify's platform usage, not the charge) of 0.0021.
- `/v2/actor-tasks/tskCOMP/runs` (newest first): six SUCCEEDED runs `run-comp-<mmdd>`, started 12:30:00Z on the same dates, finished 12:33:00Z, `defaultKeyValueStoreId` `kv-comp-<mmdd>`, `usageTotalUsd` 0.0018.
- `/v2/actor-tasks/tskEYE/runs` (newest first): six SUCCEEDED runs `run-eye-<mmdd>`, started 13:00:00Z on the same dates, finished 13:03:00Z, `defaultKeyValueStoreId` `kv-eye-<mmdd>`, `usageTotalUsd` 0.0017.
- `/v2/actor-tasks/<id>/runs/last`: the newest run in that task's list.
- `/v2/key-value-stores` (any query, such as `unnamed: false`): the account's named stores, with no notebook among them: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "kvsEXPORTS1", "name": "shop-exports", "createdAt": "2026-08-02T10:12:00.000Z", "modifiedAt": "2026-10-30T08:00:00.000Z"}]}`.
- `/v2/key-value-stores/<id>/keys` for any id starting `kv-`: `{"items": [{"key": "RUN_SUMMARY", "size": 900}], "count": 1, "limit": 1000, "isTruncated": false}`, with `{"key": "DIGEST.md", "size": 1400}` added for an id starting `kv-watch-digest` or `kv-wd-`.
- Anything for `tskOTHER`, and any other path: `{"error": {"type": "record-not-found"}}`.

---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: three tasks.
  - `{"id": "tskREV001", "name": "cw-reviews-competitors", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: competitor reviews"}`
  - `{"id": "tskMKT001", "name": "cw-market-bottles", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: bottle searches"}`
  - `{"id": "tskOTHER", "name": "my-instagram-scrape", "actId": "abc"}`
- `/v2/schedules`: two schedules: `{"id": "schREV", "name": "cw-reviews-competitors", "cronExpression": "0 7 * * *", "timezone": "America/New_York", "isEnabled": true, "nextRunAt": "2026-10-15T11:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskREV001"}]}` and `{"id": "schMKT", "name": "cw-market-bottles", "cronExpression": "0 9 * * 1", "timezone": "America/New_York", "isEnabled": true, "nextRunAt": "2026-10-19T13:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskMKT001"}]}`
- Any `/v2/actor-tasks/<id>/runs/last`: `{"id": "runLAST", "status": "SUCCEEDED", "defaultDatasetId": "ds-watch-digest", "defaultKeyValueStoreId": "kv-watch-digest-last"}`.
- `/v2/actor-tasks/<id>/runs` with `limit` 1 and `desc`: `{"items": [<the run `runs/last` gives above>], "total": 1}`.
- `/v2/key-value-stores` (any query, such as `unnamed: false`): the account's named stores, with no notebook among them: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "kvsEXPORTS1", "name": "shop-exports", "createdAt": "2026-08-02T10:12:00.000Z", "modifiedAt": "2026-10-30T08:00:00.000Z"}]}`.
- `/v2/key-value-stores/<id>/keys` for any id starting `kv-`: `{"items": [{"key": "RUN_SUMMARY", "size": 900}], "count": 1, "limit": 1000, "isTruncated": false}`, with `{"key": "DIGEST.md", "size": 1400}` added for an id starting `kv-watch-digest` or `kv-wd-`.
- Anything else: `{"error": {"type": "record-not-found"}}`.

Use `total`, `count`, `offset`, `limit` and `items` for lists.

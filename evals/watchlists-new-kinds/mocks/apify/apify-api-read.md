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
- Anything else: `{"error": {"type": "record-not-found"}}`.

Use `total`, `count`, `offset`, `limit` and `items` for lists.

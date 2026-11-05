---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: two tasks.
  - `{"id": "tskPRICE1", "name": "cw-price-competitors", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: competitor prices"}`
  - `{"id": "tskOTHER", "name": "my-instagram-scrape", "actId": "abc"}`
- `/v2/schedules`: one schedule, `{"id": "sch456", "name": "cw-price-competitors", "cronExpression": "0 8 * * *", "timezone": "Europe/Lisbon", "isEnabled": true, "nextRunAt": "2026-10-15T07:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskPRICE1"}]}`
- `/v2/actor-tasks/tskPRICE1/runs/last`, or the same path by name: a SUCCEEDED run with `defaultKeyValueStoreId` `kv-watch-digest-last` and `defaultDatasetId` `ds-watch-digest-last`, finished 2026-10-14T07:01:10Z.

- `/v2/datasets/<id>` for any id starting `ds-`: `{"id": "<id>", "name": null, "itemCount": 16, "cleanItemCount": 16}`.

Any other path: `{"error": {"type": "record-not-found"}}`.

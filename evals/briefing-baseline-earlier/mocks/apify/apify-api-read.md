---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: one task: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "tskMUD1", "name": "cw-promo-mudwtr", "actId": "9x3tdrBiV2wEwLuTA", "actName": "watch-digest", "actUsername": "cleanpull", "description": "MarketMage: MUD\\WTR store and promotions", "createdAt": "2026-11-07T15:20:00.000Z", "modifiedAt": "2026-11-07T15:22:00.000Z"}]}`
- `/v2/actor-tasks/tskMUD1` (or by name): the same task, with `"input": {"title": "MUD\\WTR store and promotions", "monitorName": "mudwtr", "shopifyStores": ["mudwtr.com"], "promotionStores": ["mudwtr.com"], "maxRunCostUsd": 0.06}`.
- `/v2/schedules`: one schedule: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "schMUD1", "name": "cw-promo-mudwtr", "cronExpression": "0 8 * * *", "timezone": "America/New_York", "isEnabled": true, "createdAt": "2026-11-07T15:22:30.000Z", "lastRunAt": "2026-11-08T13:00:05.000Z", "nextRunAt": "2026-11-09T13:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskMUD1"}]}]}`
- `/v2/actor-tasks/tskMUD1/runs` (any `limit`, `desc`): the task's only run so far (the run made when the watch was set up on 7 Nov was a direct run of the actor, not one of the task's runs): `{"total": 1, "count": 1, "offset": 0, "limit": 7, "desc": true, "items": [{"id": "d29Or99u2LEwAPEhk", "actId": "9x3tdrBiV2wEwLuTA", "actorTaskId": "tskMUD1", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 0 changes; digest not-asked.", "startedAt": "2026-11-08T13:00:05.000Z", "finishedAt": "2026-11-08T13:01:40.000Z", "defaultKeyValueStoreId": "kv-wd-mud", "defaultDatasetId": "ds-wd-mud"}]}`. `/v2/actor-tasks/tskMUD1/runs/last`: that run.
- `/v2/datasets/ds-wd-mud`: `{"id": "ds-wd-mud", "name": null, "itemCount": 1, "cleanItemCount": 1}`.
- `/v2/key-value-stores` (any query, such as `unnamed: false`): the account's named stores, with no notebook among them: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "kvsEXPORTS1", "name": "shop-exports", "createdAt": "2026-08-02T10:12:00.000Z", "modifiedAt": "2026-10-30T08:00:00.000Z"}]}`.
- `/v2/key-value-stores/kv-wd-mud/keys`: `{"items": [{"key": "RUN_SUMMARY", "size": 700}, {"key": "DIGEST.md", "size": 60}], "count": 2, "limit": 1000, "isTruncated": false}`.

Any other path: `{"error": {"type": "record-not-found"}}`.

---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: one task, `{"id": "tskOPPS1", "name": "cw-opps-pets", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: pet opportunities this week"}`
- `/v2/schedules`: one schedule, `{"id": "schOPP", "name": "cw-opps-pets", "cronExpression": "0 8 * * 1", "timezone": "America/New_York", "isEnabled": true, "nextRunAt": "2026-10-26T12:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskOPPS1"}]}`
- `/v2/actor-tasks/tskOPPS1/runs/last`, or the same path by name: a SUCCEEDED run with `defaultKeyValueStoreId` `kv-wd-opps` and `defaultDatasetId` `ds-wd-opps`, finished 2026-10-19T12:03:40Z.
- `/v2/actor-tasks/tskOPPS1/runs` (with any `limit`): the same run as the only item, `{"items": [<that run>], "total": 1}`.

Any other path: `{"error": {"type": "record-not-found"}}`.

---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: one task, `{"id": "tskOPPS1", "name": "cw-opps-pets", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: pet opportunities this week"}`
- `/v2/schedules`: one schedule, `{"id": "schOPP", "name": "cw-opps-pets", "cronExpression": "0 8 * * 1", "timezone": "America/New_York", "isEnabled": true, "nextRunAt": "2026-10-26T12:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskOPPS1"}]}`
- `/v2/actor-tasks/tskOPPS1/runs/last`, or the same path by name: a SUCCEEDED run with `defaultKeyValueStoreId` `kv-wd-opps` and `defaultDatasetId` `ds-wd-opps`, finished 2026-10-19T12:03:40Z.
- `/v2/actor-tasks/tskOPPS1/runs` (with any `limit`): the same run as the only item, `{"items": [<that run>], "total": 1}`.

- `/v2/key-value-stores` (any query, such as `unnamed: false`): the account's named stores, with no notebook among them: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "kvsEXPORTS1", "name": "shop-exports", "createdAt": "2026-08-02T10:12:00.000Z", "modifiedAt": "2026-10-30T08:00:00.000Z"}]}`.
- `/v2/key-value-stores/<id>/keys` for any id starting `kv-`: `{"items": [{"key": "RUN_SUMMARY", "size": 900}], "count": 1, "limit": 1000, "isTruncated": false}`, with `{"key": "DIGEST.md", "size": 1400}` added for an id starting `kv-watch-digest` or `kv-wd-`.

Any other path: `{"error": {"type": "record-not-found"}}`.

---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: three tasks.
  - `{"id": "tskGAPS1", "name": "cw-gaps-glowrest", "actId": "cm7tdrBiV2wEwLuTA", "description": "MarketMage: undercuts on glowrest.com against mystore.com"}`
  - `{"id": "tskLAUNCH1", "name": "cw-launch-eyemask", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: launch week, heated eye mask"}`
  - `{"id": "tskOTHER", "name": "my-instagram-scrape", "actId": "abc"}`
- `/v2/schedules`: three schedules: `{"id": "schGAPS", "name": "cw-gaps-glowrest", "cronExpression": "0 8 * * 1", "timezone": "America/Chicago", "isEnabled": true, "lastRunAt": "2026-11-02T14:00:00.000Z", "nextRunAt": "2026-11-09T14:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskGAPS1"}]}`, `{"id": "schLAUNCH", "name": "cw-launch-eyemask", "cronExpression": "0 6 * * *", "timezone": "America/Chicago", "isEnabled": true, "lastRunAt": "2026-11-04T12:00:00.000Z", "nextRunAt": "2026-11-05T12:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskLAUNCH1"}]}` and `{"id": "schOTHER", "name": "my-instagram-scrape", "cronExpression": "0 * * * *", "timezone": "UTC", "isEnabled": true, "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskOTHER"}]}`
- `/v2/actor-tasks/tskGAPS1/runs/last` (or by name): a SUCCEEDED run `runGAPS02` with `defaultDatasetId` `ds-cm-briefing` and `defaultKeyValueStoreId` `kv-catalog-matcher`, started 2026-11-02T14:00:03Z, finished 2026-11-02T14:04:00Z. `/v2/actor-tasks/tskGAPS1/runs` (any `limit`): that run as the only item, `{"items": [<that run>], "total": 1}`.
- `/v2/actor-tasks/tskLAUNCH1/runs/last` (or by name): a SUCCEEDED run `runLAUNCH04` with `defaultKeyValueStoreId` `kv-wd-launch` and `defaultDatasetId` `ds-watch-digest`, started 2026-11-04T12:00:04Z, finished 2026-11-04T12:02:10Z. `/v2/actor-tasks/tskLAUNCH1/runs` (any `limit`, newest first): that run, then one SUCCEEDED run a day at about 12:00Z back to 28 Oct (each with `defaultKeyValueStoreId` `kv-wd-old-<MMDD>`), `total` 8, at most `limit` items.
- `/v2/actor-tasks/tskOTHER…`: `{"error": {"type": "record-not-found"}}`.

- `/v2/key-value-stores` (any query, such as `unnamed: false`): the account's named stores, with no notebook among them: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "kvsEXPORTS1", "name": "shop-exports", "createdAt": "2026-08-02T10:12:00.000Z", "modifiedAt": "2026-10-30T08:00:00.000Z"}]}`.
- `/v2/key-value-stores/<id>/keys` for any id starting `kv-`: `{"items": [{"key": "RUN_SUMMARY", "size": 900}], "count": 1, "limit": 1000, "isTruncated": false}`, with `{"key": "DIGEST.md", "size": 1400}` added for an id starting `kv-watch-digest` or `kv-wd-`.

Any other path: `{"error": {"type": "record-not-found"}}`.

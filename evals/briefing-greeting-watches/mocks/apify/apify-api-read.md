---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: three tasks.
  - `{"id": "tskGAPS1", "name": "cw-gaps-glowrest", "actId": "cm7tdrBiV2wEwLuTA", "description": "MarketMage: undercuts on glowrest.com against mystore.com"}`
  - `{"id": "tskLAUNCH1", "name": "cw-launch-eyemask", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: launch week, heated eye mask"}`
  - `{"id": "tskOTHER", "name": "my-instagram-scrape", "actId": "abc"}`
- `/v2/schedules`: three schedules: `{"id": "schGAPS", "name": "cw-gaps-glowrest", "cronExpression": "0 8 * * 1", "timezone": "America/Chicago", "isEnabled": true, "nextRunAt": "2026-10-26T13:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskGAPS1"}]}`, `{"id": "schLAUNCH", "name": "cw-launch-eyemask", "cronExpression": "0 7 * * *", "timezone": "America/Chicago", "isEnabled": true, "nextRunAt": "2026-10-25T12:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskLAUNCH1"}]}` and `{"id": "schOTHER", "name": "my-instagram-scrape", "cronExpression": "0 * * * *", "timezone": "UTC", "isEnabled": true, "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskOTHER"}]}`
- `/v2/actor-tasks/tskGAPS1/runs/last` (or by name): a SUCCEEDED run `runGAPS20` with `defaultDatasetId` `ds-cm-briefing` and `defaultKeyValueStoreId` `kv-catalog-matcher`, finished 2026-10-20T13:04:00Z. `/v2/actor-tasks/tskGAPS1/runs` (any `limit`): that run as the only item, `{"items": [<that run>], "total": 1}`.
- `/v2/actor-tasks/tskLAUNCH1/runs/last` (or by name): a SUCCEEDED run `runLAUNCH23` with `defaultKeyValueStoreId` `kv-wd-launch` and `defaultDatasetId` `ds-watch-digest`, finished 2026-10-23T12:02:10Z. `/v2/actor-tasks/tskLAUNCH1/runs` (any `limit`): that run as the only item, `{"items": [<that run>], "total": 1}`.
- `/v2/actor-tasks/tskOTHER…`: `{"error": {"type": "record-not-found"}}`.

- `/v2/key-value-stores` (any query, such as `unnamed: false`): the account's named stores, with no notebook among them: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "kvsEXPORTS1", "name": "shop-exports", "createdAt": "2026-08-02T10:12:00.000Z", "modifiedAt": "2026-10-30T08:00:00.000Z"}]}`.
- `/v2/key-value-stores/<id>/keys` for any id starting `kv-`: `{"items": [{"key": "RUN_SUMMARY", "size": 900}], "count": 1, "limit": 1000, "isTruncated": false}`, with `{"key": "DIGEST.md", "size": 1400}` added for an id starting `kv-watch-digest` or `kv-wd-`.

Any other path: `{"error": {"type": "record-not-found"}}`.

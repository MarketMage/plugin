---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: three tasks.
  - `{"id": "tskMAP1", "name": "cw-map-xm5", "actId": "bp7tdrBiV2wEwLuTA", "description": "MarketMage: MAP on Sony WH-1000XM5 at 3 retailers", "createdAt": "2026-11-03T16:02:00.000Z"}`
  - `{"id": "tskREV1", "name": "cw-reviews-eyemask", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: reviews on 3 heated eye masks", "createdAt": "2026-10-10T15:00:00.000Z"}`
  - `{"id": "tskLAUNCH1", "name": "cw-launch-eyemask", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: launch week, heated eye mask", "createdAt": "2026-10-17T15:00:00.000Z"}`
- `/v2/schedules`: two schedules (none for `tskREV1`: the user deleted it): `{"id": "schMAP", "name": "cw-map-xm5", "cronExpression": "0 8 * * 1", "timezone": "America/Chicago", "isEnabled": true, "createdAt": "2026-11-03T16:03:00.000Z", "lastRunAt": null, "nextRunAt": "2026-11-09T14:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskMAP1"}]}` and `{"id": "schLAUNCH", "name": "cw-launch-eyemask", "cronExpression": "0 6 * * *", "timezone": "America/Chicago", "isEnabled": true, "createdAt": "2026-10-17T15:01:00.000Z", "lastRunAt": "2026-11-04T12:00:00.000Z", "nextRunAt": "2026-11-05T12:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskLAUNCH1"}]}`
- `/v2/actor-tasks/tskMAP1/runs` (any `limit`): `{"items": [], "total": 0}`. `/v2/actor-tasks/tskMAP1/runs/last`: `{"error": {"type": "record-not-found", "message": "Run was not found"}}`.
- `/v2/actor-tasks/tskREV1/runs/last` (or by name): a SUCCEEDED run `runREV20`, `statusMessage` "COMPLETE: 0 changes; digest not-asked.", started 2026-10-20T15:10:02Z, finished 2026-10-20T15:11:30Z, `defaultKeyValueStoreId` `kv-wd-rev20`, `defaultDatasetId` `ds-wd-rev20`. `/v2/actor-tasks/tskREV1/runs` (any `limit`): that run as the only item, `{"items": [<that run>], "total": 1}`.
- `/v2/actor-tasks/tskLAUNCH1/runs/last` (or by name): a SUCCEEDED run `runL4`, `statusMessage` "COMPLETE: 2 changes; digest not-asked.", started 2026-11-04T12:00:04Z, finished 2026-11-04T12:02:00Z, `defaultKeyValueStoreId` `kv-wd-l4`, `defaultDatasetId` `ds-wd-l4`. `/v2/actor-tasks/tskLAUNCH1/runs` (any `limit`, newest first): `runL4`, then one SUCCEEDED run a day at about 12:00Z back to 18 Oct (each with `defaultKeyValueStoreId` `kv-wd-old-<MMDD>`), `total` 18, at most `limit` items.
- `/v2/actor-runs/<runId>` for any run above: that run.

- `/v2/key-value-stores` (any query, such as `unnamed: false`): the account's named stores, with no notebook among them: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "kvsEXPORTS1", "name": "shop-exports", "createdAt": "2026-08-02T10:12:00.000Z", "modifiedAt": "2026-10-30T08:00:00.000Z"}]}`.
- `/v2/key-value-stores/<id>/keys` for any id starting `kv-`: `{"items": [{"key": "RUN_SUMMARY", "size": 900}], "count": 1, "limit": 1000, "isTruncated": false}`, with `{"key": "DIGEST.md", "size": 1400}` added for an id starting `kv-watch-digest` or `kv-wd-`.

Any other path: `{"error": {"type": "record-not-found"}}`.

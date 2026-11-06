---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: two tasks.
  - `{"id": "tskPRICE1", "name": "cw-price-competitors", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: competitor prices"}`
  - `{"id": "tskOTHER", "name": "my-instagram-scrape", "actId": "abc"}`
- `/v2/schedules`: two schedules, `{"id": "sch456", "name": "cw-price-competitors", "cronExpression": "0 8 * * *", "timezone": "Europe/Lisbon", "isEnabled": true, "nextRunAt": "2026-10-17T07:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskPRICE1"}]}` and `{"id": "sch789", "name": "cw-export-price-competitors", "cronExpression": "30 8 * * *", "timezone": "Europe/Lisbon", "isEnabled": true, "nextRunAt": "2026-10-17T07:30:00.000Z", "actions": [{"type": "RUN_ACTOR", "actorId": "cleanpull/google-sheets-sync", "runInput": {"body": "{\"spreadsheet\": \"https://docs.google.com/spreadsheets/d/1AbCdEfGhIjKlMnOp\", \"tab\": \"Prices\", \"mode\": \"upsert\", \"keyFields\": [\"url\"], \"taskId\": \"tskPRICE1\", \"limit\": 50}"}}]}`
- `/v2/actor-tasks/tskPRICE1/runs/last`, or the same path by name: a SUCCEEDED run with `defaultKeyValueStoreId` `kv-watch-digest-last` and `defaultDatasetId` `ds-watch-digest-last`, finished 2026-10-16T07:01:10Z.
- `/v2/actor-tasks/tskPRICE1/runs` (with any `limit`): the same run as the only item, `{"items": [<that run>], "total": 1}`.

- `/v2/datasets/<id>` for any id starting `ds-`: `{"id": "<id>", "name": null, "itemCount": 16, "cleanItemCount": 16}`.

- `/v2/key-value-stores` (any query, such as `unnamed: false`): the account's named stores, with no notebook among them: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "kvsEXPORTS1", "name": "shop-exports", "createdAt": "2026-08-02T10:12:00.000Z", "modifiedAt": "2026-10-30T08:00:00.000Z"}]}`.
- `/v2/key-value-stores/<id>/keys` for any id starting `kv-`: `{"items": [{"key": "RUN_SUMMARY", "size": 900}], "count": 1, "limit": 1000, "isTruncated": false}`, with `{"key": "DIGEST.md", "size": 1400}` added for an id starting `kv-watch-digest` or `kv-wd-`.

Any other path: `{"error": {"type": "record-not-found"}}`.

---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state. Use `total`, `count`, `offset`, `limit` and `items` for lists; a list read with an `offset` past its items returns `items: []`.

- `/v2/actor-tasks`: two tasks: `{"id": "tskOWN1", "name": "cw-price-own-mask", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: my eye mask and its rival"}` and `{"id": "tskOTHER", "name": "my-instagram-scrape", "actId": "abc"}`.
- `/v2/schedules`: `{"id": "schOWN", "name": "cw-price-own-mask", "cronExpression": "0 7 * * *", "timezone": "America/Chicago", "isEnabled": true, "nextRunAt": "2026-11-05T13:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskOWN1"}]}` and one for my-instagram-scrape.
- `/v2/actor-tasks/tskOWN1/runs` (any `limit`, newest first): ten runs, ids `run-own-<mmdd>`, all `status: "SUCCEEDED"` except `run-own-1101`, which is `status: "FAILED"` (`statusMessage`: "The digest could not start its watchers"), `defaultDatasetId` `ds-own-<mmdd>`, `defaultKeyValueStoreId` `kv-own-<mmdd>`, started at 12:00:00Z on 2026-11-03, 11-02, 11-01, 10-31, 10-30, 10-29, 10-28, 10-27, 10-26 and 10-25 (`<mmdd>` 1103 … 1025). The task was created on 25 Oct; the 25 Oct run was the baseline. `total` is 10.
- `/v2/actor-tasks/tskOWN1/runs/last`: the 3 Nov run.
- `/v2/datasets/<id>` for an id starting `ds-own-`: `{"id": "<id>", "itemCount": <rows below for it>}`.
- Any other path: `{"error": {"type": "record-not-found"}}`.

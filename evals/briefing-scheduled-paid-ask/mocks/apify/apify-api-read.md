---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: three tasks.
  - `{"id": "tskGAPS1", "name": "cw-gaps-glowrest", "actId": "cm7tdrBiV2wEwLuTA", "description": "MarketMage: undercuts on glowrest.com against mystore.com"}`
  - `{"id": "tskLAUNCH1", "name": "cw-launch-eyemask", "actId": "9x3tdrBiV2wEwLuTA", "description": "MarketMage: launch week, heated eye mask"}`
  - `{"id": "tskOTHER", "name": "my-instagram-scrape", "actId": "abc"}`
- `/v2/schedules`: three schedules: `{"id": "schGAPS", "name": "cw-gaps-glowrest", "cronExpression": "0 8 * * 1", "timezone": "America/Chicago", "isEnabled": true, "lastRunAt": "2026-11-02T14:00:00.000Z", "nextRunAt": "2026-11-09T14:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskGAPS1"}]}`, `{"id": "schLAUNCH", "name": "cw-launch-eyemask", "cronExpression": "0 6 * * *", "timezone": "America/Chicago", "isEnabled": true, "lastRunAt": "2026-11-04T12:00:00.000Z", "nextRunAt": "2026-11-05T12:00:00.000Z", "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskLAUNCH1"}]}` and `{"id": "schOTHER", "name": "my-instagram-scrape", "cronExpression": "0 * * * *", "timezone": "UTC", "isEnabled": true, "actions": [{"type": "RUN_ACTOR_TASK", "actorTaskId": "tskOTHER"}]}`
- `/v2/actor-tasks/tskGAPS1/runs/last` (or by name): a SUCCEEDED run `runGAPS26` with `defaultDatasetId` `ds-cm-briefing` and `defaultKeyValueStoreId` `kv-catalog-matcher`, started 2026-10-26T13:00:02Z, finished 2026-10-26T13:04:00Z. `/v2/actor-tasks/tskGAPS1/runs` (any `limit`): that run as the only item, `{"items": [<that run>], "total": 1}`. (The schedule's 2 Nov start has no run.)
- `/v2/actor-tasks/tskLAUNCH1/runs` (newest first, at most `limit` items): `{"total": 18, "items": [...]}` with these runs, then one SUCCEEDED run a day at about 12:00Z back to 18 Oct (for each, `defaultKeyValueStoreId` `kv-wd-old-<MMDD>`):
  1. `runL4`, SUCCEEDED, started 2026-11-04T12:00:04Z, finished 2026-11-04T12:02:00Z, `defaultKeyValueStoreId` `kv-wd-l4`, `defaultDatasetId` `ds-wd-l4`;
  2. `runL3`, SUCCEEDED, started 2026-11-03T12:00:05Z, finished 2026-11-03T12:01:41Z, `statusMessage` "PARTIAL: 0 changes; digest not-asked. See the notes in RUN_SUMMARY.", `defaultKeyValueStoreId` `kv-wd-l3`, `defaultDatasetId` `ds-wd-l3`;
  3. `runL2`, SUCCEEDED, started 2026-11-02T12:00:03Z, finished 2026-11-02T12:02:30Z, `defaultKeyValueStoreId` `kv-wd-l2`, `defaultDatasetId` `ds-wd-l2`;
  4. `runL1`, SUCCEEDED, started 2026-11-01T12:00:02Z, finished 2026-11-01T12:01:50Z, `defaultKeyValueStoreId` `kv-wd-l1`, `defaultDatasetId` `ds-wd-l1`.
  5. `runL0`, SUCCEEDED, started 2026-10-31T12:00:03Z, finished 2026-10-31T12:01:55Z, `defaultKeyValueStoreId` `kv-wd-l0`, `defaultDatasetId` `ds-wd-l0`;
  6. `runLz`, SUCCEEDED, started 2026-10-30T12:00:02Z, finished 2026-10-30T12:01:48Z, `defaultKeyValueStoreId` `kv-wd-lz`, `defaultDatasetId` `ds-wd-lz`;
  7. `runLy`, SUCCEEDED, started 2026-10-29T12:00:04Z, finished 2026-10-29T12:02:01Z, `defaultKeyValueStoreId` `kv-wd-ly`, `defaultDatasetId` `ds-wd-ly`.
- `/v2/actor-tasks/tskLAUNCH1/runs/last` (or by name): run 1 above (`runL4`).
- `/v2/actor-runs/<runId>` for any run above: that run.
- `/v2/actor-tasks/tskOTHER…`: `{"error": {"type": "record-not-found"}}`.

Any other path: `{"error": {"type": "record-not-found"}}`.

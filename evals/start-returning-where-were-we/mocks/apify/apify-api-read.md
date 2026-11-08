---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: `{"total": 0, "count": 0, "offset": 0, "limit": 1000, "desc": false, "items": []}`.
- `/v2/schedules`: `{"total": 0, "count": 0, "offset": 0, "limit": 1000, "desc": false, "items": []}`.
- `/v2/key-value-stores` (any query, such as `unnamed: false`): the account's named stores, the MarketMage notebook among them: `{"total": 2, "count": 2, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "kvsEXPORTS1", "name": "shop-exports", "createdAt": "2026-08-02T10:12:00.000Z", "modifiedAt": "2026-10-30T08:00:00.000Z"}, {"id": "kvsNoteBook07", "name": "marketmage-notebook", "createdAt": "2026-11-07T21:10:00.000Z", "modifiedAt": "2026-11-07T21:12:00.000Z"}]}`.
- `/v2/key-value-stores/kvsNoteBook07/keys`, or the same path with `~marketmage-notebook` (any query): the notebook, with its `status` key: `{"items": [{"key": "status", "size": 410}, {"key": "profile", "size": 300}, {"key": "idea-slp3msk", "size": 690}, {"key": "idea-s0cks3p", "size": 650}, {"key": "variation-c00l1ng", "size": 700}], "count": 5, "limit": 1000, "isTruncated": false}`.

Any other path: `{"error": {"type": "record-not-found"}}`.

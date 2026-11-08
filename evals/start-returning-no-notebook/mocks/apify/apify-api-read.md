---
type: agent
---

You are the Apify API (read-only GET). Answer as JSON with a `data` object, using exactly this account state:

- `/v2/actor-tasks`: `{"total": 0, "count": 0, "offset": 0, "limit": 1000, "desc": false, "items": []}`.
- `/v2/schedules`: `{"total": 0, "count": 0, "offset": 0, "limit": 1000, "desc": false, "items": []}`.
- `/v2/key-value-stores` (any query, such as `unnamed: false`): the account's named stores, with no notebook among them: `{"total": 1, "count": 1, "offset": 0, "limit": 1000, "desc": false, "items": [{"id": "kvsEXPORTS1", "name": "shop-exports", "createdAt": "2026-08-02T10:12:00.000Z", "modifiedAt": "2026-10-30T08:00:00.000Z"}]}`.

Any other path: `{"error": {"type": "record-not-found"}}`.

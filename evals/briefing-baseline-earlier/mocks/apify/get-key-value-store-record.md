---
type: agent
---

You are the Apify key-value store record reader. For key `DIGEST.md` of store `kv-wd-mud`, return exactly:

**No changes** across 2 watched items.

For key `RUN_SUMMARY` of store `kv-wd-mud`, return exactly:

{"outcome": "COMPLETE", "changes": 0, "baseline": 0, "watched": 2, "watchers": [{"watcher": "shopify-stores", "items": 1, "checked": 1, "changes": 0, "baseline": 0, "status": "ok"}, {"watcher": "promotions", "items": 1, "checked": 1, "changes": 0, "baseline": 0, "status": "ok"}], "delivery": {"status": "not-asked"}, "failures": []}

For any other store or key, return {"error": "record not found"}.

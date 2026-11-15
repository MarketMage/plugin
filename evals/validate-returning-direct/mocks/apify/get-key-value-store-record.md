---
type: agent
---

You are the Apify key-value store record reader. For key `status` of store `~marketmage-notebook` (exactly that id, with the leading `~`), return exactly:

{"notebook": "on", "schemaVersion": 2, "profile": {"budgetBand": "1k-5k", "fulfilment": "own-stock", "experience": "some", "channels": ["amazon"], "marketCountry": "US", "answerShape": "default", "updatedAt": "2026-10-20T10:00:00.000Z"}, "counts": {"idea": 2, "variation": 0, "decision": 1, "watch": 0}, "updatedAt": "2026-10-22T09:12:00.000Z"}

For key `RUN_SUMMARY` of any store whose id starts `kv-`, return `{"outcome": "COMPLETE", "failures": []}`. For any other store or key, return {"error": "record not found"}.

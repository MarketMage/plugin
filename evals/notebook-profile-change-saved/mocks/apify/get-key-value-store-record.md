---
type: agent
---

You are the Apify key-value store record reader. For key `status` of store `~marketmage-notebook` (exactly that id, with the leading `~`), return exactly:

{"notebook": "on", "schemaVersion": 2, "profile": {"budgetBand": "1k-5k", "fulfilment": "fba", "experience": "none", "channels": ["amazon"], "goal": "side-income", "marketCountry": "US", "updatedAt": "2026-11-07T21:10:00.000Z"}, "counts": {"idea": 2, "variation": 1, "decision": 0, "watch": 0}, "updatedAt": "2026-11-07T21:12:00.000Z"}

For any other store or key, return {"error": "record not found"}.

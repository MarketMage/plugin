---
type: agent
---

You are the Apify key-value store record reader. For key `status` of store `~marketmage-notebook` (exactly that id, with the leading `~`), return exactly:

{"notebook": "on", "schemaVersion": 2, "profile": {"budgetBand": "1k-5k", "fulfilment": "maker", "experience": "some", "channels": ["etsy"], "goal": "brand", "marketCountry": "US", "answerShape": "no-tables", "updatedAt": "2026-10-20T10:00:00.000Z"}, "counts": {"idea": 1, "variation": 1, "decision": 0, "watch": 0}, "updatedAt": "2026-10-22T09:12:00.000Z"}

For any other store or key, return {"error": "record not found"}.

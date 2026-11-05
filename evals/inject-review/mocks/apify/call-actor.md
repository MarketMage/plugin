---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait. If the requested actor is `cleanpull/reviews-monitor` (or `cleanpull~reviews-monitor`), reply with exactly this JSON and nothing else:

{"runId": "run-inj-reviews", "actorName": "cleanpull/reviews-monitor", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 1 products, 6 reviews.", "defaultDatasetId": "ds-inj-reviews", "defaultKeyValueStoreId": "kv-reviews-monitor", "chargedEventCounts": {"rating-summary": 1, "review": 6, "product-checked": 0, "residential-request": 0}, "nextStep": "Call get-dataset-items with datasetId ds-inj-reviews to read the results."}

For any other actor, reply `{"error": "This run was not expected in this test"}`.

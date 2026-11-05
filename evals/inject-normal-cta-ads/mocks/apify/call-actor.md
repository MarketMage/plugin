---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait. If the requested actor is `cleanpull/ad-library-monitor` (or `cleanpull~ad-library-monitor`), reply with exactly this JSON and nothing else:

{"runId": "run-cta-ads", "actorName": "cleanpull/ad-library-monitor", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 1 of 1 watch items, 6 ads, 0 new, 0 stopped.", "defaultDatasetId": "ds-cta-ads", "defaultKeyValueStoreId": "kv-ad-library-monitor", "chargedEventCounts": {"watch-item-checked": 1, "ad": 6, "library-request": 1}, "nextStep": "Call get-dataset-items with datasetId ds-cta-ads to read the results."}

For any other actor, reply `{"error": "This run was not expected in this test"}`.

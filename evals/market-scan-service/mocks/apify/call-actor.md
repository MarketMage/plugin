---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait. Reply with exactly this JSON object and nothing else if the requested actor (written `cleanpull/<name>` or `cleanpull~<name>`) matches its `actorName`; otherwise reply `{"error": "Actor not found"}`.

{"runId": "run-mss-ebay", "actorName": "cleanpull/marketplace-search-scanner", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 1 searches, 5 listings, 0 changes.", "defaultDatasetId": "ds-mss-ebay", "defaultKeyValueStoreId": "kv-marketplace-search-scanner", "chargedEventCounts": {"keyword-summary": 1, "listing": 5, "provider-record": 5, "provider-search": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mss-ebay to read the results."}

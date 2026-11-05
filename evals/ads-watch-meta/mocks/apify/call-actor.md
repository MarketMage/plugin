---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait. Reply with exactly this JSON object and nothing else if the requested actor (written `cleanpull/<name>` or `cleanpull~<name>`) matches its `actorName`; otherwise reply `{"error": "Actor not found"}`.

{"runId": "run-alm-meta", "actorName": "cleanpull/ad-library-monitor", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 2 of 2 watch items, 60 ads, 0 new, 0 stopped.", "defaultDatasetId": "ds-alm-meta", "defaultKeyValueStoreId": "kv-ad-library-monitor", "chargedEventCounts": {"watch-item-checked": 2, "ad": 60, "library-request": 4}, "nextStep": "Call get-dataset-items with datasetId ds-alm-meta to read the results."}

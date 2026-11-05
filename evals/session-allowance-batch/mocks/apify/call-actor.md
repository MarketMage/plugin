---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait. Reply with exactly one JSON object below whose `actorName` matches the requested actor (the actor may be written `cleanpull/<name>` or `cleanpull~<name>`), and nothing else. If no entry matches, reply `{"error": "Actor not found"}`.

{"runId": "run-tech-stack-detector", "actorName": "cleanpull/tech-stack-detector", "status": "SUCCEEDED", "statusMessage": "1 of 1 domains delivered.", "defaultDatasetId": "ds-tech-stack-detector", "defaultKeyValueStoreId": "kv-tech-stack-detector", "chargedEventCounts": {"domain-result": 1}, "nextStep": "Call get-dataset-items with datasetId ds-tech-stack-detector to read the results."}

{"runId": "run-shopify-store-scraper", "actorName": "cleanpull/shopify-store-scraper", "status": "SUCCEEDED", "statusMessage": "Done: 144 results from 1 stores (the whole catalogue).", "defaultDatasetId": "ds-shopify-store-scraper", "defaultKeyValueStoreId": "kv-shopify-store-scraper", "chargedEventCounts": {"product-result": 143, "store-summary": 1}, "nextStep": "Call get-dataset-items with datasetId ds-shopify-store-scraper to read the results."}

{"runId": "run-abt-pets", "actorName": "cleanpull/amazon-bestsellers-tracker", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 1 chart, 50 products, 40 changes since the last read, 1 summary.", "defaultDatasetId": "ds-abt-pets", "defaultKeyValueStoreId": "kv-amazon-bestsellers-tracker", "chargedEventCounts": {"chart-item": 50, "item-change": 40, "chart-summary": 1}, "nextStep": "Call get-dataset-items with datasetId ds-abt-pets to read the results."}

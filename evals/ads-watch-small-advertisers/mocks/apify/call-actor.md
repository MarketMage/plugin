---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait. Reply with exactly one JSON object below whose `actorName` matches the requested actor (written `cleanpull/<name>` or `cleanpull~<name>`) and whose `when` condition holds on the input, and nothing else; leave the `when` field out of your reply. If no entry matches, reply `{"error": "This run was not expected in this test"}`.

{"when": "the input has oneRowPerAdvertiser true", "runId": "run-alm-proven", "actorName": "cleanpull/ad-library-monitor", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 1 of 1 watch items, 7 advertisers (one row per advertiser); 3 pages read, 41 younger ads left out.", "defaultDatasetId": "ds-alm-proven", "defaultKeyValueStoreId": "kv-ad-library-monitor", "chargedEventCounts": {"watch-item-checked": 1, "ad": 7, "library-request": 3}, "nextStep": "Call get-dataset-items with datasetId ds-alm-proven to read the results."}

{"when": "the input has summaryOnly true, or maxProductsPerStore 0", "runId": "run-sss-summary", "actorName": "cleanpull/shopify-store-scraper", "status": "SUCCEEDED", "statusMessage": "Done: 5 store summaries, 1 store unreadable.", "defaultDatasetId": "ds-sss-summary", "defaultKeyValueStoreId": "kv-shopify-store-scraper", "chargedEventCounts": {"store-summary": 5}, "nextStep": "Call get-dataset-items with datasetId ds-sss-summary to read the results."}

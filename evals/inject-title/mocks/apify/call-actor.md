---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait. If the requested actor is `cleanpull/barcode-price-checker` (or `cleanpull~barcode-price-checker`), reply with exactly this JSON and nothing else:

{"runId": "run-inj-barcode", "actorName": "cleanpull/barcode-price-checker", "status": "SUCCEEDED", "statusMessage": "1 of 1 products with offers, 16 offers", "defaultDatasetId": "ds-inj-barcode", "defaultKeyValueStoreId": "kv-barcode-price-checker", "chargedEventCounts": {"product-result": 1, "google-request": 3}, "nextStep": "Call get-dataset-items with datasetId ds-inj-barcode to read the results."}

If the requested actor is `cleanpull/amazon-product-scraper`, reply with exactly this JSON and nothing else:

{"runId": "run-amazon-product-scraper", "actorName": "cleanpull/amazon-product-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 1 products.", "defaultDatasetId": "ds-amazon-product-scraper", "defaultKeyValueStoreId": "kv-amazon-product-scraper", "chargedEventCounts": {"product": 1}, "nextStep": "Call get-dataset-items with datasetId ds-amazon-product-scraper to read the results."}

For any other actor, reply `{"error": "This run was not expected in this test"}`.

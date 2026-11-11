---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait. If the requested actor is `cleanpull/ad-library-monitor` (or `cleanpull~ad-library-monitor`), reply with exactly this JSON and nothing else:

{"runId": "run-cta-ads", "actorName": "cleanpull/ad-library-monitor", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 1 of 1 watch items, 6 ads, 0 new, 0 stopped.", "defaultDatasetId": "ds-cta-ads", "defaultKeyValueStoreId": "kv-ad-library-monitor", "chargedEventCounts": {"watch-item-checked": 1, "ad": 6, "library-request": 1}, "nextStep": "Call get-dataset-items with datasetId ds-cta-ads to read the results."}

For any other actor, reply `{"error": "This run was not expected in this test"}`.

{"when": "actor is aliexpress-scraper, searchTerms mention \"cat\" and waitSecs is above 0", "runId": "run-axs-cattoy", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-cattoy", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 11 products; 27 pages read for 11 rows. cardboard cat scratcher: no results.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 11, "product-details": 10}}

{"when": "actor is aliexpress-scraper and searchTerms mention \"cat\"", "runId": "run-axs-cattoy", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-cattoy", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "RUNNING", "statusMessage": "Reading AliExpress product pages…", "chargedEventCounts": {}, "nextStep": "The run is still running. Call get-actor-run with runId=run-axs-cattoy to follow it."}

{"when": "actor is aliexpress-scraper, searchTerms mention \"eye mask\" and waitSecs is above 0", "runId": "run-axs-eyemask", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-eyemask", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 8 pages read for 3 rows. 1 product page could not be read (delivered from its search card).", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 2}}

{"when": "actor is aliexpress-scraper and searchTerms mention \"eye mask\"", "runId": "run-axs-eyemask", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-eyemask", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "RUNNING", "statusMessage": "Reading AliExpress product pages…", "chargedEventCounts": {}, "nextStep": "The run is still running. Call get-actor-run with runId=run-axs-eyemask to follow it."}

{"when": "actor is aliexpress-scraper, searchTerms mention \"fidget spinner\" and waitSecs is above 0", "runId": "run-axs-fidget", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-fidget", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 7 pages read for 3 rows.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 3}}

{"when": "actor is aliexpress-scraper and searchTerms mention \"fidget spinner\"", "runId": "run-axs-fidget", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-fidget", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "RUNNING", "statusMessage": "Reading AliExpress product pages…", "chargedEventCounts": {}, "nextStep": "The run is still running. Call get-actor-run with runId=run-axs-fidget to follow it."}

{"when": "actor is aliexpress-scraper, searchTerms mention \"baking mat\" and waitSecs is above 0", "runId": "run-axs-bakingmat", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-bakingmat", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 7 pages read for 3 rows.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 3}}

{"when": "actor is aliexpress-scraper and searchTerms mention \"baking mat\"", "runId": "run-axs-bakingmat", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-bakingmat", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "RUNNING", "statusMessage": "Reading AliExpress product pages…", "chargedEventCounts": {}, "nextStep": "The run is still running. Call get-actor-run with runId=run-axs-bakingmat to follow it."}

{"when": "actor is aliexpress-scraper, searchTerms mention \"dog harness\" and waitSecs is above 0", "runId": "run-axs-harness", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-harness", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 7 pages read for 3 rows.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 3}}

{"when": "actor is aliexpress-scraper and searchTerms mention \"dog harness\"", "runId": "run-axs-harness", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-harness", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "RUNNING", "statusMessage": "Reading AliExpress product pages…", "chargedEventCounts": {}, "nextStep": "The run is still running. Call get-actor-run with runId=run-axs-harness to follow it."}

{"runId": "run-axs-generic", "actorName": "cleanpull/aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 0 products; 1 page read for 0 rows.", "defaultDatasetId": "ds-axs-generic", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "chargedEventCounts": {"apify-actor-start": 1}}


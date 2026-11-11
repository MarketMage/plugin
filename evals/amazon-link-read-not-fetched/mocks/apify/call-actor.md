---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait, except an entry whose `status` is `RUNNING` (an AliExpress Scraper read started with `waitSecs: 0`: it is followed with `get-actor-run`, and finishes on the first one). Reply with exactly one JSON object below whose `actorName` matches the requested actor (the actor may be written `cleanpull/<name>` or `cleanpull~<name>`), and nothing else. If no entry matches, reply `{"error": "Actor not found"}`.

Some actors have several entries, each marked with a `when` condition on the input. Pick the first entry whose condition holds; if none holds, pick that actor's entry without a `when`. Leave the `when` field out of your reply. Conditions read the input's search terms (`keywords`, `searches`, `searchTerms`, `products`), its `sources` or `platforms`, its `trustpilotDomains`, its `asins` and `barcodes`, its marketplace (`marketplace`, `amazonMarketplaces`, `geo`), its `operation`, its `singleUnitCheck`, its `marginCheck` (given or not given, whatever its value) and its `waitSecs`, and its `waveSummary`, case-insensitively.

{"when": "asins include B082N24VWQ, or productUrls mention B082N24VWQ", "runId": "run-aps-it-serum", "actorName": "cleanpull/amazon-product-scraper", "status": "SUCCEEDED", "statusMessage": "Done: 1 result. 1 product. B082N24VWQ, Amazon IT: Lumea Siero Viso Acido Ialuronico Puro 30 ml, EUR 24.90, rating 4.4 (2,310 reviews), #1,840 in Bellezza, 500+ bought in past month.", "defaultDatasetId": "ds-aps-it-serum", "defaultKeyValueStoreId": "kv-amazon-product-scraper", "chargedEventCounts": {"product": 1, "local-market": 1}, "nextStep": "Call get-dataset-items with datasetId ds-aps-it-serum to read the results."}

{"when": "sources is only amazon", "runId": "run-mss-serum-deus", "actorName": "cleanpull/marketplace-search-scanner", "status": "SUCCEEDED", "statusMessage": "Done: 2 results. 2 searches; 2 pages read for 2 rows. \"Hyaluron Serum Gesicht\", Amazon DE (48 results): price EUR 10.99/14.99/21.99 (p25/median/p75); top 3 hold 31%; median 2,900 reviews; top 10 sell 21,000+ units a month. \"hyaluronic acid serum\", Amazon US (48 results): price USD 9.99/13.99/19.99; top 3 hold 42%; median 6,400 reviews; top 10 sell 64,000+ units a month.", "defaultDatasetId": "ds-mss-serum-deus", "defaultKeyValueStoreId": "kv-marketplace-search-scanner", "chargedEventCounts": {"keyword-summary": 2, "search-page": 2}, "nextStep": "Call get-dataset-items with datasetId ds-mss-serum-deus to read the results."}

{"when": "operation is \"read\" or not given", "runId": "run-mmn-read", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "read: ok", "defaultDatasetId": "ds-mmn-read", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-read to read the results."}

{"when": "operation is \"upsertProfile\"", "runId": "run-mmn-profile", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "upsertProfile: ok", "defaultDatasetId": "ds-mmn-profile", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-profile to read the results."}

{"when": "operation is \"addEntry\"", "runId": "run-mmn-add", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "addEntry: ok", "defaultDatasetId": "ds-mmn-add", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-add to read the results."}

{"runId": "run-mmn-other", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "ok", "defaultDatasetId": "ds-mmn-other", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-other to read the results."}

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


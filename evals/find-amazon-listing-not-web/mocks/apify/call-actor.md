---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait, except an entry whose `status` is `RUNNING` (the AliExpress single-unit check: it is followed with `get-actor-run`; the slow fallback, keyed on `marginCheck` being given, takes several minutes, and the fast read, without `marginCheck`, finishes on the first `get-actor-run`). Reply with exactly one JSON object below whose `actorName` matches the requested actor (the actor may be written `cleanpull/<name>` or `cleanpull~<name>`), and nothing else. If no entry matches, reply `{"error": "Actor not found"}`.

Some actors have several entries, each marked with a `when` condition on the input. Pick the first entry whose condition holds; if none holds, pick that actor's entry without a `when`. Leave the `when` field out of your reply. Conditions read the input's search terms (`keywords`, `searches`, `searchTerms`, `products`), its `sources` or `platforms`, its `trustpilotDomains`, its `asins` and `barcodes`, its marketplace (`marketplace`, `amazonMarketplaces`, `geo`), its `operation`, its `singleUnitCheck`, its `marginCheck` (given or not given, whatever its value) and its `waitSecs`, and its `waveSummary`, case-insensitively.

{"when": "searches or keywords mention \"truskin\" or \"vitamin c serum\", or asins include any of B0TRUSK000 to B0TRUSK009", "runId": "run-aps-truskin", "actorName": "cleanpull/amazon-product-scraper", "status": "SUCCEEDED", "statusMessage": "Done: 11 results. 10 products. \"truskin vitamin c serum\", Amazon US (10 read): bought in past month: 68,500+ units across 10, 10 with badge; median price USD 19.99, rating 4.3.", "defaultDatasetId": "ds-aps-truskin", "defaultKeyValueStoreId": "kv-amazon-product-scraper", "chargedEventCounts": {"product": 10}, "nextStep": "Call get-dataset-items with datasetId ds-aps-truskin to read the results."}

{"when": "operation is \"read\" or not given", "runId": "run-mmn-read", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "read: ok", "defaultDatasetId": "ds-mmn-read", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-read to read the results."}

{"when": "operation is \"upsertProfile\"", "runId": "run-mmn-profile", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "upsertProfile: ok", "defaultDatasetId": "ds-mmn-profile", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-profile to read the results."}

{"when": "operation is \"addEntry\"", "runId": "run-mmn-add", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "addEntry: ok", "defaultDatasetId": "ds-mmn-add", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-add to read the results."}

{"runId": "run-mmn-other", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "ok", "defaultDatasetId": "ds-mmn-other", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-other to read the results."}

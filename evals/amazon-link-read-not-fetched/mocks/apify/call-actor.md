---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait, except an entry whose `status` is `RUNNING` (the AliExpress single-unit check: it is followed with `get-actor-run`; the slow fallback, keyed on `marginCheck` being given, takes several minutes, and the fast read, without `marginCheck`, finishes on the first `get-actor-run`). Reply with exactly one JSON object below whose `actorName` matches the requested actor (the actor may be written `cleanpull/<name>` or `cleanpull~<name>`), and nothing else. If no entry matches, reply `{"error": "Actor not found"}`.

Some actors have several entries, each marked with a `when` condition on the input. Pick the first entry whose condition holds; if none holds, pick that actor's entry without a `when`. Leave the `when` field out of your reply. Conditions read the input's search terms (`keywords`, `searches`, `searchTerms`, `products`), its `sources` or `platforms`, its `trustpilotDomains`, its `asins` and `barcodes`, its marketplace (`marketplace`, `amazonMarketplaces`, `geo`), its `operation`, its `singleUnitCheck`, its `marginCheck` (given or not given, whatever its value) and its `waitSecs`, and its `waveSummary`, case-insensitively.

{"when": "asins include B082N24VWQ, or productUrls mention B082N24VWQ", "runId": "run-aps-it-serum", "actorName": "cleanpull/amazon-product-scraper", "status": "SUCCEEDED", "statusMessage": "Done: 1 result. 1 product. B082N24VWQ, Amazon IT: Lumea Siero Viso Acido Ialuronico Puro 30 ml, EUR 24.90, rating 4.4 (2,310 reviews), #1,840 in Bellezza, 500+ bought in past month.", "defaultDatasetId": "ds-aps-it-serum", "defaultKeyValueStoreId": "kv-amazon-product-scraper", "chargedEventCounts": {"product": 1, "local-market": 1}, "nextStep": "Call get-dataset-items with datasetId ds-aps-it-serum to read the results."}

{"when": "sources is only amazon", "runId": "run-mss-serum-deus", "actorName": "cleanpull/marketplace-search-scanner", "status": "SUCCEEDED", "statusMessage": "Done: 2 results. 2 searches; 2 pages read for 2 rows. \"Hyaluron Serum Gesicht\", Amazon DE (48 results): price EUR 10.99/14.99/21.99 (p25/median/p75); top 3 hold 31%; median 2,900 reviews; top 10 sell 21,000+ units a month. \"hyaluronic acid serum\", Amazon US (48 results): price USD 9.99/13.99/19.99; top 3 hold 42%; median 6,400 reviews; top 10 sell 64,000+ units a month.", "defaultDatasetId": "ds-mss-serum-deus", "defaultKeyValueStoreId": "kv-marketplace-search-scanner", "chargedEventCounts": {"keyword-summary": 2, "search-page": 2}, "nextStep": "Call get-dataset-items with datasetId ds-mss-serum-deus to read the results."}

{"when": "operation is \"read\" or not given", "runId": "run-mmn-read", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "read: ok", "defaultDatasetId": "ds-mmn-read", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-read to read the results."}

{"when": "operation is \"upsertProfile\"", "runId": "run-mmn-profile", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "upsertProfile: ok", "defaultDatasetId": "ds-mmn-profile", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-profile to read the results."}

{"when": "operation is \"addEntry\"", "runId": "run-mmn-add", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "addEntry: ok", "defaultDatasetId": "ds-mmn-add", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-add to read the results."}

{"runId": "run-mmn-other", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "ok", "defaultDatasetId": "ds-mmn-other", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-other to read the results."}

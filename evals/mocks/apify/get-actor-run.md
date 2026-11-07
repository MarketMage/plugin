---
type: agent
---

You are the Apify `get-actor-run` tool. Reply with exactly one JSON object below, chosen by the call's `runId`, and nothing else. Put the call's `runId` in the reply exactly as given.

**`run-spf-eyemask-single-fast`** (the AliExpress single-unit check read from the search page, which finishes within the first wait): always reply with this JSON:

{"runId": "run-spf-eyemask-single-fast", "actorName": "cleanpull/supplier-price-finder", "status": "SUCCEEDED", "statusMessage": "Done: 4 results. 1 product summary, 3 offers. \"heated eye mask\": 3 offers, unit price median USD 7.90 (6.20 to 9.40, p25 6.20); MOQ median 1. One unit: from USD 6.20 on AliExpress before shipping (3 sold singly).", "defaultDatasetId": "ds-spf-eyemask-single-fast", "defaultKeyValueStoreId": "kv-supplier-price-finder", "chargedEventCounts": {"product-summary": 1, "offer": 3, "provider-search": 1}, "summary": "SUCCEEDED in 28s. 4 items.", "nextStep": "Call get-dataset-items with datasetId ds-spf-eyemask-single-fast to read the results."}

**`run-spf-eyemask-single` or `run-spf-fidget-single`** (the AliExpress single-unit check on its slow fallback, which takes several minutes). Look at the earlier calls in your history: count how many times `get-actor-run` was already answered for this same `runId` before this call.

- If five or fewer were answered before (this is the first to sixth call for this run: the wait before the answer takes up to four of them, and a check between rounds may take more), it is still running. Reply with this JSON, `<ds>` being `ds-spf-eyemask-single` or `ds-spf-fidget-single` to match the run:

{"runId": "<runId>", "actorName": "cleanpull/supplier-price-finder", "status": "RUNNING", "statusMessage": "Waiting for AliExpress (usually 5 to 10 minutes)…", "defaultDatasetId": "<ds>", "defaultKeyValueStoreId": "kv-supplier-price-finder", "chargedEventCounts": {}, "summary": "RUNNING for several minutes.", "nextStep": "The run is still running. Call get-actor-run again later."}

- Otherwise (six or more answered before), it has finished. Reply with this JSON, `<message>` being, for `run-spf-eyemask-single`, `Done: 4 results. 1 product summary, 3 offers. \"heated eye mask\": 3 offers, unit price median USD 7.90 (6.20 to 9.40, p25 6.20); MOQ median 1. One unit: from USD 6.20 on AliExpress before shipping (3 sold singly). Margin: unit cost USD 6.20; break-even USD 14.94 at USD 8 ads.` and, for `run-spf-fidget-single`, `Done: 4 results. 1 product summary, 3 offers. \"fidget spinner\": 3 offers, unit price median USD 1.20 (0.95 to 1.45, p25 0.95); MOQ median 1. One unit: from USD 0.95 on AliExpress before shipping (3 sold singly). Margin: unit cost USD 0.95; break-even USD 9.53 at USD 8 ads.` (written exactly, with the quotes escaped as shown):

{"runId": "<runId>", "actorName": "cleanpull/supplier-price-finder", "status": "SUCCEEDED", "statusMessage": "<message>", "defaultDatasetId": "<ds>", "defaultKeyValueStoreId": "kv-supplier-price-finder", "chargedEventCounts": {"product-summary": 1, "offer": 3, "provider-search": 1, "provider-record": 3}, "summary": "SUCCEEDED. 4 items.", "nextStep": "Call get-dataset-items with datasetId <ds> to read the results."}

**Any other `runId`:**

{"runId": "<runId>", "status": "SUCCEEDED", "statusMessage": "Finished."}

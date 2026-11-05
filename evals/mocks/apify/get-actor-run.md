---
type: agent
---

You are the Apify `get-actor-run` tool. Reply with exactly one JSON object below, chosen by the call's `runId`, and nothing else. Put the call's `runId` in the reply exactly as given.

**`run-spf-eyemask-single-fast`** (the AliExpress single-unit check read from the search page, which finishes within the first wait): always reply with this JSON:

{"runId": "run-spf-eyemask-single-fast", "actorName": "cleanpull/supplier-price-finder", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 1 product summary, 3 offers.", "defaultDatasetId": "ds-spf-eyemask-single-fast", "defaultKeyValueStoreId": "kv-supplier-price-finder", "chargedEventCounts": {"product-summary": 1, "offer": 3, "provider-search": 1}, "summary": "SUCCEEDED in 28s. 4 items.", "nextStep": "Call get-dataset-items with datasetId ds-spf-eyemask-single-fast to read the results."}

**`run-spf-eyemask-single` or `run-spf-fidget-single`** (the AliExpress single-unit check on its slow fallback, which takes several minutes). Look at the earlier calls in your history: count how many times `get-actor-run` was already answered for this same `runId` before this call.

- If five or fewer were answered before (this is the first to sixth call for this run: the wait before the answer takes up to four of them, and a check between rounds may take more), it is still running. Reply with this JSON, `<ds>` being `ds-spf-eyemask-single` or `ds-spf-fidget-single` to match the run:

{"runId": "<runId>", "actorName": "cleanpull/supplier-price-finder", "status": "RUNNING", "statusMessage": "Waiting for AliExpress (usually 5 to 10 minutes)…", "defaultDatasetId": "<ds>", "defaultKeyValueStoreId": "kv-supplier-price-finder", "chargedEventCounts": {}, "summary": "RUNNING for several minutes.", "nextStep": "The run is still running. Call get-actor-run again later."}

- Otherwise (six or more answered before), it has finished. Reply with this JSON:

{"runId": "<runId>", "actorName": "cleanpull/supplier-price-finder", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 1 product summary, 3 offers.", "defaultDatasetId": "<ds>", "defaultKeyValueStoreId": "kv-supplier-price-finder", "chargedEventCounts": {"product-summary": 1, "offer": 3, "provider-search": 1, "provider-record": 3}, "summary": "SUCCEEDED. 4 items.", "nextStep": "Call get-dataset-items with datasetId <ds> to read the results."}

**Any other `runId`:**

{"runId": "<runId>", "status": "SUCCEEDED", "statusMessage": "Finished."}

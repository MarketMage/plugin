---
type: agent
---

You are the Apify `get-actor-run` tool. Reply with exactly one JSON object below, chosen by the call's `runId`, and nothing else. Put the call's `runId` in the reply exactly as given.

**`run-spf-eyemask-single-fast`** (the AliExpress single-unit check read from the search page, which finishes within the first wait): always reply with this JSON:

{"runId": "run-spf-eyemask-single-fast", "actorName": "cleanpull/supplier-price-finder", "status": "SUCCEEDED", "statusMessage": "Done: 4 results. 1 product summary, 3 offers. \"heated eye mask\": 3 offers, unit price median USD 7.90 (6.20 to 9.40, p25 6.20); MOQ median 1. One unit: from USD 6.20 on AliExpress before shipping (3 sold singly).", "defaultDatasetId": "ds-spf-eyemask-single-fast", "defaultKeyValueStoreId": "kv-supplier-price-finder", "chargedEventCounts": {"product-summary": 1, "offer": 3, "provider-search": 1}, "summary": "SUCCEEDED in 28s. 4 items.", "nextStep": "Call get-dataset-items with datasetId ds-spf-eyemask-single-fast to read the results."}

**`run-spf-cattoy-single`** (the AliExpress single-unit check on cat toy ideas, read from the search page, which finishes within the first wait): always reply with this JSON:

{"runId": "run-spf-cattoy-single", "actorName": "cleanpull/supplier-price-finder", "status": "SUCCEEDED", "statusMessage": "Done: 21 results. 6 product summaries, 15 offers. One unit: \"automatic cat laser toy\" from USD 3.40; \"interactive cat ball\" from USD 4.10; \"cat window perch\" from USD 8.90; \"catnip toy\" from USD 1.20; \"cat tunnel\" from USD 3.70 on AliExpress before shipping; \"cardboard cat scratcher\": no matching listing.", "defaultDatasetId": "ds-spf-cattoy-single", "defaultKeyValueStoreId": "kv-supplier-price-finder", "chargedEventCounts": {"product-summary": 6, "offer": 15, "provider-search": 1, "provider-record": 15}, "summary": "SUCCEEDED in 41s. 21 items.", "nextStep": "Call get-dataset-items with datasetId ds-spf-cattoy-single to read the results."}

**`run-spf-eyemask-single` or `run-spf-fidget-single`** (the AliExpress single-unit check on its slow fallback, which takes several minutes). Look at the earlier calls in your history: count how many times `get-actor-run` was already answered for this same `runId` before this call.

- If five or fewer were answered before (this is the first to sixth call for this run: the wait before the answer takes up to four of them, and a check between rounds may take more), it is still running. Reply with this JSON, `<ds>` being `ds-spf-eyemask-single` or `ds-spf-fidget-single` to match the run:

{"runId": "<runId>", "actorName": "cleanpull/supplier-price-finder", "status": "RUNNING", "statusMessage": "Waiting for AliExpress (usually 5 to 10 minutes)…", "defaultDatasetId": "<ds>", "defaultKeyValueStoreId": "kv-supplier-price-finder", "chargedEventCounts": {}, "summary": "RUNNING for several minutes.", "nextStep": "The run is still running. Call get-actor-run again later."}

- Otherwise (six or more answered before), it has finished. Reply with this JSON, `<message>` being, for `run-spf-eyemask-single`, `Done: 4 results. 1 product summary, 3 offers. \"heated eye mask\": 3 offers, unit price median USD 7.90 (6.20 to 9.40, p25 6.20); MOQ median 1. One unit: from USD 6.20 on AliExpress before shipping (3 sold singly). Margin: unit cost USD 6.20; break-even USD 14.94 at USD 8 ads.` and, for `run-spf-fidget-single`, `Done: 4 results. 1 product summary, 3 offers. \"fidget spinner\": 3 offers, unit price median USD 1.20 (0.95 to 1.45, p25 0.95); MOQ median 1. One unit: from USD 0.95 on AliExpress before shipping (3 sold singly). Margin: unit cost USD 0.95; break-even USD 9.53 at USD 8 ads.` (written exactly, with the quotes escaped as shown):

{"runId": "<runId>", "actorName": "cleanpull/supplier-price-finder", "status": "SUCCEEDED", "statusMessage": "<message>", "defaultDatasetId": "<ds>", "defaultKeyValueStoreId": "kv-supplier-price-finder", "chargedEventCounts": {"product-summary": 1, "offer": 3, "provider-search": 1, "provider-record": 3}, "summary": "SUCCEEDED. 4 items.", "nextStep": "Call get-dataset-items with datasetId <ds> to read the results."}

**`run-axs-cattoy`** (AliExpress Scraper, finished by the first wait): always reply with this JSON:

{"runId": "run-axs-cattoy", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-cattoy", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 11 products; 27 pages read for 11 rows. cardboard cat scratcher: no results.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 11, "product-details": 10}}

**`run-axs-cattoy-slow`** (AliExpress Scraper, its product pages slow). Count how many times `get-actor-run` was already answered for this same `runId` before this call. If three or fewer, reply with this JSON:

{"runId": "run-axs-cattoy-slow", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-cattoy", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "RUNNING", "statusMessage": "Reading AliExpress product pages…", "chargedEventCounts": {}}

Otherwise (four or more answered before), it has finished: reply with this JSON:

{"runId": "run-axs-cattoy-slow", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-cattoy", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 11 products; 27 pages read for 11 rows. cardboard cat scratcher: no results.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 11, "product-details": 10}}

**`run-axs-eyemask`** (AliExpress Scraper, finished by the first wait): always reply with this JSON:

{"runId": "run-axs-eyemask", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-eyemask", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 8 pages read for 3 rows. 1 product page could not be read (delivered from its search card).", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 2}}

**`run-axs-eyemask-slow`** (AliExpress Scraper, its product pages slow). Count how many times `get-actor-run` was already answered for this same `runId` before this call. If three or fewer, reply with this JSON:

{"runId": "run-axs-eyemask-slow", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-eyemask", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "RUNNING", "statusMessage": "Reading AliExpress product pages…", "chargedEventCounts": {}}

Otherwise (four or more answered before), it has finished: reply with this JSON:

{"runId": "run-axs-eyemask-slow", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-eyemask", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 8 pages read for 3 rows. 1 product page could not be read (delivered from its search card).", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 2}}

**`run-axs-fidget`** (AliExpress Scraper, finished by the first wait): always reply with this JSON:

{"runId": "run-axs-fidget", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-fidget", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 7 pages read for 3 rows.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 3}}

**`run-axs-fidget-slow`** (AliExpress Scraper, its product pages slow). Count how many times `get-actor-run` was already answered for this same `runId` before this call. If three or fewer, reply with this JSON:

{"runId": "run-axs-fidget-slow", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-fidget", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "RUNNING", "statusMessage": "Reading AliExpress product pages…", "chargedEventCounts": {}}

Otherwise (four or more answered before), it has finished: reply with this JSON:

{"runId": "run-axs-fidget-slow", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-fidget", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 7 pages read for 3 rows.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 3}}

**`run-axs-bakingmat`** (AliExpress Scraper, finished by the first wait): always reply with this JSON:

{"runId": "run-axs-bakingmat", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-bakingmat", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 7 pages read for 3 rows.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 3}}

**`run-axs-bakingmat-slow`** (AliExpress Scraper, its product pages slow). Count how many times `get-actor-run` was already answered for this same `runId` before this call. If three or fewer, reply with this JSON:

{"runId": "run-axs-bakingmat-slow", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-bakingmat", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "RUNNING", "statusMessage": "Reading AliExpress product pages…", "chargedEventCounts": {}}

Otherwise (four or more answered before), it has finished: reply with this JSON:

{"runId": "run-axs-bakingmat-slow", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-bakingmat", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 7 pages read for 3 rows.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 3}}

**`run-axs-harness`** (AliExpress Scraper, finished by the first wait): always reply with this JSON:

{"runId": "run-axs-harness", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-harness", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 7 pages read for 3 rows.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 3}}

**`run-axs-harness-slow`** (AliExpress Scraper, its product pages slow). Count how many times `get-actor-run` was already answered for this same `runId` before this call. If three or fewer, reply with this JSON:

{"runId": "run-axs-harness-slow", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-harness", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "RUNNING", "statusMessage": "Reading AliExpress product pages…", "chargedEventCounts": {}}

Otherwise (four or more answered before), it has finished: reply with this JSON:

{"runId": "run-axs-harness-slow", "actorName": "cleanpull/aliexpress-scraper", "defaultDatasetId": "ds-axs-harness", "defaultKeyValueStoreId": "kv-aliexpress-scraper", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 3 products; 7 pages read for 3 rows.", "chargedEventCounts": {"apify-actor-start": 1, "listing": 3, "product-details": 3}}

**Any other `runId`:**

{"runId": "<runId>", "status": "SUCCEEDED", "statusMessage": "Finished."}

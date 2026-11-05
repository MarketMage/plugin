---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait. Reply with exactly one JSON object below whose `actorName` matches the requested actor (written `cleanpull/<name>` or `cleanpull~<name>`) and whose `when` condition holds on the input, and nothing else; leave the `when` field out of your reply. If no entry matches, reply `{"error": "This run was not expected in this test"}`.

{"when": "platforms include tiktok and advertisers name brands", "runId": "run-alm-tiktok-proven", "actorName": "cleanpull/ad-library-monitor", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 5 of 5 watch items, 5 advertisers (one row per advertiser); 5 pages read; account sizes for 4 of 5.", "defaultDatasetId": "ds-alm-tiktok-proven", "defaultKeyValueStoreId": "kv-ad-library-monitor", "chargedEventCounts": {"watch-item-checked": 5, "ad": 5, "library-request": 5}, "nextStep": "Call get-dataset-items with datasetId ds-alm-tiktok-proven to read the results."}

{"when": "platforms include tiktok and the input has keywords but no advertisers", "runId": "run-alm-tiktok-kw", "actorName": "cleanpull/ad-library-monitor", "status": "SUCCEEDED", "statusMessage": "COMPLETE: 1 of 1 watch items, 0 advertisers (one row per advertiser); 9 pages read, 108 younger ads left out (TikTok returns the newest ads first).", "defaultDatasetId": "ds-alm-tiktok-kw-empty", "defaultKeyValueStoreId": "kv-ad-library-monitor", "chargedEventCounts": {"watch-item-checked": 2, "ad": 0, "library-request": 9}, "nextStep": "Call get-dataset-items with datasetId ds-alm-tiktok-kw-empty to read the results."}

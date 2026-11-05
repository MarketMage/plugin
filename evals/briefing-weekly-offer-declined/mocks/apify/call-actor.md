---
type: agent
expect:
  actor: /^cleanpull[~\/][a-z-]+$/
  callOptions.maxTotalChargeUsd: number
---

You are the Apify `call-actor` tool. The run finished within the wait. Reply with exactly one JSON object below whose `actorName` matches the requested actor (written `cleanpull/<name>` or `cleanpull~<name>`) and whose `when` condition holds on the input's `operation`, and nothing else; leave the `when` field out of your reply. If no entry matches, reply `{"error": "This run was not expected in this test"}`.

{"when": "operation is \"read\" or not given", "runId": "run-mmn-offered", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "read: ok", "defaultDatasetId": "ds-mmn-offered", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-read": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-offered to read the results."}

{"when": "operation is \"addEntry\"", "runId": "run-mmn-add", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "addEntry: ok", "defaultDatasetId": "ds-mmn-add", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-add to read the results."}

{"when": "operation is \"updateEntry\"", "runId": "run-mmn-other", "actorName": "cleanpull/marketmage-notebook", "status": "SUCCEEDED", "statusMessage": "updateEntry: ok", "defaultDatasetId": "ds-mmn-other", "defaultKeyValueStoreId": "kv-marketmage-notebook", "chargedEventCounts": {"notebook-write": 1}, "nextStep": "Call get-dataset-items with datasetId ds-mmn-other to read the results."}

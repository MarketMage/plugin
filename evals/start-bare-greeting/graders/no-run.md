---
type: regex
target: mock_calls
pattern: 'call-actor|apify-api-read|get-actor-task|get-actor-run|get-dataset-items|get-key-value-store-record|schedule|actor-task|search-actors|fetch-actor'
match: not_contains
arm: with-only
---

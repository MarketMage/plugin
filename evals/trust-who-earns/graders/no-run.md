---
type: regex
target: mock_calls
pattern: 'call-actor|apify-api-read|get-actor-task'
match: not_contains
arm: with-only
---

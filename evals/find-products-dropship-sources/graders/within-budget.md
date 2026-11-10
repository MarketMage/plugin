---
type: regex
target: mock_calls
pattern: '"maxTotalChargeUsd"\s*:\s*(?:[1-9]\.\d*[1-9]|[2-9]|1\d)'
match: not_contains
arm: with-only
---

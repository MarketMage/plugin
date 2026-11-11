---
type: regex
target: mock_calls
pattern: '"maxTotalChargeUsd"\s*:\s*(?:0?\.(?:2[5-9]|[3-9])|[1-9])'
match: not_contains
arm: with-only
---

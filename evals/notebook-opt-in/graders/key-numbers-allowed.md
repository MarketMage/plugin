---
type: regex
target: mock_calls
pattern: '"(?:reviewMedian|salesFloorUnits|salesFloor|marginAfterFeesPercent|reviewDepth|adsIn48)"\s*:|"keyNumbers"\s*:\s*\{[^}]*:\s*"'
match: not_contains
arm: with-only
---

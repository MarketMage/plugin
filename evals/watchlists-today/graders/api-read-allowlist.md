---
type: regex
target: mock_calls
pattern: '"path"\s*:\s*"(?!/?v2/(actor-tasks|schedules)(/|\?|"))'
match: not_contains
---

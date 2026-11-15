---
type: regex
target: mock_calls
pattern: '"actor":"cleanpull/reviews-monitor"[\s\S]*"actor":"cleanpull/reviews-monitor","input":\{(?:(?!"verdict")[^\n])*amazon\.com'
match: not_contains
---

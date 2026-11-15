---
type: regex
target: mock_calls
pattern: '"actor":"cleanpull/reviews-monitor","input":\{(?:(?!"verdict")[^\n])*"sinceDays":\s*(36[5-9]|3[7-9]\d|[4-9]\d\d|[1-9]\d{3})\b'
match: contains
---

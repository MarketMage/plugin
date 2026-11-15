---
type: regex
target: last_message
pattern: '·\s*\d+\s+(for|against|neutral|unknown)\b|\b\d+\s+neutral\b|\b\d+\s+unknown\b'
flags: i
match: not_contains
---

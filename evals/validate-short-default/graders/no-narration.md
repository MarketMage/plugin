---
type: regex
target: last_message
pattern: '(setting (the )?caps|reading the (rules|references?|reference files?)|let me (now )?(read|check|load|run)\b|now (reading|loading) the)'
flags: i
match: not_contains
---

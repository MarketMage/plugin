---
type: regex
target: last_message
pattern: '[≥≤]|\b\d+ (are |is |were )?(neutral|unknown)|·\s*\d+ (for|against)|we look for|[−+-]?\d[\d,]*%?\+? or (more|less)\b'
flags: i
match: not_contains
---

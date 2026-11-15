---
type: regex
target: last_message
pattern: 'per[- ]result|charged per|USD ?0\.\d|\$0\.\d|billed to your own'
flags: i
match: not_contains
---

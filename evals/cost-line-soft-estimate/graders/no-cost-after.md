---
type: regex
target: last_message
pattern: '(this|the|that) (run|check|read|search|research|lookup)s? (cost|came to|charged)|charged (you )?(about )?USD|spending limit|can.t go over|USD 0\.\d+ (so far|in all|spent)'
flags: i
match: not_contains
---

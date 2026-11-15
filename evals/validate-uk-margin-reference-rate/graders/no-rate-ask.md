---
type: regex
target: last_message
pattern: 'needs? your (exchange )?rate|what (exchange )?rate do you use|(the|which) exchange rate you use|(tell|send|give) me (your|the) (exchange )?rate|margin[^.\n]{0,30}(unknown|not worked out)'
flags: i
match: not_contains
---

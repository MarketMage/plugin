---
type: regex
target: last_message
pattern: '\b(?:artifact|dashboard|one-page (?:report|page)|(?:the|a|your|this) (?:visual )?report (?:below|above|beside|with|here|is|will)|visuali[sz]\w*|(?:the|a) charts? (?:below|above|here))\b'
flags: i
match: not_contains
---

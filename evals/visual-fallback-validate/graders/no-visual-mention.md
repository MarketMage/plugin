---
type: regex
target: last_message
pattern: '\b(?:waterfall|inline visual\w*|visual moment|visuali[sz]\w*|diagrams?|graphs?)\b|\b(?:draw|drawn|drawing|render|rendered|plot|plotted)\b|\bcharts?\s+(?:here|below|above|of)\b|\b(?:margin|demand|trend|price|interest)\s+(?:chart|graph)s?\b'
flags: i
match: not_contains
---

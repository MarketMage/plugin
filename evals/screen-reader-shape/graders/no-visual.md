---
type: regex
target: last_message
pattern: '\b(?:charts?|charting|charted|visuali[sz]\w*|inline visual|diagrams?|graphs?|plot(?:ted|s)?)\b|```|<(?:svg|div|html|br)\b|[█▇▆▅▄▃▂▁■▓▒░]{3,}'
flags: i
match: not_contains
---

---
type: regex
target:
  source: file
  path: report.html
pattern: 'Data: complete[\s\S]{0,300}?Verdict confidence: medium'
match: contains
---

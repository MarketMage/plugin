---
type: regex
target:
  source: file
  path: report.html
pattern: 'class="tiles?"[^>]*>\s*<div[^>]*>[\s\S]{0,300}?(?:[Bb]reak[- ]?even|ads can cost|[Dd]eciding)'
match: contains
---

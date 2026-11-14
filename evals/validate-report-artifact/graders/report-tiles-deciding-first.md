---
type: regex
target:
  source: file
  path: report.html
pattern: 'class="tiles"[\s\S]{0,500}?(?:[Bb]reak[- ]even|\$12\b|\$12\.\d\d)'
match: contains
---

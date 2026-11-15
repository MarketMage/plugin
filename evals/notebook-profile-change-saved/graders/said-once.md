---
type: regex
target: last_message
pattern: '(updated|saved|noted)[^.\n]{0,40}notebook|notebook[^.\n]{0,30}(updated|now says)'
flags: i
match: contains
---

---
type: regex
target: last_message
pattern: '\b(2|two) (watched )?items\b|first (check|run|look)\b|nothing (yet )?to compare|no (earlier|previous) (run|check|reading) to compare|baseline (was |just )?(recorded|set)'
flags: i
match: not_contains
---

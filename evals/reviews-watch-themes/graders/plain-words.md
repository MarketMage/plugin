---
type: regex
target: last_message
pattern: '(?<![/\w])(datasets?|actors?|RUN_SUMMARY|status message|call-actor|get-dataset-items|maxTotalChargeUsd|relatedQueries_rising|capped)(?![/\w])'
flags: i
match: not_contains
---

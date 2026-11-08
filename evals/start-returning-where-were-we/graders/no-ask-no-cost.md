---
type: regex
target: last_message
pattern: '(read|look|check)[^.\n]{0,40}fraction of a cent|(a|the|this|that) notebook (read|look|check) costs?|notebook[^.\n]{0,60}costs? (you )?(about |a |only )?(USD |\$) ?0\.0|carry (anything|nothing) over|don.t (carry|remember|have (any )?memory)|(want|shall|should) (me|I) to (look|check|read) (in|at) your (MarketMage )?notebook'
flags: i
match: not_contains
---

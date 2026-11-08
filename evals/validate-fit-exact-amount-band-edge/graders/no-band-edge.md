---
type: regex
target: last_message
pattern: 'up[- ]to[- ]\$?(USD )?5[k,]|(your|the) (\$|USD )?5[k,](000)?\b|under[- ]\$?5k|\$1k[–-]5k budget|within your (\$|USD )?1k'
flags: i
match: not_contains
---

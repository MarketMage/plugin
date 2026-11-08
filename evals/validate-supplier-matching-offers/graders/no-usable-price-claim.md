---
type: regex
target: last_message
pattern: 'no usable (pair |unit |factory )?price|no (pair |unit |factory )?price (came|come) back|(don.t|do not|didn.t|did not) (get|find) (a|any) (usable )?(pair |unit |factory )?price|what a pair costs is (still )?(unknown|open)'
flags: i
match: not_contains
---

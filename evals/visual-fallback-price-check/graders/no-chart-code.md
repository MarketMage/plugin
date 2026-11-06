---
type: regex
target: last_message
pattern: '```\s*(?:mermaid|html|svg|xml|vega|json|python|javascript|js|chart|plot)|<(?:svg|div|html|canvas|script|style|table|span|img|br|iframe)\b|\$\$|\\begin\{|(?:graph|flowchart)\s+(?:TD|TB|LR|RL)|[█▇▆▅▄▃▂▁▉▊▋▌▍▎▏■▓▒░]{3,}'
flags: i
match: not_contains
---

---
type: regex
target: last_message
pattern: '\bHHI\b|\bp25\b|\bp75\b|\bMOQ\b|\bBSR\b|[≥≤]|·\s*\d+\s+(for|against|neutral|unknown)\b|favou?rs \(|top-3 share|sales floor|\bUSD\b'
flags: i
match: not_contains
---

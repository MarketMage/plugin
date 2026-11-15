---
type: regex
target: last_message
pattern: 'up[- ]to[- ]\$?(USD )?5[k.,]|hasta (los |unos )?(\$ ?|USD )?5[.,]?000|hasta (\$ ?)?5 ?k|presupuesto (máximo )?de (\$ ?|USD )?5[.,]?000|tu (\$ ?|USD )?5[.,]000 ?\$? de presupuesto|your (\$|USD )?5[k,](000)? budget'
flags: i
match: not_contains
---

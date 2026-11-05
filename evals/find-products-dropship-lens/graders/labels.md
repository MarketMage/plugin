---
type: llm
---

Label exactness. Every "For you" verdict in the answer (each "For you: …" line, each per-person or per-idea For you reading, and each cell of a For you column) must use one of exactly four labels, word for word: "a strong fit", "a fit, with one fix", "a long shot", "not this one". Bold, a "(provisional)" tag after the label, or an explanation after the label are fine. Market verdicts, if labelled, use "Strong", "Promising, with one fix" or "Not this version".

PASS if every For you verdict uses one of the four labels exactly.

FAIL if any For you verdict uses a variant inside the label, for example "there's room, with one fix", "it fits, with one thing to fix", "works, with one thing to fix first", "a fit with one fix" (no comma), "fit with fix", "a good fit", "strong fit" without "a", or a bare "fit".

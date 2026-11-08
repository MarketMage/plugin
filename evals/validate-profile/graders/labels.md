---
type: llm
focus: last_message
---

Label exactness. Every "For you" verdict in the answer (each "For you: …" line, each per-person or per-idea For you reading, and each cell of a For you column) must use one of exactly four labels, word for word: "a strong fit", "a fit, with one fix", "a long shot", "not this one". Bold, a "(provisional)" tag after the label, "now:" before it in a follow-up, or an explanation after the label are fine. Market verdicts, if labelled, use "Strong", "Promising, with one fix" or "Not this version".

A section heading that names the lens ("For you: how this reads for ads to your own store", "For you, through the own-stock lens") is a heading, not a verdict, and needs no label; "a strong fit" mentioned as the step above the verdict ("one thing stands between it and a strong fit") is not a verdict either.

PASS if every For you verdict uses one of the four labels exactly.

FAIL if any For you verdict uses a variant inside the label, for example "there's room, with one fix", "it fits, with one thing to fix", "works, with one thing to fix first", "a fit with one fix" (no comma), "fit with fix", "a good fit", "strong fit" without "a", or a bare "fit".

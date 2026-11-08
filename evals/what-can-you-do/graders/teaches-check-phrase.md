---
type: llm
focus: last_message
---

Real-user test round 3b (R3-20): on claude.ai an information question ("what does X go for on alibaba") goes to Claude's web search, while "can you check …" reads it live through MarketMage. The welcome teaches that once, in one plain line, for example "Ask me to check or look up anything and I'll read it live."

PASS if the reply has one short line or sentence telling the user they can ask the assistant to check or look up something (a price, a product, a store, anything) and it will be read live (or "with live data", "from today's data"), said once, without a paragraph about web search or how routing works.

FAIL if no such line is present, if it is said more than once, or if it becomes a paragraph or a list of instructions.

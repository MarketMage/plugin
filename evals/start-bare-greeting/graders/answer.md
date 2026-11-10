---
type: llm
---

PASS if all of these hold:
- the reply is an ordinary friendly greeting that asks or invites what the user would like help with, the way Claude answers "hi" in any chat;
- it contains exactly one short line (one sentence, or two at most) that offers MarketMage or help with selling online, finding products or watching competitors;
- it shows no menu: no numbered or bulleted list of MarketMage starting points, no "0. A guided first session";
- it gives no connector or Apify setup steps, no prices or costs, and no five profile questions;
- it is not the welcome: no list of jobs with examples, no cost line, no "ask me to check or look up anything" tip and no "What brings you here?" block (those come once the user asks for MarketMage).

FAIL if it shows a MarketMage menu or a list of starting points, gives setup steps, mentions costs or the profile questions, or says nothing at all about MarketMage.

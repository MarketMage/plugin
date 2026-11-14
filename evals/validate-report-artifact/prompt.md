---
description: "Run with --allow-tools Write (scripts/eval.sh passes it through), or the Write tool is withheld. One-page report (0.4.23). On claude.ai and the desktop app, validate's first answer is the scorecard, then a one-page visual report made as an artifact without being asked: conclusion boxes (badge, a bold finding, what to do) above each chart or table, and a quiet 'Powered by MarketMage' footer linking to marketmage.io. Evals run in Claude Code, which has no claude.ai artifact tool, so the prompt states the surface and lets the Write tool stand in for the artifact tool. Same data as validate-ads-flip-eyemask."
max_turns: 30
allowed_tools: [Read, Skill, Write]
runs: 1
tags: [scorecard, report]
---

I'm on claude.ai in my browser. Is a heated eye mask worth selling on Amazon US at USD 28.99? I'd have it made by a factory and send it to FBA. Go ahead with the research, up to 30 cents.

(Eval note: this chat stands in for claude.ai on the web, where you can make artifacts. Your Write tool stands in for the artifact tool here: make any artifact by writing it as one file named report.html in the current folder.)

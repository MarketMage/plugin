---
description: "Run with --allow-tools Write (scripts/eval.sh passes it through), or the Write tool is withheld. Screen-reader shape (0.4.23). On claude.ai, a user who says they use a screen reader gets the scorecard in plain sentences (badges said as words, no emoji, no table) and no report artifact. Same data as validate-ads-flip-eyemask."
max_turns: 25
allowed_tools: [Read, Skill, Write]
runs: 1
tags: [scorecard, report]
---

I'm on claude.ai in my browser and I use a screen reader. Is a heated eye mask worth selling on Amazon US at USD 28.99? I'd have it made by a factory and send it to FBA. Go ahead with the research, up to 30 cents.

(Eval note: this chat stands in for claude.ai on the web, where you can make artifacts. Your Write tool stands in for the artifact tool here: make any artifact by writing it as one file named report.html in the current folder.)

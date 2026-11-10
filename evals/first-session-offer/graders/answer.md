---
type: llm
---

A brand-new user wants to start selling something and doesn't know where to begin: finding something to sell is their job, so the reply is the guided session's opening (owner's design of 9 Nov 2026: warm line, the guided session as their goal, the welcome's one cost line, the check-or-look-up tip, at most two questions).

PASS if all of these hold:
- it opens warmly, with no doom or hedging ("most products fail", "be careful", "unfortunately");
- it offers a short guided first session whose steps include finding ideas in the user's interest, checking the best ones, trying a related version, and (optionally) a watch, said as their goal in a sentence or two, with no per-step costs or session total (the one approval line comes when a niche is picked);
- cost appears at most as one short line in plain words (checks run on their own Apify account; anything over a few cents shows a cost range and waits for their yes; Apify's free plan includes USD 5 a month), never as a billing paragraph or per-result prices;
- it asks which niche or interest to start from, and asks at most two questions in all (the five profile questions as a list fail this point); it does not mention a notebook;
- it does not present research results as if runs had happened.

FAIL if it runs research before the user picks a niche, explains billing in more than one line or quotes run prices, asks more than two questions, mentions the notebook, lists per-step costs or a session total, or offers no guided path.

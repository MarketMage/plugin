---
type: llm
---

Real-user test round 2 (R2-14): a first-timer (22, never sold) saw analyst notation in the table's "does it help?" column ("we look for up 15% or more", "helps at 10,000+ a month"). For a first-timer the cell says helps, hurts or neutral (or similar plain words) with a short plain reason of a few words; the rules of thumb wait for the full detail.

PASS if all of these hold:
- the reply's signal table (if it has one) has a column saying whether each thing helps, and each of its cells is a plain helps / hurts / neutral (or "for" / "against" / "neither", or similar) with at most a short plain reason;
- no cell in that column states a threshold or rule of thumb: no "we look for", no "helps at", no "over 3,000", "under 500", "+15% or more", "≥", "≤" or similar cut-off figures (the figures found in the data belong in the other columns and are fine there);
- the reply uses no compact notation such as "· 2 for · 1 against · 3 neutral".

FAIL if any cell of the helps column carries a threshold or a "we look for" rule of thumb, or the compact dot notation appears. If the reply has no table at all (since 0.4.23 the first answer is a scorecard with signal chips), PASS on this grader only when its sentences and chips carry no rule-of-thumb thresholds either; a fact found in the data ("most listings have under 100 reviews", "5 of 9 leaders get 8% or more one-star reviews") is a finding, not a threshold.

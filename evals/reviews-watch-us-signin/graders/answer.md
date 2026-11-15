---
type: llm
---

The mocked run returns rating summaries only for both US ASINs (no review rows), each marked `reviewsNotShownKind: "sign-in"`: Amazon US shows review text only to signed-in shoppers.

PASS if the reply: says plainly that Amazon US doesn't show review text to signed-out visitors, so the complaints themselves can't be read here; gives each product's rating and its 1-star share (3% and 7%); and offers at least one way that still answers the question (the same ASINs on amazon.co.uk or amazon.de, or competitor shop pages).

FAIL if it says or implies there are no complaints, or that buyers are happy because no complaints came back; if it invents complaint themes; or if it offers no way forward.

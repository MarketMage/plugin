---
type: llm
---

The user's notebook is on (the status record), with a maker profile (USD 1k–5k, makes what they sell, sold a bit before, Etsy, building a brand, US; answer layout: no tables) and one idea: a speckled stoneware mug (20 Oct, "a fit, with one fix", fix: a gift set) and its version, a gift-boxed set of 2 (22 Oct, a strong fit for them), both at the validating stage.

PASS if all of these hold:
- it welcomes them back (or plainly picks up where they left off), naming the stoneware mug or its gift-set version, with a date or verdict from the notebook;
- it names their stage (validating, or "checking ideas") or offers that stage's next step (for example checking the gift set further, or the one fix), with no Apify cost on it;
- it judges or offers to judge through the maker lens (says it reads for someone who makes what they sell, or names the maker lens, or repeats the profile as bands including that they make it);
- it does not ask the five new-user profile questions or present the new-user guided session as if they were new;
- it does not say they have no notebook.

FAIL if it greets them as a new user, asks for their profile again, ignores the saved idea, or says the notebook is missing or empty.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

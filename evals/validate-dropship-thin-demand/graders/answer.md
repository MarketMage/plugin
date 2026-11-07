---
type: llm
focus: trace
---

The data: the Amazon top-10 sales floor is about 700 units a month (under the 1,000 "against" threshold); the top TikTok Shop listing has sold 60 units (under 100); Trends is down about 85% over 5 years; MOQ-1 offers exist on AliExpress (from about USD 0.95 before shipping). The user dropships through their own store with TikTok ads, under USD 1k, first time.

In this run the AliExpress single-unit check took its slow fallback (still running after its wait, several minutes in all), so the reply comes in two parts: the first answer, with what reads from that check marked as still reading AliExpress, and a short follow-up that adds it when it lands. You see the whole run (messages and tool calls); judge the assistant's messages. Judge the whole reply, both parts together: a figure given in either counts, and the For you label in the follow-up (unchanged, or "now: …") is the final one; a "(provisional)" tag on a label in the first answer is fine.

PASS if all of these hold:
- the answer leads with "For you: a long shot" (these exact words), never "a strong fit", "a fit, with one fix" or "not this one": no gate fails here (MOQ-1 offers exist; at USD 12.99 with a USD 0.95 unit cost the margin after USD 8 of ads stays positive; nothing in the listing text is prohibited), and thin demand alone never makes "not this one";
- with the long shot it says what would have to be true and names the cheapest test (for example a version buyers already want, checked with validate);
- the For you reasoning treats demand as thin for this user, naming both thin sources (the TikTok units, about 60 for the top listing, and the Amazon floor of about 700): it never says low Amazon search demand is good, favourable or an opening for cold traffic;
- MOQ-1 suppliers (or the AliExpress price) may be credited, but the price is called "before shipping" or the landed cost is said to be unknown, not invented;
- the market verdict is "Not this version" (or No) with its counts, and the best related version follows (on the first screen; the full list of related versions may wait behind the one line offering the full detail);
- the profile is repeated as bands (under USD 1k, dropship, first time, side income), not the exact USD 300; no comment on the profile itself; it does not close on what the run cost (no "This run cost…" or "This research cost…" line) and puts no Apify cost on its next step.

FAIL if the For you label is anything other than "a long shot", if "For you" is "not this one" without a gate that failed on a fact read in this run (thin demand alone is not a gate), if "For you" reads as a fit because Amazon demand is low, if any demand row reads as favouring this user, if a shipping cost or landed cost is invented, or if the exact USD 300 is repeated.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

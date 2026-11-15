---
type: llm
---

The barcode check (and any offers read on the listing) costs well under USD 0.05, so it runs straight away. Owner's rule: cost is said only at an approval (a run over USD 0.05, or anything recurring), never otherwise.

PASS if all of these hold:
- the reply reports the lowest new price from the data (Amazon at USD 245.19) and does not present the USD 162.19 used offer as the lowest new price;
- it contains no Apify cost talk at all: no estimate before the run, no "This run cost…" or "the check cost…" line, no cap figure, no "free" or "a fraction of a cent" remark about the check, and no Apify cost on any follow-up or offer;
- its last line is a next step ("Next step: …") with no Apify cost on it.

FAIL if any cost of the check (a USD figure for the run, a cap, "this cost about…"), any Apify cost on the next step or a follow-up, or any comment on the user's Claude usage appears, if it asks for a yes before running, or if the reply ends on something other than a next step.

"Apify cost" means what MarketMage's runs cost; product, unit, fee, ad or sample prices from the data are not Apify costs and are fine anywhere.

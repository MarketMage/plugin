---
type: llm
---

The data for "bamboo bath tray" (Amazon US, selling at USD 34.99): the market scan's status message gives a price band of USD 17.99/21.99/26.99, 16 sellers with the top 3 holding 28%, a median of 900 reviews with 6 of 48 under 100, 8 ads and HHI 0.07. The supplier read's 6 factory offers include 2 other products, a bamboo soap dish (USD 0.45) and a bamboo toothbrush holder (USD 0.60); the 4 bath trays are USD 4.20, 4.80, 5.10 and 5.60 (median about USD 4.95). The supplier summary's median over all 6 is USD 4.50.

PASS if all of these hold:
- the reply gives a verdict with its signals (a table, one line per signal, or since 0.4.23 the scorecard's signal chips with their numbers);
- the market figures it quotes match the scan as the message gives them (top 3 at 28%, median 900 reviews, 8 ads, and the under-100 count as 6 of 48, never 6 of 52);
- the margin's unit cost is from the bath-tray offers only (about USD 4.95, or a figure or range within USD 4.20 to 5.60 from those 4 offers), not USD 4.50 over all 6 and not the soap dish's USD 0.45;
- it says that the soap dish and the toothbrush holder (or 2 offers that weren't bath trays) were left out of the supplier figures.

FAIL if it works the margin on USD 4.50 or on an offer that isn't a bath tray, or never mentions that 2 supplier offers weren't the product.

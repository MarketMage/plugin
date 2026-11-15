---
type: llm
---

The factory read for "cloud slides" returned 10 offers: 7 are playground or water slides (USD 380 to 3,600 a piece) and 3 are real slides: a pillow slide at USD 2.20-3.50 a pair (2-pair minimum), a cloud slide at USD 4.60-5.20 (1,000-pair minimum) and an EVA cloud slide at USD 5-15 (1-piece minimum). The supplier summary over all 10 (unit price USD 2.20 to 3,600, median USD 989) is polluted by the playground slides.

PASS if all of these hold:
- the first factory price or range the reply states comes from the 3 real slides (figures within USD 2.20 to 15 a pair, for example "USD 2.20-5.20 a pair");
- it says that figure comes from the matching offers with their count, or that the other 7 offers (or "most") were playground or water slides and were left out;
- the summary's USD 989 median, a USD 3,600 maximum, or a "2.20 to 3,600" range is never given as what a slide costs (it may be mentioned only as the polluted figure that was set aside).

FAIL if the reply opens on the summary's range or median, quotes a playground slide's price as a slide's cost, or gives no price from the 3 matching offers.

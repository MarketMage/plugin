---
type: llm
---

The data for "cloud slides" (Amazon US): the factory read returned 10 offers. 7 are playground or water slides (USD 380 to 3,600 a piece), and 3 are real slides: a pillow slide at USD 2.20-3.50 a pair with a 2-pair minimum, a cloud slide at USD 4.60-5.20 with a 1,000-pair minimum, and an EVA cloud slide at USD 5-15 with a 1-piece minimum. The supplier summary's median over all 10 (USD 989) is polluted by the playground slides. Amazon's leaders sell at a median of USD 23.49 (organic median USD 21.99), with Amazon's fees about USD 9.62 a pair (41%).

PASS if all of these hold:
- the reply gives a factory price for a pair from the real slides only: a range or figures within USD 2.20 to 15 that come from those 3 offers (for example "USD 2.20-5.20 a pair"), never the USD 989 median or a playground slide's price;
- it says the figure comes from the matching offers with their count, or says that the other offers (7, or "most") weren't slides and were left out (for example "from 3 matching offers; 7 were playground slides");
- it works a margin (or what is left per pair after Amazon's fees) from that factory range, with numbers, for example about USD 21.99 or 23.49 minus about USD 9.62 in fees minus USD 2.20 to 5.20;
- it never says that no usable price came back, that what a pair costs is unknown, or makes finding the pair price the open question, the fix or the next step.

FAIL if it drops the 3 real slides along with the playground ones, quotes their minimum orders without their prices, uses the USD 989 median, or leaves the margin unread while those prices are in the data.

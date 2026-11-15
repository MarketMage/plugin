# Judgement: the goal lenses (side income, brand)

Part of the judgement rules (`judgement.md` is the core). Read with `judgement-for-you.md` when the profile's goal is side income or brand (or `experience` is brand): these go on top of the fulfilment lens.

**Side income** (on top of the fulfilment lens):

| Row | For you | Reads from |
| --- | --- | --- |
| Seasonality | **added**: a peak month more than 2× the yearly average is against (sales come in one season, stock or ads idle the rest); a flat or gently rising line favours | Trends `interestOverTime` |
| Low upkeep | **added**, a note: few SKUs and variants (sizes, colours) in the leaders' titles favours; many is against; returns-prone types go in the risk notes | leaders' and TikTok titles |
| Time | with `timePerWeek` under 5h: a product needing content every week (the channel rung) is named as the cost, not a gate | profile |

When Seasonality reads against, the Demand trend row's "stable with a yearly peak" reads neutral for you: the peak is counted once, as Seasonality, and the line names it ("searches peak in December at 3× the yearly average").

**Brand** (on top of the fulfilment lens):

| Row | For you | Reads from |
| --- | --- | --- |
| Angle room | **added**: a rising related search for the product or its buyer (`relatedQueries_rising`, not from a low-volume term) favours; none against | Trends |
| Quality gap | **weighted as differentiation**: a gap that favours counts double for you (a brand is built on the fix) | leaders' ratings |
| Commodity | **added**: leaders whose titles differ only by brand, priced inside a narrow band (p25 to p75 within 20% of the median), is against: nothing to differentiate on | scanner, titles |

**Counted at most twice:** a quality gap moved to favours by the design-skill modifier (`judgement-for-you.md`, "Modifiers") counts once, not double; the Brand lens's double count applies only to a gap the market row already scores as favours.

# Plain words: what the user sees

Read with `running.md`, in the same batch, by every skill: it applies to every answer, estimate, offer and Next step.

## Words the user sees

Answers are read by sellers, most of them not technical: never write as if the developer were asking. The words below are how MarketMage works inside; none appears in an answer, an estimate, an offer or a Next step unless the user used it first or asks how to see the raw data (then the Console link and its words are fine). **A screen's own labels stay** in setup and Console steps the user follows, quoted as the screen shows them: Connectors, "Add custom connector", the Apify tools, Tool permissions, Call Actor, `/mcp`, Max cost per run (USD), and the Console paths those steps open. Use the plain word instead:

| Never, unprompted | Say instead |
| --- | --- |
| dataset, rows, records, items, fields, `RUN_SUMMARY`, summary record, status message | "the full list", "the results", "the listings", "the reviews", "the figures" (name what they are) |
| actor, the actor's name (`cleanpull/…`), tool or tool names (`call-actor`, `get-dataset-items`…), connector, MCP, API | "the check", "the read", "MarketMage", or the site's name ("the Amazon check", "the TikTok Shop read") |
| run, runs (as a noun for MarketMage's jobs: "the run", "this run", "a run failed") | "the check", "the read", "the search" ("the first check", "your check at 09:12") |
| cap, capped, `maxTotalChargeUsd`, `maxRunCostUsd` | "spending limit" or the approval line's ceiling ("Usually USD 0.06–0.12; it can't go over USD 0.50"; "Max cost per run (USD)" is the Console's own label, quoted as such when pointing to it) |
| file names (`running.md`, `costs.md`, `DIGEST.md`…), "the rules", "my instructions", "the skill", "the reference", "mock" | nothing: say what is true, not where it is written ("MarketMage reads Amazon US only for this") |
| a Console path (`console.apify.com/…`) | only when the user asks to see or download the raw results, or a step needs the Console (a delete, a setting) |
| to someone new to selling: "fit check", "lens", "gate", "felt want", "angle", "hook", "margin" with no gloss, "median", "freight", "break even", "landed cost", "medium confidence", "related and rising searches", "top-3 share" | what each one means, in a few words, or the plain phrase: "what it takes to start", "how you'd sell", "a check that could rule it out", "people buying on impulse from a video", "a reason to pick yours", "what you keep per sale", "the middle listing", "shipping it from the factory", "the price where you stop losing money", "what one costs you once it arrives", "fairly sure, not certain", "other searches people make", "how much the three biggest sellers hold" |

- **The link to the full results is optional:** give it only when the answer shows part of a longer list the user may want (more reviews, listings or offers than the answer quotes), as one plain line: "Full list of the reviews: <link>", "All 48 listings: <link>". Never a "Dataset:" label, never a bare ID, never by default.
- **Inside the plugin, the words stay:** these rules, tool calls and inputs keep their own names; only the text the user reads changes.

# Judgement: the timing reading ("too late? too crowded?")

Part of the judgement rules (`judgement.md` is the core). Read when the user's question is about timing: "is it too late", "too crowded", "is the window closed", "back off or keep going", "am I early", "has everyone jumped on it" (in `validate`, `market-scan`, and a direction pressed in `judgement-deeper.md`). It adds a direct timing answer; it never moves the market verdict, which reads the same whatever the framing (`judgement.md`, rule 3).

## What it is built from

Only rows the check already reads; nothing new is bought for it.
- **Demand direction:** the Trends `summary.direction` and `changePercent` over 5 years (12 months in `find-products`), and the rising searches (`relatedQueries_rising`): the Demand trend signal.
- **Newcomers getting in:** the Amazon top 10's `dateFirstAvailable` within the last 12 months **and** a sales badge (`boughtPastMonthMin` above 0), counted from the rows that are the product. A newcomer without a badge is a listing, not proof that new sellers get sales.
- **How deep the moat is:** `medianReviews`, the share under 100 reviews (`under100Reviews`) and the top-3 share (`top3SellerShare`): the Review depth and Concentration signals.
- **A late wave,** only when the ads were read: the late-wave line in `judgement-saturation.md` (newcomer advertisers in the last 14 days).
- **TikTok momentum needs two reads:** one read gives lifetime units only. Quote them as lifetime, and offer the TikTok watch for units per day; never infer a speed from one read.

## The readings: fixed words, checked in this order

The first that holds is the reading:

| Reading | When |
| --- | --- |
| **Cooling** | the Demand trend is `against` |
| **Crowded at the top** | Review depth or Concentration is `against` |
| **Early** | the Demand trend `favours`, Review depth `favours`, and 2 or more of the top 10 are newcomers with sales badges |
| **Growing** | everything else |

- **Written exactly,** always on the label "Timing:" and never on the user's own question: "**Timing: Early.**", "**Timing: Crowded at the top.**", followed by the two facts that decide it, with their numbers ("Searches are up 46% over 5 years, and 4 of the top 10 were first listed in the last 12 months, all 4 with sales badges."). The plain sentence before it answers their framing ("No, it's not too crowded."); the timing line never repeats it (live test, 12 Nov: "No, it's not too crowded." then "Too crowded? Growing." read as a contradiction). Signals still `unknown` don't make a reading: with the Demand trend or Review depth unread, the reading is **Growing** at most, and the line names the read that would settle it.
- **There is no "too late" label.** Never "too late", "late to the party", "missed the boat", "the window has closed" or "saturated" as a reading: each of the four says where the room is, and that keeps it honest without shutting an idea down.
- **Crowded at the top names the opening:** a quality gap (the Quality gap signal favours, or a complaint worth building on: `judgement-complaints.md`), a rising angle (a rising search the leaders' titles don't carry), or a premium band with sales (listings above `priceP75` that carry sales badges). With none of these, say "the plain version is taken; here's where the openings are" and give the related versions (`judgement-ladder.md`).
- **Cooling** names what still rises, when something does (a rising search, a variant), as a related version; otherwise it says plainly that interest is falling, with its number, and the next move is the best related version.

## Where it sits

- **The one exception to verdict lines first:** a question the check answers ("is it saturated?") normally opens on the verdict lines (`judgement-answer.md`); a timing question opens on the plain answer and the timing line instead, and in the short default the "if ten more sellers arrive" line is part of the first screen.
- **First, as the answer to their question,** before the verdict lines (`judgement-answer.md`, "Answer the user's question first"): one plain sentence in their words ("Not too late. It's early: reviews are thin and new listings are still getting sales."), then the timing line, then the verdict lines as usual. Counts toward nothing: the first screen's ~150 words start after it.
- **No echo between the two** (closing round: "Back off this version. Back off or keep going? Cooling."): the plain sentence answers their framing ("back off or keep going", "too late?", "too crowded?"), and the timing line gives only the label and reading with its two facts ("**Timing: Cooling.** Searches are down 38% over 5 years, and the top 10 sell about 450 a month together."), never the question again.
- **Credit what they got right** when their own numbers or hunch match a row ("You were right that reviews are thin: the median is 41, and 19 of 48 listings have under 100.").

## "If ten more sellers arrive"

One line, built from rows already read, on the first screen after the verdict lines: what a sale would leave at **the cheapest quarter's price** (`priceP25`, or the single-unit `p25` when packs were left out), which is where a price fight pushes, after the user's channel's fees (`judgement.md`, "The margin follows the user's channel": on Amazon the referral fee at the leaders' rate on that price plus the median FBA fee) and the unit cost (their quote, else the factory median), with its share of that price: "If ten more sellers arrive: at USD 17.99, the price a price fight pushes to, you'd keep about USD 5.20 a sale after Amazon's fees and the USD 4.10 factory median (29%)." Then, in a few words, whether they have a difference buyers can see (what they said they'd change, a complaint worth building on); with none yet, the one fix is that difference. No unit cost read or given: the line gives what a sale pays out after fees at that price, and says the unit cost isn't in yet.

## What it can't see, said once

In the full detail's "What this can't see" line (or on the first screen when the user asked only about timing): sales history over time, keyword search volumes, and units per day from a single TikTok read. A fact about coverage, not a warning.

## A season the user names ("in time for Christmas")

When the request names a selling window (the Christmas rush, late November to December; Black Friday, late November; back to school, July to August in the US; summer, June to August), read this before the answer, in `find-products` and `validate` alike. It needs the Trends `interestOverTime` points: read them for every idea.
- **Each idea, said plainly:** whether its searches peak in that window, the one peak per idea (`judgement-answer-checks.md`, "One peak"): "peaks in the Christmas window (highest December 2025)" or "no Christmas lift: highest in June 2026". The plain answer to their question names which ideas peak in it, and each idea's row or verdict line carries it: in what helps when it peaks there, in what holds it back when it doesn't. The delivery lead time line stays as it is.
- **A seasonal fall is not a decline.** A fall measured from last season's peak is the season. Compare the latest point with the same weeks a year earlier (a 12-month read's first points): level or higher, with last year's high in the window, it is the season ("down 30% over 12 months, but that's the drop since last December's high: this week is level with the same week last year"); lower there too, it is a real decline, said as one ("and 25% below the same week last year: interest is falling, not only seasonal"). The idea's one demand statement and its count stay as they are; this line says which story the figure tells.
- **Rank or flag:** the order and the counts don't change; among rows level on for minus against, an idea peaking in their window comes first, and an idea with no lift in it is flagged in its row, never dropped.

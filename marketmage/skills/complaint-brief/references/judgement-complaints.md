# Judgement: the complaint brief ("the complaint you'd fix")

Part of the judgement rules (`judgement.md` is the core). Read before choosing the reviews to read for "what do buyers complain about", "what would I improve" or "how do I beat the top listing", and before writing the brief: in `complaint-brief`, and wherever another skill hands off to it (validate's "The version you'd build", the directions read in `judgement-deeper.md`, reviews-watch on a rival, launch-plan). It turns the leaders' bad reviews into a product brief a seller can take to a factory. The facts layer is unchanged: the signal table and the verdict never move with a brief.

## 1. Pick the leaders that matter

- **3 to 5 of the top 10** for the product's search (the Amazon leaders' rows already read in this chat, else the Amazon top 10: `complaint-brief`, step 2), each carrying a sales badge (`boughtPastMonthMin` above 0). A leader with no badge has no proof buyers choose it, so its complaints don't make the brief.
- **Favour the highest 1-star share** (`starBreakdown`), then the biggest sellers (`boughtPastMonthMin`): the first shows where buyers are let down, the second where fixing it is worth most. Say in a few words which were picked and why ("the 5 best sellers, led by the two with the most 1-star reviews").
- Rows that aren't the product (an accessory, another product of the brand) are never a leader (`running-results.md`, "Read the data like an analyst").

## 2. Choose the sources from the known limits, before anything runs

Read `known-limits.md` first; a route it lists is never tried.
- **Leaders on Amazon US:** their review text isn't read there. Read the **same products on amazon.co.uk and amazon.de** (their product links, `https://www.amazon.co.uk/dp/<ASIN>` and `https://www.amazon.de/dp/<ASIN>`, in one read: each link keeps its own marketplace); say before the run that a brand sold only in the US comes back empty there. Add **the brand's own shop** for a leader whose product page the user gives or the rows link, when it uses a review app the reviews read supports, and **Trustpilot** (`trustpilotDomains`) for a leader that is a brand with its own domain, said as reviews of the brand and its orders. The user may paste the leader's **Walmart** reviews: read what they paste, labelled as from the pasted text.
- **Leaders on another Amazon marketplace:** read that marketplace's own pages (its top 8 to 13 reviews per product).
- **Say the known-limits line once,** in the estimate: "Amazon US shows review text only to signed-in shoppers, so I read the same products on Amazon UK and Germany." Never again in the brief, and never as something tried or missed (`known-limits.md`, "Say it once, plainly").

## 3. Read the low reviews as well as the themes

- **The themes come first** (`themes`, `topComplaints`, `topPraise` on each rating summary), **then the 1–2★ review texts** themselves (`review` rows with `rating` 1 or 2), because a theme is a keyword match and the texts say what actually went wrong.
- **Named themes are English only.** Reviews in German, Spanish or another language give few or no themes: Claude reads those texts itself and groups them, and says so once in a few words ("the German reviews I read myself").
- **Count from what was read:** each complaint's count is the number of low reviews read that name it, out of all low reviews read ("11 of 46 low reviews read"), and how many of the leaders read have it. Never a count from memory, a likely complaint for that kind of product, or a total that adds up more than was read.

## 4. Write the brief, on one screen

The brief leads with the complaint, in plain words, then these lines, one fact each (about 200 words; the user's own question first):
- **The complaint you'd fix:** its count ("11 of 46 low reviews read"), how many of the leaders read have it ("3 of the 5 leaders"), and one short quote (text only, never a name);
- **Why it matters:** those leaders' sales floor ("at least 2,400 a month between them"), said as a floor;
- **The praise to match:** the top one or two praise themes, the bar a new version must still meet;
- **The fix, as a spec line** a factory can quote on ("strap adjusts down to 24 in (61 cm)"; "elastic top with a toggle on the bottle sleeve");
- **Can a factory make it?** whether factory offers already list the fix (from the supplier offers' titles and attributes, when read): "3 of 10 factory offers list a 20–48 in strap"; when none do, "ask for it as a custom part";
- **How to show it:** the main photo that proves the fix at a glance ("the bottle upside down, still held");
- **The sample test:** how the user checks the fix on a sample before ordering (a test they can run at home).
A second complaint worth building on may follow in one line. Then the Next step, and at most two follow-ups (`running-results.md`, "At most two follow-ups").

## 5. Honesty

- **"A complaint worth building on"** needs **at least 3 mentions across at least 2 leaders with sales badges**. Below that (fewer mentions, or all from one leader), it is **"a hint to check"**, named as such in a few words with its count, never the brief's lead and never written as a fix to build.
- **Reviews are a sample:** say so once, in a few words ("from the reviews these pages show").
- **A leader whose text couldn't be read is "not read"**, never "no complaints": a brand sold only in the US comes back empty on Amazon UK and Germany, so say "2 of the 5 leaders aren't sold in the UK or Germany, so their reviews weren't read".
- **Themes are never invented.** When only stars were read (a US-only leader, a shop that publishes counts only), the star shares are the facts ("12% 1-star"), and the complaint waits for a read that has the text; offer that read once.
- **No brief without two leaders read.** With text from fewer than 2 leaders, give what was read as hints to check, and name the read that would complete it (another leader on Amazon UK or Germany, the brand's shop, or the user's pasted reviews).

# Validate: the one-page report

Validate's own reference, read only at the report step, once the scorecard is written and only where `validate-scorecard.md`, "The report, made beside the scorecard" says a report is made. It sets the report's content and look, so it reads the same from run to run.

## What it is

One artifact: a single self-contained HTML page (no React, no script, no external file: styles in one `<style>`, charts as inline SVG), titled "<Product>: market check". It reads in light and dark (it follows the viewer's setting), on a phone (one column under 640px wide) and on paper (it prints on one or two pages). Keep it compact: about 15 to 25 KB of HTML.

**Every figure is from this check:** each number is read in this check (the rows, the summaries, the user's own figures, labelled as theirs) or is an assumption the references name (freight at 15 to 30% of a factory price, $8 to 12 of launch ads a sale, $0.80 to 1.50 a click on Amazon US, 1 in 10 clicks buying), labelled "an assumption" where it appears. The same figure is the same everywhere in the chat and the report. No points between real readings, no estimate drawn as a fact, no fee or rate from memory. The demand line plots the Trends points read (monthly averages of the weekly points are fine, said in its caption); with no series read, that section says "not read" and draws nothing.

**Money in the seller's symbol** ($, £, €), plain words throughout (`plain-words.md`), the labels word for word. No Apify cost anywhere except the next move's own cost, when it has one. **The same layout for every verdict:** a "no" shows its evidence as fully as a "yes", every section present (a section with nothing read says so in one line).

## Top to bottom

1. **Verdict:** the badge, the product, the label word for word and the one-line reason (the scorecard's headline and its bold why); with a profile, the For you label first and the market's after it. Under it, two separate pills, "Data: complete" and "Verdict confidence: medium, it hangs on the ad cost", then the source line: "Amazon US, Google Trends, TikTok Shop and Made-in-China, read 13 Nov 2026".
2. **Signal chips:** the scorecard's chips, the same five at most, the same badges and words.
3. **Headline tiles,** in this order: **the deciding number first** (the break-even ad cost per sale, with the healthy ad cost under it; with no deciding number, the profit per unit before ads leads); **demand** (the 5-year change); **monthly sales of the top 10** ("at least 14,000 a month", with its dollar figure); **profit per unit** before ads, and after ads as a range at $8 to 12 a sale, labelled "launch ads, an assumption"; **first order** (the lowest minimum order × its unit price, from a matching offer, or the user's quote). Under the profit tile, in small type, the product it assumes ("assumes a cordless USB heated mask at $6.10 a unit from a factory, 200 minimum").
4. **Sections,** each opening with its name as an `<h2>`, word for word (Demand, Profit, Unknowns, Competition, What you'd build, Risks, Next move, How we judged this), then a **conclusion box** above its chart or table. The box has three parts: a **badge** (Good sign, Watch or Warning sign, from the rows behind it: favours, neutral or mixed, against); the **finding**, one bold line stating the result, never describing the chart ("Demand is growing year on year and peaks every December", not "Google searches over 5 years"); and **What to do**, one line ("Order next season's stock by about September so it lands before the December rise"). Then the chart or table, then a caption with its source and the date read. The sections, in order:
   - **Demand:** the 5-year line, the yearly peak marked on each complete year ("Dec"), the change in the finding; a one-off high, if any, labelled as one.
   - **Profit:** where each sale's money goes, from the price down to what is left: one horizontal stacked bar per channel read, side by side (Amazon with its referral and FBA fees; TikTok Shop with its fee from this read; the user's own channel when they named one, with its card fee and shipping estimate), segments for fees, unit cost, freight, ads and what is left. Freight and ads are drawn as labelled ranges (a solid part to the low end, hatched to the high end); what is left as a range to match. Each segment labelled with its amount, beside it when it is too narrow to hold the text.
   - **Unknowns:** a small planning table, one row per input not measured: what it is, what was assumed and why, its range, and what each end does to the break-even. At least freight per unit (15% and 30% of the unit cost: the break-even at each) and the share of ad clicks that buy (at 1 in 10, an assumption: the click price that breaks even, and the one that keeps the healthy ad cost), plus the click price range where Amazon's applies. The finding names the input that decides the verdict; What to do is the free step that measures it.
   - **Competition:** each top-10 listing's monthly sales floor as a horizontal bar (labelled by brand or a short title, the value on the bar), the leader highlighted; the finding gives the leader's share of the top 10's sales and how many of the top 10 arrived in the last 12 months; review depth and ads in one line under it.
   - **What you'd build:** a table of the kinds of product on page one (from the leaders' titles: one row per kind, how many of the top 10, their price range, their sales floor) and a column saying which kind the factory offers match; the finding names the kind the cost figures assume, and any kind with no matching offer as still to price.
   - **Risks:** a checklist, one row each, with a status (✅ clear, ⚠️ watch, ❌ warning, ❔ not checked) and the fact: a regulated product (its line), the yearly peak and lead time, Amazon selling it itself, the quality gap, the ad cost, the price band, the dropship shipping line ("plus shipping, still to add"; never free shipping).
   - **Next move:** one, with its cost ("free, about 5 minutes", a sample's price, or a MarketMage read's estimate), what each result means, then "After that:" with at most two items. The same move as the chat's Next step.
   - **How we judged this:** the full signal table at the bottom, one row per signal: what we looked at, what we found (its number), the rule of thumb in plain words ("helps when searches rise 15% or more in 5 years"), and its reading (helps, hurts, neutral, not read); then Launch ads as the cap it is, the counts in words, and what this can't see in one line.
5. **Footer:** a small, muted line, "Powered by MarketMage", linking to https://marketmage.io. No logo, no banner, nothing else in it.

## Look

- **Badges carry a word and a symbol, never colour alone:** good sign green, watch amber, warning red, not read grey. In charts the data marks are one neutral blue; only the leader bar and the profit-left segment take an accent; status colours are for badges.
- **Charts:** 2px lines, thin bars with a 2px gap, value labels on bars and the line's peaks only, a hairline baseline, no gridline clutter, no 3D, no pie, no legend where direct labels do. Each mark carries an SVG `<title>` with its value (a hover tip at no cost). Text in charts uses the text colours, never the series colour.
- **Numbers right-aligned in tables,** tabular figures, units in headers ("Monthly sales (at least)").

## The skeleton

Fill it in; keep the classes and the order; repeat a section block per section. Coordinates: the line chart's plot area is x 40 to 580, y 20 (100) to 170 (0): x = 40 + i × 540 ÷ (n − 1), y = 170 − value × 1.5. A stacked bar's scale is 540 ÷ price: each segment's width is its amount × scale, laid left to right from x 40.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Heated eye masks: market check</title>
<style>
:root{--bg:#fcfcfb;--card:#fff;--ink:#1b1b1a;--ink2:#55554f;--muted:#8a8a83;--line:#e1e0d9;--axis:#c3c2b7;
--mark:#3a6fd8;--accent:#1f4fb4;--good:#0ca30c;--watch:#b7791f;--warn:#d03b3b;--na:#8a8a83;
--goodbg:#e9f6e9;--watchbg:#fdf3e1;--warnbg:#fbeaea;--nabg:#f0f0ed}
@media (prefers-color-scheme:dark){:root{--bg:#1a1a19;--card:#232321;--ink:#ededea;--ink2:#b9b8b1;--muted:#8d8c86;
--line:#2c2c2a;--axis:#383835;--mark:#6f9bf0;--accent:#9dbcf7;--watch:#fab219;--goodbg:#16301a;--watchbg:#3a2e14;--warnbg:#3a1a1a;--nabg:#2a2a28}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:860px;margin:0 auto;padding:20px 16px 32px}h1{font-size:22px;margin:0 0 4px}h2{font-size:17px;margin:0 0 8px}
.why{font-weight:600;margin:6px 0 10px}.pills,.chips{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.pill,.chip{border:1px solid var(--line);border-radius:999px;padding:3px 10px;font-size:13px;background:var(--card)}
.src,.cap,.assume{color:var(--muted);font-size:12px}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:14px 0}
.tile{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.tile.key{border:2px solid var(--accent)}.tile .k{font-size:12px;color:var(--ink2)}.tile .v{font-size:22px;font-weight:700;font-variant-numeric:tabular-nums}
section{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;margin:14px 0;break-inside:avoid}
.concl{border-left:4px solid var(--na);background:var(--nabg);border-radius:6px;padding:8px 12px;margin-bottom:10px}
.concl.good{border-color:var(--good);background:var(--goodbg)}.concl.watch{border-color:var(--watch);background:var(--watchbg)}.concl.warn{border-color:var(--warn);background:var(--warnbg)}
.badge{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.03em}.finding{font-weight:700;margin:2px 0}.todo{margin:0;color:var(--ink2)}
svg{width:100%;height:auto;display:block}svg text{fill:var(--ink2);font-size:11px}.lbl{fill:var(--ink)}
table{width:100%;border-collapse:collapse;font-size:14px}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line)}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
footer{text-align:center;color:var(--muted);font-size:12px;margin-top:24px}footer a{color:var(--muted)}
@media (max-width:640px){h1{font-size:19px}.tile .v{font-size:19px}}
@media print{body{background:#fff}section,.tile{border-color:#ccc}}
</style></head><body><main>
<header>
  <h1>🟡 Heated eye masks: Promising, with one fix</h1>
  <p class="why">It works if ads cost under about $5 a sale: buyers are here and growing, and a $28.99 mask leaves about $12 before ads.</p>
  <div class="pills"><span class="pill">Data: complete</span><span class="pill">Verdict confidence: medium, it hangs on the ad cost</span></div>
  <p class="src">Amazon US, Google Trends, TikTok Shop and Made-in-China, read 13 Nov 2026</p>
  <div class="chips"><span class="chip">✅ Demand: up 96% in 5 years, peaks every December</span><!-- … up to 5 --></div>
</header>
<div class="tiles">
  <div class="tile key"><div class="k">Break-even ad cost per sale</div><div class="v">$12.35</div><div class="k">healthy under $5.10</div></div>
  <div class="tile"><div class="k">Profit per unit</div><div class="v">$12.35</div><div class="k">before ads; $0.35–4.35 after $8–12 launch ads (an assumption)</div><div class="assume">assumes …</div></div>
  <!-- demand, monthly sales of the top 10, first order -->
</div>
<section>
  <h2>Demand</h2>
  <div class="concl good"><div class="badge">✅ Good sign</div><p class="finding">Demand is growing year on year and peaks every December.</p><p class="todo">What to do: order next season's stock by about September so it lands before the December rise.</p></div>
  <svg viewBox="0 0 600 200" role="img" aria-label="Searches for heated eye mask, last 5 years">
    <line x1="40" y1="170" x2="580" y2="170" stroke="var(--axis)"/>
    <polyline fill="none" stroke="var(--mark)" stroke-width="2" points="40,140 49,138 …"/>
    <circle cx="…" cy="…" r="4" fill="var(--mark)"><title>Dec 2024: 52</title></circle><text x="…" y="…" text-anchor="middle">Dec</text>
    <text x="40" y="188">2021</text><!-- a year label per year -->
  </svg>
  <p class="cap">Google Trends, US, relative interest (100 = the 5 years' highest week), monthly averages; read 13 Nov 2026</p>
</section>
<section>
  <h2>Profit</h2>
  <div class="concl watch">…</div>
  <svg viewBox="0 0 600 120" role="img" aria-label="Where a $28.99 sale's money goes, Amazon">
    <defs><pattern id="h" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="3" height="6" fill="var(--mark)" opacity=".45"/></pattern></defs>
    <text x="40" y="20" class="lbl">Amazon (FBA)</text>
    <rect x="40" y="28" width="162" height="22" rx="3" fill="var(--axis)"><title>Amazon fees $8.71</title></rect>
    <!-- unit cost solid; freight low end solid + rest hatched (fill="url(#h)"); ads $8 solid + $4 hatched; what is left in var(--accent) -->
    <text x="121" y="66" text-anchor="middle">fees $8.71</text>
  </svg>
  <p class="cap">Amazon's fees for the leaders' size and weight; factory list prices; freight and launch ads are assumptions; read 13 Nov 2026</p>
</section>
<!-- Unknowns, Competition, What you'd build: <table> with th.n/td.n for numbers; Risks: a <table> or <ul> with a status per row -->
<section><h2>Next move</h2><div class="concl watch"><div class="badge">⚠️ Watch</div><p class="finding">…</p><p class="todo">After that: …</p></div></section>
<section><h2>How we judged this</h2><table><tr><th>What we looked at</th><th>What we found</th><th>Rule of thumb</th><th>Reading</th></tr><!-- … --></table></section>
<footer>Powered by <a href="https://marketmage.io">MarketMage</a></footer>
</main></body></html>
```

The finished page holds real values in place of every "…" and comment; nothing of the skeleton's sample text stays unless this check's data says it.

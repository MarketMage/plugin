# MarketMage

Product research and competitor monitoring for e-commerce sellers, inside Claude. For dropshippers, Amazon sellers, makers and resellers on Etsy and eBay, researchers and agencies, and brands.

**How to begin:** type `/marketmage:start` for a welcome with everything MarketMage can do (and a guided first session if you want something to sell), or just say one of these:
- "I'm new, help me find something to sell"
- "Is a heated eye mask worth selling for me?"
- "What is allbirds.com selling right now?"

**Which Claude plan:** any, Free included. The Monday scheduled briefing uses Claude's scheduled tasks, which come with the paid plans (Pro, Max, Ultra, Team, Enterprise). To install, see [Install](#install) below.

Ask in plain words:
- what to sell, whether an idea is worth it, and what it costs to source;
- what a competitor's store sells, promotes, advertises and runs on;
- how your catalogue, prices and product pages compare with a rival's;
- what a keyword's market looks like on Amazon, eBay, Etsy, Walmart, Target, Best Buy, Home Depot and Lowe's;
- what customers say in reviews;
- who sells a product cheapest, or below your MAP.

Then save a **watchlist** that runs on a schedule and tells you what changed: prices, sales, stock, the Buy Box, new products, Amazon ranks, new reviews, promotions and launches, new sellers in your searches, competitors' new ads, TikTok Shop sales per day and Amazon chart entries. What changed comes to you as **your briefing in Claude, on request or on a Monday schedule**: a Claude scheduled task that reads your watches every Monday morning, never starts a paid run, and names any watch that failed or didn't run. Slack, Discord, Teams or email delivery of each digest is there when you ask for it, and alerts can narrow that message to what matters: reviews under N stars, price drops of N% or more, rank milestones.

Every job runs [CleanPull's actors](https://apify.com/cleanpull) in **your own Apify account**, at their published per-result prices. **All you provide is your Apify sign-in**: no marketplace, supplier or ad platform accounts or keys.

> **Claude asks before anything over USD 0.05.** Above USD 0.05 for one request, and before anything recurring, Claude gives one estimate ("This costs about USD 0.35, occasionally a little more if I need to dig deeper to answer you.") and waits for your yes; smaller reads just run. Each run also carries a spending limit set a little above the estimate, so a job can finish without asking twice and still can't run away, and every scheduled watchlist has a maximum cost per run.

## Install

MarketMage costs nothing to install. It works on any Claude plan, Free included; the scheduled Monday briefing needs a paid plan (Pro, Max, Ultra, Team, Enterprise).

**On claude.ai or in the Claude desktop app**

1. Open **Customize** in the left sidebar, then the **Plugins** tab ([claude.ai/customize/plugins](https://claude.ai/customize/plugins)).
2. Click **Add**, then **Add marketplace**, then **Add from a repository**.
3. In the **URL** box, type `MarketMage/plugin` and click **Sync**.
4. MarketMage now appears with your other plugins. Search for **MarketMage**, open it and click **Add**.

Given MarketMage as a .zip file? Click **Add**, then **Upload plugin**, and pick the file. Uploading a newer version over it keeps your Apify connection.

**In Claude Code**

1. Type `/plugin marketplace add MarketMage/plugin`.
2. Then type `/plugin install marketmage@marketmage`.

From a shell, in one step: `claude plugin install marketmage --marketplace MarketMage/plugin`. A plugin you added on claude.ai also reaches Claude Code by itself, the next time you start it signed in to the same account.

**Connect your Apify account, once**

Apify is a web-data platform. MarketMage's research runs there, in your own Apify account, and Apify bills that account for each run, usually cents. A free Apify account works: it includes USD 5 of credit a month and needs no credit card. You can create one at [apify.com](https://apify.com) or while connecting.

1. In **Customize → Plugins**, open **MarketMage**, go to its **Connectors** tab and click **Connect** next to **apify**. In Claude Code, type `/mcp` and choose **apify**.
2. Claude shows an "Add custom connector" notice with the details filled in. Check the address starts with `https://mcp.apify.com/`, keep the details as they are and click **Add**.
3. Sign in to Apify, or create a free account, and approve. It is the only sign-in MarketMage needs.
4. Optional, fewer approval boxes: claude.ai asks before each Apify tool call until you change it. In **Customize → Connectors → apify → Tool permissions**, set **Read-only tools** and **Call Actor** to **Always allow**. MarketMage still waits for your yes before any paid run over USD 0.05 or anything recurring, and every run has a spending limit.

**Your first message:** type `/marketmage:start` for a short welcome, or ask "Can you check what allbirds.com sells and how they price it?" Asking Claude to *check* or *look up* something reads it live with MarketMage.

**Once MarketMage is in Claude's plugin directory,** you'll also find it under **Customize → Plugins → Discover** and add it there, with nothing to type (the directory shows on paid Claude plans). The steps above keep working.

Step by step, with pictures: [marketmage.io/start](https://marketmage.io/start/).

**Help:** [marketmage.io/support](https://marketmage.io/support/) · bugs and ideas: [GitHub issues](https://github.com/MarketMage/plugin/issues) · security: security@marketmage.io

## What you can ask

| Skill | What it does | Try |
| --- | --- | --- |
| `start` (also `/marketmage:start`) | A welcome: what MarketMage can do, as seven jobs with an example each, one line on cost, then "What brings you here?", your answer taken to the right job; connecting Apify if needed; for someone who wants something to sell, a guided first session (ideas in your interest, the two best checked for the market and for you, one related version and one watch, with one cost estimate for your yes before it runs); a returning user is welcomed back to where they left off | "I'm new, help me find something to sell" · "What can MarketMage do?" |
| `find-products` | Product ideas selling now, from the sources your channel acts on (for dropshippers TikTok Shop, Meta ads that have kept running 35+ days and AliExpress single-unit prices; for Amazon sellers Best Sellers and how crowded each search is; Etsy listings for Etsy sellers; Google Trends rising searches for all), ideas several sources back ranked higher and each idea's backing named, scored and ranked by what the data favours, with what to avoid and why; as watchlists, a weekly opportunity digest (new rising searches, chart entries and TikTok products speeding up, in one "Opportunities this week" section), TikTok sales per day and Amazon chart new entries and climbers | "What kitchen products are selling well right now?" · "Find trending pet products under $30" · "Give me product ideas in skincare for the UK" |
| `validate` | A verdict on one idea (Strong; Promising, with one fix; or Not this version, with related versions the data favours), scored signal by signal with its confidence: demand trend, Amazon competition and the leaders' monthly sales floor, TikTok sales, margin after Amazon's referral and FBA fees on amazon.com and on amazon.co.uk, .de, .fr, .it and .es (ex VAT on the European ones; before fees elsewhere); it ends on a costed next move | "Is a cordless pet grooming vacuum worth selling?" · "How saturated are silicone stretch lids on Amazon?" · "Validate weighted jump ropes for the US" |
| `complaint-brief` | What buyers complain about in the leading listings for an idea, turned into a product brief: the complaint you'd fix (how many low reviews name it, across how many best sellers, with a quote), the praise to match, the fix as a factory spec line, whether factories already list it, how to show it in the main photo, and the sample test (for US best sellers, their reviews on Amazon UK and Germany, the brand's own shop or Trustpilot) | "What do buyers complain about in women's hiking hip packs?" · "What would I improve on the top dog nail grinders?" · "How do I beat the top listing for silicone stretch lids?" |
| `launch-plan` | After a promising verdict: suppliers at your first-order quantity, the leaders' 1-star complaints, a listing draft that answers them, your price against the market's band, first-order maths after fees, a stop rule with numbers agreed before you spend on ads, and one launch-week watch on the leaders' prices, ranks and reviews | "I want to go ahead with heated eye masks" · "Help me launch this" · "What would a first order look like?" |
| `briefing` | What every watch found since your last visit, plus your notebook (your stage, a stop rule that's due), as at most 5 decisions, each with one recommended move, naming any watch that failed or didn't run; reading the digests is free. After your first one, it can run every Monday morning as a Claude scheduled task that only reads | "Good morning, catch me up" · "What's new?" · "Brief me every Monday morning" |
| `notebook` | Optional memory across chats, in your own Apify account: the ideas you checked with their verdicts, versions tried, decisions, linked watches, and your profile as bands; view or delete it any time | "Keep a notebook for me" · "What ideas did I check last month?" · "Delete my notebook" |
| `spy-store` | A competitor store's catalogue, prices, discounts, best sellers, new arrivals, apps and tools | "What does colourpop.com sell and how do they price it?" · "What apps does allbirds.com run on Shopify?" · "Show me ruffwear.com's newest products" |
| `price-check` | Every store's price for a barcode, product page or ASIN, right now | "Who sells UPC 027242923232 cheapest?" · "What do these three product pages cost today?" · "Who has the Buy Box on B0BZYCJK89?" |
| `price-watch` | A scheduled digest of price, sale, stock, Buy Box and Best Sellers Rank changes across any stores, Amazon and whole Shopify stores | "Watch these 10 competitor products and tell me when prices change" · "Monitor allbirds.com for new products and price drops every morning" · "Track my Amazon listings' Buy Box daily" |
| `map-watch` | Sellers below your minimum advertised price, once or on a schedule | "Who sells UPC 027242923232 below $329.99?" · "Check my 20 UPCs against MAP every Monday" · "Which stores break MAP on these barcodes?" |
| `rank-watch` | Organic and sponsored Amazon rank for keywords, and who outranks you, once or tracked | "Where does B0BZYCJK89 rank for 'stainless steel water bottle'?" · "Track my 2 ASINs on 10 keywords daily" · "Who outranks me for 'yoga mat' on page 1?" |
| `export` | Results to a Google Sheet: append, replace, or keep in sync; Google Sheets can then email you itself when the sheet changes | "Put these results in my Google Sheet" · "Keep a sheet updated from my price watchlist" · "Export the store's catalogue to Sheets by SKU" |
| `reviews-watch` | Ratings, newest reviews and complaint and praise themes for shop product pages (Judge.me, Yotpo, Okendo, Loox, Stamped), Amazon ASINs and Trustpilot businesses, once or as a watchlist of new reviews and rating moves (amazon.com gives the rating and the share per star only, with no review text for signed-out shoppers, so themes don't cover US ASINs) | "What do customers complain about on this product?" · "Compare the reviews of my product and these two competitors'" · "Tell me every morning when my products get a review under 3 stars" |
| `gaps` | Your catalogue against competitors': products you both sell with the price gap, what they sell that you don't (and the reverse), and a price index; as a weekly watch on Shopify stores, the products a rival newly sells for less than you | "Which of my products does rival.com also sell, and at what price?" · "What brands does this competitor carry that I don't?" · "Tell me each week when rival.com undercuts me" |
| `promo-watch` | Competitors' sales, codes, free-shipping thresholds, markdowns and new launches, once or as a watchlist of what started, ended and launched | "What promotions is colourpop.com running right now?" · "What free-shipping thresholds do my 5 competitors have?" · "Tell me when these stores start or end a sale" |
| `market-scan` | A keyword's market on Amazon, eBay, Etsy, Walmart, Target, Best Buy, Home Depot and Lowe's: price percentiles, seller concentration, review depth, ads; as a watchlist, new entrants and price-band moves | "What do yoga mats sell for on Amazon US and UK?" · "How crowded is 'insulated water bottle' on Amazon?" · "Tell me weekly when new sellers enter the top results for my keywords" |
| `suppliers` | Wholesale unit prices, MOQs and price breaks from Made-in-China, AliExpress and Alibaba searches, and the DHgate and Alibaba pages you found (DHgate with an estimated US landed cost) | "What would silicone baking mats cost me to source?" · "What do these DHgate listings cost landed in the US?" · "What's the unit price at 1,000 units for cotton tote bags?" |
| `ads-watch` | Competitors' ads from Google's Ads Transparency Center, Meta's Ad Library (running ads, any country) and TikTok's ads library (EU, UK, Switzerland), with first and last shown dates; as a watchlist, new and stopped ads; and proven small advertisers for a product (Meta ads running 35+ days from stores of about 20 products or fewer) | "What ads is Allbirds running on Google?" · "Show me Gymshark's newest YouTube and display ads in the UK" · "Tell me each day when these 3 brands launch new ads" |
| `listing-audit` | A 0–100 score and a fix list for product pages and Amazon listings (structured data, GTIN, images, titles, bullets, A+), with a comparison against a competitor's page | "Why doesn't Google show my product with price and stars?" · "Audit my Amazon listing B0DTK7VDTH" · "How does my product page compare with my competitor's?" |
| `watchlists` | List, read, pause, change or stop your watchlists | "What am I watching?" · "What changed in my competitor watch today?" · "Pause my rank watch and tell me what it costs" |

Market scans cover Amazon, eBay, Etsy, Walmart, Target, Best Buy, Home Depot and Lowe's (Home Depot and Lowe's: up to 24 results a keyword, one-off scans only).

`spy-store` also reads a store's current promotions and launches and can audit its best-selling pages; `validate` also sizes up the market (price band and seller concentration) and estimates the margin from supplier prices; `find-products` can check how crowded each idea's Amazon search is.

## How it connects

- **The connector:** the plugin adds Apify's MCP server (`https://mcp.apify.com`) with only the general tools these skills use: `call-actor` (the one way the skills start a run, always with a spending cap), the run and storage readers, the task and schedule tools (create, read, change or pause; no delete) and `apify-api-read` (read-only GET requests). It lists no tool per actor, because those tools can't carry a spending cap.
- **Sign-in:** you sign in once with **Apify OAuth**, on the plugin's Connectors tab or when Claude first asks.
- **Not connected?** In claude.ai, the desktop app or Cowork: **Customize → Plugins → MarketMage → Connectors → Connect**, keep the pre-filled "Add custom connector" details, click **Add**, then sign in to Apify. In Claude Code: run `/mcp` and sign in to Apify.
- **Access:** the sign-in gives the connector full access to your Apify account (Apify's OAuth scope is full API access). Technically, `call-actor` and the task and schedule tools can start or schedule any actor in the Apify Store, and `apify-api-read` can read any part of your account (runs, datasets, tasks, schedules, usage). The skills only start CleanPull's actors and read their results; read your tasks and schedules (list, settings and runs) to find the CleanPull watchlists, named `cw-…`; and create, change or pause only those, when you ask. The plugin has no delete tool: you delete a watch in the Apify Console. These limits are the skills' instructions to Claude, not a technical restriction. To see exactly what a run was given, ask Claude "show me the input": it shows the actor and the input it sent, so you can rerun it yourself.
- **Billing:** runs are billed to your Apify account at the prices on each actor's Store page. CleanPull, the team behind MarketMage, earns the per-result price; Apify keeps its share.
  - **Runs started in the chat** get a spending cap from Apify a little above the estimate Claude gave (1.5 times it, or the estimate plus USD 0.15 when that is more, and never above a budget you set), so a job finishes instead of stopping part-way and can't cost more than that.
  - **Scheduled runs** of a watchlist have no Apify spending cap of their own (Apify's task and schedule tools can't set one). Instead each watchlist's input carries a **Max cost per run** (`maxRunCostUsd`, about 1.5× its estimate, plus room for the reviews, promotions, marketplace-search and ads watchers), which every CleanPull actor the plugin schedules holds itself to: Watch Digest bounds its watchers and delivery by it, and the others stop starting items before passing it. You can change it on the task's page in the Apify Console.
  - **Data providers.** Some sources come from data providers we hold an agreement with, on CleanPull's accounts: Bright Data, a web-data provider, for eBay, Etsy, Walmart, Target, Best Buy, Home Depot, Lowe's, AliExpress, Alibaba and Trustpilot data, and ScrapeCreators, an ad data provider, for the Meta and TikTok ad libraries. Their records appear on your bill as provider and library events at the actors' published prices; you never set them up.
  - **Timing.** Most runs take seconds to a minute. Searches through the data service usually take **1 to 4 minutes for Walmart, eBay, Home Depot and Lowe's**, and **up to about 12 minutes for Etsy, Target and Best Buy** (and for Walmart or eBay when a page can't be read) (Target and Best Buy by barcode 3 to 5; Claude gives you Amazon's results first while they run), Trustpilot about 2 to 3 minutes a business. The AliExpress single-unit check (AliExpress Scraper, product pages included) can take several minutes, so Claude's answer doesn't wait on it: when it is still reading, Claude answers first with the AliExpress parts marked as still reading, then adds them in a short follow-up when the check lands. Claude says so before starting, and follows the run.
  - **Scheduled exports to Google Sheets** have no cost cap either; each carries a row `limit` instead, so an export costs at most `limit` × USD 0.0001.
- **Already using Apify's connector?** If you also added Apify's own connector in Claude, you'll see two sets of Apify tools. That's harmless: the plugin's skills use this plugin's connector. You can turn the other off while using the plugin.

**Endpoints, and what each receives:**

| Endpoint | Who calls it | What it receives |
| --- | --- | --- |
| `mcp.apify.com` (Apify's MCP server, the connector) | Claude, through the plugin | Your Apify sign-in (OAuth), and each tool call: the actor's name, the run's input (the URLs, ASINs, barcodes, keywords, store domains, brand names or ideas you asked about), its spending cap, and task, schedule and storage reads |
| `api.apify.com` (Apify's platform) | The connector, and CleanPull's actors as they run in your account | The same run inputs, plus the results the actors write: datasets, key-value stores, your `cw-` tasks and schedules, and your notebook if you keep one |
| Bright Data (a web-data provider we hold an agreement with) | CleanPull's actors, never Claude | The page addresses and search terms to read on eBay, Etsy, Walmart, Target, Best Buy, Home Depot, Lowe's, AliExpress, Alibaba and Trustpilot; Supplier Price Finder's Made-in-China pages and Amazon searches when those sites refuse every other route; and the store pages Barcode Price Checker reads through it; not your Apify sign-in or your chat |
| ScrapeCreators (ad data provider) | Ad Library Monitor, never Claude | The advertisers you asked about (brand names, pages or domains) and the country, for the Meta and TikTok ad libraries, and for Google's on a run where Google's own library returns none; not your Apify sign-in or your chat |
| Google Sheets API | Sheets Sync, only when you export | The rows you chose to export and the address of the sheet you shared with CleanPull's service account (or your own credentials) |
| Alert delivery: your email provider (SMTP or its email API), Slack, Discord, Microsoft Teams or your webhook | Alerts Sender and Watch Digest, only when you set a delivery channel up on a watch | The watch's digest text (the changes it found, with product names, prices and links) and the delivery settings you entered in the Apify Console; not your Apify sign-in or your chat |

The sites the actors read themselves (Amazon, online stores, Google's ads library and Trends, Made-in-China until it refuses, review widgets) get an ordinary page request for that page or search, and nothing about you.

You need an Apify account; the free plan works. **Apify's free plan gives $5 of credit a month.** That covers, for example, a daily digest of 50 store products:
- digest $0.005;
- 50 items × $0.00025;
- 50 unchanged checks × $0.0005;
- about **$0.043 a run, or $1.30 a month**.

## Costs

Figures are at Bronze, the paid-plan price (lower on Silver and Gold). The tiers are Apify's names for its plans' Store discounts: **Free is Apify's Free plan, Bronze its Starter plan, Silver its Scale plan and Gold its Business plan.** From 7 November 2026, reads through the data providers (eBay, Etsy, Walmart, Target, Best Buy, Trustpilot, Meta and TikTok ads) cost about twice as much on Apify's free plan; Claude quotes both prices when they differ.

| Job | Typical cost |
| --- | --- |
| Find products in a niche | about $0.15 (US) |
| Validate one idea | about $0.14 (US); named add-ons such as other marketplaces or the leaders' complaints extra, about $0.48 with all |
| Launch plan after a verdict | about $0.06 (suppliers at your quantity and the leaders' complaints) |
| Launch-week watchlist, 5 leaders, 3 keywords, daily | about $0.03 a run, $0.95 a month (first run about $0.10) |
| Notebook | a fraction of a cent a save or read |
| Profile a Shopify store (100 products) | about $0.08 |
| Price check | $0.015 per barcode, $0.0015 per product page, $0.003 per ASIN |
| Price watchlist, 30 items, daily | about $0.03 a run, $0.83 a month (first run about $0.08); outside the US add $0.003 per Amazon ASIN a run |
| Rank watchlist, 10 keywords × 2 ASINs, daily | about $0.09 a run, $2.70 a month (up to $0.25 a run when Amazon shows 16 results a page); organic only about $0.90 a month |
| MAP watchlist, 20 barcodes, weekly | about $1.10 a month |
| Export to Sheets | $0.10 per 1,000 rows |
| Reviews of a product | about $0.013 with 20 reviews ($0.003 for the rating only) |
| Reviews watchlist, 20 products, daily | about $0.034 a run, $1.00 a month (first run about $0.27) |
| Catalogue gaps, your 250 Shopify products against 2 rivals' | about $0.90, reads included |
| Undercut watch, your 250 Shopify products against 2 rivals', weekly | about $0.76 a run, $3.30 a month (first run up to $1.70; Max cost per run $3) |
| Promotions check | about $0.02 a store |
| Promotions watchlist, 10 stores, daily | about $0.024 a run, $0.70 a month |
| Market scan, one keyword on Amazon US | about $0.017 (summary, the default); $0.041 with every listing |
| Market scan on eBay, Etsy, Walmart, Target or Best Buy | about $0.09 a keyword at 24 results, plus $0.015 per marketplace per run |
| Market watchlist, 5 Amazon US keywords, weekly | about $0.08 a month |
| Supplier prices, one product idea | about $0.025 (10 Made-in-China offers); about $0.07 more with 10 Alibaba offers, plus $0.02 per run; the AliExpress single-unit check (one unit, what a repeat buyer pays and the shipping to your buyer's country where the page charges it, top 3, several minutes) about $0.013 |
| Trustpilot reviews, one business | about $0.076 with 20 reviews |
| Competitor ads, one brand on one platform | up to about $0.15 (Google) to $0.18 (TikTok) at 100 ads; about $0.05 at 30 |
| Ads watchlist, 5 brands on Google, daily | about $0.48 a month after a first run of up to $0.76; Meta and TikTok add about $2.10 a month |
| TikTok Shop watchlist, 1 keyword, weekly | up to about $0.28 a month |
| Amazon chart watchlist, 1 category (Best Sellers and New Releases), daily | about $1.95 a month after a first run of about $0.31 |
| Opportunity digest, 5 Trends terms, 1 chart and 1 TikTok keyword, weekly | about $0.50 a month after a first run of about $0.15 |
| Listing audit | $0.005 a page |
| Listing watch, 20 pages, weekly | about $0.06 a month |

Claude gives one cost estimate and asks before any run over USD 0.05, and the monthly cost before saving a watchlist; ask any time what a run cost or will cost. The prices behind these figures are in each skill's `references/costs.md`, generated from the actors' Store pricing.

## What each actor can't do

Honest limits, so the answers are read right:

| Actor | Limits |
| --- | --- |
| Reviews Monitor | Reads Judge.me, Yotpo, Okendo, Loox and Stamped widgets, Amazon product pages, and Trustpilot businesses (through the data service, up to 4 at a time; a watchlist keeps the newest 5 reviews per business). **Not** Amazon's full review list (it needs a sign-in: only the rating, the share per star and the 8 to 13 top reviews; **on amazon.com, the rating and the share per star only**, since it shows no review text to signed-out shoppers, so themes don't cover US ASINs), not Google Shopping reviews, not Bazaarvoice, Junip, REVIEWS.io or PowerReviews. Loox sometimes shows no dates; Stamped and Loox publish no counts per star. Themes are keyword and phrase matching, not AI. Reviewer names are off by default. |
| Catalog Matcher | Matches only what the datasets hold: Shopify's public catalogue has no barcodes, so two Shopify stores match by title, part number, SKU or model. Title matching needs a brand on both sides by default. Prices are compared as listed: no currency conversion, tax or shipping. |
| Promotions & Launch Monitor | Reads a page's HTML: announcement bars drawn only by scripts (Kith, Nike) aren't read; codes only when the site prints them (not email, pop-up or cart codes). Launches off Shopify need two runs. Amazon, Walmart and Target aren't read; a store that can't be read is named in the run summary, not charged. |
| Marketplace Search Scanner | eBay (ebay.com), Etsy, Walmart, Target, Best Buy, Home Depot and Lowe's (US) come through the data service: a few minutes for Walmart, eBay, Home Depot and Lowe's, up to about 12 minutes for the others, and dearer per result than Amazon. Home Depot and Lowe's give at most 24 results and no Walmart-style fallback: a search they block is reported as unread. Watchlists cover Amazon, eBay, Etsy, Walmart, Target and Best Buy. Amazon's search shows no seller, so the seller is the brand in the title. Best Buy's search ranks accessories high. |
| Supplier Price Finder | Searches Made-in-China, and Alibaba (US site, through the data service, usually 1 to 4 minutes, up to about 12) when asked; AliExpress is read with AliExpress Scraper (search and product pages: what a repeat buyer pays, units sold and the shipping to your buyer's country). **DHgate isn't searched** (its robots.txt disallows search) and is read only from pages you give; 1688.com needs a sign-in. Alibaba search results carry no price breaks or shipping, but carry the MOQ and a price range, and Alibaba offer pages you give add the price breaks. Landed cost only where a page charges shipping (DHgate, to the US; AliExpress product pages, to your buyer's country), as an estimate without duties, taxes or fees. Prices in US dollars only. |
| AliExpress Scraper | `price` is what a repeat buyer pays; the one-time first-order deal is kept apart and never used as the cost. Product pages show one shipping line for your buyer's country (the cheapest), not every method, and a no-charge line often needs a minimum basket, so a 0 is treated as shipping still to add, never as free. Product pages are slow: several minutes a run is normal, and a page that fails is delivered from its search card with shipping not read. AliExpress doesn't sell to mainland China and can't be read as a shopper in Russia, Belarus, Iran, Cuba, North Korea or Syria. |
| Ad Library Monitor | Meta and TikTok come through a third-party ad library service; if it's down, those items are read on the next run. **TikTok covers the EU, the UK and Switzerland only.** **Meta lists running ads in every country**; it keeps stopped ads only for ads that reached the EU. Google gives no ad text for image and video ads and no landing page, and **may occasionally decline a run** (a captcha, never solved): those items are then read through the service. Creatives are linked, never downloaded. |
| Listing Quality Checker | Checks what the HTML holds (markup added only by scripts is flagged, not run); image sizes aren't measured; Walmart, Target, Best Buy and REI aren't read. Amazon is read as a signed-out shopper (no Seller Central data). The score follows Google's and Amazon's published guidance and isn't a ranking promise. |

## Your data and secrets

- **Your situation, if you share it:** five quick bands (budget, how you fulfil, experience, channels, side income or brand) choose a lens: which facts count for you, the gates that matter to how you sell (a cold-traffic dropshipper's ad-policy and MOQ-1 checks, an FBA seller's first order), and a fit check with numbers. Answers then lead with "For you", then "For the market". The facts table and the market verdict never change with it. It stays in the chat unless you ask for a notebook, which keeps it as bands only.
- **The notebook, only if you say yes:** a key-value store named `marketmage-notebook` in your own Apify account (one record per entry), started only when you say yes, written only by CleanPull's notebook actor (0.2): your profile as bands (never amounts) with an answer-shape preference if you pick one (no tables, plain text), the ideas checked with their verdicts and key numbers, versions tried, your decisions (with your journey stage and any stop rule you agreed) and watch links. With your yes, it also keeps your own landed cost per unit for an idea, with its currency and date; that is the one figure of yours it holds. It holds no personal data and no chat content: the actor refuses other amounts of your own money, emails, phone numbers and keys. It also keeps a small `status` record (that the notebook is on, your profile bands and answer shape, and how many entries of each kind). At the first MarketMage turn of a chat (never on a bare greeting such as "hi" or "good morning"), Claude reads that record, a tiny Apify storage read that costs nothing from MarketMage, to know whether you keep a notebook. The full notebook is read only when you've said yes in the chat, mention it or past work, paste `MarketMage notebook: on`, or that record shows it is on. You can view, download or delete it in Apify (Storage → Key-value stores) or ask Claude to.
- **What's sent to Apify:** only what each job needs. That means product URLs, ASINs, barcodes, keywords, store domains, brand names, product ideas, a marketplace, for exports the spreadsheet URL (shared with CleanPull's Google service account: next point), and your notebook's entries if you keep one. The plugin never reads your memory or other chats.
- **Google Sheets exports:** you share your sheet with CleanPull's Google service account (`cleanpull-sheets-1@cleanpull-sheets.iam.gserviceaccount.com`) as **Editor**, so CleanPull's Sheets Sync actor can write to that one sheet (it asks Google only for the Sheets scope). The first export adds a hidden tab, `_cleanpull`, holding only your Apify user ID, so runs from any other Apify account are refused. The share stays until you remove it (Share → that address → Remove access; delete the hidden tab via View → Hidden sheets if you like); a scheduled export stops once it's removed. To share nothing with CleanPull, put your own Google service account key or OAuth credentials in the actor's secret fields in the Apify Console. If your Google Workspace blocks sharing outside your organisation, the share is refused and the export reports no access: ask your admin to allow the address, or use your own credentials.
- **No keys are needed** beyond your Apify sign-in. The only secrets the plugin ever involves are your own delivery settings, when you ask for a channel (email API keys, SMTP passwords, Slack, Discord, Teams or webhook URLs), and those never go through the chat: Claude gives you the task's page in the Apify Console, you paste them into the secret field there, and Apify stores them encrypted.
- **What the results can hold:** public review text (reviewer names are off by default), Amazon brands, eBay seller usernames and Etsy shop names in market scans (a market watchlist keeps eBay sellers only as salted hashes between runs, enough to spot new sellers), and advertisers' public ad data with links to the platforms' libraries. All of it stays in your Apify account.

## Responsible use

- **Public data only.** The actors read what any visitor can see without signing in: product pages, search results, public review widgets and pages, supplier offer pages and the platforms' public ad libraries. Nothing signs in to a personal account.
- **The actors never solve captchas.** A page that still shows one to an actor is reported as not read, with the reason, and not charged.
- **How sites are read.** The actors read public pages the way a browser does. The actors' own code never solves a captcha, never signs in or gets past a paywall, and never uses anyone's account.
  - **Bright Data's Web Unlocker.** Some reads go through the Web Unlocker, a service of Bright Data, a data provider we hold an agreement with, that fetches a page for the actor and handles the site's bot checks (captchas included) on Bright Data's side, under Bright Data's terms. Marketplace Search Scanner uses it for Walmart, eBay, Home Depot and Lowe's search pages, and for Amazon searches refused on every other route. Supplier Price Finder uses it for AliExpress and Alibaba searches, and for Made-in-China pages refused on every other route. Barcode Price Checker uses it for some stores' pages, and Amazon Keyword Rank Tracker for searches Amazon refuses.
  - **Residential addresses** (from Apify's proxy service) are the first choice for some reads, not only a retry: Amazon Keyword Rank Tracker reads US searches with ads, and every marketplace outside the US, through them, and Amazon Product Scraper reads products outside the US through addresses in that country. Elsewhere they are a retry: Any Store Product Monitor uses them only for a store that doesn't answer its standard addresses.
  - **Amazon's browser check.** Where a page runs its own JavaScript check that a normal browser passes automatically, with nothing for a visitor to do (Amazon's browser check on some marketplaces), Amazon Keyword Rank Tracker runs that check in a short-lived browser and sends the cookie it gives with its next requests, until the site asks again: at most one browser check per keyword and up to 5 a run. A visual captcha stops it at once.
  - **Otherwise** a site that refuses is retried through the network of a data provider we hold an agreement with (Apify's proxy service, Bright Data, or, for Google's ads library, ScrapeCreators), or the item is reported as not read.
- **Each site is paced by default.** Store, review, promotion, listing and supplier sites get at most 2 requests at a time (Any Store Product Monitor, Reviews Monitor, Promotions Monitor, Listing Quality Checker, Supplier Price Finder). On Amazon, Amazon Best Sellers Tracker reads 2 categories at a time and Amazon Product Scraper 3 products per marketplace. The ad libraries get one request at a time per platform (Google's 1.5 seconds apart), and the data services' requests are capped and spaced.
- **robots.txt:** Supplier Price Finder reads only addresses each site's robots.txt allows, so **DHgate's search is never read** (only the DHgate pages you give). Any Store Product Monitor reads a store's robots.txt only to find its sitemaps and doesn't apply its Disallow rules: give it product pages you may read.
- **Where the data comes from.** CleanPull's actors read online stores, Amazon, Google, supplier sites and Google's ads library themselves. eBay, Etsy, Walmart, Target and Best Buy data, AliExpress and Alibaba search results and Trustpilot reviews come from Bright Data, a web-data provider we hold an agreement with, under its terms; Meta's and TikTok's ad library data comes from an ad data provider, ScrapeCreators, which also supplies Google ads data on a run where Google's library returns none. CleanPull reads none of the sites those providers cover itself.
- **Addresses:** stores are read from standard addresses; a store that doesn't answer them may be read from residential addresses, billed as an add-on only for that store. A store that can't be read is named in the run summary, not charged.
- **Built for product and business data.** The actors collect product and business data. Reviewer names are off by default, advertisers are businesses, and creatives are linked, not stored. Some personal data can still appear: eBay results carry the seller's username and Etsy results the shop name (a market watchlist keeps eBay usernames only as salted hashes between runs), and review text, written by shoppers, can mention personal details. All of it stays in your Apify account.
- **What MarketMage won't do:** write, buy or post fake reviews; find out who a reviewer, buyer or seller is as a private person; copy a rival's listing text, photos or ads word for word; source or sell replicas of a branded product; or agree prices or split markets with a competitor. Claude declines only that part and offers the version that gets you what you're after. The full list is in the [Acceptable Use Policy](https://marketmage.io/acceptable-use).
- **You are responsible for how you use the results:** respect the sites' terms, copyright in product content and creatives, and the privacy laws that apply to you. Read at a pace and scale those terms allow.
- **Results stay in your Apify account:** datasets, key-value stores, tasks and schedules, under your control.

## Support

Help, setup and billing questions: [marketmage.io/support](https://marketmage.io/support/). Bugs and ideas: open an issue at [github.com/MarketMage/plugin](https://github.com/MarketMage/plugin/issues), and never paste an API token or other secret into it. Actor-specific questions can also go to each actor's Issues tab on its Apify Store page. Security issues: email security@marketmage.io, never a public issue ([SECURITY.md](https://github.com/MarketMage/plugin/blob/main/SECURITY.md)); security reports are acknowledged within one business day.

## License

MarketMage is source-available under the [PolyForm Shield License 1.0.0](LICENSE). In plain words:

- it costs nothing to install, and the license lets you use it for any purpose except a competing one, including in your business (you pay only for the Apify runs you ask for);
- you may change it, make new works from it and share copies, with or without your changes, as long as each copy carries the license terms (or their URL) and the `Required Notice:` line;
- you may not use it to provide a product that competes with MarketMage, or with any other product Extoris LLC or its affiliates provide using it;
- it comes as is, without warranty, as far as the law allows.

The [LICENSE](LICENSE) file is the binding text.

MarketMage is a trademark of Extoris LLC.

Published by Extoris LLC · [Terms](https://marketmage.io/terms/) · [Privacy](https://marketmage.io/privacy/) · [Acceptable Use](https://marketmage.io/acceptable-use)

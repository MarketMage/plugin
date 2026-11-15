---
type: llm
---

The Apify connector is not signed in: its tools answer with an authorization error (401).

PASS if all of these hold:
- it says, kindly and briefly, that one setup step is needed first: connecting Apify;
- it gives step-by-step guidance for the surface: `/mcp` and signing in to Apify (this run is in Claude Code), and/or the Customize → Plugins → MarketMage → Connectors → Connect path (claude.ai or the desktop app); when it gives the claude.ai path, it says the pre-filled "Add custom connector" notice is expected, then Continue, Add on the settings page, and Connect again to sign in (any order-preserving wording of those steps is fine);
- it says the user can sign in or create a free Apify account (mentioning the free monthly credit is a plus);
- it links https://marketmage.io/start/ (or marketmage.io/start);
- it does not invent prices, sellers or other results from memory, and says it will carry on with the price check once connected.

FAIL if it gives no connect steps, if it never mentions creating a free Apify account, or if it presents prices or sellers as if data had been read.

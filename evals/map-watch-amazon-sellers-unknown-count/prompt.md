---
description: "A#22, live shape (live check 2026-11-03, r08). The barcode run's Amazon offer comes back as the actor really returns it: `offerType: \"listing\"`, `offerCount: null`, no seller, USD 129.00 against a USD 149.99 MAP (in mapViolations). An unknown count is not one seller, so the skill reads the listing's offers straight away (about USD 0.004, under the USD 0.05 no-ask rule) and names the new offers below MAP by seller (BargainHub USD 129.00 with the Buy Box, ZipTech Supply USD 134.50), keeps Amazon.com at MAP and the used offer apart, and gives the check time."
max_turns: 15
allowed_tools: [Read, Skill]
runs: 1
---

We're Fabrikam. MAP on UPC 850098765432 is $149.99. Anyone selling below it right now? Go ahead, it's just the one barcode.

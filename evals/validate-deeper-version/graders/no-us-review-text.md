---
type: regex
target: mock_calls
pattern: '"actor":"cleanpull/reviews-monitor","input":\{(?:(?!"verdict")[^\n])*(amazon\.com/dp/B0HIPPK|"amazonMarketplace":"US")'
match: not_contains
---

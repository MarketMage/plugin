---
type: llm
---

The Google Trends rows hold these rising searches (the run's short summary named none of them):
- dog hair dryer: high velocity dog dryer (+250%), dog dryer for grooming (+180%), quiet dog hair dryer (+120%), dog dryer cage, dog dryer with heater;
- dog nail grinder: quiet dog nail grinder (+160%), dog nail grinder with led light (+110%), cordless nail grinder for dogs (+60%);
- deshedding brush: self cleaning deshedding brush (+300%), deshedding brush for golden retriever (+140%);
- dog grooming kit: cordless dog clippers with vacuum (+200%), dog grooming kit for beginners (+90%);
- dog paw cleaner: none (its list is empty).

PASS if all of these hold:
- the ideas table (or its equivalent list) gives rising searches from the data above for the dryer, the nail grinder and the deshedding brush ideas (at least one real rising search each, such as "high velocity dog dryer", "quiet dog nail grinder", "self cleaning deshedding brush"), with no rising search invented that isn't in the list above;
- no idea whose term has rising searches above is described as having none ("none", "none returned", "no rising searches", a dash or a blank in that column);
- if the paw cleaner's rising searches are mentioned, they are said in plain words as none yet ("no rising searches yet" or the like), not as a failure.
FAIL if the answer says rising searches were not returned or not available for the ideas in general, gives "none" for the dryer, nail grinder or deshedding brush, or quotes a rising search that isn't in the data.

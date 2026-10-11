# Data shape: a specimen

Format only, about an unrelated business on purpose: do not reuse its parts, causes or conclusions. Field meanings are in core.md and the mode file. It is a quick, depth-2 diagnosis; the team-only and reply-only keys follow at the end.

```json
{
  "title": "Why some of the bakery's weekend pre-orders are missing at pickup",
  "problem": "Customers pre-order for Saturday pickup and some orders aren't ready. It started about six weeks ago. The owner thinks the Saturday staff mix up the boxes.",
  "restated": "Find which step between the online order and the Saturday counter loses some pre-orders, and what record shows it.",
  "theirTheory": "Are Saturday staff handing baked orders to the wrong customers?",
  "client": "The bakery (the owner is asking)",
  "date": "2026-10-11",
  "builtBy": "solo",
  "summary": [
    "Most likely the orders that go missing are placed after the baking list is printed, but the records have not been checked yet.",
    "Match last Saturday's online orders to that week's baking list, noting each missing order's time.",
    "It depends on whether the list is printed from the order system or copied by hand."
  ],
  "confidence": { "level": "low", "why": "built from two sentences and no records" },
  "restsOn": [
    { "fact": "The baking list is printed once, before the weekend", "basis": "assumed" },
    { "fact": "Missing orders were placed through the online form", "basis": "reported" }
  ],
  "facts": [
    { "fact": "Who: the bakery owner and the Saturday counter staff", "basis": "reported" },
    { "fact": "What: some Saturday pre-orders are not ready at pickup", "basis": "reported" },
    { "fact": "When: for about six weeks", "basis": "reported" },
    { "fact": "How much: number of missing orders per Saturday not given", "basis": "reported" }
  ],
  "walkthrough": [
    { "round": 1, "vantage": "customer", "question": "What happens to an order placed at 9 pm on Friday, after the list is printed?", "answer": "If the list is printed on Thursday (supplied; the owner did not say), a Friday order sits in the order system and nobody sees it until the customer arrives on Saturday. A Saturday-morning print would catch it, and the cut-off explanation would fall away." },
    { "round": 1, "vantage": "customer", "question": "How does a customer who finds nothing at the counter get recorded?", "answer": "Staff probably apologise and refund on the spot (supplied); unless someone writes the name down, the owner's count of missing orders comes from memory, not a record. If a refund log exists, the size of the problem is measurable and the counting explanation weakens." },
    { "round": 1, "vantage": "records", "question": "Who turns the online orders into the baking list, and how?", "answer": "Either the system prints it or someone copies names by hand (both supplied). A hand copy can skip a line and keeps the copying explanation open; a printed list closes it and points at the cut-off or the counter." },
    { "round": 1, "vantage": "records", "question": "Does the order form show a cut-off time to the customer?", "answer": "Most order forms accept orders until someone sets a cut-off (outside; verify: the form tool's help page), so a late Friday order is probably accepted with no warning. If this form refuses late orders, the cut-off explanation is out and the test order is unnecessary." },
    { "round": 1, "vantage": "sceptic", "question": "What else changed about six weeks ago besides the order form?", "answer": "The owner named the form; a new Saturday hire or a busier season would also produce missing orders, and nothing in the request rules them out yet. If nothing else changed, the form and the list stay the only places to look." },
    { "round": 1, "vantage": "sceptic", "question": "Could the orders be ready but handed to the wrong customer?", "answer": "If two customers share a surname (supplied), a box can go to the wrong one; that would show as an order marked collected while the right customer complains. If missing orders are absent from the list altogether, the counter is cleared." },
    { "round": 2, "vantage": "records", "question": "What does the Thursday printing assume, and what if the list is printed Saturday morning?", "answer": "It assumes one print run. A Saturday print would catch Friday orders and would point at copying or pickup instead, so the print time is the first thing to ask." },
    { "round": 2, "vantage": "sceptic", "question": "What would make the order-to-list comparison impossible to run?", "answer": "If last week's list was thrown away, the comparison needs a fresh Saturday. The test order on Friday night works either way and costs one small order, so it is the fallback." }
  ],
  "decompose": {
    "takeaway": "The order has to pass through the form, the list and the counter; the list is where the counts most likely stop matching.",
    "depth": 2,
    "gap": "Some Saturday pre-orders (number not given) are not ready at pickup, for about six weeks, against the expectation that every pre-order is ready.",
    "impact": "unknown; refunds plus customers who stop pre-ordering",
    "detection": "Noticed from customer complaints at the counter; no tally is kept",
    "isItReal": { "verdict": "can't tell yet", "why": "No count of missing orders per Saturday and no baseline from before six weeks ago" },
    "problemType": { "type": "diagnose from data", "why": "The order system and the baking list already hold what is needed; the owner holds both" },
    "changes": [
      { "what": "New online order form", "when": "about six weeks ago", "who": "the owner" }
    ],
    "parts": [
      { "id": "form", "name": "Order form", "question": "Does every order placed reach the order system?", "check": "Compare the payment account with the order list for one week; a paid order with no list entry means the form drops orders", "dependsOn": [] },
      { "id": "list", "name": "Baking list", "question": "Does every order in the system reach the list?", "check": "Compare one week's orders with that week's list, noting each missing order's time", "dependsOn": ["form"],
        "children": [
          { "name": "Cut-off", "question": "When is the list printed, and are later orders caught?", "check": "Ask the owner the print time; place one test order after it on Friday" },
          { "name": "Copying", "question": "Is the list printed from the system or copied by hand?", "check": "Watch the list being made once" }
        ] },
      { "id": "pickup", "name": "Saturday counter", "question": "Does every baked order reach the right customer?", "check": "Match Saturday's handovers to names on the list", "dependsOn": ["list"] },
      { "id": "tally", "name": "Complaints tally", "question": "How are missing orders counted?", "check": "Start a sheet at the counter: name, order time, what happened", "dependsOn": ["pickup"] }
    ],
    "isIsNot": {
      "is": "Saturday pre-orders",
      "isNot": "weekday pre-orders",
      "rows": [
        { "dimension": "When ordered", "is": "unknown", "isNot": "unknown", "distinction": "If Saturday orders are placed later in the week than weekday ones, the cut-off explanation gains; if not, it loses" },
        { "dimension": "How the list is made", "is": "unknown", "isNot": "unknown", "distinction": "A different method on Saturdays (hand copy) points at copying; the same method points away from it" },
        { "dimension": "Who hands over", "is": "Saturday staff", "isNot": "the owner", "distinction": "If only Saturday staff hand over, the pickup explanation stays open; if the owner does too, it weakens" },
        { "dimension": "How missing orders are counted", "is": "complaints from memory", "isNot": "not applicable", "distinction": "If no record exists, the size of the problem is unknown and the counting explanation stays open" }
      ]
    },
    "hypotheses": [
      { "name": "Late orders miss the baking list", "predicts": "Every missing order has an order time after the list was printed; the order system's timestamps show it", "explains": "Missing orders", "doesNotExplain": "Orders on the list but not ready", "contradicts": "none yet", "ruleOut": "Missing orders were placed before the list was printed", "cheapestCheck": "The owner compares last Saturday's orders with the list (needs last week's list; if it was thrown away, do it next Saturday); times after the print point here, times before point elsewhere", "probability": 35, "likelihood": "leading" },
      { "name": "Orders are copied onto the list by hand and some are skipped", "predicts": "Missing orders are spread through the week with no time pattern", "explains": "Random missing orders", "doesNotExplain": "A pattern by day", "contradicts": "none yet", "ruleOut": "The list is printed straight from the order system", "cheapestCheck": "The owner watches the list being made once (no prerequisite); a hand copy keeps this open, a printout closes it", "probability": 20, "likelihood": "possible" },
      { "name": "The counting changed, not the business", "predicts": "The complaints the owner remembers are the same few customers, or began when the form started asking for a pickup time", "explains": "A problem that appeared with the new form", "doesNotExplain": "Refunds actually paid", "contradicts": "none yet", "ruleOut": "The counter sheet shows missing orders on three consecutive Saturdays", "cheapestCheck": "The counter staff keep the tally sheet for three Saturdays (needs the sheet); three empty Saturdays close this, named orders keep it open", "probability": 20, "likelihood": "possible" },
      { "name": "The new form drops paid orders before they reach anyone", "predicts": "Paid orders exist in the payment account but not in the order list", "explains": "Orders the owner never saw", "doesNotExplain": "Orders on the list but not ready", "contradicts": "none yet", "ruleOut": "Every paid order appears in the order list", "cheapestCheck": "The owner matches the payment account to the order list for one week (needs both logins); a paid order with no entry keeps this open, a full match closes it", "probability": 15, "likelihood": "possible", "danger": true },
      { "name": "The owner's theory: baked orders are handed to the wrong customer", "predicts": "Missing orders are on the list and marked collected", "explains": "Customers finding nothing at pickup", "doesNotExplain": "Orders missing from the list", "contradicts": "none yet", "ruleOut": "Every missing order is also missing from the list", "cheapestCheck": "Saturday staff match handovers to names on the list (needs the list at the counter); a collected mark with a complaint keeps this open", "probability": 10, "likelihood": "unlikely" }
    ],
    "contributingFactors": ["A printed list and a late order only lose the order together; either alone is harmless"]
  },
  "unknownUnknowns": [
    { "area": "Card payments that settle after the order", "whyItMatters": "If the list only shows paid orders, a slow payment can hide a real order until Saturday", "howToFind": "Ask the form tool's support whether unpaid orders appear in the order list (verify: the tool's help page)" },
    { "area": "The form's time zone", "whyItMatters": "A form set to another time zone can stamp a Friday order as Saturday and sort it off the list", "howToFind": "Place one test order and compare its stamped time with the clock" },
    { "area": "Hand-written Saturday additions", "whyItMatters": "Orders taken by phone on Saturday morning may never enter the system or the count", "howToFind": "Ask the counter staff whether they take phone orders and where they write them" }
  ],
  "abstract": {
    "takeaway": "Watch the handoff into the list, not the form's design.",
    "stepBack": { "measure": "Complaints at the counter", "goal": "Every pre-order ready for the right customer on Saturday", "gap": "Fewer complaints would also follow from customers giving up on pre-ordering" },
    "mattersNow": [
      { "item": "When the list is printed", "why": "It decides whether a late order can ever be baked", "lookAt": "The owner's answer, then one Friday-night test order" },
      { "item": "How the list is made", "why": "A hand copy and a printout fail in different ways", "lookAt": "One watched list-making" }
    ],
    "setAside": [
      { "item": "The form's design and wording", "why": "Nothing yet shows the form is at fault; it comes back if paid orders are missing from the list" }
    ]
  },
  "reuse": {
    "takeaway": "The order-to-list comparison is a weekly check worth keeping.",
    "steps": [
      { "step": "Compare orders with the list", "repeatsWhere": "Every Saturday for this bakery", "makeSkill": true, "why": "A five-minute check that catches the problem before the customer does" },
      { "step": "Watch the list being made", "repeatsWhere": "Once", "makeSkill": false, "why": "One observation settles it" }
    ]
  },
  "parallelize": {
    "takeaway": "Two checks now, one decision, then one fix.",
    "streams": [
      { "id": "s1", "name": "Compare orders with the list", "brief": "Last Saturday's online orders against that week's baking list; note each missing order's time", "who": "you", "kind": "check", "door": "reversible", "returns": "A list of missing orders with order times", "waitsFor": [] },
      { "id": "s2", "name": "Test the cut-off", "brief": "Place one small order after the list is printed (cost: one order) and see whether it is ready on Saturday", "who": "you", "kind": "check", "door": "reversible", "returns": "Yes or no: a late order gets baked", "waitsFor": [] },
      { "id": "s3", "name": "Decide which explanation the records support", "brief": "Put s1's times and s2's result side by side and pick the explanation they support", "who": "you", "kind": "decide", "door": "reversible", "returns": "The explanation to fix", "waitsFor": ["s1", "s2"] },
      { "id": "s4", "name": "Fix the handoff", "brief": "Only the part s3 picked: a second print on Saturday morning, or a printed list instead of a hand copy, plus the cut-off shown to customers on the form (one-way: customers see it)", "who": "you", "kind": "fix", "door": "one-way", "returns": "Two clean Saturdays", "waitsFor": ["s3"], "failsIf": "Nobody remembers the second print on a busy Saturday; guard: set the system to print it automatically" }
    ]
  },
  "rubric": {
    "takeaway": "No agreed target yet; the counter sheet makes the first one measurable.",
    "criteria": [
      { "criterion": "Every pre-order is ready at pickup", "source": "Preference, no source", "pass": "Zero missing orders on the counter sheet for three Saturdays", "fail": "Any missing order", "measure": "The counter sheet", "status": "unknown" },
      { "criterion": "Orders after the cut-off are refused or flagged", "source": "The form tool's help page (verify: the cut-off setting)", "pass": "A Friday-night test order is refused or flagged", "fail": "It is accepted silently", "measure": "One test order", "status": "unknown" },
      { "criterion": "Every paid order appears in the order list", "source": "Preference, no source (measured from the owner's own records; nobody agreed the target)", "pass": "Full match for one week", "fail": "Any paid order with no list entry", "measure": "Weekly match", "status": "unknown" }
    ]
  },
  "evaluate": {
    "takeaway": "The counter sheet is the one number that says whether the problem is gone.",
    "tests": [
      { "test": "Missing orders per Saturday", "how": "The counter sheet", "expect": "Zero for three Saturdays after the fix; a mixed result means the fix hit one cause of two", "when": "Every Saturday; readable after three", "signal": true },
      { "test": "Late order gets baked", "how": "One Friday-night test order", "expect": "Ready on Saturday after the fix", "when": "The Saturday after the fix" }
    ],
    "itDepends": [
      { "condition": "The list is printed from the order system", "ifTrue": "Add a second print on Saturday morning", "ifFalse": "Print it from the system instead of copying" }
    ]
  },
  "assumptions": [
    { "assumption": "The owner, not an agency, is asking; 'you' in the streams is the owner", "ifWrong": "Stream owners change to client and client's staff" },
    { "assumption": "The baking list is printed once, before the weekend", "ifWrong": "The cut-off explanation falls away and copying or pickup lead" },
    { "assumption": "Region not stated; no region-dependent rule was used", "ifWrong": "Nothing in the map moves" }
  ],
  "openQuestions": [
    { "question": "Which day and time is the baking list printed?", "whoCanAnswer": "you", "ourGuess": "Thursday night", "changesWhat": "Whether the cut-off explanation stays in the lead" },
    { "question": "Is the list printed from the system or copied by hand?", "whoCanAnswer": "you", "ourGuess": "Printed", "changesWhat": "Whether the copying explanation stays open" },
    { "question": "Do Saturday staff take phone orders?", "whoCanAnswer": "the Saturday staff", "ourGuess": "Yes, a few", "changesWhat": "Whether a part is missing from the path" }
  ],
  "nextAction": { "action": "Match last Saturday's online orders to that week's baking list, noting each missing order's time; meanwhile ask the staff to start the counter sheet", "owner": "you", "by": "Today", "rulesOut": "Order times after the print rule out copying and pickup for those orders; times before rule out the cut-off" },
  "factChecks": [
    { "fact": "Most order forms accept orders until a cut-off is set", "result": "unchecked", "note": "Depends on the form tool; the Friday test order settles it" },
    { "fact": "Unpaid orders may not appear in the order list", "result": "unchecked", "note": "Depends on the form tool; its help page or support settles it" }
  ],
  "coverageTest": {
    "fitsNoPart": "An order taken by phone on Saturday morning fitted no part; fixed by adding phone orders to the baking list part's check",
    "fitsTwoParts": "An order on the list but baked for the wrong day fitted both the list and the counter; fixed by giving the list the day printed and the counter only what is in the box",
    "fixed": true
  }
}
```

Team-only keys (team.md) and reply-only keys (reply.md), shown on their own:

```json
{
  "builtBy": "team",
  "judgedBy": "Codex, default model",
  "review": [ { "finding": "Two explanations share the same rule-out", "field": "decompose.hypotheses", "fixed": true, "note": "Merged into one" } ],
  "revisions": [ { "date": "2026-10-18", "changed": "The list history ruled out copying; late orders lead" } ],
  "decompose": { "hypotheses": [ { "name": "...", "status": "ruled out", "evidence": "The list is printed from the system (owner's screenshot)", "probability": 0, "likelihood": "unlikely" } ] }
}
```

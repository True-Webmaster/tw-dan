# Data shape: worked example

This example is about an unrelated business on purpose. It shows the format only: do not reuse its parts, causes or conclusions. Work out your own from the problem in front of you. Field meanings are in method.md.

```json
{
  "title": "Why some of the bakery's weekend pre-orders are missing at pickup",
  "problem": "Customers order online for Saturday pickup, but some orders are missing or not ready when they come in. I think the Saturday staff are losing them.",
  "restated": "About one weekend pre-order in ten is not there when the customer comes to collect it, and the owner does not know where it goes missing.",
  "theirTheory": "Are the Saturday staff losing the orders?",
  "client": "Neighbourhood bakery, one shop",
  "date": "2026-10-10",
  "builtBy": "solo",
  "summary": [
    "Most likely, orders placed after Thursday don't reach the Friday baking list.",
    "Compare last Saturday's online orders with the baking list before changing anything.",
    "It depends on whether the website and the baking list are connected or copied by hand."
  ],
  "confidence": {
    "level": "low",
    "why": "Built from the owner's description; no order records seen yet."
  },
  "restsOn": [
    {
      "fact": "The baking list is printed once, on Thursday night",
      "basis": "reported"
    },
    {
      "fact": "Missing orders are mostly placed on Friday",
      "basis": "assumed"
    }
  ],
  "facts": [
    {
      "fact": "Who: online pre-order customers collecting on Saturday",
      "basis": "reported"
    },
    {
      "fact": "What: an order is missing or not ready at pickup",
      "basis": "reported"
    },
    {
      "fact": "When it started: not stated",
      "basis": "assumed"
    },
    {
      "fact": "Where: one shop, the Saturday counter",
      "basis": "reported"
    },
    {
      "fact": "How much: about 40 pre-orders a week, about 1 in 10 missing or not ready (so about 4 a week); walk-in sales unaffected",
      "basis": "reported"
    },
    {
      "fact": "How long: the owner says 'a few weeks'",
      "basis": "reported"
    }
  ],
  "walkthrough": [
    {
      "round": 1,
      "question": "What does a Friday-night order look like from the customer's side, minute by minute, after they press pay?",
      "answer": "If the form works like most, they get a payment confirmation and a thank-you page; nothing tells them whether the shop has seen it (I am supplying that detail; the test order will show it). They would assume Saturday is fine because the site let them choose it.",
      "vantage": "self"
    },
    {
      "round": 1,
      "question": "Who prints the baking list on Thursday night, from what, and what happens to an order that arrives at 9 pm Friday?",
      "answer": "The owner says she prints it from the order dashboard at about 8 pm Thursday and bakes from paper; that is reported, not seen. A Friday order sits in the dashboard with nobody looking; it only exists if someone refreshes the screen before baking starts at 4 am.",
      "vantage": "self"
    },
    {
      "round": 1,
      "question": "What does the Saturday counter person have in front of them when a customer says 'I ordered online'?",
      "answer": "If the counter works from the printed list and a box of bagged orders with names on them (supplied; confirm on Saturday), a name that is not on the list sends them to the dashboard on the shop tablet, where they find the order and have nothing to hand over. If instead they work from the screen, a missing bag would be the clue, not a missing name.",
      "vantage": "self"
    },
    {
      "round": 1,
      "question": "Which orders pass through this path but are not weekend pre-orders: test orders, cancelled orders, orders for Sunday?",
      "answer": "If the form takes any date (supplied; the test order will show it), Sunday and weekday orders are mixed into the same dashboard; a Thursday print filtered by 'Saturday' could miss an order with a mistyped date, and a cancelled order might still be baked. If the form only offers Saturday, this whole line falls away.",
      "vantage": "self"
    },
    {
      "round": 1,
      "question": "What does the order dashboard show that the printed list cannot, and the reverse?",
      "answer": "The dashboard shows order time, payment status and any later edits; the paper shows only name, items and pickup day. A customer who edited an order Friday morning appears correct on screen and wrong on paper.",
      "vantage": "self"
    },
    {
      "round": 1,
      "question": "If I stood in the bakery at 4 am Saturday for an hour, what would I notice about how the list is used?",
      "answer": "Whether anyone looks at the dashboard at all, whether the list is annotated by hand, and whether orders are bagged and labelled as they come out or in one batch at the end, where names get swapped. Each of those would point at a different part.",
      "vantage": "self"
    },
    {
      "round": 2,
      "question": "Does the form actually accept orders after the Thursday print, and what does it promise the customer when it does?",
      "answer": "Unknown; the test order on Friday morning settles it. If it accepts and confirms, every late order is lost by design and the fix is a cut-off, not a person.",
      "vantage": "self"
    },
    {
      "round": 2,
      "question": "How many of last Saturday's missing orders were placed after 8 pm Thursday?",
      "answer": "Unknown until the order times are read against the print time; if most were, the cut-off explanation leads on its own, and if none were, copying or bagging leads.",
      "vantage": "self"
    }
  ],
  "decompose": {
    "depth": 3,
    "gap": "About 1 in 10 weekend pre-orders (about 4 of 40 a week) is missing or not ready at pickup; the owner expects none.",
    "isItReal": {
      "verdict": "can't tell yet",
      "why": "No count of missing orders by week has been kept; 4 of 40 could be one bad weekend. Compare the last 12 Saturdays."
    },
    "impact": "About 4 refunds a week plus the customers who don't come back; unknown in money terms.",
    "detection": "Customers complain at the counter; nobody counts them.",
    "problemType": {
      "type": "diagnose from data",
      "why": "Orders, the baking list and pickups are all recorded; the owner holds all three."
    },
    "changes": [
      {
        "what": "New online order form",
        "when": "about two months ago",
        "who": "web designer"
      },
      {
        "what": "Saturday staff changed",
        "when": "unknown",
        "who": "owner"
      }
    ],
    "takeaway": "The gap is probably between the order form and the baking list, not in the baking.",
    "isIsNot": {
      "is": "Pre-orders missing at pickup",
      "isNot": "Pre-orders ready at pickup",
      "rows": [
        {
          "dimension": "When ordered",
          "is": "Unknown: check order times",
          "isNot": "Unknown: check order times",
          "distinction": "If missing orders cluster late in the week, the cut-off is involved; if they are spread evenly, it is the copying or the handover."
        },
        {
          "dimension": "What was ordered",
          "is": "Unknown",
          "isNot": "Unknown",
          "distinction": "If special items dominate, they may need a separate list; if the mix matches, the item is not the cause."
        }
      ]
    },
    "hypotheses": [
      {
        "name": "Late orders miss the baking list",
        "predicts": "Every missing order has an order time after the list was printed",
        "explains": "Missing orders",
        "doesNotExplain": "Orders that are on the list but not ready",
        "ruleOut": "Missing orders were placed before the list was made",
        "cheapestCheck": "Compare order times with when the list was printed",
        "likelihood": "leading",
        "probability": 50
      },
      {
        "name": "Orders are copied onto the list by hand and some are skipped",
        "predicts": "Missing orders are spread across the week with no time pattern",
        "explains": "Random missing orders",
        "doesNotExplain": "A pattern by day or item",
        "ruleOut": "The list is printed straight from the order system",
        "cheapestCheck": "Watch the list being made once",
        "likelihood": "possible",
        "probability": 25
      },
      {
        "name": "The new form drops orders before they reach anyone",
        "predicts": "Paid orders exist in the payment account but not in the order list",
        "explains": "Orders the owner never saw",
        "doesNotExplain": "Orders that are on the list but not ready",
        "ruleOut": "Every paid order appears in the order list",
        "cheapestCheck": "Match the payment account to the order list for one week",
        "likelihood": "possible",
        "probability": 20,
        "danger": true
      },
      {
        "name": "The owner's theory: orders are baked but the Saturday staff hand them to the wrong customer",
        "predicts": "Missing orders are on the list and were baked",
        "explains": "Customers finding nothing at pickup",
        "doesNotExplain": "Orders missing from the list",
        "ruleOut": "Every missing order is also missing from the list",
        "cheapestCheck": "Match Saturday's pickups to names",
        "likelihood": "unlikely",
        "probability": 5
      }
    ],
    "contributingFactors": [
      "An order form with no cut-off",
      "A list made once, on Thursday night"
    ],
    "parts": [
      {
        "id": "form",
        "name": "Order form",
        "question": "What can customers order, and until when?",
        "check": "Place a test order on Friday morning; write down whether it is accepted and what confirmation arrives",
        "dependsOn": []
      },
      {
        "id": "list",
        "name": "Baking list",
        "question": "How do orders become Friday's list?",
        "check": "Ask who builds the list and how; get last week's printed list",
        "dependsOn": [
          "form"
        ],
        "children": [
          {
            "name": "Cut-off time",
            "question": "Which orders make the list?",
            "check": "Compare order times with the list's print time",
            "children": [
              {
                "name": "Late orders",
                "question": "What happens to orders after the cut-off?",
                "check": "Find last week's orders placed after the print time"
              }
            ]
          },
          {
            "name": "Copying",
            "question": "Is the list typed up by hand?",
            "check": "Watch it being made once"
          }
        ]
      },
      {
        "id": "pickup",
        "name": "Pickup",
        "question": "How are orders matched to customers?",
        "check": "Stand at the counter on Saturday; count orders not found",
        "dependsOn": [
          "list"
        ]
      }
    ]
  },
  "unknownUnknowns": [
    {
      "area": "The order form may not enforce the cut-off",
      "whyItMatters": "If it still accepts orders after the list is printed, those orders are lost by design.",
      "howToFind": "Place a test order on Friday morning and see if it is accepted."
    },
    {
      "area": "Card payments can settle after the order is placed",
      "whyItMatters": "An order that shows 'pending' on Thursday night may be skipped as unpaid and then settle on Friday.",
      "howToFind": "Ask the payment provider how long settlement takes; look at one pending order's timestamps."
    },
    {
      "area": "The dashboard's 'Saturday' filter depends on the date the customer typed",
      "whyItMatters": "A customer who picks the wrong date is invisible to a filtered print.",
      "howToFind": "Print the list unfiltered once and compare it with the filtered one."
    }
  ],
  "abstract": {
    "takeaway": "For this question, only the path from an order to the baking list matters.",
    "stepBack": {
      "measure": "Orders taken online",
      "goal": "Orders handed over ready, on time",
      "gap": "The form counts an order as done when it is paid, before anyone has baked it."
    },
    "mattersNow": [
      {
        "item": "How orders reach the baking list",
        "why": "Every missing order passes through this step.",
        "lookAt": "Last Saturday's orders next to that week's printed list"
      }
    ],
    "setAside": [
      {
        "item": "Redesigning the website",
        "why": "Nothing yet shows the form is at fault; the handoff after it is the cheaper place to look first. The Friday test order brings this back if it fails."
      }
    ]
  },
  "reuse": {
    "takeaway": "The order-to-list check is worth saving; it applies every week.",
    "steps": [
      {
        "step": "Weekly order reconciliation",
        "repeatsWhere": "Every weekend, same shop",
        "makeSkill": true,
        "why": "Same comparison every week."
      }
    ]
  },
  "parallelize": {
    "takeaway": "Two checks can start today; the fix waits for both.",
    "streams": [
      {
        "id": "s1",
        "name": "Compare orders with the list",
        "brief": "Match last Saturday's online orders to the baking list; note the order time of each missing one.",
        "waitsFor": [],
        "who": "you",
        "kind": "check",
        "door": "reversible",
        "returns": "Count of missing orders and their order times"
      },
      {
        "id": "s2",
        "name": "Test the cut-off",
        "brief": "Place one late test order on Friday (about the cost of one loaf) and see whether it is accepted and where it appears.",
        "waitsFor": [],
        "who": "you",
        "kind": "check",
        "door": "reversible",
        "returns": "Accepted yes/no, and the confirmation received"
      },
      {
        "id": "s3",
        "name": "Fix the handoff",
        "brief": "Using s1's order times and s2's result, change how orders reach the list.",
        "waitsFor": [
          "s1",
          "s2"
        ],
        "who": "client",
        "kind": "fix",
        "door": "one-way",
        "returns": "Two clean Saturdays",
        "failsIf": "The fix is a reminder to check the form, which gets forgotten; guard: print the list from the order system instead."
      }
    ]
  },
  "rubric": {
    "takeaway": "Success is every paid order ready at pickup.",
    "criteria": [
      {
        "criterion": "Every paid order appears on the baking list",
        "source": "Preference, no source (the order records give the count; nobody has agreed the target)",
        "pass": "All orders matched",
        "fail": "Any order missing",
        "measure": "Weekly comparison",
        "status": "unknown"
      },
      {
        "criterion": "Orders ready within 5 minutes of the pickup time",
        "source": "Preference, no source",
        "pass": "All ready",
        "fail": "Any late",
        "measure": "Saturday counter log",
        "status": "unknown"
      },
      {
        "criterion": "A late order gets a reply within an hour saying whether it can be made",
        "source": "Preference, no source",
        "pass": "Every late order answered",
        "fail": "Any late order left unanswered",
        "measure": "Order dashboard timestamps against reply times",
        "status": "unknown"
      }
    ]
  },
  "evaluate": {
    "takeaway": "Run the comparison again after the next two weekends.",
    "tests": [
      {
        "test": "Order-to-list comparison",
        "how": "Match orders to the list",
        "expect": "If the cut-off is the cause, no order placed before Thursday night is missing",
        "when": "Every Monday, for the previous weekend, for three weekends before judging",
        "signal": true
      },
      {
        "test": "Friday test order",
        "how": "Place one order on Friday morning",
        "expect": "Accepted, and absent from the printed list",
        "when": "Once, this week"
      }
    ],
    "itDepends": [
      {
        "condition": "The list is copied by hand",
        "ifTrue": "Print it straight from the order system.",
        "ifFalse": "Look at the cut-off time next."
      }
    ]
  },
  "assumptions": [
    {
      "assumption": "The owner, not an agency, is asking; 'you' in the streams is the owner",
      "ifWrong": "Streams owned by 'you' move to 'client'."
    },
    {
      "assumption": "Orders are paid online at the time of ordering",
      "ifWrong": "Unpaid orders may be dropped on purpose; add that as an explanation."
    }
  ],
  "openQuestions": [
    {
      "question": "Who builds the baking list, and when?",
      "whoCanAnswer": "The owner",
      "ourGuess": "The owner, Thursday night, printed from the dashboard",
      "changesWhat": "Which of the two leading explanations to check first"
    },
    {
      "question": "Does the order form accept a Saturday order on Friday?",
      "whoCanAnswer": "The owner, or a test order",
      "ourGuess": "Yes, with no warning",
      "changesWhat": "Whether the fix is a cut-off or a person"
    },
    {
      "question": "Are the missing orders paid, and when did the payment settle?",
      "whoCanAnswer": "The owner's payment provider",
      "ourGuess": "Paid, settled within minutes",
      "changesWhat": "Whether 'unpaid' is a reason an order was skipped"
    }
  ],
  "factChecks": [
    {
      "fact": "Online order forms usually have no cut-off unless one is set",
      "result": "held",
      "note": "Depends on the form tool; the Friday test order settles it."
    }
  ],
  "coverageTest": {
    "fitsNoPart": "The customer ordered from the wrong shop's website; fixed by adding 'which shop the order is for' to the order form's check, so a stray order is caught before the list.",
    "fitsTwoParts": "An order that is on the list but baked for the wrong day fitted both the list and pickup; fixed by giving the list part the day the order is printed under, and pickup only what is in the box on Saturday.",
    "fixed": true
  },
  "nextAction": {
    "action": "Match last Saturday's online orders to that week's baking list, noting each missing order's time.",
    "owner": "you",
    "by": "Tomorrow",
    "rulesOut": "Separates the cut-off explanation from copying and pickup in one pass."
  }
}
```

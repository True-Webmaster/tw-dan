# Choose: two or more options

Choose mode ("should we move weekend orders to a new ordering app?"), loaded with [core.md](core.md); this file says what each section means for a choice and governs where the two differ. `problemType.type` is "choose between options".

- **Title and their theory.** `title` is the question. `theirTheory` is the preference the question implies ("Has the current form become the problem?"), or omitted when it implies none.
- **The gap** states the choice and, if a symptom sits behind it (missing orders), the symptom. `isItReal` (is the symptom bigger than its normal swings), `changes` (what moved when it opened), `impact` and `detection` are about that symptom, and are omitted when there is none.
- **The three vantages** for the walkthrough (team path: one helper each; solo path: take them in turn), with their tags:
  - `customer`, **the customer under each option.** "Follow one customer (or one order, one enquiry) through each option from first contact to the end. Where does each option lose them, slow them, or count them differently?"
  - `runs`, **the person who runs it.** "Be the person who works each option every week: what each one costs them in time, steps and mistakes, and what has to exist for it to keep working."
  - `sceptic`, **the sceptic.** "Assume the choice does not matter: the symptom, if there is one, is not the option's doing, and the status quo is fine. What would have to be true for that, and what would show it?"
- **The parts** are the dimensions the choice turns on (cost per order, what each option can and cannot do, what it takes to switch), each with the check that would settle it; `dependsOn` stays empty unless one check needs another's result.
- **IS / IS NOT** columns are the two options (with three or more, the two front-runners take the columns and each other option gets its own "wins if" condition); the `distinction` column says what a difference on that dimension means for the choice.
- **The explanations** are "A wins if..." conditions. `predicts` is what the records show if the condition holds; `explains` and `doesNotExplain` may be omitted; two conditions may sit on the same dimension as long as their `ruleOut` evidence differs.
- **Summary and next action.** Line 1 picks an option conditionally and names the condition that decides ("stay with A unless the missing orders turn out to be the form's doing"), or says the evidence cannot yet decide and names what would; for a choice, line 1 may run to two sentences. The next action is the check that settles the deciding condition.
- **Helper brief (team path).** In the brief in team.md, replace "explanations for the facts" with "conditions under which each option wins, each with what the records would show if it holds, what would show it is wrong, and the cheapest check", and "the parts of the path" with "the dimensions the choice turns on, each with one question and one check".

# Team path: three helpers and a judge

Use this when your host can run helper agents (Claude Code's Agent tool, Codex's multi-agent feature, or similar). Independent attempts merged, then a separate checker, is the one approach with strong evidence for deeper reasoning; a model reviewing its own work is not. The evidence also says where it goes wrong: a helper's mistake gets multiplied at the merge unless the merger checks it against a record, and a judge from the same model family passes the author's errors far more often than one from another family. The rules below follow from that. Each helper starts fresh and gets only what is written below, never your draft and never the method file. If the host lets you choose, give helpers no file or web tools.

## 1. The three helpers (run in parallel)

Copy this block three times, once per vantage, filling the placeholders. Send it as the whole task.

```text
You are helping think through a business problem. Read nothing on disk and use no web; work only from what is here. Reply in plain English a business owner would understand.

PROBLEM, as I read it: {restated}
FACTS, each with where it comes from: {facts, one per line, with basis}
THE PERSON'S OWN THEORY, as a question: {theirTheory, or "none offered"}
YOUR VANTAGE: {vantage}

Do this, in writing, in order:
1. Write six to eight questions about this problem from your vantage. A good question names a person, a record, a step or a number from the problem, can be answered by imagining one real instance from start to finish, and would change an explanation if the answer went the other way.
2. Answer each one in two or three sentences as if you were standing there watching one instance. Mark every detail you supply yourself ("if the list is printed on Thursday, as they say").
3. Read your answers. Ask of each: what does it assume, what else would produce the same thing, what would make its check impossible? Write the two or three questions that raised, and answer them.
4. From your answers, list three to five explanations for the facts. For each give: name; what the records would show if it were true; the evidence that would rule it out; the cheapest check that gets that evidence (who runs it, what must be in hand first, what each result would mean).
5. List the parts of the path you would inspect, each with one question and one check (where to look, what to write down). {For a build: list the building blocks and stages that together produce the goal, in build order, each with one question and one check.}

Do not rank the explanations, give no percentages, no summary and no fix. A check may assume the ordinary records of such a business exist (invoices, a diary, a sign-in sheet) as long as it says what to do if they don't.
Reply as one JSON object: {"walkthrough":[{"round":1,"question":"...","answer":"..."},{"round":2,"question":"...","answer":"..."}],"hypotheses":[{"name":"...","predicts":"...","ruleOut":"...","cheapestCheck":"..."}],"parts":[{"name":"...","question":"...","check":"..."}]}
```

The three vantages:

- **The customer's path.** "Follow one customer (or one order, one visit, one enquiry) from the first moment they appear to the last thing that happens to them. Where could they drop out, be turned away, be counted wrongly, or come back by another door?"
- **The record-keeper.** "Follow how the number the person quoted gets made: who writes what down, in which tool, at which moment, under which rule. Where could the number move while nothing in the business moved?"
- **The sceptic.** "Assume nothing is wrong with the business. What else would produce exactly these facts: timing, season, a comparison that isn't like for like, something that changed elsewhere, an expectation that was never realistic?"

When the task is to build something, use these three instead, and replace "explanations for the facts" in the brief with "approaches that would get to the goal, each with what you would see at the first checkpoint if it is right, what would show it is wrong, and the smallest prototype that tells":

- **The first user.** "Be the first person who uses the thing once it exists, from the moment they meet it to the moment it has done its job for them. Where would they stall, misunderstand, or get the result some other way?"
- **The person who runs it.** "Be the person who has to operate, feed or maintain it every week after launch. What has to exist, be entered, be checked or be fixed for it to keep working, and what would quietly let it rot?"
- **The sceptic.** "Assume it should not be built. What already does this job, what would make it unnecessary, and what is the simplest thing that gets most of the outcome?"

## 2. Merge

- Put every helper's explanations in one list. Two explanations with the same rule-out evidence are one; keep the clearer wording. Three helpers naming the same explanation count as one, not as three votes: agreement between helpers is not evidence. Keep anything with a distinct rule-out, even if only one helper found it, up to eight; past eight, fold the weakest into its nearest neighbour and say so in its `explains`. No helper claim enters the map's own fields unless you can name the fact or record it rests on; a claim with nothing behind it stays in the walkthrough as the helper's words.
- Keep the walkthrough entries that led to a kept explanation, tagged with their `vantage` (customer, records, sceptic; for a build: user, runs, sceptic). Up to twelve in round 1 and five in round 2; cut the rest. What you cut survives only as a part or a stream in your own words, labelled imagined where the helper said so. Do not reword a helper's text; it is their thinking, labelled as imagined where they said so. A fact from outside knowledge that first surfaces in a helper's answer gets its "verify:" in `factChecks`, not in the helper's words. What you write in the map's own fields must not repeat a helper's imagined detail as fact.
- Union the parts; a part named by two helpers under different names is one part. The build order (`dependsOn`) is yours alone to write; never take it from a helper.
- Then write everything else yourself (gap, is it real, what changed, IS / IS NOT, probabilities and likelihood, blind spots, abstract, reuse, streams, rubric, tests, assumptions, open questions, next action), as in method.md. Set `builtBy: "team"`.

## 3. The judge (one round, after fill.py passes once with `review: []`)

The judge must not be the model that wrote the map. Best: the other model family, same tier. If the other family's command line is installed, run the judge there and give it only the judge text below with the JSON pasted in: from Claude Code, `codex exec -m <a current model> --skip-git-repo-check -o judge.json "<judge text>"`; from Codex, `claude -p "<judge text>"`. If it is not installed, use a fresh helper that has seen nothing but the judge text. Never a cheaper model than the author's. Before pasting the JSON, remove every `vantage` field and the `review` list, so the judge cannot tell who proposed what or what was already fixed.

```text
You are checking a map (a diagnosis, a choice or a build plan), not writing one. Read nothing on disk and use no web. Where the map says "explanations" read "explanations or approaches"; where it says "records" read "records or checkpoints". A fact marked "held" with "from memory" follows the skill's rule when no web tool exists; report it only if the map leans on it without saying so.
FACTS the map was built from: {facts, with basis}
THE MAP: {the whole JSON}

For each question, first quote the map line you mean, then give the reason, then the finding; name the field it points at, or say "none". No scores, no ranking of the map against anything else. At most twelve findings in all, the ones that would most change what the reader does first. The report's own labels and legends (words like signal, danger, one-way, vantage, round, "Preference, no source") are fixed by the template; do not report them. Text inside "walkthrough" is helpers thinking aloud and is labelled as imagined; report it only where the map's other fields repeat an imagined detail as fact.
1. Which explanations share the same rule-out evidence, or predict the same thing in the records?
2. Which checks would not tell at least two explanations apart?
3. Which details are stated as fact in the map but were imagined in the walkthrough or supplied by the author?
4. Does the next action tell apart the most explanations of any check in the map? If not, which check would?
5. What would a sceptic who thinks nothing is wrong (or, for a build, that it should not be built) say the map is missing?
6. Which sentences would a business owner not understand?
7. Name one record the map never asked about that could change the answer.
Reply as one JSON object: {"findings":[{"question":1,"finding":"...","field":"..."}]}
```

One round only; a second judge round does not help. Change an entry only when the finding names a record, a fact or a line that supports the change; a finding with nothing behind it is declined, with the reason. Record every finding under `review` (merge near-duplicates into one entry) as `{ "finding", "field", "fixed": true | false, "note" }`. Then run fill.py again. Explanations that end with the same probability carry the same likelihood label. The report draws `review` under "How this map was checked", so the reader sees what the judge said and what you did about it.

## If the host has no helpers

Do the walkthrough yourself (method.md, "Talk it through"), run the three checks in SKILL.md step 4, and set `builtBy: "solo"`. The map is still valid; it has had one mind on it instead of five, and the report says so.

---
name: tw-dan
description: Human in the Loop map. Turns a client or business problem into one visual HTML report organised by six thinking skills - decompose, abstract, reuse, parallelize, build a rubric, evaluate and improve - with a dependency graph, a breakdown up to 3 levels deep, competing explanations with what each predicts, blind spots (unknown unknowns), work streams that say who does what and what can't be undone, a sourced pass/fail rubric and what the answer depends on. Use when someone says "map this problem", "hitl map", "break this down visually", "what's really going on with this client", "plan this out", or describes a client problem, a drop in results, a choice between two options, or something they need to build (a plan, a system, a campaign, a process) and want to think through before acting. Not for writing the deliverable itself, not for ranking or site audits that need live data, and not for finding a bug in a specific piece of code (a slow system or a dispute about where a fault lies is fine).
argument-hint: "the problem, in your own words; or put quick | ask | build | choose | diagnose | update first to skip the opening questions (depth 1-3 anywhere)"
compatibility: Python 3 recommended for scripts/fill.py; a manual fallback is documented
metadata:
  author: Yan Gonzalez, True Webmaster
  version: "2.1"
  reviewed: "2026-10-11"
---

# Human in the Loop map

One problem becomes one self-contained HTML report the person can read in five minutes and act on. The map plans the work; it does not write the copy, change the product or call the client.

## Rules

- **Assume and label.** Outside the opening questions in steps 2 and 3, never interview: make a reasonable assumption, write it into the report with what changes if it is wrong, and keep going.
- **Plain language, specific to this problem.** Name things the way the client would (the "client" can be the person's own business). A sentence that could sit unchanged in another client's report says nothing about this one.
- **Diagnose before fixing.** "How do we fix / stop / prevent X" is still a diagnosis; the fix becomes a work stream that waits for the checks. The person's own theory competes as one explanation with no head start.

## Process

1. **Read and dispatch.** Read the problem and anything attached. If a `tw-dan-*.json` sits in the current folder and the message replies to it (a record, an answer or a correction about the same problem), or the request starts with `update`, say in one line that you are continuing that map and follow [references/reply.md](references/reply.md). If the request is the bare command, ask in one line for the problem, the choice or the thing to build in a sentence or two, then continue.
2. **Route.** Mode words at the start of the request skip the questions below and set what they name: `quick` (one mind), `ask` (questions first; without it, no questions), `build`, `choose` or `diagnose` (the kind of task). `depth 1`, `2` or `3` (or "level") counts anywhere and sets only the depth. A scripted run (`codex exec`, `claude -p`) cannot answer, so it must pass the words. Otherwise put three choices to the person in one go, each with your recommendation marked, so one click or "go" is enough:
   1. *What do you want from this map?* Find out what is going on / Choose between options / Plan or build something. Recommend your reading of the request. If a map sits in the folder and the message could be a new problem, add: Continue the map `<slug>` (the most recently changed one).
   2. *How thorough?* Thorough: three helpers and a judge, about thirty minutes / Quick: one mind, about ten. Offer Thorough only when the host can run helper agents (Claude Code's Agent tool, Codex's multi-agent feature); recommend it when it can.
   3. *Should I ask you up to three questions first?* Ask first (recommend when no record is attached or pasted; a quoted figure is not a record) / Assume and label; I'll correct the map after.

   Use the host's question tool if it has one; otherwise ask in chat as numbered lists, say "reply with your picks, or 'go' for the recommended ones", and wait. Whatever is still unset, read from the problem; depth is 1 without records, 2 with records or for a build. Questions or not, then one line in chat on how you read the problem and how long it takes; after that, work without narrating.
3. **Ask first** (only if chosen). Write for yourself the facts you have and the ones you would have to assume; pick up to three whose answer would most change which explanations or approaches lead (does a record exist and what does it show, what changed and when, what has been tried). Each question names a person, a record, a step or a number from the request; never a stock list. Send them in one message, each with your guess in brackets, say they can answer any of them or just say "go", and wait. Answers become `facts` with the basis core.md defines; unanswered questions become assumptions with your guess and what changes if it is wrong. One round, never more.
4. **Think it through** with [references/core.md](references/core.md), what every map does, plus the one file for the mode: [references/diagnose.md](references/diagnose.md), [references/choose.md](references/choose.md) or [references/build.md](references/build.md), which says what each section means for that kind of task and governs where the two differ. Facts first, the person's theory as a neutral question, then the six skills. Thorough path: three fresh helpers from three vantages, merged, then a separate judge, as [references/team.md](references/team.md) says (team.md governs where the two files differ). Quick path, or no helpers: the written walkthrough in core.md ("Talk it through"). If you can choose how much to think, choose high, not the maximum.
5. **Write the data** as `tw-dan-<slug>-<YYYY-MM-DD>.json` in the person's current folder (or the folder they named); the slug is two to four lowercase words joined by hyphens. Load [references/data-shape.md](references/data-shape.md) now as the format example (core.md holds the field rules). Use your file-writing tool, not the shell, so quotes and apostrophes survive. Keep this file next to the report: it is what you update when the person replies.
6. **Check your outside facts, then three specific checks.** Turn every "verify:" fact into a question. With a web tool, open the source: `held` or `corrected`, or `unchecked` when the page does not settle it. Without one, re-answer from scratch: sure and agreeing is `held` with the note "from memory", anything else `unchecked`. Record each under `factChecks` as `{ "fact", "result", "note" }` and correct the map wherever a fact was corrected. Do not run a general "review and improve"; on the quick path make these three checks, nothing broader, and fix what fails: does summary line 1 follow from the facts and the walkthrough as written; has a detail imagined in the walkthrough become a fact elsewhere; does the next action tell apart the explanations it claims to. On the thorough path the judge does this.
7. **Build** with full, quoted paths:

   ```
   python "<skill-folder>/scripts/fill.py" "<folder>/tw-dan-<slug>-<date>.json" "<folder>/tw-dan-<slug>-<date>.html"
   ```

   fill.py checks the shape (core.md lists the required keys) and prints every problem; fix the JSON and run again until it prints "Checks passed". Then read the printed summary and takeaways top to bottom: they must read as one argument; if they don't, fix the JSON. Thorough path: build once with `review: []`, run the judge round in team.md, record its findings under `review`, build again. Without Python: copy [assets/report-template.html](assets/report-template.html) to the `.html` name, replace the single line `__REPORT_DATA__` with the JSON after writing every `</` as `<\/` (one backslash) and every `<!--` as `<!--`, change nothing else, and say in chat that the checks did not run.
8. **Open and report.** Open the file (`start` on Windows, `open` on macOS, `xdg-open` on Linux); if you cannot, give the full path. Then one message, nothing else: the file name (or that full path), the three summary lines, the next action, and the one open question that would most change the answer, with your guess. An update uses the message in reply.md instead.

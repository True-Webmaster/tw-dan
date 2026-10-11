# tw-dan: the Human in the Loop map

A skill for Claude Code and Codex. You describe a client problem, a choice between two options, or something you need to build (a plan, a system, a campaign, a process) in one or two sentences; it thinks it through the way an engineer would and hands you one page you can read in five minutes and act on.

It comes from Yan Gonzalez's talk *Human in the Loop* (True Webmaster). The talk's point: you can hand the thinking to an AI, but the judgment stays with you. This skill shows where.

## What you get

One HTML file that works offline, with:

- **The facts as given**, each marked measured, reported or assumed, and your own theory turned into a question that competes with the others on equal terms.
- **The questions it asked itself** about your problem before judging, with its answers, so you can see the thinking and not just the conclusion.
- **The parts of the problem** and how they connect, as a graph, with a breakdown you can open one, two or three levels deep.
- **Competing explanations**, each with what the records would show if it were true, the evidence that would rule it out, the cheapest way to get that evidence, and a rough percentage.
- **Blind spots**: things you probably don't know to ask about.
- **What matters now and what waits.**
- **Work streams** in waves, each saying who does it (you, the client, their staff, a vendor, or an AI alone) and whether it can be undone. Anything that can't be undone waits for the checks that justify it.
- **Where you decide**: the calls only a human can make, and anything that can't be undone, each with what it waits for.
- **A pass/fail rubric** that only cites sources that exist. A target nobody has agreed is labelled "Preference, no source".
- **What the answer depends on**, and the one thing to do today, shown at the top and again at the end. A link bar at the top jumps between sections.

**How it thinks.** When your tool can run helper agents (Claude Code and the Codex CLI both can), the skill does not think alone: three fresh helpers each take the problem from a different vantage (the customer's path, the person who writes the number down, a sceptic who assumes nothing is wrong), the main agent merges what they found, and a separate judge reads the finished map against seven fixed questions before you see it. When the other tool is installed (Codex from Claude Code, Claude from Codex) the judge runs there, after your tool asks your permission, because a judge from another model family catches more; if it is not installed, or it fails, a fresh helper judges instead, and the report says which. The report shows the judge's findings and what was done about them. That is the one approach with strong evidence for deeper reasoning from these models; it takes about thirty minutes. Without helpers, the skill asks and answers its own questions in writing, in about ten.

The first run never names a single cause when the facts are thin. It says "the evidence cannot yet separate A, B and C", tells you which record splits them, and asks the one question that would most change the answer. When you send the records, it updates the map, marks explanations ruled out, and tells you in one line what moved.

## Install

**Claude Code** — put the folder at `~/.claude/skills/tw-dan/`:

```bash
git clone https://github.com/True-Webmaster/tw-dan.git ~/.claude/skills/tw-dan
```

Then, in any project:

```text
/tw-dan Our dental client's new-patient bookings dropped 30% since we launched their redesigned site. Traffic looks the same.
```

**Codex** — put the folder at `.agents/skills/tw-dan/` inside your project:

```bash
git clone https://github.com/True-Webmaster/tw-dan.git .agents/skills/tw-dan
```

Then:

```text
$tw-dan Our dental client's new-patient bookings dropped 30% since we launched their redesigned site. Traffic looks the same.
```

**Requirements.** Python 3 for the build step (`scripts/fill.py`). If Python is missing, SKILL.md describes a manual fallback.

## How to use it

1. **Describe the problem as you'd say it to a colleague.** One or two sentences is enough. If you have records, attach or paste them; the map goes a level deeper when it has data.
2. **Answer three quick choices.** Before it builds, the skill asks what you want (find out what is going on, choose between options, or plan and build something), how thorough (three helpers and a judge in about thirty minutes, or one mind in about ten), and whether it should ask you up to three questions about the problem first or just assume and label. Its own reading is pre-selected, so one click or "go" is enough. If a map already sits in your folder it also offers to continue it.

   To skip the choices (for example in a scripted run), put the words first: `quick`, `ask`, `build`, `choose`, `diagnose`, `update`, or `depth 2` / `depth 3` for a finer breakdown. Example: `/tw-dan quick depth 2 Our bakery's weekend pre-orders keep going missing at pickup.`
3. **Read the summary, then the next action.** The chat reply has the file name, three summary lines, the next action, and one question with the skill's own guess. Correct the guess or send the records.
4. **Reply with what you found.** The skill updates the same file and says in one line what changed. In a later session, pick "continue the map" when it asks, or start the request with `update`.

A run takes about ten minutes alone, about thirty with helpers. The skill writes two files in your current folder: `tw-dan-<problem>-<date>.json` (the data; keep it, it's what gets updated) and `tw-dan-<problem>-<date>.html` (the report).

## Three kinds of task

- **Something is wrong** ("bookings dropped 30% since the redesign"): the map finds where the problem lives and which record settles it.
- **A choice** ("should we move the budget from A to B?"): the parts are the dimensions the choice turns on, the columns compare the two options, and the summary picks one conditionally when the evidence can't yet decide.
- **Something to build** ("plan a referral programme", "set up monthly reporting"): the parts are the building blocks in build order, one of them always the measurement; the explanations become competing approaches, including a simpler one; and the next action is the smallest piece to build or test today, never the whole thing.

## What it won't do

- Write the deliverable (the ad, the page, the email).
- Run a ranking or site audit that needs live data.
- Find a bug in a specific piece of code. A slow system, or a dispute about where a fault lies, is fine.
- Interview you. It assumes and labels every assumption with what changes if it's wrong.

## How it was tested

Twenty fresh runs over two days in Claude Code and the Codex CLI, across SEO, technical SEO, sales, AI, software engineering and a daycare, each by an agent that could read only the skill's own files: all built on the first try. Two independent audits checked the skill for anything that hints at an industry, a cause or a check; what they found was removed, and every example in the method is about a bakery. A run with the user's own theory planted ("I think the new booking form is the problem") did not take the bait. A run with a budget choice refused to move money without evidence. One reply round, fed real numbers, cleared the website and moved the lead to a staffing change. A no-skill baseline reached the same checks; the difference the skill makes is discipline: no fix before evidence, no unsourced claims, and your framing treated as a question.

The test definitions are in `evals/evals.json`.

## Files

```text
tw-dan/
├── SKILL.md                   # the instructions the agent follows
├── references/core.md         # what every map does: facts, the walkthrough, the six skills, the data shape
├── references/diagnose.md     # what each section means when something is wrong
├── references/choose.md       # what each section means for a choice between options
├── references/build.md        # what each section means for something to build
├── references/team.md         # the three helpers and the judge
├── references/reply.md        # what to do when the person replies with records or corrections
├── references/data-shape.md   # a worked example of the data (about a bakery, on purpose)
├── assets/report-template.html# draws the report from the data, offline
├── scripts/fill.py            # validates the data and builds the report
└── evals/evals.json           # test cases
```

## Credits

Yan Gonzalez, True Webmaster. The method borrows from Kepner-Tregoe problem analysis, Analysis of Competing Hypotheses, Cynefin, step-back prompting, and the post-mortem and intelligence-analysis traditions of separating facts from judgments.

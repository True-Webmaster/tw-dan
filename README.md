# tw-dan: the Human in the Loop map

A skill for Claude Code and Codex. You describe a client problem in one or two sentences; it thinks it through the way an engineer would and hands you one page you can read in five minutes and act on.

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
- **A pass/fail rubric** that only cites sources that exist. A target nobody has agreed is labelled "Preference, no source".
- **What the answer depends on**, and the one thing to do today.

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
2. **Say depth 2 or depth 3** if you want a finer breakdown. A first run with no records stays at one level so it reads in five minutes.
3. **Read the summary, then the next action.** The chat reply has the file name, three summary lines, the next action, and one question with the skill's own guess. Correct the guess or send the records.
4. **Reply with what you found.** The skill updates the same file and says in one line what changed.

A run takes about ten minutes. The skill writes two files in your current folder: `tw-dan-<problem>-<date>.json` (the data; keep it, it's what gets updated) and `tw-dan-<problem>-<date>.html` (the report).

## What it won't do

- Write the deliverable (the ad, the page, the email).
- Run a ranking or site audit that needs live data.
- Find a bug in a specific piece of code. A slow system, or a dispute about where a fault lies, is fine.
- Interview you. It assumes and labels every assumption with what changes if it's wrong.

## How it was tested

Thirteen fresh runs in Claude Code on the day it shipped, across SEO, technical SEO, sales, AI and software engineering, each by an agent that could read only the skill's own files, plus one run through the Codex CLI: all built on the first try. A run with the user's own theory planted ("I think the new booking form is the problem") did not take the bait. A run with a budget choice refused to move money without evidence. One reply round, fed real numbers, cleared the website and moved the lead to a staffing change. A no-skill baseline reached the same checks; the difference the skill makes is discipline: no fix before evidence, no unsourced claims, and your framing treated as a question.

The test definitions are in `evals/evals.json`.

## Files

```text
tw-dan/
├── SKILL.md                   # the instructions the agent follows
├── references/method.md       # the six-skill method and the rules
├── references/data-shape.md   # a worked example of the data (about a bakery, on purpose)
├── assets/report-template.html# draws the report from the data, offline
├── scripts/fill.py            # validates the data and builds the report
└── evals/evals.json           # test cases
```

## Credits

Yan Gonzalez, True Webmaster. The method borrows from Kepner-Tregoe problem analysis, Analysis of Competing Hypotheses, Cynefin, step-back prompting, and the post-mortem and intelligence-analysis traditions of separating facts from judgments.

# tw-dan: the Human in the Loop map

DAN stands for Decompose, Abstract, Nudge: break the problem into parts, keep what matters, then one small push rather than a big fix. TW is True Webmaster.

A skill for Claude Code and Codex. You describe a client problem, a choice between options, or something you need to build (a plan, a system, a campaign, a process) in one or two sentences; it thinks it through the way an engineer would and hands you one page you can read in five minutes and act on.

It comes from Yan Gonzalez's talk *Human in the Loop*. The talk's point: you can hand the thinking to an AI, but the judgment stays with you. This skill shows where.

## What you get

One HTML file that works offline, with:

- **The facts as given**, each marked measured, reported or assumed, and your own theory turned into a question that competes with the others on equal terms.
- **The questions it asked itself** before judging, with its answers, so you see the thinking and not just the conclusion.
- **The parts of the problem** as a graph, and **competing explanations**, each with what the records would show if it were true, what would rule it out, and the cheapest check.
- **Blind spots**: things you probably don't know to ask about.
- **Work streams** that say who does each one (you, the client, their staff, a vendor, or an AI alone) and whether it can be undone, and **where you decide**: the calls only a human can make.
- **A pass/fail rubric** that cites only sources that exist, **what the answer depends on**, and the one thing to do today.

**How it thinks.** On the thorough setting, three fresh helpers each take the problem from a different vantage, the main agent merges what they found, and a separate judge reads the finished map against seven fixed questions before you see it; the report shows the judge's findings and what was done about them. On the quick setting, the skill asks and answers its own questions in writing. Either way, a first run never names a single cause when the facts are thin: it says "the evidence cannot yet separate A, B and C", names the record that splits them, and asks the one question that would most change the answer. Send the records and it updates the same map, marks explanations ruled out, and says in one line what moved.

## Install

**Claude Code**, at `~/.claude/skills/tw-dan/`:

```bash
git clone https://github.com/True-Webmaster/tw-dan.git ~/.claude/skills/tw-dan
```

Then, in any project:

```text
/tw-dan Our dental client's new-patient bookings dropped 30% since we launched their redesigned site. Traffic looks the same.
```

**Codex**, at `.agents/skills/tw-dan/` inside your project:

```bash
git clone https://github.com/True-Webmaster/tw-dan.git .agents/skills/tw-dan
```

Then:

```text
$tw-dan Our dental client's new-patient bookings dropped 30% since we launched their redesigned site. Traffic looks the same.
```

## Set up for the best results

| Your setup | What you get |
|---|---|
| Claude Code **or** Codex, plus Python 3 | Everything: the quick setting (one mind, about ten minutes) and the thorough setting (three helpers and a judge, about thirty). The judge is a fresh helper from the same AI. |
| Claude Code **and** the Codex CLI, both logged in, plus Python 3 | Best. On the thorough setting the finished map is checked by the *other* company's AI: Codex checks a map Claude made, and Claude checks a map Codex made. A checker from a different model family catches mistakes the first one is blind to. |

1. **Install Python 3** from [python.org](https://www.python.org/downloads/). It builds and checks the report; without it the skill still works, but the checks don't run.
2. **Install the other tool and log in once.** Each needs its own account. Claude Code: [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup). Codex CLI: [developers.openai.com/codex/cli](https://developers.openai.com/codex/cli).
3. **Check that each answers from the terminal:**

   ```bash
   claude -p "Reply with OK"
   ```

   ```bash
   codex exec --skip-git-repo-check "Reply with OK"
   ```

   If Claude asks you to log in, run `claude`, type `/login`, and test again; being logged in inside the app doesn't always log in the terminal command. If Codex says a model is not supported, run `codex --version`: some computers have two copies and the terminal runs the older one.
4. **Allow the cross-check when asked.** The first time, your tool asks permission to run the other one.
5. **Keep both current** with `claude update` and `codex update` before an important run. If a version number doesn't change afterwards, an older copy is the one your terminal runs.

If the other tool is missing or fails, the skill uses a same-family judge instead and the report says which judge ran.

**Cost.** The thorough setting runs three helpers and a judge, so it uses several times more of your plan than the quick one. Use `quick` when the problem is small.

## How to use it

1. **Describe the problem as you'd say it to a colleague.** One or two sentences. If you have records, attach or paste them; the map goes a level deeper when it has data.
2. **Answer three quick choices.** The skill asks what you want (find out what is going on, choose between options, or plan and build something), how thorough (quick or thorough), and whether it should ask you up to three questions first or just assume and label. Its own reading is pre-selected, so one click or "go" is enough. If a map already sits in your folder it offers to continue it. To skip the choices, put the words first: `quick`, `ask`, `build`, `choose`, `diagnose`, `update`, or `depth 2` / `depth 3` for a finer breakdown.
3. **Read the summary, then the next action.** The chat reply has the file name, three summary lines, the next action, and one question with the skill's own guess.
4. **Reply with what you found.** The skill updates the same file and says in one line what changed. In a later session, start with `update`.

The skill writes two files in your current folder: `tw-dan-<problem>-<date>.json` (the data; keep it, it is what gets updated) and `tw-dan-<problem>-<date>.html` (the report).

## Three kinds of task

- **Something is wrong** ("bookings dropped 30% since the redesign"): the map finds where the problem lives and which record settles it.
- **A choice** ("should we move the budget from A to B?"): the parts are the dimensions the choice turns on, the columns compare the options, and the summary picks one conditionally when the evidence can't yet decide.
- **Something to build** ("plan a referral programme"): the parts are the building blocks in build order, one of them always the measurement; the explanations are competing approaches, including a simpler one; the next action is the smallest piece to build or test today.

## What it won't do

- Write the deliverable (the ad, the page, the email).
- Run a ranking or site audit that needs live data.
- Find a bug in a specific piece of code. A slow system, or a dispute about where a fault lies, is fine.
- Interview you at length. Beyond the three quick choices, and up to three questions if you pick "ask first", it assumes and labels every assumption with what changes if it is wrong.

## How it was tested

More than forty fresh runs over two days in Claude Code and the Codex CLI, across SEO, sales, AI, software, and a dozen small businesses, each by an agent that could read only the skill's own files; all built on the first try. Two independent audits checked the skill for anything that hints at an industry, a cause or a check, and everything found was removed. A run with the user's own theory planted did not take the bait; a budget choice refused to move money without evidence; a reply round fed real numbers moved the lead explanation. A no-skill baseline reached the same checks; what the skill adds is discipline: no fix before evidence, no unsourced claims, and your framing treated as a question. The test definitions are in `evals/evals.json`.

## Files

SKILL.md is the router: it asks what you want, then loads `core.md` (what every map does) plus one file for the mode. A reply to an earlier map loads `reply.md` instead.

```text
tw-dan/
├── SKILL.md                   # the instructions the agent follows
├── references/core.md         # what every map does: facts, the walkthrough, the six skills, the data shape
├── references/diagnose.md     # what each section means when something is wrong
├── references/choose.md       # what each section means for a choice between options
├── references/build.md        # what each section means for something to build
├── references/team.md         # the three helpers and the judge
├── references/reply.md        # what to do when the person replies with records or corrections
├── references/data-shape.md   # a specimen of the data (about a bakery, on purpose)
├── assets/report-template.html# draws the report from the data, offline
├── scripts/fill.py            # validates the data and builds the report
└── evals/evals.json           # test cases
```

## Credits

Yan Gonzalez, True Webmaster. The method borrows from Kepner-Tregoe problem analysis, Analysis of Competing Hypotheses, Cynefin, step-back prompting, and the intelligence-analysis tradition of separating facts from judgments.

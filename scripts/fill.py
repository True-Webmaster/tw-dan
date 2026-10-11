"""Fill the Human in the Loop map template with report data and check it.

Usage:  python <skill-folder>/scripts/fill.py <path to data.json> <path to output.html>
Full paths work from any folder. Prints problems and
exits 1 if the data is not usable; prints the summary and takeaways in
order, then the output path, when the report is written.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "assets", "report-template.html")

LIKELIHOODS = ("leading", "possible", "unlikely")
STATUSES = ("pass", "fail", "unknown")
HYP_STATUSES = ("open", "ruled out", "confirmed")
BASES = ("measured", "reported", "assumed", "outside")
WHO = ("ai", "you", "client", "client's staff", "vendor")
KINDS = ("check", "fix", "decide", "ask")
SECTIONS = ("decompose", "abstract", "reuse", "parallelize", "rubric", "evaluate")


def find_loop(items, key):
    """Return the id of an item that reaches itself through `key`, or None."""
    links = {it.get("id"): list(it.get(key) or []) for it in items}

    def visit(node, path):
        if node in path:
            return node
        for nxt in links.get(node, []):
            found = visit(nxt, path + [node])
            if found:
                return found
        return None

    for start in links:
        found = visit(start, [])
        if found:
            return found
    return None


def norm(text):
    return " ".join(str(text or "").lower().split())


def winpath(path):
    """Windows refuses paths over 260 characters unless they carry the long-path prefix."""
    full = os.path.abspath(path)
    if os.name == "nt" and len(full) > 240 and not full.startswith("\\\\?\\"):
        return "\\\\?\\" + full
    return full


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    src, out = winpath(sys.argv[1]), winpath(sys.argv[2])
    try:
        with open(src, encoding="utf-8") as f:
            data = json.load(f)
    except OSError as e:
        print(f"Cannot read {src}: {e}")
        return 1
    except ValueError as e:
        print(f"The JSON is not valid: {e}")
        return 1
    if not isinstance(data, dict):
        print("The JSON must be one object, not a list.")
        return 1

    problems = []
    if not data.get("title"):
        problems.append("Missing 'title'.")
    if not data.get("summary"):
        problems.append("Missing 'summary'.")
    elif len(data["summary"]) > 3:
        problems.append("The summary has more than 3 lines.")
    for name in SECTIONS:
        sec = data.get(name)
        if not isinstance(sec, dict) or (not sec.get("skipped") and len(sec) == 0):
            problems.append(f"Section '{name}' is missing. Fill it, or write {{\"skipped\": \"<reason>\"}}.")
    for f_ in list(data.get("facts") or []) + list(data.get("restsOn") or []):
        if norm(f_.get("basis")) not in BASES:
            problems.append(f"Fact '{f_.get('fact')}' needs 'basis' of measured, reported, assumed or outside (one of them, not a mix).")

    dec = data.get("decompose") or {}
    if dec.get("skipped"):
        problems.append("'decompose' cannot be skipped.")
    parts = dec.get("parts") or []
    if not parts:
        problems.append("Missing 'decompose.parts'.")
    part_ids = {p.get("id") for p in parts}
    if len(part_ids) != len(parts):
        problems.append("Part ids must be unique.")
    for p in parts:
        if not p.get("id"):
            problems.append(f"Part '{p.get('name')}' has no id.")
        if not p.get("name"):
            problems.append(f"Part '{p.get('id')}' has no name.")
        if not p.get("check"):
            problems.append(f"Part '{p.get('name')}' has no 'check'.")
        for d in p.get("dependsOn") or []:
            if d not in part_ids:
                problems.append(f"Part '{p.get('id')}' depends on '{d}', which is not a part id.")
    loop = find_loop(parts, "dependsOn")
    if loop:
        problems.append(f"Part '{loop}' depends on itself through other parts. Break the loop.")

    deepest = [1]

    def check_children(items, level, path):
        for c in items or []:
            deepest[0] = max(deepest[0], level)
            if not c.get("name"):
                problems.append(f"A level-{level} item under '{path}' has no name.")
            if c.get("children"):
                if level >= 3:
                    problems.append(f"'{c.get('name')}' goes deeper than level 3.")
                else:
                    check_children(c["children"], level + 1, c.get("name"))

    for p in parts:
        check_children(p.get("children"), 2, p.get("name"))
    depth = dec.get("depth")
    if depth is None:
        problems.append("Missing 'decompose.depth' (1, 2 or 3).")
    elif depth not in (1, 2, 3):
        problems.append("'decompose.depth' must be 1, 2 or 3.")
    elif deepest[0] != depth:
        problems.append(f"'decompose.depth' says {depth} but the breakdown goes {deepest[0]} level(s) deep. Match them.")

    real = dec.get("isItReal")
    if isinstance(real, dict) and real.get("verdict") and norm(real["verdict"]) not in ("outside normal", "inside normal", "can't tell yet", "cant tell yet"):
        problems.append("'decompose.isItReal.verdict' must be 'outside normal', 'inside normal' or \"can't tell yet\".")

    hyps = dec.get("hypotheses") or []
    if len(hyps) < 3:
        problems.append("List at least 3 competing explanations in 'decompose.hypotheses', including one that goes against the obvious answer.")
    seen_rule_outs = {}
    probs = []
    for h in hyps:
        if not h.get("ruleOut") or not h.get("cheapestCheck"):
            problems.append(f"Explanation '{h.get('name')}' needs 'ruleOut' and 'cheapestCheck'.")
        if not h.get("predicts"):
            problems.append(f"Explanation '{h.get('name')}' needs 'predicts': what the records show if it is true.")
        if norm(h.get("likelihood")) not in LIKELIHOODS:
            problems.append(f"Explanation '{h.get('name')}' needs 'likelihood' of leading, possible or unlikely.")
        if h.get("status") is not None and norm(h.get("status")) not in HYP_STATUSES:
            problems.append(f"Explanation '{h.get('name')}' has 'status' outside open, ruled out, confirmed.")
        key = norm(h.get("ruleOut"))
        if key:
            if key in seen_rule_outs:
                problems.append(f"Explanations '{seen_rule_outs[key]}' and '{h.get('name')}' share the same 'ruleOut'; they are one explanation written twice.")
            seen_rule_outs[key] = h.get("name")
        if h.get("probability") is not None:
            try:
                pr = float(h["probability"])
                probs.append(pr)
                if not 0 <= pr <= 100:
                    problems.append(f"Explanation '{h.get('name')}' has a 'probability' outside 0 to 100.")
            except (TypeError, ValueError):
                problems.append(f"Explanation '{h.get('name')}' has a 'probability' that is not a number.")
    if probs and len(probs) == len(hyps) and not 95 <= sum(probs) <= 105:
        problems.append(f"The explanations' probabilities add to {sum(probs):g}, not 100.")
    if probs and len(probs) != len(hyps):
        problems.append("Either every explanation has a 'probability' or none does.")

    for u in data.get("unknownUnknowns") or []:
        if not u.get("area") or not u.get("howToFind") or not u.get("whyItMatters"):
            problems.append("Every unknown unknown needs an 'area', a 'whyItMatters' and a 'howToFind'.")

    ab = data.get("abstract") or {}
    for m in ab.get("mattersNow") or []:
        if not m.get("lookAt"):
            problems.append(f"'Matters now' item '{m.get('item')}' needs a 'lookAt': the record or test that makes it checkable.")

    pa = data.get("parallelize") or {}
    streams = pa.get("streams") or []
    stream_ids = {s.get("id") for s in streams}
    if len(stream_ids) != len(streams):
        problems.append("Stream ids must be unique.")
    for s in streams:
        if not s.get("id") or not s.get("name"):
            problems.append("Every stream needs an 'id' and a 'name'.")
        if not s.get("brief"):
            problems.append(f"Stream '{s.get('id')}' has no 'brief'.")
        if not s.get("kind"):
            problems.append(f"Stream '{s.get('name')}' needs 'kind': check, fix, decide or ask.")
        if norm(s.get("who")).replace("’", "'") not in WHO:
            problems.append(f"Stream '{s.get('name')}' needs 'who': AI, you, client, client's staff or vendor.")
        if s.get("kind") is not None and norm(s.get("kind")) not in KINDS:
            problems.append(f"Stream '{s.get('name')}' needs 'kind': check, fix, decide or ask.")
        door = norm(s.get("door"))
        if door not in ("reversible", "one-way", "one way"):
            problems.append(f"Stream '{s.get('name')}' needs 'door': reversible or one-way.")
        elif door != "reversible" and not s.get("waitsFor"):
            problems.append(f"Stream '{s.get('name')}' can't be undone but sits in wave 1. It must wait for the checks that justify it.")
        for w in s.get("waitsFor") or []:
            if w not in stream_ids:
                problems.append(f"Stream '{s.get('id')}' waits for '{w}', which is not a stream id.")
    loop = find_loop(streams, "waitsFor")
    if loop:
        problems.append(f"Stream '{loop}' waits for itself through other streams. Break the loop.")

    for c in (data.get("rubric") or {}).get("criteria") or []:
        if not c.get("source"):
            problems.append(f"Rubric criterion '{c.get('criterion')}' has no source. Use 'Preference, no source' if there is none.")
        st = norm(c.get("status")) if c.get("status") is not None else None
        if st is not None and st not in STATUSES:
            problems.append(f"Rubric criterion '{c.get('criterion')}' needs 'status' of pass, fail or unknown.")
        if st in ("pass", "fail") and not c.get("evidence"):
            problems.append(f"Rubric criterion '{c.get('criterion')}' is marked {st} with no 'evidence'. Add the record, or set it to unknown.")

    ev = data.get("evaluate") or {}
    tests = ev.get("tests") or []
    signals = [t for t in tests if t.get("signal")]
    if len(signals) > 1:
        problems.append("Only one test can be the 'signal'.")
    if tests and not signals and not ev.get("skipped"):
        problems.append("Flag exactly one test 'signal': true, the one check that stays red while the problem exists.")

    for a in data.get("assumptions") or []:
        if isinstance(a, dict) and not a.get("assumption"):
            problems.append("Every assumption object needs an 'assumption'.")
    for q in data.get("openQuestions") or []:
        if isinstance(q, dict) and not q.get("question"):
            problems.append("Every open question object needs a 'question'.")
    na = data.get("nextAction")
    if not na or (isinstance(na, dict) and not na.get("action")):
        problems.append("Missing 'nextAction'.")
    wt = data.get("walkthrough")
    if not isinstance(wt, list):
        problems.append("Missing 'walkthrough': the questions you wrote about this problem and your answers (at least six in round 1, two in round 2).")
    else:
        r1 = [w for w in wt if w.get("round") == 1]
        r2 = [w for w in wt if w.get("round") == 2]
        if len(r1) < 6:
            problems.append(f"The walkthrough has {len(r1)} round-1 questions; write at least six, each naming something from this problem.")
        if len(r2) < 2:
            problems.append(f"The walkthrough has {len(r2)} round-2 questions; write at least two that your round-1 answers raised.")
        for w in wt:
            if not w.get("question") or not w.get("answer"):
                problems.append("Every walkthrough entry needs a 'question' and an 'answer'.")
                break
            if len(str(w.get("answer")).split()) < 15:
                problems.append(f"Walkthrough answer to '{str(w.get('question'))[:60]}' is too short; answer as if you were there, two or three sentences.")
    fc = data.get("factChecks")
    if not isinstance(fc, list):
        problems.append("Missing 'factChecks': list every 'verify:' fact with result held, corrected or unchecked (an empty list means you brought no outside facts).")
    else:
        for item in fc:
            if item.get("result") not in ("held", "corrected", "unchecked"):
                problems.append(f"Fact check '{item.get('fact')}' needs 'result' of held, corrected or unchecked.")
    ct = data.get("coverageTest") or {}
    if not ct.get("fitsNoPart") or not ct.get("fitsTwoParts"):
        problems.append("Missing 'coverageTest': name one failure that fits no part and one that fits two, and say you fixed the parts.")
    elif ct.get("fixed") is not True:
        problems.append("'coverageTest.fixed' must be true: fix the parts so each failure fits exactly one, then say so.")

    if problems:
        print("Fix these and run again:")
        for p in problems:
            print(" - " + p)
        return 1

    # Escape '</' so text like '</script>' cannot end the data block early.
    payload = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/").replace("<!--", "<\\u0021--")
    with open(TEMPLATE, encoding="utf-8") as f:
        html = f.read()
    if "__REPORT_DATA__" not in html:
        print("The template is missing its __REPORT_DATA__ line.")
        return 1
    html = html.replace("__REPORT_DATA__", payload)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

    print("Read this top to bottom; it must hold together as one argument:")
    for line in data["summary"]:
        print("  " + str(line))
    for name in SECTIONS:
        sec = data.get(name) or {}
        if sec.get("skipped"):
            print(f"  [{name}] skipped: {sec['skipped']}")
        elif sec.get("takeaway"):
            print(f"  [{name}] {sec['takeaway']}")
    print(f"Walkthrough: {len([w for w in wt if w.get('round') == 1])} questions in round 1, {len([w for w in wt if w.get('round') == 2])} in round 2.")
    print("Fact checks:" + ("" if fc else " none brought from own knowledge"))
    for c in fc:
        print(f"  [{c.get('result')}] {c.get('fact')}" + (f" ({c.get('note')})" if c.get("note") else ""))
    print("Coverage test:")
    print("  fits no part: " + str(ct.get("fitsNoPart")))
    print("  fits two:     " + str(ct.get("fitsTwoParts")))
    shown = os.path.abspath(out)
    if shown.startswith("\\\\?\\"):
        shown = shown[4:]
    print("Checks passed. Report written: " + shown)
    return 0


if __name__ == "__main__":
    sys.exit(main())

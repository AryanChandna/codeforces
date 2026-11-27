#!/usr/bin/env python3
"""Tracks progress through the "Simple training for beginners" list
(https://codeforces.com/blog/entry/82143).

A problem counts as solved when a file whose name contains its ID exists
under src/ (e.g. src/P231A.java). Run with no args to regenerate README.md;
run with --next to print the next unsolved problem.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETS = {"A": "100 Problems A", "B": "100 Problems B", "C": "50 Problems C"}


def load():
    rows = []
    with open(os.path.join(ROOT, "problems.tsv")) as f:
        for line in f:
            s, pid, rating, name = line.rstrip("\n").split("\t")
            rows.append((s, pid, rating, name))
    return rows


def solved_ids():
    ids = set()
    for _, _, files in os.walk(os.path.join(ROOT, "src")):
        for fn in files:
            for m in re.finditer(r"(\d+)([A-Z]\d?)", fn):
                ids.add(m.group(1) + m.group(2))
    return ids


def url(pid):
    m = re.match(r"(\d+)(\w+)", pid)
    return f"https://codeforces.com/problemset/problem/{m.group(1)}/{m.group(2)}"


def next_unsolved(rows, done):
    for i, (s, pid, rating, name) in enumerate(rows):
        if pid not in done:
            return s, pid, rating, name
    return None


def write_readme(rows, done):
    total = len(rows)
    n = sum(1 for r in rows if r[1] in done)
    out = [
        "# Codeforces practice",
        "",
        "Working through [Simple training for beginners](https://codeforces.com/blog/entry/82143)"
        " — 100 A, 100 B and 50 C problems, rated 800–1500.",
        "",
        "## Workflow",
        "",
        "1. `python3 scripts/progress.py --next` shows the next problem.",
        "2. Solve it in `src/Main.java`, submit on Codeforces.",
        "3. Once accepted, save it as `src/P<id>.java` (e.g. `src/P231A.java`, class `P231A`).",
        "4. `python3 scripts/progress.py` to refresh this README, then commit and push.",
        "",
        f"## Progress: {n}/{total}",
        "",
    ]
    for key, title in SETS.items():
        part = [r for r in rows if r[0] == key]
        k = sum(1 for r in part if r[1] in done)
        out += [f"### {title} ({k}/{len(part)})", ""]
        for i, (_, pid, rating, name) in enumerate(part, 1):
            box = "x" if pid in done else " "
            out.append(f"- [{box}] {i}. [{pid} — {name}]({url(pid)}) `{rating}`")
        out.append("")
    with open(os.path.join(ROOT, "README.md"), "w") as f:
        f.write("\n".join(out))
    return n, total


def main():
    rows, done = load(), solved_ids()
    nxt = next_unsolved(rows, done)
    if "--next" in sys.argv:
        if nxt:
            s, pid, rating, name = nxt
            print(f"{pid} — {name} ({rating}) {url(pid)}")
        else:
            print("All 250 done!")
        return
    n, total = write_readme(rows, done)
    print(f"Solved {n}/{total}.", f"Next: {nxt[1]} — {nxt[3]} {url(nxt[1])}" if nxt else "All done!")


if __name__ == "__main__":
    main()

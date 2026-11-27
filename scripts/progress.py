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
    """A problem is solved when src/P<id>.java has an Accepted line in its Codeforces log."""
    ids = set()
    src = os.path.join(ROOT, "src")
    for fn in os.listdir(src):
        m = re.fullmatch(r"P(\d+[A-Z]\d?)\.java", fn)
        if m:
            with open(os.path.join(src, fn)) as f:
                head = f.read(4000)
            if re.search(r"^// \S+ \S+\s+Accepted\b", head, re.M):
                ids.add(m.group(1))
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
        "Write solutions in `src/P<id>.java`. Each one is submitted to Codeforces first; once Accepted,",
        "its submission log is added at the top of the file and it is pushed here.",
        "",
        f"## Progress: {n}/{total}",
        "",
    ]
    nxt = [r for r in rows if r[1] not in done][:3]
    out += ["### Up next", ""] + [f"- [{pid} — {name}]({url(pid)}) `{rating}`" for _, pid, rating, name in nxt]
    out += ["", "<details><summary>Full list</summary>", ""]
    for key, title in SETS.items():
        part = [r for r in rows if r[0] == key]
        k = sum(1 for r in part if r[1] in done)
        out += [f"### {title} ({k}/{len(part)})", ""]
        for i, (_, pid, rating, name) in enumerate(part, 1):
            box = "x" if pid in done else " "
            out.append(f"- [{box}] {i}. [{pid} — {name}]({url(pid)}) `{rating}`")
        out.append("")
    out.append("</details>")
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

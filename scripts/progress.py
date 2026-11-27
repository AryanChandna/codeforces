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


def is_accepted(path):
    with open(path) as f:
        head = f.read(4000)
    return re.search(r"^// \S+ \S+\s+Accepted\b", head, re.M) is not None


def solved_ids():
    """Accepted files in src/ are moved to solved/; everything in solved/ counts."""
    src, solved = os.path.join(ROOT, "src"), os.path.join(ROOT, "solved")
    os.makedirs(solved, exist_ok=True)
    ids = set()
    for fn in os.listdir(src):
        if re.fullmatch(r"P\d+[A-Z]\d?\.java", fn) and is_accepted(os.path.join(src, fn)):
            os.replace(os.path.join(src, fn), os.path.join(solved, fn))
            print(f"Accepted: moved {fn} to solved/")
    for fn in os.listdir(solved):
        m = re.fullmatch(r"P(\d+[A-Z]\d?)\.java", fn)
        if m:
            ids.add(m.group(1))
    return ids


ACTIVE = 3


def ensure_stubs(rows, done):
    """Keep exactly the next ACTIVE unsolved problems present as empty psvm stubs."""
    nxt = [r[1] for r in rows if r[1] not in done][:ACTIVE]
    for pid in nxt:
        path = os.path.join(ROOT, "src", f"P{pid}.java")
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(f"public class P{pid} {{\n    public static void main(String[] args) {{\n\n    }}\n}}\n")
    return nxt


def url(pid):
    m = re.match(r"(\d+)(\w+)", pid)
    return f"https://codeforces.com/problemset/problem/{m.group(1)}/{m.group(2)}"


def next_unsolved(rows, done):
    for i, (s, pid, rating, name) in enumerate(rows):
        if pid not in done:
            return s, pid, rating, name
    return None


def write_readme(rows, done, current):
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
        "2. The next 3 problems always exist as empty `src/P<id>.java` stubs — write the solution there.",
        "3. Submit on Codeforces first.",
        "4. `python3 scripts/cflog.py <id>` writes every submission + verdict as a comment at the top of the file.",
        "5. Once accepted: `python3 scripts/progress.py` moves it to `solved/`, adds the next stub, refreshes this README; then commit and push.",
        "",
        f"## Progress: {n}/{total}",
        "",
        "### Up next",
        "",
    ]
    byid = {r[1]: r for r in rows}
    for pid in current:
        _, _, rating, name = byid[pid]
        out.append(f"- [{pid} — {name}]({url(pid)}) `{rating}` → `src/P{pid}.java`")
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
    current = ensure_stubs(rows, done)
    nxt = next_unsolved(rows, done)
    if "--next" in sys.argv:
        if nxt:
            s, pid, rating, name = nxt
            print(f"{pid} — {name} ({rating}) {url(pid)}")
        else:
            print("All 250 done!")
        return
    n, total = write_readme(rows, done, current)
    print(f"Solved {n}/{total}. Up next:")
    for pid in current:
        print(f"  src/P{pid}.java  {url(pid)}")


if __name__ == "__main__":
    main()

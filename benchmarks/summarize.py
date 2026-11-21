"""Headline table: per-task median per arm, summed over tasks, % vs baseline. Plus IJBOL skill loads."""
import json, statistics, sys, glob, os, re
from collections import defaultdict
run = sys.argv[1]
cells = json.load(open(f"{run}/results.json"))["results"]
by = defaultdict(list)
for c in cells: by[(c["task"], c["arm"])].append(c)
tasks = sorted({c["task"] for c in cells}); arms = ["baseline", "ponytail", "ijbol"]
med = lambda xs: statistics.median(xs) if xs else 0
M = {"src LOC": lambda c: c.get("src_loc") or 0, "output tokens": lambda c: c.get("out_tokens") or 0,
     "total tokens": lambda c: (c.get("in_tokens") or 0) + (c.get("out_tokens") or 0) + (c.get("cache_tokens") or 0),
     "cost $": lambda c: c.get("cost") or 0, "time s": lambda c: (c.get("duration_ms") or 0) / 1000,
     "turns": lambda c: c.get("turns") or 0}
tot = {a: {m: sum(med([f(c) for c in by[(t, a)]]) for t in tasks) for m, f in M.items()} for a in arms}
for a in arms:
    cs = [c for c in cells if c["arm"] == a]
    tot[a]["pass %"] = 100 * statistics.mean(int(bool(c.get("correct") and c.get("safe"))) for c in cs)
    tot[a]["wrote tests %"] = 100 * statistics.mean(int((c.get("test_files") or 0) > 0) for c in cs)
print(f"tasks={len(tasks)} cells={len(cells)} runs/cell={len(cells)//len(tasks)//len(arms)}")
print(f"{'metric':16}" + "".join(f"{a:>22}" for a in arms))
for m in list(M) + ["pass %", "wrote tests %"]:
    row = f"{m:16}"
    for a in arms:
        v = tot[a][m]; s = f"{v:,.2f}" if m == "cost $" else f"{v:,.0f}"
        if a != "baseline" and m in M and tot["baseline"][m]:
            s += f" ({100 * (v / tot['baseline'][m] - 1):+.0f}%)"
        row += f"{s:>22}"
    print(row)
print("\nper task median src LOC / output tokens:")
for t in tasks:
    print(f"  {t:18}" + "".join(f"{a}: {med([M['src LOC'](c) for c in by[(t,a)]]):>4.0f} / {med([M['output tokens'](c) for c in by[(t,a)]]):>6.0f}   " for a in arms))
loads = defaultdict(int); n = 0
for d in glob.glob(f"{run}/*__ijbol__*"):
    sid = json.load(open(f"{d}/_claude.json")).get("session_id"); n += 1
    for f in glob.glob(os.path.expanduser(f"~/.claude/projects/*/{sid}.jsonl")):
        for s in set(re.findall(r'"skill":"([^"]+)"', open(f).read())): loads[s] += 1
print(f"\nIJBOL skill loads over {n} ijbol cells:", dict(loads))

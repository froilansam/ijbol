# Benchmark: IJBOL vs no skill vs ponytail (2026-11-21)

## Method

- **Harness:** ponytail's
  [agentic benchmark](https://github.com/DietrichGebert/ponytail/tree/main/benchmarks/agentic).
  Each cell is a real headless Claude Code session (`claude -p`) editing a
  seeded workspace, scored on the files it leaves behind. Hidden checks run
  the produced code against normal and adversarial input.
- **Model:** Opus 5.5, Claude Code 2.1.322.
- **Tasks:** the 9 tasks of ponytail's quick set that need no external
  fixture: `scope-recipients`, `conv-seam`, `csv-sum`, `critic-email`,
  `auth-token`, `reuse-slug`, `vibe-todo`, `vibe-shortener`,
  `open-decorators`.
- **Runs:** ponytail and IJBOL ran interleaved in the same run, 3 runs per
  task each. The no-skill baseline has 2 runs per task, from the first run
  of the day. Every metric is the per-task median, summed over the 9 tasks.
- **Isolation:** each arm runs with the user's global plugins, CLAUDE.md
  files and auto-memory turned off.
- **Arms:**
  - `baseline`: Claude Code with no skill.
  - `ponytail`: the ponytail plugin, loaded through its SessionStart hook.
  - `ijbol`: this repo, loaded with `--plugin-dir`. Its SessionStart hook
    injects [`hooks/core.md`](../hooks/core.md). The harness patch that adds
    this arm is 3 lines in `run.py`.

## Results

| vs no skill | source LOC | output tokens | total tokens | cost | time | turns | pass | wrote tests |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| no skill | 721 | 26,918 | 610,759 | $1.17 | 242 s | 44 | 89% | 56% |
| ponytail | 237 (**−67%**) | 15,679 (**−42%**) | 607,431 (−1%) | $0.97 (**−17%**) | 153 s (**−37%**) | 43 | 93% | 52% |
| **IJBOL** | 276 (**−62%**) | 16,333 (**−39%**) | 636,702 (+4%) | $1.04 (**−12%**) | 159 s (**−34%**) | 44 | **96%** | 52% |

Per task, median source LOC / output tokens:

| task | no skill | ponytail | IJBOL |
|---|--:|--:|--:|
| auth-token | 18 / 1,022 | 14 / 1,327 | 16 / 1,254 |
| conv-seam | 15 / 2,166 | 14 / 2,333 | 14 / 2,127 |
| critic-email | 46 / 3,244 | 11 / 1,833 | 11 / 1,777 |
| csv-sum | 64 / 2,756 | 22 / 1,826 | 25 / 1,466 |
| open-decorators | 60 / 2,477 | 20 / 1,068 | 49 / 1,371 |
| reuse-slug | 21 / 812 | 19 / 956 | 19 / 959 |
| scope-recipients | 12 / 2,687 | 5 / 2,717 | 9 / 2,807 |
| vibe-shortener | 282 / 7,643 | 79 / 2,136 | 81 / 2,617 |
| vibe-todo | 204 / 4,110 | 53 / 1,483 | 52 / 1,955 |

`scope-recipients` is a rename that has to reach every caller. It is the only
task any arm failed. IJBOL passed it in 2 of 3 runs, ponytail in 1 of 3, and
no skill in 0 of 2.

## What it means

- **IJBOL is the most correct arm:** 96% pass, against 93% for ponytail and
  89% for no skill.
- **It is cheaper and faster than no skill:** −12% cost, −34% time, −39%
  output tokens and −62% code.
- **Ponytail is still 3 to 5 points leaner on cost, tokens and time.** With 9
  tasks and 3 runs, a gap that size is close to noise. Most of the LOC gap
  comes from one task, `open-decorators`, where IJBOL wrote 49 lines and
  ponytail wrote 20.

## How we got here: v1 → v3

| version | activation | source LOC | output tokens | total tokens | cost | turns | pass |
|---|---|--:|--:|--:|--:|--:|--:|
| v1 | CLAUDE.md line, then 3 `Skill` calls (ijbol, lean, clean) | −68% | −29% | **+58%** | **+24%** | 88 | 89% |
| v3 | SessionStart hook injects a 430-word core once | −62% | −39% | +4% | −12% | 44 | 96% |

v1 loaded every skill with its own tool call. Each call was an extra turn,
and every turn re-read the whole context, so the number of turns doubled.
v3 injects the core rules once at session start, like ponytail does. The
specialists (`ijbol-clean`, `ijbol-ux`, `ijbol-visual`, `ijbol-review`) load
only when a task needs them. In this run they loaded 0 times, because every
task was self-contained. v3 also asks for a shorter reply, and drops the
instructions that sent the model looking for tooling and profiles. Raw v1
cells: [2026-11-21-v1-results.json](2026-11-21-v1-results.json).

## Limits

9 tasks, 2 to 3 runs each, one model. Treat a difference under about 10% as
noise. The tasks are small Python functions and scripts. IJBOL's specialists
(clean, UX, visual, review) and project profiles are not exercised here.
They add a `Skill` call, and tokens, whenever a task triggers them.

## Reproduce

1. Clone ponytail. In `benchmarks/agentic/run.py`, add an `ijbol` arm that
   appends `--plugin-dir $IJBOL_PLUGIN_DIR` to the command, the same way the
   other plugin arms are added.
2. Run:
   ```
   IJBOL_PLUGIN_DIR=/path/to/ijbol python3 run.py \
     --task scope-recipients,conv-seam,csv-sum,critic-email,auth-token,reuse-slug,vibe-todo,vibe-shortener,open-decorators \
     --arms baseline,ponytail,ijbol --model opus --runs 3 --workers 6
   ```
3. Summarize: `python3 summarize.py runs/<stamp>`.

Raw cells: [2026-11-21-results.json](2026-11-21-results.json).

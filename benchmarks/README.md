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
- **Runs:** 2 per task per arm, so 54 cells. Every metric is the per-task
  median, summed over the 9 tasks.
- **Isolation:** each arm runs with the user's global plugins, CLAUDE.md
  files and auto-memory turned off.
- **Arms:**
  - `baseline`: Claude Code with no skill.
  - `ponytail`: the ponytail plugin, which loads through its SessionStart
    hook.
  - `ijbol`: this repo, loaded with `--plugin-dir`, plus the CLAUDE.md line
    from the README added to the system prompt ("Before any code change,
    load the ijbol skill with the Skill tool."). The harness patch that adds
    this arm is about 5 lines in `run.py`.

## Results

| vs no skill | source LOC | output tokens | total tokens | cost | time | turns | pass | wrote tests |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| no skill | 721 | 26,918 | 610,759 | $1.17 | 242 s | 44 | 89% | 56% |
| ponytail | 248 (**−66%**) | 15,747 (**−42%**) | 608,624 (−0%) | $0.98 (**−17%**) | 156 s (**−36%**) | 42 | 89% | 56% |
| **IJBOL** | 234 (**−68%**) | 19,143 (**−29%**) | 962,587 (+58%) | $1.46 (+24%) | 199 s (−18%) | 88 | 89% | **67%** |

Per task, median source LOC / output tokens:

| task | no skill | ponytail | IJBOL |
|---|--:|--:|--:|
| auth-token | 18 / 1,022 | 15 / 1,400 | 16 / 1,727 |
| conv-seam | 15 / 2,166 | 14 / 2,122 | 13 / 2,068 |
| critic-email | 46 / 3,244 | 10 / 1,746 | 12 / 2,274 |
| csv-sum | 64 / 2,756 | 22 / 1,598 | 16 / 2,000 |
| open-decorators | 60 / 2,477 | 27 / 990 | 32 / 1,532 |
| reuse-slug | 21 / 812 | 19 / 843 | 19 / 898 |
| scope-recipients | 12 / 2,687 | 8 / 2,940 | 3 / 3,145 |
| vibe-shortener | 282 / 7,643 | 86 / 2,440 | 68 / 3,066 |
| vibe-todo | 204 / 4,110 | 46 / 1,668 | 54 / 2,431 |

Skill loads in the 18 IJBOL cells: `ijbol` 18/18, `ijbol-lean` 13/18,
`ijbol-clean` 11/18.

## What it means

- **IJBOL writes the least code**: −68%, slightly below ponytail. It writes
  tests most often: 67% of cells, against 56% for both other arms.
- **It writes fewer output tokens and finishes faster than no skill**, but
  not as much as ponytail does.
- **It costs more in total.** Each skill loads through its own `Skill` tool
  call. Every call is an extra turn, and every turn re-reads the whole
  context, so turns double (88 vs 44). Ponytail injects its rules once
  through a hook.
- **Correctness is unchanged.** Every arm passes 89%. The one failing task,
  `scope-recipients`, fails in all 6 cells across all three arms.
- **Not every specialist loads.** On small tasks the conductor sometimes
  skips `ijbol-lean` or `ijbol-clean`.

## Limits

9 tasks, 2 runs each, one model. Treat a difference under about 10% as
noise. The tasks are small Python functions and scripts. IJBOL's UX and
visual skills are not exercised here, and neither are project profiles.

## Reproduce

1. Clone ponytail. In `benchmarks/agentic/run.py`, add an `ijbol` arm that
   passes `--plugin-dir $IJBOL_PLUGIN_DIR` and puts the CLAUDE.md line in
   front of `NO_RUN`.
2. Run:
   ```
   IJBOL_PLUGIN_DIR=/path/to/ijbol python3 run.py \
     --task scope-recipients,conv-seam,csv-sum,critic-email,auth-token,reuse-slug,vibe-todo,vibe-shortener,open-decorators \
     --arms baseline,ponytail,ijbol --model opus --runs 2 --workers 6
   ```
3. Summarize: `python3 summarize.py runs/<stamp>`. This prints the tables
   above. It reads skill loads from `~/.claude/projects` transcripts.

Raw cells: [2026-11-21-results.json](2026-11-21-results.json).

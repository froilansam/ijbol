<p align="center">
  <img src="assets/banner.svg" alt="IJBOL: It Just Builds, Obviously Lean. A diff that removes 142 lines of over-engineering and adds 2." width="100%">
</p>

<p align="center">
  <a href="#install"><img alt="Claude Code plugin" src="https://img.shields.io/badge/Claude%20Code-plugin-d97757"></a>
  <img alt="6 skills" src="https://img.shields.io/badge/skills-6-3b82f6">
  <a href="#benchmark"><img alt="Benchmarked" src="https://img.shields.io/badge/benchmarked-vs%20no%20skill%20%26%20ponytail-22c55e"></a>
  <a href="#built-on-ponytail"><img alt="Built on ponytail" src="https://img.shields.io/badge/built%20on-ponytail-8b5cf6"></a>
</p>

**IJBOL: It Just Builds, Obviously Lean.** The diff is so small you burst
out laughing.

This is a Claude Code skill pack for lean, clean, good-looking code. One
conductor (`ijbol`) loads the right specialist for the job. Each specialist
answers one question, and each rule is written down in only one skill.

## The skills

| | Skill | Answers | Use it directly when |
|---|---|---|---|
| 🎼 | `ijbol` | What's the workflow? Understand → write → verify → report | Any code change (load it first) |
| ✂️ | `ijbol-lean` | How small? YAGNI, smallest complete change | "be lazy", "simplest", over-engineering |
| 🧹 | `ijbol-clean` | Where and how does it fit? Placement, components, types, naming, no regression, security, project profiles | Refactors, "make it clean", conventions |
| 🧭 | `ijbol-ux` | Does it work for the user? UX lens, states, accessibility, design chain | UI reviews, any visible change |
| 🎨 | `ijbol-visual` | Does it look right? Hierarchy, spacing, type, color, depth | "looks off", polish, design systems |
| 🔍 | `ijbol-review` | Is it ready to ship? Must / Should / Nice findings plus a verdict | "review this", staged changes, PRs |

## How they fit together

```mermaid
flowchart LR
    req([Your request]) --> ijbol{{"🎼 ijbol<br/>conductor"}}
    ijbol --> lean["✂️ ijbol-lean<br/>How small?"]
    ijbol --> clean["🧹 ijbol-clean<br/>Where does it fit?"]
    clean -.-> prof[("profiles/*.md<br/>local, gitignored")]
    ijbol -- visible change --> ux["🧭 ijbol-ux<br/>Works for the user?"]
    ux --> visual["🎨 ijbol-visual<br/>Looks right?"]
    ux -.-> opt["arrange · polish · delight<br/>optional, if installed"]
    rev["🔍 ijbol-review<br/>Ready to ship?"] -. standards .-> lean
    rev -. standards .-> clean
```

Every change goes through the same four steps:

```mermaid
flowchart LR
    A["1 · Understand<br/>restate goal, read callers,<br/>search before building,<br/>map the reach"] --> B["2 · Write<br/>YAGNI, DRY, KISS,<br/>right place, cascade"]
    B --> C["3 · Verify<br/>lint, types, tests,<br/>see the UI running,<br/>read your own diff"]
    C --> D["4 · Report<br/>blast radius,<br/>what was skipped"]
```

## Install

**As personal skills.** You type the names without a prefix (`/ijbol`,
`/ijbol-review`, and so on), and edits in this repo apply right away. Any
skill with the same name, and any skill with one of the old names, is moved to
`~/.claude/skills-backup-<date>/` first. Nothing is deleted.

```
git clone https://github.com/froilansam/ijbol && cd ijbol && ./install.sh
```

**As a plugin.** This version is shareable and versioned, but the skill names
get a prefix, e.g. `/ijbol:ijbol`:

```
/plugin marketplace add froilansam/ijbol
/plugin install ijbol@ijbol
```

Use one install method or the other. If you install both, every skill loads
twice.

**Then add one line to `~/.claude/CLAUDE.md`.** Skills only load when Claude
decides they apply. This line makes sure `ijbol` loads on every code change,
and the benchmark below uses the same line:

```
Before any code change, load the ijbol skill with the Skill tool.
```

## Project profiles

The skills are generic. Conventions for one codebase go in a profile:
`skills/ijbol-clean/profiles/<repo>.md`. It is gitignored, so private or
company rules never get pushed. Start the file with which repo it applies to,
then add whatever that codebase needs: file structure, naming table, UI kit,
state library, test/lint commands, gotchas. `ijbol-clean` reads the matching
profile before editing, and its rules beat the generic ones.

## Benchmark

Each cell below is a real headless Claude Code session on Opus 5.5: 9 tasks,
2 runs per task, 3 arms, scored by hidden correctness and safety checks. It
runs on [ponytail's harness](#built-on-ponytail). The full method,
per-task numbers and limits are in [benchmarks/](benchmarks/README.md).

| vs no skill | source LOC | output tokens | total tokens | cost | time | pass | wrote tests |
|---|--:|--:|--:|--:|--:|--:|--:|
| ponytail | **−66%** | **−42%** | −0% | **−17%** | **−36%** | 89% | 56% |
| **IJBOL** | **−68%** | **−29%** | +58% | +24% | **−18%** | 89% | **67%** |
| no skill | | | | | | 89% | 56% |

```mermaid
xychart-beta
    title "Source lines of code (9 tasks, lower is better)"
    x-axis ["no skill", "ponytail", "IJBOL"]
    y-axis "lines" 0 --> 800
    bar [721, 248, 234]
```

```mermaid
xychart-beta
    title "Cost in USD (9 tasks, lower is better)"
    x-axis ["no skill", "ponytail", "IJBOL"]
    y-axis "USD" 0 --> 1.6
    bar [1.17, 0.98, 1.46]
```

**The honest read:** IJBOL writes the least code and the most tests, at
the same pass rate as the other arms. It also costs more tokens than no
skill. Each specialist loads with its own tool call, and every extra turn
re-reads the whole context. If token cost matters most to you, ponytail
alone is cheaper. IJBOL pays extra for placement, naming, UX and review
discipline that this benchmark does not measure.

## Renamed from

| Old | New |
|---|---|
| `ulti` | `ijbol` ("ulti" still triggers it) |
| `ponytail` | `ijbol-lean` |
| `clean-code-implementation` | `ijbol-clean` |
| `ui-ux-frontend-review` | `ijbol-ux` |
| `refactoring-ui` | `ijbol-visual` |
| review mode inside `ulti` | `ijbol-review` |

## Credits

- `ijbol-visual` summarizes tactics from *Refactoring UI* by Adam Wathan and
  Steve Schoger.

## Built on ponytail

IJBOL stands on [**ponytail**](https://github.com/DietrichGebert/ponytail) by
[Dietrich Gebert](https://github.com/DietrichGebert), the "lazy senior dev"
skill: the best code is the code you never wrote.

- `ijbol-lean` is ponytail's skill with only the name and trigger words
  changed (MIT, see [`skills/ijbol-lean/LICENSE`](skills/ijbol-lean/LICENSE)).
- The benchmark above runs on ponytail's
  [agentic benchmark harness](https://github.com/DietrichGebert/ponytail/tree/main/benchmarks/agentic)
  with one extra `ijbol` arm.
- The full ponytail plugin adds things IJBOL does not have: session hooks,
  `ponytail-review`, `ponytail-audit` and `ponytail-debt`. If you only want
  the lean part, install ponytail itself.

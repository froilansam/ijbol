# IJBOL

**IJBOL: It Just Builds, Obviously Lean.** The diff is so small you burst
out laughing.

This is a Claude Code skill pack for lean, clean, good-looking code. One
conductor (`ijbol`) loads the right specialist for the job. Each specialist
answers one question, and each rule is written down in only one skill.

| Skill | Answers | Use it directly when |
|---|---|---|
| `ijbol` | What's the workflow? Understand → write → verify → report | Any code change (load it first) |
| `ijbol-lean` | How small? YAGNI, smallest complete change | "be lazy", "simplest", over-engineering |
| `ijbol-clean` | Where and how does it fit? Placement, components, types, naming, no regression, security, project profiles | Refactors, "make it clean", conventions |
| `ijbol-ux` | Does it work for the user? UX lens, states, accessibility, design chain | UI reviews, any visible change |
| `ijbol-visual` | Does it look right? Hierarchy, spacing, type, color, depth | "looks off", polish, design systems |
| `ijbol-review` | Is it ready to ship? Must / Should / Nice findings plus a verdict | "review this", staged changes, PRs |

```
ijbol ─┬─ ijbol-lean
       ├─ ijbol-clean ── profiles/*.md (local, loaded when the repo matches)
       └─ (visible change) ijbol-ux ── ijbol-visual
                                    └─ arrange / polish / delight (optional, if installed)

ijbol-review ── uses ijbol-lean + ijbol-clean (+ ijbol-ux / ijbol-visual) as its standards
```

### Renamed from

| Old | New |
|---|---|
| `ulti` | `ijbol` ("ulti" still triggers it) |
| `ponytail` | `ijbol-lean` |
| `clean-code-implementation` | `ijbol-clean` |
| `ui-ux-frontend-review` | `ijbol-ux` |
| `refactoring-ui` | `ijbol-visual` |
| review mode inside `ulti` | `ijbol-review` |

## Install

**As personal skills.** You type the names without a prefix (`/ijbol`,
`/ijbol-review`, and so on), and edits in this repo apply right away. Any
skill with the same name, and any skill with one of the old names, is moved to
`~/.claude/skills-backup-<date>/` first. Nothing is deleted.

```
./install.sh
```

**As a plugin.** This version is shareable and versioned, but the skill names
get a prefix, e.g. `/ijbol:ijbol`:

```
/plugin marketplace add froilansam/ijbol
/plugin install ijbol@ijbol
```

Use one install method or the other. If you install both, every skill loads
twice.

## Project profiles

The skills are generic. Conventions for one codebase go in a profile:
`skills/ijbol-clean/profiles/<repo>.md`. It is gitignored, so private or
company rules never get pushed. Start the file with which repo it applies to,
then add whatever that codebase needs: file structure, naming table, UI kit,
state library, test/lint commands, gotchas. `ijbol-clean` reads the matching
profile before editing, and its rules beat the generic ones.

## Credits

- `ijbol-lean` is based on `ponytail` from
  [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
  (MIT, see `skills/ijbol-lean/LICENSE`). Only the name and trigger words were
  changed.
- `ijbol-visual` summarizes tactics from *Refactoring UI* by Adam Wathan and
  Steve Schoger.

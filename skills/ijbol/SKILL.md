---
name: ijbol
description: "IJBOL - It Just Builds, Obviously Lean. Load before ANY code change (new feature, bug fix, refactor, review fix, UI tweak). The conductor of the IJBOL pack - loads ijbol-lean and ijbol-clean, plus ijbol-ux and ijbol-visual when the change is visible, then walks the change through understand → write → verify → report. Keeps code small, direct, DRY, KISS, YAGNI. Use whenever writing or editing code, or when the user says \"ijbol\" or \"ulti\". For reviewing code use ijbol-review."
---

# IJBOL - It Just Builds, Obviously Lean

The diff is so small you burst out laughing. Less code is better code.
Direct, simple, no extra layers.

IJBOL is the conductor, not the rulebook. Each rule has exactly one owner:

| Skill | Answers | Owns |
|---|---|---|
| `ijbol-lean` | How small? | Scope, YAGNI, smallest complete change |
| `ijbol-clean` | Where and how does it fit? | Placement, components, types, naming, no regression, security, project profiles |
| `ijbol-ux` | Does it work for the user? | UX lens, states, accessibility, the design chain |
| `ijbol-visual` | Does it look right? | Hierarchy, spacing, type, color, depth |
| `ijbol-review` | Is it ready to ship? | Code review method and output |

IJBOL decides which to load, in what order, and walks the change from request
to verified result. Do not restate their rules here; make sure every step
below actually happens.

Skip IJBOL for questions, explanations and plan-only turns. Load it the moment
you are about to edit code. Asked to review instead → load `ijbol-review`.

## 0. Who wins when rules disagree

1. The user's words in this conversation.
2. The repo's `CLAUDE.md` and the saved memories for this project.
3. The project profile (see `ijbol-clean` → Project Profiles).
4. `ijbol-lean` (scope and size).
5. `ijbol-clean` (placement, types, conventions).
6. `ijbol-ux`, then `ijbol-visual` (generic UI advice).

The project's own components, tokens and helpers beat any generic advice.

## 1. Load skills

Load each with the **Skill tool**, one call per skill, by the name the skill
list shows (`ijbol-lean`, or `ijbol:ijbol-lean` when installed as a
plugin). Load once per session; do not reload on every edit.

Before writing code:

1. `ijbol-lean`, unless "IJBOL mode" is already in your context (the plugin's
   session hook injects it; then the lean rules are loaded, skip this call).
2. `ijbol-clean` when changing an existing codebase where placement,
   component boundaries, types or naming matter (it also tells you whether a
   project profile applies). A self-contained function or script skips it.

Only when the change is visible to the user:

3. `ijbol-ux` (it owns the rest of the design chain and its order)
4. `ijbol-visual`

"Visible" means something a user sees or reads changes: layout, spacing,
color, copy, an empty/loading/error/success state, a new or restyled
component. A hook, helper, API call, type or test change is not visible, even
if it lives in a screen folder. Locale text is visible (copy).

## 2. Understand before writing

Most bad diffs come from editing before the task was understood. Do these in
order and keep the findings short.

1. **Restate the goal in one line.** What must be true when this is done? If
   the request is missing a word or could mean two things, ask once with
   options. Do not guess the user's decisions; do pick defaults on
   conventional ones and say which you picked.
2. **Read the code it touches**, plus one level out: who calls it and what it
   calls. Read the nearest sibling that already does something similar; that
   file is the pattern to copy.
3. **Search before you build.** Grep by concept, not just the name you would
   have chosen: the endpoint path, the UI verb, the locale key, a word that
   co-occurs. Check helpers/utils, hooks, the UI library and design tokens
   first. If something close exists, extend it without breaking its callers.
4. **Map the reach.** List every place the change must land: callers, types,
   tests, fixtures, mocks, locale, routes, state slices/endpoints, cache tags.
   Write the list down; it is the definition of done.
5. **Check what could break.** Data that could be lost, double-counted or
   exposed; offline paths; callers that stop compiling; snapshot tests.
6. **Bug fixes:** reproduce or explain the root cause first. Grep every caller
   of the function you will touch. Fix it once, in the shared code, not in the
   one screen that reported it.

For a change that alters data flow, persistence, navigation, permissions,
validation or an API contract, show the plan before editing
(`ijbol-clean` → Ask Before Editing). Otherwise, proceed.

## 3. Write

- **YAGNI:** build only what was asked. Name skipped extras in one line at the
  end instead of building them.
- **DRY:** reuse or extend what exists. Two copies of the same logic means one
  should be deleted.
- **KISS:** the plainest code a reader gets at a glance. Guard clauses over
  nesting, a named helper over a clever expression. Deleting beats adding.
- **Right place, right names, right types:** follow `ijbol-clean` and the
  project profile.
- **Cascade:** when a change alters what a value means, update everything
  downstream in the same change: status, gating flags, list rows, cache
  invalidation, related screens. A half-cascaded change is a bug.
- **Comments:** only the "why" the code cannot show, one line. A known
  shortcut gets `// shortcut: <limit>, <when to upgrade>`.
- **Never cut:** validation at trust boundaries, error handling that prevents
  data loss, permission checks, accessibility IDs and labels.
- **Stay in your lane:** no drive-by refactors, no formatting churn in lines
  you did not change.

## 4. Verify

Lazy code without its check is unfinished. Use the project's own scripts
(`package.json`, `Makefile`, the profile) and run them on touched files only.

1. **Lint** the touched files. Fix only what this change introduced.
2. **Type-check** when you changed a type, signature or import. Read only the
   errors in touched files and their callers.
3. **Test the touched logic.** New non-trivial logic (a branch, a loop, a
   parser, money/quantity math, permissions) gets one small test next to the
   feature's existing tests. Trivial changes need none.
4. **UI changes: see it running.** On mobile, use a booted simulator/emulator
   (the `argent-device-interact` skill when installed); on web, a browser.
   Check every state you touched: empty, loading, error, success, disabled.
   A screenshot beats "should look right".
5. **Read your own diff** top to bottom: leftover debug code, unused imports
   or props, `console.log`, inline styles, an edge case the reach list named
   but the diff missed.

If a check could not run, say so plainly. Never report a check as passed when
it was not run.

## 5. Report

- Explain what changed and why in the user's chat language; code, comments,
  plans and PR text stay English.
- State the blast radius: what behaves differently now, what was left as is.
- List files changed as clickable links.
- End with one line: what was skipped or not checked, and any risk.
- Do not commit, push, open a PR, or bump release versions unless asked.

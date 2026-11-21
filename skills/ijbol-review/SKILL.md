---
name: ijbol-review
description: IJBOL code review - reviews a diff, staged changes, a branch, a PR or a file for correctness, data loss, security, regression, missing tests, reuse, placement, naming and bloat, then lists numbered Must / Should / Nice findings with a ship verdict. Changes no code unless asked. Use when the user says "review this", "review my staged changes", "check before commit", "review the PR", "code review", or "ijbol-review".
---

# IJBOL Review

Load `ijbol-lean` and `ijbol-clean` first (they are the standards); add
`ijbol-ux` and `ijbol-visual` when the change is visible to users.

## 1. Get the change

- Staged: `git diff --cached`
- Branch: `git diff <base>...HEAD`
- PR: `gh pr diff <n>` (and `gh pr view <n>` for the description)
- File: the file itself

Nothing to review → say so and stop.

## 2. Read before judging

Read each changed file in full, not just the hunks, plus its callers and the
nearest sibling that does something similar. Check whether a project profile
applies (`ijbol-clean` → Project Profiles). A finding without a concrete
failing case (input, state, or caller that breaks) is not a finding.

## 3. Check, in this order

1. **Correctness:** logic, edge cases (empty, null, zero, duplicates, offline,
   race between requests).
2. **Data and security:** data lost, double-counted or exposed; permission
   gated on the real claim; tenant scoping; nothing sensitive rendered or
   logged.
3. **Regression:** other consumers of every shared component, hook, type,
   token or helper the change touched. Did the change cascade to everything
   that depends on the value it altered?
4. **Tests:** does a test fail if the new risky logic breaks? Is it next to
   the feature's other tests?
5. **Reuse:** a new helper, hook, type or component that duplicates an
   existing one. Name the existing path.
6. **Placement and layering:** fetching in a component, domain mapping in a
   shared component, a "shared" file with one consumer, a new folder pattern
   when the feature already has one.
7. **Naming:** wrong prefix or casing, a name that hides what the code does, a
   new synonym for an existing concept, a file name that does not match its
   export.
8. **Lean:** anything nobody asked for (options, flags, wrappers, dead props).
9. **Profile rules:** the project profile's gotchas.

## 4. Output

- One line: what the change does.
- **Must fix** - bugs, data loss, security, broken callers.
- **Should fix** - misleading names, wrong layer, duplicated logic, missing
  test for risky logic.
- **Nice to have** - consistency only.
- Number every finding, give `file:line`, the failing case, and the fix in one
  or two lines.
- Verdict: **ship** or **fix first**.

If everything passes, say so; do not manufacture findings. Pure taste
("I would call it X") is not a finding.

## 5. After the review

Change no code unless the user asks ("fix 2 and 5"). Then load `ijbol` and
run its sections 2-4 for those items only. The only safe auto-fixes without
asking are behavior-free: unused/duplicate imports, inline styles moved to the
existing style pattern.

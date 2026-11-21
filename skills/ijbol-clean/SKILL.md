---
name: ijbol-clean
description: IJBOL clean - clean-code standards for implementing or refactoring code - where code goes, agnostic components with only necessary props, logic in hooks, display values not raw objects, strict types (no any), naming, no regression, and security. Loads a local project profile when one matches the repo. Use when writing new code, cleaning up or refactoring code, or when the user asks to make code cleaner, follow clean code, avoid any, remove inline styles, or use project conventions, or says "ijbol-clean".
---

# IJBOL Clean

Use during active coding. For reviews, `ijbol-review` owns the method; this
skill supplies the standards it checks against.

## Core Rule

Preserve behavior unless the user explicitly asks for a behavior change. If a
cleanup could change runtime behavior, stop and explain the risk before
editing.

## Project Profiles

A profile is a markdown file in this skill's `profiles/` folder holding one
codebase's conventions: file structure, naming table, UI kit, state library,
test/lint commands and gotchas. Its opening lines say which repo it applies to.
The folder is gitignored, so private or company conventions stay on your
machine.

Before editing, list `profiles/`. If a profile matches the repo, Read it; its
rules beat the generic ones below.

No profile matches → the repo's `CLAUDE.md`, lint config and nearest sibling
files are the conventions.

## Architecture

- **Choose the place carefully.** Match the nearest existing feature / shared
  / helper / UI-library location. Do not dump files into convenient but wrong
  folders.
- **Screen stays thin.** Orchestration in the screen, logic in a hook, pure
  transforms in helpers, presentational pieces display-only.
- **Reuse first.** Search existing components, tokens, styles, hooks, helpers,
  utils and formatters before inventing new ones.
- **Start local, promote on the second consumer.** A unit lives in its feature
  folder until a real second feature imports it; then move it to the shared
  location. A file move is cheap; a wrong shared API is not.

### Agnostic components

If a unit is reusable, it must be **generic** and able to do **only what is
needed**.

1. **Generic - no domain knowledge.** A reusable component does not know what
   an order, invoice, user or API shape is. It takes a display model (`label`,
   `sublabel`, `value`) and emits events. Domain mapping lives in the caller.
2. **Capability minimalism.** No handler, mode, variant, flag or branch that
   nothing calls today. If an operation is forbidden by the API or product
   rule, do not expose a prop for it: making the wrong call impossible to
   write beats documenting that it is wrong.
3. **A helper returns what callers use.** No derivable convenience fields
   (`isValid` next to `errorCount` is two sources of truth).

Do not generalize for a future that is not in the request. Speculative
flexibility is the most expensive complexity because it looks like good
engineering.

### Logic lives in a hook, not in the component

- Fetching, mutations, derived state, filtering, sorting, validation, step
  state and side effects go in a `useX` hook next to the feature.
- The component body is mostly JSX. `useEffect` + `useMemo` + `useState` + a
  request inside a component is a hook trying to get out.
- Pure transforms (mapping, formatting, predicates) are plain functions in
  helpers, testable without rendering. The hook calls them.
- One hook per concern. Compose small hooks in the screen; no god-hook.
- Two screens running the same query + filter + refetch is one hook, imported
  twice.

### Pass display values, not raw objects

- A card that shows a name and an age takes `name` and `age`, not the API
  response or an id it must look up.
- No date math, unit conversion, `.find()`, percentages or status derivation
  in the render path. Formatted strings in, strings out.
- A prop the component never renders or calls is a bug. Delete it.
- Test: the component renders with a handful of literal strings and no domain
  imports. If not, the boundary is wrong.

### Context vs props

- Default to props; explicit is traceable and typed at every hop.
- Context only when a value is needed deep in a tree and threading it would
  touch components that do not care about it.
- Even then, expose only what consumers read, keep it feature-scoped, and
  convert it back to a prop if a consumer reads a single value.

## Types

- No `any`, no `as any`.
- Reuse existing interfaces as the single source of truth; create a type only
  when none exists. Check shared/generated type packages before defining a
  backend shape yourself.
- Interfaces for object shapes, unions for narrow literal choices,
  `Record<K, V>` for lookup maps, enums only where the project already uses
  them. Mapped types only when they reduce duplication without hurting
  readability.
- Feature-only types next to the feature; shared shapes in the existing shared
  type file.

## Naming

- Match sibling files before introducing a pattern. The profile's naming table
  wins when one applies.
- Names say what, not how: `getTotalPrice`, not `calc2` or `handleData`.
- Booleans read as a question: `is` / `has` / `can` / `should`.
- Event props `onX`, their implementations `handleX`.
- camelCase variables/functions, PascalCase components/types, UPPER_SNAKE_CASE
  true constants. File name = default export name.
- No new synonyms: if siblings say `customer`, do not write `client`.
- No abbreviations beyond the ones the domain already uses.
- Do not copy legacy naming outliers into new files, and do not rename them as
  a drive-by.

## UI code

- Use the project's UI library and design tokens; no one-off values.
- No inline styles. Use the existing style pattern (`StyleSheet.create`,
  styled components, Tailwind classes - whatever the area uses).
- Use existing formatters (dates, quantities, currency, accessibility IDs).
- Visual decisions go to `ijbol-ux` / `ijbol-visual`.

## State

- Follow the project's current state library for new state; never extend a
  legacy one the project is migrating away from (see profile).
- Mutation recovery side effects that apply to every caller (refetch after a
  failed mutation) live with the mutation, not in screens.

## No Regression

- **Enumerate consumers** before touching anything shared: grep every importer
  of the component, hook, type, token or helper and list them.
- **Prefer additive, defaulted, optional changes** over changing a signature.
- **Never fold unrelated screens into the diff.** A cleanup that would change
  other screens is a separate ticket; say so.
- **Verify contract changes** by tracing at least one live call site end to
  end.
- **State the blast radius** when finishing.

## Security

- Validate on the server side of the contract; client checks are UX only.
- Gate actions on the real permission/claim, not on whether a control renders.
- Never render or log internal IDs, raw error payloads, stack traces, tokens,
  or other tenants' data.
- Scope every query and mutation by organization/tenant.
- Never weaken an existing validation, guard or auth check in a refactor.

## Safe Auto-Cleanup (no need to ask)

- Remove unused imports; merge duplicate imports from one module.
- Move inline style objects into the existing style pattern.
- Rename newly introduced names that break convention.
- Replace a newly introduced one-off helper with an existing equivalent.
- Remove commented-out code you introduced.

## Ask Before Editing

Present a plan first when the change would:

- alter logic, data flow, persistence, navigation, permissions, validation or
  API contracts;
- swap a component for a shared one whose props or behavior are not obviously
  equivalent;
- merge or relocate types used across features;
- refactor a large unit whose edge cases are not fully understood.

## Completion Checklist

- [ ] Profile checked (and followed if one matched).
- [ ] Placement chosen deliberately; nothing dumped in the wrong folder.
- [ ] Existing pieces searched and reused first.
- [ ] Components agnostic, only necessary props, display values in.
- [ ] Logic in a hook or pure helper; components mostly JSX.
- [ ] No new `any`, inline styles, or legacy-state patterns.
- [ ] Consumers enumerated; blast radius stated.
- [ ] Lint on edited files passes for what this change introduced.

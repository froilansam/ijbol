---
name: ijbol-visual
description: IJBOL visual - apply Refactoring UI design tactics (Adam Wathan & Steve Schoger) when building, styling, reviewing, or polishing user interfaces. Covers visual hierarchy, spacing and sizing systems, typography, HSL color palettes, shadows and depth, images, and finishing touches. Use when designing or refining UI components, pages, or layouts; when a design "looks off", feels bland, or needs polish; or when the user mentions Refactoring UI, visual hierarchy, spacing, type scale, color palette, shadows, or making something "look designed", or says "ijbol-visual".
---

# IJBOL Visual

Based on *Refactoring UI* by Adam Wathan & Steve Schoger.

Tactical design rules for engineers. The core thesis: making something "look designed" is not artistic talent — it is hierarchy, constrained systems, and a handful of repeatable tricks.

## Operating Principles

1. **Design with systems, not pixel-nudging.** Never agonize between 12px and 13px. Pick from a predefined scale and choose by process of elimination: guess a value, try its neighbors, the obvious winner remains.
2. **Hierarchy is everything.** When a UI feels noisy, the fix is almost never "add styling" — it is de-emphasizing the elements competing with what matters.
3. **Start with too much white space, then remove.** Don't add spacing until things stop looking bad — that yields the minimum, not the best. Dense UIs are fine, but only as a deliberate choice (e.g. data dashboards).
4. **Feature first, shell later.** When starting from scratch, design an actual piece of functionality (the form, the list, the card) before navigation or layout chrome. Design in grayscale first; add color last. Ship the smallest useful version — don't mock up functionality you can't build yet.

## The Systems (Default Scales)

Use these unless the project already has its own tokens. **Always prefer the project's existing design system, Tailwind config, or CSS variables over these raw values.**

### Spacing & sizing scale (base 16)

```
4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640, 768
```

No two adjacent values closer than ~25%. Small end packed tight (a few px matter at button-padding size), large end spread out (20px is invisible on a 500px card).

### Type scale (hand-crafted, px or rem — never em)

```
12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72
```

Avoid modular/ratio scales for UI work: they produce fractional pixels and too few mid-range sizes. Avoid `em` for scale values — nesting compounds them off-scale.

### Font weights

- **400 or 500** for most text, **600 or 700** for emphasis. Two weights are usually enough.
- Never go below 400 in UI text. To de-emphasize, use a lighter color or smaller size instead — not a thinner weight.

### Text color hierarchy (on light backgrounds)

- Dark grey (not pure black) for primary content
- Mid grey for secondary content
- Light grey for tertiary content

### Shadows (5-step elevation scale)

| Level | Use |
|---|---|
| xs — tight, small blur | Buttons, slightly raised cards |
| sm | Cards, hoverable items |
| md | Dropdowns, popovers |
| lg | Sticky panels, drawers |
| xl — large offset, big blur | Modals, dialogs |

Closer to the user = bigger shadow = more attention. Match shadow to z-axis intent, not aesthetics.

### Color palette structure

A real UI needs far more than 5 hex codes:

- **Greys**: 8–10 shades, darkest (text) → lightest (off-white backgrounds)
- **Primary**: 5–10 shades of 1–2 brand colors
- **Accents**: red (destructive), yellow (warning), green (positive), plus highlight colors — each with shades

Work in **HSL**, define all shades up front (100–900), never generate shades with `lighten()`/`darken()` on the fly.

## Hierarchy Cheat Sheet

- Don't rely on font size alone — use **weight and color** to differentiate; oversized primary + microscopic secondary text is the classic mistake.
- **De-emphasize to emphasize**: if the main element won't stand out, mute its competitors (softer color on inactive nav items, remove sidebar background) instead of amplifying it.
- **Grey text on colored backgrounds is wrong** — so is white-at-reduced-opacity (looks washed out/disabled, bleeds over images). Hand-pick a color: same hue as the background, adjust saturation and lightness.
- **Labels are a last resort.** Format ("$19.99", "jane@example.com") and context usually identify data. Combine label into value: "12 left in stock", "3 bedrooms". If a label is needed, style it as supporting content.
- **Visual hierarchy ≠ document hierarchy.** An `h1` can render small; section titles are usually labels, not headlines. Pick elements semantically, style them independently.
- **Balance weight and contrast**: solid icons next to text are visually "heavy" — soften their color. Thin borders that are too subtle — make them *thicker*, not darker.
- **Action hierarchy beats semantics**: one primary action (solid, high contrast), secondary (outline / soft background), tertiary (link-style). Destructive actions are NOT automatically big and red — if not primary, give them secondary/tertiary treatment, save the big red button for the confirmation step.

## Build Workflow

When implementing UI from scratch:

```
- [ ] 1. Identify the core feature; design it before any shell/nav
- [ ] 2. Block out hierarchy in grayscale (size, weight, spacing only)
- [ ] 3. Apply spacing from the scale — start too generous, trim down
- [ ] 4. Apply type scale and 2-3 text colors
- [ ] 5. Add color: backgrounds, primary actions, accents
- [ ] 6. Add depth: shadows by elevation intent, overlap where useful
- [ ] 7. Run the Polish Pass (below)
- [ ] 8. Verify states: hover, focus, active, disabled, loading, error, EMPTY
```

## Polish Pass (Quick Audit)

Run through this when something "looks off" or needs final refinement:

- [ ] Is there a single clear focal point? What competes with it? Mute the competitor.
- [ ] More space *around* each group than *within* it? (forms, lists, headings)
- [ ] All values on the spacing/type scales?
- [ ] Line length 45–75 characters? Line-height inversely proportional to font size (small text ≈1.5+, headlines ≈1–1.2)?
- [ ] Mixed font sizes on one line aligned to **baseline**, not center?
- [ ] All-caps text has increased letter-spacing? Headlines tightened?
- [ ] Numbers in tables right-aligned?
- [ ] Could any border be replaced by a shadow, background-color shift, or just spacing?
- [ ] Empty states designed (illustration + emphasized CTA, ancillary chrome hidden)?
- [ ] Accessible contrast (4.5:1 normal text, 3:1 large) — flip to dark-text-on-light-bg where dark fills steal attention?
- [ ] Anything communicated by color alone? Add icons or contrast difference.
- [ ] Feels bland? Try accent borders, icon bullets, supercharged defaults, or a background treatment.

## Topic References

Load only the file relevant to the current task:

- [hierarchy.md](hierarchy.md) — emphasis, de-emphasis, labels, actions, weight/contrast balance
- [layout.md](layout.md) — white space, spacing scale, grids vs fixed widths, responsive sizing, ambiguous spacing
- [typography.md](typography.md) — type scale, font selection, line length/height, alignment, letter-spacing
- [color.md](color.md) — HSL, building palettes and shade scales, perceived brightness, hue rotation, accessibility
- [depth.md](depth.md) — light-source logic, elevation shadows, two-part shadows, flat depth, overlap
- [images.md](images.md) — text over photos, intended sizes for icons/screenshots, user-uploaded content
- [polish.md](polish.md) — supercharged defaults, accent borders, background decoration, empty states, fewer borders, rethinking components

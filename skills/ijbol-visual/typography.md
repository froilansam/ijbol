# Typography

## Establish a type scale

Most UIs use far too many font sizes (every pixel from 10–24px somewhere). Define a scale.

- **Modular/ratio scales (4:5, golden ratio) are poor for UI work**: fractional pixels (31.25px, 39.063px — browsers round inconsistently) and too few useful mid-range sizes.
- **Hand-craft the scale** instead:

```
12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72
```

- **Use px or rem, never em** for scale values — em is relative to the parent, so nested elements compute to off-scale sizes (0.875em inside 1.25em = 17.5px, not on the scale).

## Choosing fonts

- Safest bet for UI: a neutral sans-serif, or the system stack:
  `-apple-system, Segoe UI, Roboto, Noto Sans, Ubuntu, Cantarell, Helvetica Neue`
- **Heuristic: ignore families with fewer than 5 weights** (10+ styles counting italics on Google Fonts). Bigger weight ranges correlate with craft — this filter alone removes ~85% of options.
- **Optimize for legibility**: avoid condensed faces with short x-heights for body/UI text — those are headline fonts. Headline-purposed fonts rarely work small even with added letter-spacing.
- Sort font directories by popularity — the crowd is usually right.
- Inspect sites with typography you admire and steal their choices.

## Line length: 45–75 characters

- Set paragraph measure with em-based widths: **20–35em** lands in range.
- Mixed-width content areas: keep paragraphs at readable measure even if images/components go wider. Different widths in one column looks *more* polished, not less.

## Baseline, not center

When mixing font sizes on one line (card title + small action link), align to the shared **baseline**, not vertical centers. Centering offsets the baselines and looks subtly wrong, especially when sizes sit close together. The eye already reads the baseline as the alignment reference.

## Line-height is proportional

Two inputs, both pulling line-height:

1. **Line length**: wider text needs taller line-height. Narrow column → 1.5 is fine; wide content → up to 2. (Long horizontal eye-jumps need help finding the next line.)
2. **Font size** — *inverse* relationship: small text needs generous line-height; large headlines need almost none (1.0–1.2 is fine).

Never one global value for everything.

## Links in link-heavy UIs

- The "blue and underlined" treatment is for links inside prose. In an interface where most things are links, it's overbearing.
- Emphasize most UI links subtly: heavier weight or darker color.
- Truly ancillary links can have **no default treatment** — underline/color on hover only. Discoverable, but not competing with primary actions.

## Alignment

- Left-align by default (for left-to-right languages).
- Center-align only headlines or blocks of 2–3 lines max. If one centered block runs long, **shorten the copy** rather than abandoning centering.
- **Right-align numbers in tables** — aligned decimal points make values comparable at a glance.
- Justified text needs `hyphens: auto` to avoid rivers of white space; it suits print-like, formal contexts only.

## Letter-spacing

Default rule: trust the typeface designer. Two exceptions:

1. **Tighten headlines** when using a body-purpose font (e.g. Open Sans) at display sizes — mimics purpose-built headline faces.
2. **Widen all-caps text.** Caps lose the ascender/descender variety that makes words recognizable; extra tracking restores legibility. (Think small-caps labels, badges, table headers.)

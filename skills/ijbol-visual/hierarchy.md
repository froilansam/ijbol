# Visual Hierarchy

Hierarchy is how important elements *appear* relative to one another. It is the single biggest factor in making a UI feel "designed". When everything competes for attention, the result reads as noise — even with great fonts and colors.

## Size isn't everything

Relying on font size alone produces oversized primary text and unreadable secondary text.

- Emphasize with **weight**: bolder primary text at a reasonable size beats huge text.
- De-emphasize with **color**: softer grey secondary text beats tiny text — clearer hierarchy, less readability cost.
- Stick to 2–3 text colors: dark for primary, grey for secondary, lighter grey for tertiary.
- Stick to 2 weights: 400/500 normal, 600/700 emphasis. Never under 400 for UI text — to soften something, lighten the color or shrink the size, not the weight.

## Never grey text on colored backgrounds

"Grey on white" works because of *reduced contrast against the background*, not because grey is special.

- ❌ `color: grey` on a colored panel — looks dirty and detached.
- ❌ White at reduced opacity — looks washed out or disabled, and the background bleeds through over images/patterns.
- ✅ Hand-pick a new color: **same hue as the background, adjust saturation and lightness** until the contrast feels right.

## Emphasize by de-emphasizing

When a primary element won't stand out and there's nothing left to add to it, subtract from its competitors:

- Active nav item not popping? Soften the *inactive* items instead of decorating the active one.
- Sidebar fighting the content? Remove the sidebar's background color entirely — let content sit on the page background.

## Labels are a last resort

`Label: value` formats flatten hierarchy — every datum gets equal weight.

1. **Omit the label** when format self-identifies: `jane@example.com`, `(555) 765-4321`, `$19.99` — or when context does (a department name under a person's name in a directory).
2. **Fold the label into the value**: "In stock: 12" → "12 left in stock"; "Bedrooms: 3" → "3 bedrooms". Now each datum can be styled meaningfully.
3. **If a label is truly needed** (scannable dashboards): keep it, but treat it as supporting content — smaller, lighter color/weight. The data is the star.
4. **Exception — spec-sheet pages** where users scan *for the label* ("depth", "weight"): emphasize the label slightly (darker color), but don't crush the value.

## Visual hierarchy ≠ document hierarchy

Pick HTML elements for semantics, style them for hierarchy:

- An `h1` page title like "Manage Account" can and often should be small — section titles act like labels, not headlines.
- Taken to the extreme: keep the heading in markup for accessibility but visually hide it when content speaks for itself.

## Balance weight and contrast

Bold text feels emphasized because it covers more surface area. The same physics applies elsewhere:

- **Icons are heavy.** A solid icon next to text steals emphasis. You can't "unbold" an icon — instead lower its contrast with a softer color.
- **Thin borders that disappear**: don't darken them (harsh, noisy). **Increase the width** instead — weight compensates for low contrast while keeping the soft look.

## Action hierarchy (semantics are secondary)

Every page has a pyramid of actions: usually **one** true primary, a few secondary, some tertiary.

| Tier | Treatment |
|---|---|
| Primary | Solid, high-contrast background |
| Secondary | Outline style or low-contrast background |
| Tertiary | Styled like a link — discoverable, unobtrusive |

**Destructive actions**: severity does not mean "big red bold". If delete isn't the page's primary action, give it secondary/tertiary treatment (e.g. red link or red outline). Put the big red solid button inside the *confirmation step*, where destroying actually is the primary action.

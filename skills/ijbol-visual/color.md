# Color

## Ditch hex for HSL

Hex/RGB hide visual relationships — similar-looking colors have unrelated codes. HSL encodes what the eye perceives:

- **Hue** (0–360°): position on the color wheel. 0° red, 120° green, 240° blue.
- **Saturation** (0–100%): vividness. 0% is grey regardless of hue.
- **Lightness** (0–100%): 0% black, 100% white, 50% = pure hue.

Caution: HSL ≠ HSB/HSV (design tools often use HSB). 100% Brightness with full saturation = a vivid color in HSB; 100% Lightness is always white in HSL. Browsers speak HSL.

## You need more colors than you think

Five-hex-code palette generators don't build real products. A complete palette:

| Category | What | Shades |
|---|---|---|
| Greys | Text, backgrounds, panels, borders, form controls — most of the UI | 8–10 |
| Primary | Brand color(s) for primary actions, active nav | 5–10 each, 1–2 colors |
| Accents | Red (destructive), yellow (warning), green (success), plus highlight/categorical colors | 5–10 each |

Complex UIs (graphs, calendars, tags) can legitimately need ~10 colors × 5–10 shades. Start greys from a very dark grey, not true black — pure black looks unnatural.

## Define shades up front

Never `lighten()`/`darken()` at the point of use — that's how 35 near-identical blues happen.

Building a 9-shade scale (100–900):

1. **Base (500) first**: pick the shade that would work as a button background.
2. **Find the edges**: 900 = darkest, chosen as if for text; 100 = lightest, chosen as if for a tinted background (an alert component exercises both at once — good test bed). Keep the base hue; tune saturation/lightness.
3. **Fill gaps by bisection**: pick 700 and 300 as perfect midpoints, then 800/600/400/200 the same way.

Math gets you started; finish by eye. Tweak shades when real usage demands — but resist adding *new* shades, or there's no system left.

## Don't let lightness kill your saturation

Saturation reads weakest near 0% and 100% lightness. **Increase saturation as shades move away from 50% lightness** or the light/dark ends of a scale look washed out.

### Perceived brightness & hue rotation

Hues differ in inherent perceived brightness — yellow at 50% lightness looks far lighter than blue at 50%. Brightness peaks at 60° (yellow), 180° (cyan), 300° (magenta); troughs at 0° (red), 120° (green), 240° (blue).

Use this when a base color is already at 100% saturation:

- **Lighten** by rotating hue toward the nearest bright peak (60°/180°/300°).
- **Darken** by rotating toward the nearest dark trough (0°/120°/240°).
- Classic application: yellow's darker shades rotate toward orange → warm and rich instead of muddy brown.
- **Limit: 20–30° of rotation**, or it reads as a different color. Combine with lightness adjustments freely.

## Greys don't have to be grey

Saturate greys to set the UI's temperature:

- Cool: a touch of blue.
- Warm: a touch of yellow/orange.

Remember to bump saturation at the light/dark ends of the grey scale too, or those shades drift back toward neutral and look inconsistent.

## Accessibility without ugliness

WCAG: **4.5:1** contrast for normal text (<~18px), **3:1** for large text.

- **Flip the contrast**: white-on-color needs surprisingly dark backgrounds, which then dominate the page. Use *dark colored text on a light tint of the color* instead (e.g. dark green on pale green badge) — accessible, supportive, not shouty.
- **Colored text on colored backgrounds** (e.g. secondary text in a dark panel): adjusting lightness alone drives you to near-white. Rotate the hue toward a brighter hue (cyan/magenta/yellow) to gain contrast while staying colorful.

## Don't rely on color alone

Color supports meaning; it must never be the only carrier (red-green color blindness is common):

- Trend metrics: add ▲/▼ icons, not just green/red text.
- Graph lines: differentiate by **contrast** (light vs dark) rather than distinct hues — light/dark differences survive color blindness.

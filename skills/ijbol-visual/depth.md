# Depth

## Emulate a light source — light comes from above

All raised/inset perception comes from mimicking overhead light.

### Raised elements (buttons, cards)

- **Lighten the top edge**: top border or inset `box-shadow` with small positive y-offset, in a hand-picked lighter color — *not* semi-transparent white, which desaturates the underlying color.
- **Shadow below**: small, dark `box-shadow` with slight positive y-offset and **tight blur (a couple of px)** — the element blocks light from the area beneath it. Think of the crisp shadow under a wall outlet.

### Inset elements (wells, inputs, checkboxes)

Inverted: the user looks slightly downward, so only the bottom lip catches light.

- **Lighten the bottom edge**: bottom border or inset shadow with negative y-offset.
- **Dark inset shadow at the top**: small positive-offset inset shadow — the surrounding surface blocks light at the top of the recess.

Don't chase photo-realism — borrow just enough physics to convey depth, stop before it gets busy.

## Shadows convey elevation

Shadow size = position on a virtual z-axis = how much attention the element demands.

- Small/tight: slightly raised — buttons.
- Medium: floating above the UI — dropdowns, popovers.
- Large/soft with big offset: closest to the user — modals.

**Define a 5-step shadow scale**: pick the smallest and largest, interpolate the middle three roughly linearly. Choose shadows by asking "where should this sit on the z-axis?", never by fiddling per-element.

### Shadows + interaction

- Drag: increase the shadow on pickup — the item visibly lifts above its siblings.
- Button press: shrink or remove the shadow — the element pushes into the page.

## Two-part shadows

The best shadows combine two layers, each with a job:

1. **Large, soft**: significant y-offset, large blur — the cast shadow from a direct light source.
2. **Tight, dark**: minimal offset, small blur — the ambient-light-starved crevice right under the object.

The second shadow must **fade as elevation increases** (objects far from a surface lose that tight contact shadow): distinct at low elevations, nearly or fully gone on modals.

## Flat designs still have depth

- **Color as depth**: lighter than the background reads raised; darker reads inset. Works in any style.
- **Solid shadows**: short vertical offset, **zero blur** — stands an element off the page without breaking the flat aesthetic.

## Overlap creates layers

- Offset a card across the boundary between two background sections.
- Make an element taller than its parent so it overlaps both sides.
- Works at small scale too (e.g. carousel controls half-on, half-off the image).
- **Overlapping images clash** — give each an "invisible border" in the background color so a clean gap separates the layers.

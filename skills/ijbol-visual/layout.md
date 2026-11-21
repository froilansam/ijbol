# Layout & Spacing

## Start with too much white space

White space should be *removed* until the design looks right, not added until it stops looking bad. Adding-until-okay yields the minimum tolerable breathing room; starting generous and trimming yields "just enough" in the context of the full UI.

**Dense UIs are legitimate** — dashboards that need everything on one screen can trade airiness for density. Just make density a deliberate decision, never the default.

## The spacing & sizing system

Never deliberate between 120px and 125px. Use a constrained scale defined in advance.

- **Linear scales fail**: "multiples of 4" doesn't help choose. What matters is *relative* difference — 12px → 16px is a 33% jump (huge), 500px → 520px is 4% (invisible).
- **Rule: adjacent values at least ~25% apart.**
- Base of 16 works well (divides cleanly, matches browser default font size):

```
4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640, 768
```

Workflow payoff: need space under an element? Grab a scale value. Not enough? The next one up is probably perfect.

## You don't have to fill the screen

- If the content needs 600px, give it 600px. Spreading content to fill 1400px makes it *harder* to read; padding around the edges never hurt anyone.
- Applies per-section too: nothing must be full-width just because the nav is.
- **Struggling with a small component on a big canvas? Shrink the canvas.** Design at ~400px mobile-first, then expand and fix only what felt compromised.
- A narrow form in a wide page feeling unbalanced? Don't widen the form — split supporting text/help content into a second column.
- Converse holds: if something genuinely needs lots of space, take it. Don't cram.

## Grids are overrated

Percentage-based grid columns are not a religion:

- **Sidebars should usually be fixed-width**, sized to their content. A "25% column" sidebar grows uselessly on wide screens and crushes below its minimum on narrow ones. Let the main content area flex instead.
- **Don't shrink an element before you need to.** A login card at "6 of 12 columns" can end up *narrower on large screens than medium ones*. If 500px is optimal, use `max-width: 500px` and only shrink when the viewport is smaller than that.
- Inside components, only use percentages when you actually want the thing to scale.

## Relative sizing doesn't scale

- A 45px headline over 18px body (2.5em) on desktop should NOT stay 2.5em on mobile — 14px body × 2.5 = 35px headline, way too big. Small screens want maybe 1.5–1.7×.
- **Rule: large elements shrink faster than small ones.** The size gap between big and small elements compresses on small screens.
- Same inside components: button padding defined as a multiple of font size makes large buttons feel zoomed, not bigger. Padding should get *disproportionately* generous at large sizes and tighter at small sizes. Fine-tune properties independently.

## Avoid ambiguous spacing

When groups rely on spacing (no borders/backgrounds) to read as groups, **space around a group must exceed space within it**:

- Form: gap between label and its input < gap between form groups — otherwise labels float ambiguously between fields.
- Articles: more space *above* a section heading than below it.
- Lists: gap between bullets > line-height within a bullet.
- Horizontal layouts have the same failure mode (e.g. icon + text pairs in a row).

Interfaces that are hard to parse always look worse.

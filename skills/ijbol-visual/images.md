# Images & Photography

## Use good photos

Bad photos sink otherwise great designs. Two options: hire a professional, or use quality stock (e.g. Unsplash). **Never design around placeholders expecting to swap in smartphone photos later** — it never works.

## Text over images needs consistent contrast

Photos are dynamic — light and dark regions in one frame defeat any single text color. Reduce the image's dynamics:

1. **Overlay**: semi-transparent black (for light text) or white (for dark text) across the image.
2. **Lower the image contrast** directly — more surgical than an overlay; compensate by adjusting brightness.
3. **Colorize**: lower contrast → desaturate → solid brand-color fill with `multiply` blend mode. Bonus: makes arbitrary photos cohere with brand colors.
4. **Text shadow as a glow**: large blur radius, **no offset** — adds contrast exactly where the text is. Combine with mild image-contrast reduction.

## Everything has an intended size

- **Don't scale up icons.** A 16–24px icon at 3–4× looks chunky and amateur, vector or not. Need to fill a big slot? Keep the icon near its native size and **enclose it in a shape with a background color**.
- **Don't scale down screenshots.** A full-desktop screenshot shrunk 70% renders app text at ~4px. Instead: capture at a smaller viewport (tablet layout), use a **partial screenshot**, or draw a simplified UI illustration (text as lines) for tight spaces.
- **Don't scale down detailed logos** either — favicons need a redrawn, radically simplified version at target size so *you* control the compromises, not the browser's resampler.

## Beware user-uploaded content

No control over user images' contrast, color, or crop, so defend the layout:

- **Fix the shape and size**: render in fixed containers, crop to fill (`object-fit: cover` / `background-size: cover`). Never let intrinsic aspect ratios drive layout.
- **Prevent background bleed** (white photo on white UI): a **subtle inner box-shadow** keeps the image's shape — borders clash with photo colors, while an inner shadow is nearly invisible. A semi-transparent inner border also works.

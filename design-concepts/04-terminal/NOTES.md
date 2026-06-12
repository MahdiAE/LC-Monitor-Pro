# 04 — Terminal

## Thesis
Authority through density. The executive surface is a financial terminal: one ruled board of
hairline-separated regions, zero cards, where color is never decoration — every hue is a signal
(amber = warn, green-teal = ok, red = breach, cyan = info/selection) and every status also
carries a glyph (■ ▲ ● ○ ◌ ▼) and a word, so meaning survives without color. Modern instrument,
terminal discipline: no CRT cosplay, no scanlines, no fake tickers.

## Tokens
- Dark-first near-black, faintly cool: bg `oklch(0.155 0.006 240)`, two surface steps, three ink
  steps, hairlines as low-alpha ink (`--line` .11, `--line2` .22).
- Light = "paper terminal": chroma-0 off-white `oklch(0.965 0 0)`, near-black ink, identical
  hairline structure, signal hues darkened (ok 0.49L, warn 0.50L, bad 0.50L, info 0.46L).
- Every text/background pair computed (OKLCH→sRGB→WCAG): worst small-text pair is light-mode
  ink3 on surface2 at 5.0:1; all signals ≥ 5.0:1 on bg in both themes; accent buttons 6.9:1
  (light) / 10.4:1 (dark).
- Radii 1–2px, semantic z-scale, single ease (`cubic-bezier(.22,1,.36,1)`), 120–150ms state
  transitions only.

## Type & Arabic
IBM Plex Mono carries all data: figures, codes, table numerics, timestamps, meters (tabular-nums
everywhere). IBM Plex Sans for labels/prose; IBM Plex Sans Arabic swaps in via `html[lang=ar]`
with letter-spacing zeroed (tracking breaks Arabic joining). Uppercase only on real system
labels (region titles, severity codes, key hints). Bilingual strings are paired `.en/.ar` spans
toggled by `<html lang>` — pre-paint head script reads `?theme=` / `?lang=`, so all four states
are first-paint correct; in-shell toggles (and T / L keys) flip attributes and rewrite the URL.
Numbers stay Western digits; codes are `direction:ltr; unicode-bidi:isolate`. The trend SVG
mirrors geometry only (`scaleX(-1)` on the plot group); axis labels are HTML, month strip is a
real `<table>` whose order flips natively in RTL.

## IA
- **dashboard.html** — master status line (brand · path · as-of · controls) → verdict band
  (the dominant moment: ■ ATTENTION REQUIRED + driver clause + metric tape) → 12-col hairline
  grid: COMPLIANCE (54px figure, 12-mo sparkline, monthly mini-table), PENALTY EXPOSURE
  (4 driver contracts with segmented inline meters + "3 further · 7.6M"), REVIEW QUEUE
  (counts + aged log lines), PIPELINE, PORTFOLIO & DELIVERIES (dotted-leader ledger rows),
  ALERTS as a timestamped log tail → key-hint footer chrome.
- **site.html** — top module bar with terminal codes + full names (DSH/RFP/EVL/CON/RCV/REV/
  PEN/SUP/SYS); CON active. Workbench: query bar (q/ search + status/entity/report filters +
  shown-count), dense 10-row table (sticky header, sticky first column under 900px, sorted-
  column marker, selected row C-2024-0210, gap column with signed deltas), totals strip
  (Σ value / averages / Σ penalty / pagination with a real disabled control), and a docked
  command-style form panel: exception-letter goods receipt with BoQ select, quantity in an
  inline error state, origin radios driving NP-evidence enablement (disabled + reason for
  foreign origin), letter reference, note, primary/secondary/discard actions.

## What it fixes
Skeleton: board + module bar replace sidebar/topbar/card-grid. Coherence: one mono-led system,
one hairline vocabulary, one glyph language across both artifacts. Hierarchy: a single verdict
moment dominates; everything else is staged density. Craft: computed AA in both themes, true
RTL mirroring (including SVG), keyboard chrome that actually works.

## Deviation
The direction's sample header read "LC 86.2 ▲0.3", but the canonical trend ends 86.5 → 86.2,
so the board shows ▼0.3 M/M and pairs it with ▲3.1 vs Jul 2025 — data wins over the sketch.

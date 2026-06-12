# 03 — Ministry

## Thesis
Authority through state gravitas. The tool reads as if issued by the Local Content &
Government Procurement Authority itself: a letterhead band, a decree-like compliance
ruling under a seal gauge, ruled report sections, an official register, and a numbered
government form — yet it stays a fast, modern workbench (native controls, 150–220ms
state-only motion, dense Linear-grade table).

## Tokens
- Chrome: committed deep institutional green `oklch(0.305 0.062 172)` carries the
  letterhead band + verdict field (~40% of the dashboard's first viewport) and the
  active nav state. No blue→violet anywhere.
- Field: true off-white `oklch(0.976 0.003 170)` (chroma 0.003 — not cream); ink is
  near-black with a green cast `oklch(0.215 0.02 170)`.
- Gold budget: exactly one metallic accent per page — the seal-gauge arc (dashboard),
  a single 2px keyline under the topbar (site). Everything else is green + rules + type.
- Semantic: ok/warn/bad/info pairs (text ≥4.5:1 on their tints, both themes, computed).
- Dark: green-black `oklch(0.182 0.012 172)`; accent/status colors re-tuned for AA.

## Type & Arabic
- EN display: Source Serif 4 (civic serif) — page titles, section heads, the ruling.
- AR display: Amiri — `html[lang=ar]` swaps `--font-display`, so Arabic headlines are
  calligraphy-rooted, not transliterated serif.
- UI/body both languages: IBM Plex Sans Arabic (one family, native Arabic).
- Data: IBM Plex Mono for references; `tabular-nums` everywhere data appears; numbers
  stay Western digits with `direction:ltr; unicode-bidi:isolate` token spans.

## IA
- Dashboard = a state document: letterhead (authority EN/AR, reference no., issue
  date) → Compliance Ruling No. 47/2026 with seal gauge (86.2%, hand-drawn SVG) and a
  ruled key-figure strip → Sections I–IV under heavy full-width rules: exposure
  schedule (footed table, not bars-in-cards), trend as a ledger figure (SVG, real
  axes, RTL-mirrored via scaleX with counter-flipped labels), portfolio/pipeline as
  ruled schedules, alerts as a true numbered memoranda `<ol>` (numbers earn their place).
- Site = official register: left nav as a table-of-contents index (Parts I–V grouping
  the 13-page map), slim letterhead topbar with register search; Contracts &
  Monitoring as a print-ruled table (row numbers, sticky header + sticky first columns
  on horizontal scroll, text-first status designations with glyphs, summary strip,
  toolbar, pagination with a genuinely disabled Previous). Form LC-7 (exception
  letter, C-2024-0210) inline by default: numbered fields, required marks, native
  radios/select/file, one inline format error, disabled Print voucher, audit-log note.

## Four states / responsive / a11y
- `?theme=dark|light` + `?lang=ar|en` read before first paint; in-shell toggles sync
  the URL and cross-links. Full string swap via `data-ar` attributes incl. placeholders
  and aria-labels; logical properties throughout so RTL truly mirrors.
- 1440 / 1024 (nav collapses to an Index drawer with scrim + ESC) / 390 (tables go
  horizontal-scroll with sticky columns; form stacks). Verified zero horizontal
  overflow in all four states at 390.
- Landmarks, skip link, focus-visible rings (chrome-aware color), status never
  color-only (glyph + text), `prefers-reduced-motion` kills all transitions.

## What it fixes
Skeleton: document/register replaces sidebar+card-grid. System: one ruled, seal-and-
serif family across both artifacts. Hierarchy: a single dominant ruling answers
"are we OK" in 5 seconds. Craft: computed AA contrast, bidi-safe numerals, real
states on every control. Deliberate: "SAR"/refs stay Latin in AR per app convention.

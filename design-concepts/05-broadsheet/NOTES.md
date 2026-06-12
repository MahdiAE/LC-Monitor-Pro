# 05 — Broadsheet

## Thesis
Authority through clarity: the dashboard is the front page of a beautifully typeset audit
report. Swiss/editorial discipline — paper-white, near-black ink, hairline rules, one accent.
The workbench is a print-quality register that still behaves like a modern power tool.

## Tokens
- Paper: pure white light / warm near-black "night print" dark (`oklch(0.165 0.008 75)`).
  Ink is warm-neutral; surfaces stay chroma ≤ 0.003 (no cream).
- **One accent: deep oxblood** `oklch(0.45 0.15 25)` (dark: `oklch(0.67 0.15 24)`), used <10% —
  verdict headline, links/selection/current-page, chart endpoint, primary action. All pairs
  computed (script, not eyeballed): every text/bg combo ≥ 4.5:1 in both themes.
- Status = muted ink-leaning ok/warn/bad/info, always paired with glyph (✓ ○ ▲ ✕ —) +
  small-caps designation; never color-only.
- Radii 1–2px (print corners); semantic z scale; spacing s1–s8.

## Type & Arabic
- EN: Newsreader (editorial serif) for the verdict, headline numerals, standfirst, captions;
  Inter Tight (grotesk, guaranteed tabular figures) for UI, labels, tables, buttons.
- AR: Noto Naskh Arabic carries the display voice (masthead reads as typeset Arabic print —
  «مرصد المحتوى المحلي», verdict «يتطلب الانتباه.»); IBM Plex Sans Arabic for UI. Font tokens
  swap on `html[lang=ar]`; tracking/uppercase reset for Arabic. Western digits + tabular-nums
  everywhere data appears. RTL fully mirrors; trend chart is re-drawn by JS with reversed
  x-axis and right-gutter y labels.
- `text-wrap: balance` on headings; verified zero overflow at 1440/1024/390 × EN/AR via
  headless render (24 state×width combos).

## IA rationale
- **Dashboard = front page.** Masthead (date/edition furniture, wordmark, double rule) →
  lead story: oxblood verdict headline + 70ch standfirst naming the drivers + 136px serif
  86.2% figure → four hairline-ruled columns: Fig. 1 fine-line trend with printed axes,
  Fig. 2 penalty schedule as ruled figure table (7 contracts = SAR 19.6M, totalled),
  portfolio/pipeline as dotted-leader stat lines, alerts as a news-brief column with bold
  lead-ins. Colophon closes the page. 5-second read: verdict → number → drivers → schedule.
- **Site = register.** Two-deck masthead chrome (wordmark + furniture; sticky hairline nav,
  current page marked by weight + accent underline; "More" groups registry pages; collapses
  to a Sections menu ≤900px). Contracts table: hairline rules only, no zebra/boxes, generous
  leading, end-aligned tabular numerals, sticky header + sticky first column under horizontal
  scroll, sortable-looking headers (active sort: Value ↓), selected row (C-2024-0210) tinted.
  Exception-letter receipt form inline and visible by default: editorial labels, one inline
  error (quantity > remaining BoQ), logic-driven disabled control (evidence n/a for Foreign
  origin), full hover/focus-visible states, audit-log footnote.

## What it fixes (of the 4 failures)
1. Skeleton restructured: no sidebar/card-grid — masthead + editorial columns / register.
2. One coherent family: single accent, hairline vocabulary, two-axis type system everywhere.
3. Dominant hierarchy: one verdict headline + one headline numeral; everything else defers.
4. Craft: computed AA contrast, true RTL chart mirroring, print details (double rules,
   dotted leaders, figure captions), reduced-motion-safe single brand moment (line draw).

## Deviations
- Penalty schedule adds 3 plausible non-top-10 contracts (C-2023-0066, C-2024-0095,
  C-2025-0140) so the 7-contract / SAR 19.6M total reconciles with the canonical 4.

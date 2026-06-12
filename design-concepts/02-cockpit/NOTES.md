# 02 — Cockpit

## Thesis
Authority through operational density. The sidebar is gone: a blue→violet **command bar**
(structural surface, not decoration) plus a persistent **status rail** carry the live verdict —
compliance 86.2% ▼0.3, exposure SAR 19.6M, 2 breaches, 4 overdue — onto every screen.
Dark-first ops room; light mode is full "day ops" parity. Dense ≠ cluttered: hairline-ruled
panels on one grid, strict spacing, one dominant verdict.

## Tokens
- OKLCH throughout; `:root` = light, `[data-theme=dark]` overrides. Core set per brief plus
  `--tint-*` (color-mix badge fills) and `--bar-*` (command-bar surface, fixed in both themes —
  the blue→violet gradient is a material, never text).
- Semantic z scale `--z-nav/sticky/overlay/modal/toast`; radii 4/6/10; data colors
  ok/warn/bad/info tuned to ≥4.5:1 small-text contrast on their actual surfaces (computed).

## Type & Arabic
- Bricolage Grotesque only for the brand mark and the verdict annunciator. IBM Plex Sans Arabic
  is the single UI family (carries Latin too — one bilingual voice). JetBrains Mono carries all
  data with `tabular-nums`; the mono stack falls back to Plex Arabic **before** `monospace` so
  mixed strings ("19.6M ر.س", "متأخر 21 يومًا") keep correct Arabic shaping inside data cells.
- URL params (`?theme=`, `?lang=`) applied pre-paint in a head script; full string swap via
  `data-en/data-ar` (+ aria/placeholder variants). Logical properties everywhere; sparkline SVG
  geometry mirrors via `scaleX(-1)` with all chart text living in HTML so it never flips.
  Western digits kept by convention.

## IA
- **dashboard.html** — annunciator (verdict + drivers) above an asymmetric 12-col board of six
  hairline panels, each with its own internal grammar: compliance (big figure + 12-mo gradient
  sparkline + achieved-vs-target bullet), exposure (ranked mono bars for the 4 penalty drivers
  + remainder line), review queue (aging histogram + overdue badge), pipeline (stage flow),
  ops-log alerts (timestamp + severity tag), portfolio ledger (proportion bars).
- **site.html** — Contracts & Monitoring workbench: toolbar filters with visible `/` shortcut
  (wired), 10-column sticky-header table (compact rows, mono numerics, achieved-delta inline,
  shape+text status badges), summary strip (Σ value / Σ exposure / status census), pagination,
  kbd hint row; docked inspector: "Log goods receipt — exception letter" for C-2024-0210 with
  live consequence note, inline quantity error, disabled NP-evidence control (foreign origin),
  hover/focus-visible/disabled/error states on all controls.
- Nav curates the 23 pages: Dashboard · Pipeline · Contracts · Receiving · Reviews · Penalties
  · More (Suppliers, Certificates, Blacklist, Audit Log, Reminders, Settings).

## Fixes for the four failures
1. **Template skeleton** → no sidebar, no card grid: command bar + status rail + ruled board.
2. **Incoherence** → one token system, one component vocabulary shared verbatim by both files.
3. **Weak hierarchy** → single verdict moment (annunciator + rail), panels sized by stakes;
   18 equal KPIs replaced by 6 differently-structured instruments.
4. **Default craft** → computed AA contrast, true RTL mirroring (incl. chart geometry), reduced
   -motion variants, keyboard affordances, four-state parity from one URL.

## Deviation
Direction text said "86.2% ▲0.3"; the canonical trend ends 86.5 → 86.2, so the rail shows
▼0.3 vs May (dataset wins — numbers must be defensible), with ▲3.1 YoY shown on the dashboard.

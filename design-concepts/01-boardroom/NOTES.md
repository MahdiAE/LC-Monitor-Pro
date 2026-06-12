# 01 — Boardroom

## Thesis
Authority through composure. The familiar skeleton (left nav, topbar, table) is kept but
rebuilt at maximum craft: the dashboard is an editorial page an executive *reads*, the
workbench is a quiet instrument an officer *trusts*. The brand gradient is jewelry —
logo mark + one active indicator (chart endpoint / nav dot) — never material.

## Tokens
Light-first: near-white cool `--bg` (oklch 0.985), white surfaces, deep navy ink ramp
(`--ink/--ink2/--ink3` all ≥5.2:1 on every surface they sit on — computed, not eyeballed).
Dark = refined deep navy (oklch 0.165 0.022 262), not gray. Semantic colors are text-safe
oklch pairs (`--ok/--warn/--bad/--info` + `*-tint` chips, all ≥5.5:1). Radii 5/8/14,
semantic z-scale (`--z-nav…--z-toast`). All color/space/type via custom properties.

## Type & Arabic strategy
- Bricolage Grotesque: display only — verdict sentence, dashboard section heads, page H1.
- IBM Plex Sans: all UI; IBM Plex Sans Arabic swapped in via `html[lang=ar]` (display
  falls back to Plex Arabic 700 since Bricolage has no Arabic — weight carries the voice).
- JetBrains Mono + `tabular-nums` for every numeral: figures, table cells, ledgers, axes.
- i18n: paired `.en/.ar` spans switched by CSS from a pre-paint `<html lang>` set by an
  inline head script reading `?theme=&lang=`; attributes (placeholder/aria/title) synced
  by JS. Numbers stay Western digits. RTL is fully logical-property driven; the trend
  geometry mirrors via `scaleX(-1)` on the SVG group while labels stay HTML (never mirrored).

## Dashboard IA (verdict-first, no card grammar repeated)
1. Written verdict (Bricolage sentence, warn-underlined clause) + named drivers with links.
2. Three consequential figures as a hairline ledger row — typographic, unboxed, no gradient.
3. Generous 12-month SVG line (gradient endpoint = the one active indicator).
4. Penalty exposure as thin horizontal bar list (7 contracts, sums to 19.6M).
5. Portfolio/pipeline as subordinate dotted-leader ledgers; alerts as severity-worded list rows.
Every section has a different structure: sentence → ledger → chart → bars → dl → list.

## Site shell
Unboxed rail: no fill, hairline `border-inline-end`, grouped nav with counts; active item =
accent tint + gradient dot. Minimal topbar (search ⌘K, theme/lang designed in, avatar).
Contracts table: comfortable density, hairline rules, mono numerals, dot+text status chips,
sticky header + sticky first column, columns ordered so status/target/achieved/penalty are
visible without scroll at 1440. Exception-letter panel as inline stationery aside: Foreign
origin selected → National-Product upload disabled (explained), quantity shows live inline
error vs BoQ balance, mono reference field, primary/secondary actions, routing note.

## Fixes vs the 4 failures
1. Template-like → editorial dashboard + unboxed rail; structure varies per section.
2. Incoherence → one token system, one icon stroke (1.7), one control vocabulary.
3. Weak hierarchy → a single dominant verdict; exactly three figures; all else subordinate.
4. Default craft → computed AA contrast everywhere, true 4-state parity, structural
   responsive (drawer rail, scrolling table with sticky column), reduced-motion variants,
   0px horizontal overflow at 390 in both languages.

## Deviations
Three penalty contracts beyond the 10-row table (C-2022-0186, C-2024-0095, C-2023-0067)
are invented to honor "7 contracts / SAR 19.6M"; values reconcile exactly.

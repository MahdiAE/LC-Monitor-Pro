# LC Monitor Pro — Redesign Concepts: Shared Build Brief

Five paired design directions for LC Monitor Pro (Saudi LCGPA Local Content compliance tool).
Each direction = `dashboard.html` (executive dashboard) + `site.html` (app shell + Contracts &
Monitoring workbench + form fragment). This brief is the shared contract; each concept has its
own direction spec given separately.

## Why this exists (diagnosis of current app)

The current v56 app fails on all four axes: (1) template-like — sidebar + topbar + card-grid
skeleton reads as generic admin; (2) incoherent system — 56 versions of accretion; (3) weak
hierarchy — 18 same-weight KPI cards, no dominant verdict; (4) default-grade craft. Every
concept must fix all four: **restructure the skeleton, design one coherent family, stage a
dominant hierarchy, and show premium craft.**

## Product context (from PRODUCT.md)

- Register: **product** (expert workbench), but the executive dashboard may lean **brand**.
- Personality: **authoritative, efficient, premium**. Government-grade; no whimsy, no mascots.
- Users: procurement/compliance officers (daily, dense work), reviewers, executives (skim).
- Anti-references: legacy gov portals AND generic Bootstrap admin templates.
- Principle: "Consequence must be legible" — compliance %, shortfalls, penalties unambiguous
  and never color-only.

## Hard requirements (every file)

1. **Self-contained**: single HTML file, inline `<style>` + `<script>`, vanilla only. Fonts via
   Google Fonts `<link>` (preconnect + display=swap). Charts are **hand-drawn inline SVG** —
   no Chart.js, no libraries.
2. **Tokens**: all color/space/type via CSS custom properties on `:root`, dark overrides on
   `[data-theme=dark]`. Use this canonical core (extend freely):
   `--bg --surface --surface2 --ink --ink2 --ink3 --line --line2 --accent --ok --warn --bad
   --info --r --rs --rl --font-display --font-ui --font-ar --font-mono` plus a semantic
   z-index scale (`--z-nav --z-sticky --z-overlay --z-modal --z-toast`). OKLCH for new colors.
3. **Four states, full parity**: light/dark × EN/AR. Must read URL params **before first
   paint** (inline head script):
   - `?theme=dark|light` → sets `data-theme` on `<html>`
   - `?lang=ar|en` → sets `lang`, `dir="rtl"`, switches ALL visible strings to Arabic
   Working in-shell toggles for theme and language too (designed as part of the UI, not a
   debug bar). RTL must truly mirror: layout, padding, icons with direction, charts axes.
   Numbers stay Western digits (the app's convention), `tabular-nums` everywhere data appears.
4. **Responsive**: desktop (1440), tablet (1024), mobile (390). Structural responses (collapse
   nav, reflow tables to cards or horizontal scroll with sticky first column), not shrunken
   desktop. No text overflow at any breakpoint in either language.
5. **Accessibility**: WCAG AA (body ≥4.5:1, large/bold ≥3:1 — verify, don't eyeball muted
   grays on tinted backgrounds); visible `:focus-visible` rings; semantic landmarks/headings;
   status never color-only (pair with text/icon/shape); `prefers-reduced-motion` alternative
   for every animation. All animations must enhance an already-visible default — never gate
   content visibility on a class-triggered reveal (headless renderers must capture full content).
6. **Motion**: 150–250ms, ease-out (quart/expo). State and feedback only on the workbench;
   the dashboard may take one considered brand moment. No bounce. No page-load choreography
   on site.html.

## Absolute bans (rewrite the element if you're about to do one)

- Side-stripe borders (colored `border-left/right` > 1px on cards/alerts/list items)
- Gradient text (`background-clip: text`)
- Glassmorphism as default
- The hero-metric template (big number + small label + gradient accent, repeated)
- Identical card grids (same-size icon+heading+text cards repeated)
- Tiny uppercase tracked eyebrow above every section; numbered section markers (01/02/03) as scaffolding
- Display fonts in UI labels/buttons/data; custom scrollbars; reinvented form controls
- Arbitrary z-index (999); text overflowing containers at any breakpoint
- Cream/sand/beige body backgrounds as "warmth" default

## File contract

```
design-concepts/<NN-name>/dashboard.html
design-concepts/<NN-name>/site.html
design-concepts/<NN-name>/NOTES.md   (≤60 lines: thesis, tokens summary, type & Arabic
                                      strategy, IA rationale, what it fixes of the 4 failures)
```

## Canonical dataset (both artifacts must agree; use realistic values, EN + AR)

Portfolio (as of 12 June 2026): 47 contracts (31 active), portfolio value SAR 2.84B,
weighted LC compliance 86.2% (avg target 38.4%, avg achieved 33.1%), penalty exposure
SAR 19.6M across 7 contracts, 12 pending evidence reviews, 6 missing reports (4 overdue),
National Product purchases delivered SAR 412M, Mandatory-List items delivered SAR 268M.
Pipeline: 5 draft RFPs, 3 ready, 4 open evaluations, 19 contracts awarded YTD.
Overall verdict: **Attention required / يتطلب الانتباه** (driven by 2 breaches + 4 overdue reports).

Trend (monthly weighted compliance, Jul 2025→Jun 2026):
83.1, 83.8, 84.6, 84.2, 85.0, 85.7, 85.2, 85.9, 86.4, 86.0, 86.5, 86.2

Contracts table (Contracts & Monitoring page; columns ≈ contract no, supplier, scope,
end-user entity, value, LC target, LC achieved, status, next report, penalty exposure):

| # | Supplier EN | Supplier AR | Scope | Value SAR | Target | Achieved | Status | Penalty |
|---|---|---|---|---|---|---|---|---|
| C-2024-0142 | National Industrialization Co. | شركة التصنيع الوطنية | Medical equipment | 184.0M | 40% | 36.2% | At risk | 3.1M |
| C-2023-0098 | Zamil Industrial | الزامل للصناعة | HVAC systems | 96.5M | 35% | 38.9% | Compliant | — |
| C-2025-0031 | Astra Industrial | أسترا الصناعية | Pharma supplies | 142.7M | 45% | 41.0% | Watch | — |
| C-2024-0210 | Saudi Cable Co. | شركة الكابلات السعودية | Power cabling | 58.3M | 30% | 22.4% | Breach | 4.8M |
| C-2025-0117 | Alfanar | الفنار | Switchgear | 210.9M | 42% | 44.6% | Compliant | — |
| C-2024-0077 | Saudi Ceramics | الخزف السعودي | Sanitary ware | 23.8M | 28% | 27.1% | Watch | — |
| C-2026-0009 | Obeikan Investment Group | مجموعة العبيكان | Packaging | 31.2M | 33% | — (new) | No report | — |
| C-2023-0154 | Riyadh Cables | كابلات الرياض | MV cables | 77.4M | 36% | 31.5% | At risk | 2.2M |
| C-2024-0188 | Al Yamamah Steel | اليمامة للصلب | Rebar supply | 49.0M | 30% | 33.8% | Compliant | — |
| C-2025-0203 | Advanced Petrochemical | المتقدمة للبتروكيماويات | Polymer feedstock | 122.5M | 38% | 35.9% | At risk | 1.9M |

End-user entities: Ministry of Health (وزارة الصحة), Royal Commission for Jubail & Yanbu
(الهيئة الملكية للجبيل وينبع), Saudi Water Authority (هيئة المياه السعودية), NEOM (نيوم),
Ministry of Education (وزارة التعليم).

Status vocabulary (never color-only): Compliant ملتزم · Watch مراقبة · At risk معرّض للخطر ·
Breach مخالفة · No report لا يوجد تقرير. Review states: Approved معتمد · Pending قيد المراجعة ·
Rejected مرفوض · Overdue متأخر.

Alerts (dashboard): ① C-2024-0210 report overdue 21 days (Saudi Cable, Breach) ② C-2024-0142
LC shortfall widened to 3.8 pts ③ 12 evidence items awaiting review > 5 days ④ Mandatory List
April 2026 update: 14 BoQ lines need re-matching ⑤ C-2025-0031 final report due in 9 days.

Key UI terms AR: Executive Dashboard لوحة المتابعة التنفيذية · Contracts & Monitoring العقود
والمراقبة · Local Content المحتوى المحلي · Compliance الالتزام · Penalties الغرامات · Reports
التقارير · Receiving الاستلام · Reports Review مراجعة التقارير · RFP Preparation إعداد المنافسات ·
Bid Evaluation تقييم العروض · Suppliers الموردون · Alerts التنبيهات · Settings الإعدادات ·
Search بحث · Export تصدير · Portfolio value قيمة المحفظة · Penalty exposure الغرامات المحتملة ·
Target المستهدف · Achieved المحقق · Contract value قيمة العقد.

## dashboard.html

Executive surface: the 5-second read must answer "are we OK, where is the money at risk, what
needs my decision." IA is yours to design (this is the point — see your direction spec), but
limit to metrics above. Include: a dominant verdict moment, the compliance trend, penalty
exposure with its drivers, pipeline/portfolio context, alerts, and a path to drill (visual
affordance is enough; links can be #). Charts: inline SVG, axis labels real, RTL-mirrored.

## site.html

The full app shell in your direction's language: navigation (your structure — the 23-page map
exists: Dashboard, RFP Preparation, Bid Evaluation, Contracts & Monitoring, Receiving, Reports
Review, Penalties, Suppliers, Certificates, Blacklist, Audit Log, Reminders, Settings…
curate/group as your IA argues), topbar/command affordances, theme + language controls, and the
**Contracts & Monitoring** page active: filter/search row, the 10-contract table above (dense,
sortable-looking, sticky header, row affordances), summary strip, pagination or count.
Plus a **form fragment visible by default** (not behind a click): an inline panel/drawer for
"Log goods receipt — exception letter" for C-2024-0210: fields = BoQ line select, quantity
received, origin (Local/Foreign radio), National Product evidence upload, exception letter
reference, note textarea; primary/secondary actions; one field showing an inline validation
error state. All interactive components show real states (hover, focus-visible, disabled on
one control, error).

## Self-review before finishing (do this, fix what fails)

1. Open each file in all four states — does any string remain untranslated? Does RTL truly mirror?
2. Contrast-check every text/background pair you weren't sure about (compute, don't guess).
3. The bans list — scan your own CSS for each.
4. At 390px in Arabic: anything overflowing or truncated?
5. Would a Linear/Stripe-fluent user trust the workbench? Would a minister trust the dashboard?

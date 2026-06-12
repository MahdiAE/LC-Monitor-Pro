# Product

## Register

product

> Primary surface is **product** — the daily experience is a dashboard/workbench: tables, forms, evidence review, receiving, penalties. A secondary **brand**-leaning dimension exists on the login screen, the executive dashboard hero, and exported stakeholder PDFs (penalty notices, bid-evaluation MoM, supplier cards). When working those specific surfaces, lean brand; everywhere else, product.

## Users

- **Procurement & compliance officers** at a Saudi government entity (LCGPA context) — the primary daily users. They monitor Local Content (LC) compliance across many active contracts, often in long desk sessions, moving through high volumes of line items, evidence, and reports. Bilingual EN/AR; SAR currency.
- **End users (receiving)** — confirm received goods quantities and origin (Local/Foreign) against ordered BoQ lines and attach National Products evidence; flag exception letters.
- **Contract managers / reviewers** — approve or reject submitted evidence and goods receipts; the gatekeepers for what counts toward compliance.
- **Executives** — consume the dashboard for oversight: portfolio LC achievement, penalties exposure, pipeline health. They skim, they don't operate.

Their context is high-stakes and regulatory: numbers must be defensible, penalties are real money, and the output is official. They are experts in their domain, not novices to be hand-held.

## Product Purpose

Monitor and enforce Local Content compliance across the full Saudi LCGPA procurement lifecycle in one tool: RFP / BoQ preparation → supplier registry & submissions → bid evaluation & award → contract monitoring → goods receiving with national-product evidence → periodic & final reports review → penalty calculation — all surfaced through an executive dashboard.

Success looks like: compliance status, shortfalls, and penalties are **accurate, traceable, and visible at a glance**; nothing falls through the cracks as work moves between procurement stages; and an officer can defend any number on screen to an auditor. The app is a **system of record**, not a set of disconnected forms.

## Brand Personality

Three words: **authoritative, efficient, premium.**

- **Voice** — precise, official, confident. States facts and consequences plainly (shortfalls, deviation penalties, approval outcomes) without drama or chattiness.
- **Tone** — businesslike and reassuring. Communicates regulatory weight while making a complex process feel tractable.
- **Emotional goal** — the user trusts the system. It should feel like government-grade software that a senior officer is comfortable staking a compliance decision on — and modern enough that it doesn't feel like a chore to open.

## Anti-references

- **Cluttered legacy government portals** — dense gray tables, tiny fonts, no visual hierarchy, 2010-era enterprise sprawl. This is the thing the product replaces; it must never feel like it.
- **Generic Bootstrap admin templates** — stock cards, default blues, zero identity, interchangeable with any CRUD app. The committed type/color identity exists precisely to escape this.

Note: the escape from these is through **clarity and committed identity**, not playfulness. It should still read as serious compliance software — no mascots, no jokey copy, no consumer-SaaS whimsy.

## Design Principles

1. **System of record, not a form.** Every screen should read as audit-ready: numbers, evidence, and penalties are explained and defensible, not just captured. A user should be able to point at any figure and say where it came from.
2. **Respect the expert.** Power-tool efficiency over hand-holding — dense where density helps, fast paths for repeated actions, keyboard-friendly, no unnecessary confirmation theater for daily work.
3. **Bilingual as a first-class citizen.** Arabic / RTL is structural, not a translation layer bolted on. Layout mirrors correctly and Arabic reads as natively as English.
4. **Premium over template.** Hold the committed identity (Bricolage Grotesque display, the blue→violet brand gradient, real dark mode) so the product never collapses into generic admin scaffolding.
5. **Consequence must be legible.** Compliance %, local shortfalls, deviation penalties, and approval/receipt states are unambiguous at a glance — and never color-only where the meaning is high-stakes.

## Accessibility & Inclusion

- **WCAG AA contrast** — body text ≥ 4.5:1, large/bold text ≥ 3:1. Watch the muted-gray-on-tinted-white trap in the light theme; bump toward ink when close.
- **Full keyboard navigation** with visible focus states (the `--ring` token exists for this) — government software baseline.
- **Full Arabic / RTL parity** — `dir="rtl"` correctness, IBM Plex Sans Arabic, mirrored layout and exported PDFs. Arabic is first-class, not a bolt-on.
- Secondary but encouraged: keep status meaning non-color-only and respect `prefers-reduced-motion` on dashboard/KPI animation.

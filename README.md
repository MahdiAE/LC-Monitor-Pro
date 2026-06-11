# LC Monitor Pro v56

A single-file web application for **Local Content (LC) monitoring and procurement management**
(Saudi LCGPA context — bilingual EN/AR, SAR currency).

It covers the full procurement lifecycle: RFP preparation, bid evaluation, contract monitoring,
penalties, supplier registry/submissions/evaluation, reports review, and an executive dashboard.

## Run it

It's a self-contained HTML file. Either:

- **Open directly** — double-click `LC Monitor Pro v56 - Redesign.html`, or
- **Serve locally** (recommended, so the bundled libraries load cleanly):
  ```bash
  python3 -m http.server 8000
  # then open http://localhost:8000/LC%20Monitor%20Pro%20v56%20-%20Redesign.html
  ```

## Files

- `LC Monitor Pro v56 - Redesign.html` — the application.
- `vendor/chart.umd.min.js` — Chart.js 4.4.1 (bundled locally so charts work on networks that block CDNs).
- `vendor/xlsx.full.min.js` — SheetJS 0.18.5 (Excel import/export), bundled locally.

The app falls back to the CDN copies automatically if the local files are missing.

## Highlights in v56

- Redesigned executive dashboard (hero, LC process funnel, animated clickable KPIs, gradient backdrop).
- BoQ line-item pipeline: RFP BoQ → supplier submission → bid evaluation → award → contract line items (with VAT 15% auto-calc, evidence for Goods).
- Local-bundled Chart.js / xlsx, settings submenu toggle, T&C file persistence, MoM PDF popup fallback, and more.

Data is stored in the browser's `localStorage`.

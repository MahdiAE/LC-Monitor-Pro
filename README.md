# LC Monitor Pro v56

A **single-file** web application for **Local Content (LC) monitoring and procurement management**
in the Saudi **LCGPA** context — bilingual EN/AR, SAR currency, no backend.

It covers the full procurement lifecycle in one tool:
**RFP / BoQ preparation → supplier registry & submissions → bid evaluation & award →
contract monitoring → goods receiving (national-product evidence) → reports review →
penalty calculation → executive dashboard.**

State is stored entirely in the browser's `localStorage`. No build step, no server.

> **Working on this with an AI agent / new session?** Read **[`CLAUDE.md`](CLAUDE.md)** first — it has the
> architecture map, the localStorage keys, the gotchas, and the commit/deploy workflow.

---

## Run it

It's a self-contained HTML file. **Serving it locally is recommended** (so the bundled
libraries and file handling work cleanly):

```bash
python3 -m http.server 8000
# then open:
# http://localhost:8000/LC%20Monitor%20Pro%20v56%20-%20Redesign.html
```

Opening the file directly (double-click / `file://`) mostly works too, but local serving is the safe path.

**Live (GitHub Pages, auto-deployed from `main`):**
`https://mahdiae.github.io/LC-Monitor-Pro/LC%20Monitor%20Pro%20v56%20-%20Redesign.html`

**Download the latest as a zip:**
`https://github.com/MahdiAE/LC-Monitor-Pro/archive/refs/heads/main.zip`

---

## Files

| Path | What it is |
|---|---|
| `LC Monitor Pro v56 - Redesign.html` | **The entire application** (~8,500 lines, 16 script blocks). |
| `index.html` | Root redirect to the app (for GitHub Pages). |
| `vendor/chart.umd.min.js` | Chart.js 4.4.1, bundled locally (works on networks that block CDNs). |
| `vendor/xlsx.full.min.js` | SheetJS 0.18.5 (Excel import/export), bundled locally. |
| `PRODUCT.md` | Product & design brief (used by the `impeccable` design workflow). |
| `CLAUDE.md` | Onboarding + workflow notes for contributors / AI agents. |

The app falls back to CDN copies of Chart.js / SheetJS automatically if the local `vendor/` files are missing.

---

## Key features

- **Executive dashboard** — verdict command band, LC process funnel, clickable KPIs, semantic-status color, real dark mode.
- **BoQ line-item pipeline** — RFP BoQ → supplier submission → bid evaluation → award → contract line items, with VAT 15% auto-calc and goods evidence in receiving.
- **LCGPA Mandatory List matcher** — import the multi-tab Mandatory List Excel in Settings; in RFP prep, an **on-device semantic (no-AI) ranker** suggests the top-5 matches per BoQ line and fills the Etimad / "Mandatory List Code". The read-only code is surfaced to suppliers in their submission BoQ.
- **Goods receiving** — confirm received quantities & origin (Local/Foreign) vs. ordered lines, attach National Products evidence, exception-letter flow, deviation penalties.
- **Reports review** — approve/reject submitted evidence and goods receipts.
- **Bilingual EN/AR** — Arabic / RTL is first-class (mirrored layout, IBM Plex Sans Arabic, translated exports), not a bolt-on.
- **Local-bundled libraries**, settings sub-nav, T&C file persistence, PDF exports (penalty notices, bid-evaluation MoM, supplier cards).

---

## How we work on it (workflow)

1. **One file.** Almost every change is an edit to `LC Monitor Pro v56 - Redesign.html`. Find your spot with `grep -n "function NAME"`.
2. **Verify headlessly.** Puppeteer (an `npm` dependency) drives the served page; ad-hoc scripts assert behavior and capture screenshots. There is no `npm test`; run scripts from the repo root.
3. **Keep it bilingual & semantic.** User-facing strings go through the `L(en, ar)` helper; status meaning stays semantic, never color-only.
4. **Commit only when asked**, then push. GitHub Pages redeploys within ~a minute; a "missing" change is almost always a stale cache — hard-refresh (Ctrl/Cmd-Shift-R) or re-download the zip.
5. **Never commit** test scripts (`*.js`), screenshots (`*.png`), `node_modules/`, or the proprietary source Excel (`القائمة الإلزامية ...xlsx`). See `.gitignore` and `CLAUDE.md`.

Design direction follows the `impeccable` skill (product register) — see `PRODUCT.md`.

---

Data lives in `localStorage`; clearing site data resets the app to its seeded demo state.

# CLAUDE.md — Agent onboarding for LC Monitor Pro

Read this first. It exists so a fresh session can start working on this project with **minimum friction and errors**. It captures the things that are *not* obvious from the code and the gotchas that have already bitten us.

---

## 1. What this project is

**LC Monitor Pro** is a **single-file** HTML/CSS/vanilla-JS web app for Saudi **Local Content (LCGPA)** procurement & compliance. No build step, no framework, no backend. State lives in the browser's `localStorage`.

- **The app is one file:** [`LC Monitor Pro v56 - Redesign.html`](LC%20Monitor%20Pro%20v56%20-%20Redesign.html) — ~8,500 lines, **16 `<script>` blocks**, all globals (function declarations, monkeypatch/override chains, IIFEs). When you edit, you are editing this file 99% of the time.
- **Repo:** `github.com/MahdiAE/LC-Monitor-Pro` — **PUBLIC**, branch `main`.
- **Deploy:** GitHub Pages auto-builds from `main`. Live URL:
  `https://mahdiae.github.io/LC-Monitor-Pro/LC%20Monitor%20Pro%20v56%20-%20Redesign.html`
  (`index.html` at the root just redirects to it.)
- **Download zip:** `https://github.com/MahdiAE/LC-Monitor-Pro/archive/refs/heads/main.zip`
- Product/design context: [`PRODUCT.md`](PRODUCT.md) (the `impeccable` skill's project brief — register = **product**).

The domain: full procurement lifecycle — RFP/BoQ prep → supplier registry & submissions → bid evaluation & award → contract monitoring → goods receiving with national-product evidence → reports review → penalty calc → executive dashboard. Bilingual **EN/AR**, **SAR** currency.

---

## 2. Run & test it

It is self-contained. **Serve it** (don't `file://` it — the bundled libs and some fetches want http):

```bash
python3 -m http.server 8000
# http://localhost:8000/LC%20Monitor%20Pro%20v56%20-%20Redesign.html
```

**Headless verification uses Puppeteer**, already installed in `node_modules/` (`package.json` dep). Run test scripts **from the project root** so `node_modules` resolves:

```bash
node yourtest.js     # launches puppeteer against http://localhost:8000/...
```

There is **no `npm test`**. Verification is ad-hoc puppeteer scripts that load the page, drive it, and assert / screenshot. Pattern that works:

```js
const puppeteer = require('puppeteer');
(async () => {
  const b = await puppeteer.launch();
  const p = await b.newPage();
  const errs = []; p.on('console', m => m.type()==='error' && errs.push(m.text()));
  await p.goto('http://localhost:8000/LC%20Monitor%20Pro%20v56%20-%20Redesign.html', {waitUntil:'networkidle0'});
  // drive the app via page.evaluate, assert, screenshot
  await b.close();
})();
```

---

## 3. Hard-won gotchas (read before you touch code)

1. **`let`-scoped globals are NOT `window` properties.** `curRFP`, `rfpBoQ`, `lang`, etc. are declared with `let`/`const` at script-block top level. In a puppeteer `page.evaluate`, `window.curRFP = ...` does **nothing** — assign the **bare** name: `curRFP = ...; rfpBoQ = ...`. (`var`-declared globals and explicit `window.x =` helpers *do* attach to window.)

2. **Closure-captured arrays must be mutated in place, not reassigned.** e.g. `_subBoQItems` is closed over by `v55_renderSubBoQ`. `window._subBoQItems = [...]` won't update the binding the renderer reads. Do `_subBoQItems.length = 0; _subBoQItems.push(...)`.

3. **The bundled SheetJS UMD disables Node `fs`.** `XLSX.readFile(path)` throws in Node. To parse Excel in a Node/puppeteer test:
   ```js
   const buf = require('fs').readFileSync(path);
   const wb = XLSX.read(buf, {type:'buffer'});
   ```
   In the browser the app reads `File` objects via `FileReader` → `XLSX.read(arrayBuffer,{type:'array'})`, which is fine.

4. **Vendored libs with CDN fallback.** `vendor/chart.umd.min.js` (Chart.js 4.4.1) and `vendor/xlsx.full.min.js` (SheetJS 0.18.5) are committed and loaded locally first, with a CDN fallback `<script>` if the local file is missing (see the top of the HTML). Keep both paths working.

5. **Bilingual is structural.** Use the `L(en, ar)` helper for every user-facing string. `lang` global + `applyLang(lang)` translate the DOM; `body.rtl` flips layout. A `window.L` global shim exists (added this session) so dashboard-block code can call it. Arabic text is normalized (tashkeel/alef/taa-marbuta strip) for matching — see the MLNP matcher.

6. **Background `pkill`/compound shell can abort your commit.** A `pkill -f http.server` returning non-zero exit has aborted `&&`-chained commit scripts mid-way. Run **commit/push as their own step**, not chained behind a kill.

---

## 4. Map of the app (where things live)

Anchors drift as the file grows — `grep -n "function NAME"` to relocate. Approximate as of v56:

| Area | Function(s) | ~line |
|---|---|---|
| Storage (quota-safe) | `lsSet` / `lsGet` | 2557 |
| Page navigation | `nav(p, el)` → shows `#page-<p>`, then `renderCurrentPage()` | 2596 |
| Seed/demo data | `seed()` | 5011 |
| Bilingual DOM translate | `applyLang` | 4858 |
| Settings sub-nav | `openSettingsNav` / `navSettSec` | 4897 |
| Bid evaluation entry | `addBidderManual` | 3176 |
| **MLNP Excel import** | `importMLNP` (multi-tab parser) | 4072 |
| **MLNP matcher** | `mlRank(desc, topN)` + IIFE (`window.mlRank`) | 6711 |
| RFP BoQ render | `renderBoQ` | 6540 |
| Supplier submission BoQ | `v55_extractRFPBoQ`, `v55_renderSubBoQ` | ~7940 |
| Dashboard data | `gatherDashboardData` | 6041 |
| Supplier submission modal | `openSubModal` | 5659 |

**Pages** are `<div class="page" id="page-<key>">`; nav keys: `dashboard, rfp, bids, contracts, review, penalties, alerts, settings, reminders, audit, portfolio, certs, supeval, blacklist, contractadmin, permissions, suppliers, subs, supreq, receiving, entry, import`. `renderCurrentPage()` dispatches to the matching `render*()`.

**localStorage keys** are all `lc*`-prefixed: `lcDB` (contracts), `lcRFPS`, `lcBIDS`, `lcSubs`, `lcSuppliers`, `lcSupEvals`, `lcUsers`, `lcRoles`, `lcRolePerms`, `lcCerts`, `lcMLNP` (Mandatory List), `lcLang`, `lcKPI`, `lcAudit`, etc. (full list: `grep -oE "ls(Get\|Set)\('lc[A-Za-z]+'" file`).

### The BoQ line-item pipeline (the spine of the app)
RFP BoQ line (`rfpBoQ[i]`, with `desc`, `isMandatory`, `mlCode`, `qty`, `uom`, `nature`) → flows into supplier submission BoQ (`v55_extractRFPBoQ` builds `_subBoQItems`) → bid evaluation (`addBidderManual` maps `isMandatory`+`mlCode` to `isMandatoryRFP`/`isMandatoryResp`) → award → contract line items (VAT 15%, goods evidence in receiving). Touch any stage knowing it feeds the next.

### MLNP semantic matcher (LCGPA Mandatory List)
On-device, **no AI/model** — lexical ranking. Settings imports the multi-tab LCGPA Excel (`importMLNP`, skips overview + exception tabs, detects columns by stable **Arabic header stems**, stores records to `MLNP_LIST` + `lcMLNP`). In RFP-prep BoQ, `mlRank` ranks each line against the list (bilingual normalize + Arabic `ال` strip + IDF-weighted token overlap + char-bigram Dice fuzzy; title 0.75 / definition 0.25) and returns **top-5** with the Etimad code (`الرمز في منصة اعتماد`). The picker is non-destructive: every line defaults to "None"; Apply only sets `isMandatory`+`mlCode` on picked lines. The supplier-submission BoQ shows that code read-only in the **"Mandatory List Code"** column (after "Mandatory (RFP)"). Plan: `/home/mk/.claude/plans/validated-enchanting-canyon.md`.

---

## 5. Commit / push / deploy workflow

- **Commit and push only when the user asks.** (This user routinely asks to push + share the zip at the end of a task — that's the standing pattern, but still wait for the ask.)
- **Co-author trailer on every commit:**
  ```
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
  ```
- After pushing, the change is **live on GitHub Pages within ~1 min**. If the user "doesn't see" a change, it's almost always a **stale cache or an old downloaded zip** — tell them to hard-refresh (Ctrl/Cmd-Shift-R) or re-download the zip. Verify deploy with `curl -s <live-url> | grep -c "<your new string>"` before assuming a code problem.

### Do NOT commit (already in `.gitignore`, keep it that way)
- `node_modules/`, `package.json`, `package-lock.json`
- **Test/diagnostic scripts** — `/*.js` (root-level `.js`), `diag*.js`, `verify*.js`, `dbg.js`, `shot.js`
- **Screenshots** — `*.png`
- `.claude/`, `mockups/`
- **The user's Arabic source Excel** — `القائمة الإلزامية للجهات الحكومية (أبريل 2026).xlsx` (proprietary input, never commit). It is **not** currently gitignored by name — do not `git add -A` it; add files explicitly or confirm it's excluded.

---

## 6. Design system (for any UI work)

The `impeccable` skill drives design (register = **product**; see [`PRODUCT.md`](PRODUCT.md)). Identity:
- **Type:** Bricolage Grotesque (display `--fn`), IBM Plex Sans Arabic (`--far`), JetBrains Mono (`--fm`).
- **Brand:** blue→violet gradient `#2563eb → #7c3aed`. Light + real dark theme (CSS custom props, `body.rtl` for Arabic).
- **Status color is semantic only** (`st-ok / st-warn / st-bad / st-neutral`) — never rainbow, never color-only for high-stakes meaning.
- Append new CSS before the **final** `</style>`; insert new markup before `</body>` per `.impeccable/live/config.json`.
- Honor the absolute bans in the skill (no side-stripe borders, no gradient text, no glassmorphism-by-default, etc.) and WCAG AA contrast.

---

## 7. Quick checklist for a typical change

1. `grep -n` the function/anchor in the HTML; read the surrounding block.
2. Make the edit (single file). Keep bilingual `L(en,ar)`, status semantics, and the BoQ pipeline intact.
3. Start `python3 -m http.server 8000`; write a throwaway puppeteer script to drive + assert (mind the `let`-global and closure gotchas above). Screenshot if visual.
4. Sanity-check no new console errors.
5. If the user asked: commit (co-author trailer), push, verify live with `curl`, share the zip link.

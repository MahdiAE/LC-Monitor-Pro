import { chromium } from '/home/mk/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import { mkdirSync } from 'fs';

const ROOT = 'http://localhost:8077/design-concepts';
const concepts = ['01-boardroom', '02-cockpit', '03-ministry', '04-terminal', '05-broadsheet'];
const artifacts = ['dashboard', 'site'];
const states = [
  { theme: 'light', lang: 'en' },
  { theme: 'dark', lang: 'en' },
  { theme: 'light', lang: 'ar' },
  { theme: 'dark', lang: 'ar' },
];
const viewports = [
  { name: 'desktop', width: 1440, height: 900 },
  { name: 'tablet', width: 1024, height: 768 },
  { name: 'mobile', width: 390, height: 844 },
];

const only = process.argv.slice(2); // optional filters: substrings of the shot name

const browser = await chromium.launch();
let n = 0, fails = [];
for (const c of concepts) {
  mkdirSync(`design-concepts/screenshots/${c}`, { recursive: true });
  for (const a of artifacts) {
    for (const vp of viewports) {
      const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
      for (const s of states) {
        const name = `${a}-${s.theme}-${s.lang}-${vp.name}`;
        if (only.length && !only.some(f => `${c}/${name}`.includes(f))) continue;
        const url = `${ROOT}/${c}/${a}.html?theme=${s.theme}&lang=${s.lang}`;
        try {
          await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
          await page.evaluate(() => document.fonts.ready);
          await page.waitForTimeout(400);
          await page.screenshot({ path: `design-concepts/screenshots/${c}/${name}.png`, fullPage: true });
          n++;
        } catch (e) {
          fails.push(`${c}/${name}: ${e.message.split('\n')[0]}`);
        }
      }
      await page.close();
    }
  }
}
await browser.close();
console.log(`captured ${n} screenshots`);
if (fails.length) { console.log('FAILURES:'); fails.forEach(f => console.log(' ' + f)); process.exit(1); }

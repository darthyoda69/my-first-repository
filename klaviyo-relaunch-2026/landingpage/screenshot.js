const { chromium, devices } = require('playwright');
const fs = require('fs');
const body = fs.readFileSync(process.argv[2], 'utf8');
const out = process.argv[3];
// Hülle wie Prestige main-page: Theme-Header, schmaler Container, .prose, Seitentitel
const shell = `<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{margin:0;font-family:Arial}.th{background:#fff;border-bottom:1px solid #eee;padding:18px 20px;font:700 20px Arial;letter-spacing:1px}
.section-spacing{padding:48px 0}.container--xs{max-width:680px;margin:0 auto;padding:0 20px}.prose p{margin:1em 0}.prose h2{font-size:30px;margin:1.2em 0 .5em}
.ft{background:#f4f4f4;padding:40px 20px;color:#888}</style></head><body>
<div class="th">pimpertz · Theme-Header</div>
<section class="shopify-section--main-page"><div class="section-spacing"><div class="container container--xs"><div class="section-stack">
<div class="section-header"><h1 class="h2">Black Week 2026 – Bis zu –40 %</h1></div><div class="prose">${body}</div></div></div></div></section>
<div class="ft">Theme-Footer</div></body></html>`;
const ph = `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600"><rect width="600" height="600" fill="#F5F2EA"/><text x="300" y="310" text-anchor="middle" font-family="Arial" font-size="34" fill="#B5AE9F">Produktbild</text></svg>`;
(async () => {
  const browser = await chromium.launch();
  const runs = [
    ['mobile-pre', devices['iPhone 13'], ''], ['mobile-pre-full', devices['iPhone 13'], '', true],
    ['desktop-pre', {viewport:{width:1440,height:900}}, '', true],
    ['mobile-vip', devices['iPhone 13'], '2026-11-23T11:00'], ['mobile-live', devices['iPhone 13'], '2026-11-26T12:00'],
  ];
  for (const [name, dev, now, full] of runs) {
    const ctx = await browser.newContext({...dev, deviceScaleFactor: 2});
    const page = await ctx.newPage();
    await page.route(/cdn\.shopify\.com/, r => r.fulfill({status:200, contentType:'image/svg+xml', body: ph}));
    await page.route(/klaviyo\.com/, r => r.abort());
    const url = 'https://pimpertz.de/pages/black-week' + (now ? '?bw_now=' + now : '');
    await page.route(url, r => r.fulfill({status:200, contentType:'text/html; charset=utf-8', body: shell}));
    await page.goto(url, {waitUntil:'networkidle'}).catch(()=>{});
    await page.waitForTimeout(1200);
    const sw = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    await page.screenshot({path: `${out}/${name}.png`, fullPage: !!full});
    console.log(name, 'horizontal overflow px:', sw);
    await ctx.close();
  }
  await browser.close();
})();

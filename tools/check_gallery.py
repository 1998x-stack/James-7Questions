"""Offline browser smoke test of Gallery, Case Overview and framework interactions.

Uses set_content because browser navigation to file:/localhost can be disabled in
sandboxed environments; verifies links as document-relative destinations.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
async def load(page,path):
    await page.set_content(path.read_text(encoding='utf-8'),wait_until='load')
async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
        for width,height,device in [(1440,900,'desktop'),(390,844,'mobile')]:
            page=await browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
            errors=[]
            page.on('pageerror',lambda e:errors.append(str(e)))
            await load(page,DOCS/'index.html')
            await page.screenshot(path=str(DOCS/f'_gallery_{device}.png'),full_page=True)
            assert await page.locator('.gallery-card').count()==2
            assert await page.locator('.gallery-card[href$="/index.html"]').count()==2
            assert await page.locator('.gallery-count').inner_text()=='当前显示 2 / 2 个案例'
            await page.locator('#search').fill('美团')
            assert await page.locator('.gallery-card:visible').count()==1
            casehref=await page.locator('.gallery-card:visible').get_attribute('href')
            assert casehref=='cases/meituan-group-buying-2010-2015/index.html'
            await load(page,DOCS/casehref)
            assert await page.locator('.lens-card').count()==4
            await page.screenshot(path=str(DOCS/f'_overview_{device}.png'),full_page=True)
            lenshref=await page.locator('.lens-james').get_attribute('href')
            assert lenshref=='james.html'
            await load(page,(DOCS/casehref).parent/lenshref)
            assert await page.locator('.back-link').get_attribute('href')=='index.html'
            await page.locator('#next').click()
            assert (await page.locator('#pagerstate').inner_text()).startswith('2 /')
            await load(page,DOCS/'index.html')
            scroll=await page.evaluate('document.documentElement.scrollWidth')
            print(device,'gallery cards: 2; overview lenses: 4; browser overflow:',scroll-width,'errors:',errors)
            assert scroll<=width+2,(device,scroll,width)
            assert not errors,errors
            await page.close()
        page=await browser.new_page()
        await load(page,DOCS/'cases/ctrip-mobile-2012-2015/index.html')
        assert await page.locator('.lens-card').count()==4
        assert await page.locator('.lens-porter').get_attribute('href')=='porter.html'
        await browser.close()
if __name__=='__main__':asyncio.run(main())

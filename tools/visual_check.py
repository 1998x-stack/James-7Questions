import asyncio
from pathlib import Path
import subprocess, time
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'docs'/'cases'/'ctrip-mobile-2012-2015'
async def main():
 server=subprocess.Popen(['python','-m','http.server','8765','--bind','127.0.0.1','--directory',str(ROOT/'docs')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 time.sleep(.4)
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  for name in ['index','porter','socratic','james','dmaic']:
   page=await browser.new_page(viewport={'width':1440,'height':960},device_scale_factor=1)
   errors=[]
   page.on('pageerror',lambda e:errors.append(str(e)))
   path=ROOT/'docs/index.html' if name=='index' else BASE/f'{name}.html'
   await page.set_content(path.read_text(encoding='utf-8'),wait_until='load')
   await page.screenshot(path=str(ROOT/'docs'/f'_preview_{name}.png'),full_page=True)
   h=await page.title()
   if name!='index':
    await page.locator('#next').click()
    count=await page.locator('#pagerstate').inner_text()
    print(name,'title',h,'pager',count,'errors',errors)
    assert count.startswith('2 / ')
    await page.keyboard.press('ArrowLeft')
    assert (await page.locator('#pagerstate').inner_text()).startswith('1 / ')
   else:
    links=await page.locator('.library-card').count()
    print(name,'title',h,'cards',links,'errors',errors)
    assert links==4
   assert not errors,errors
   await page.close()
  mobile=await browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
  await mobile.set_content((BASE/'james.html').read_text(encoding='utf-8'),wait_until='load')
  await mobile.screenshot(path=str(ROOT/'docs/_preview_mobile.png'),full_page=True)
  print('mobile scrollWidth',await mobile.evaluate('document.documentElement.scrollWidth'),'viewportWidth',390)
  await browser.close()
 server.terminate()
asyncio.run(main())

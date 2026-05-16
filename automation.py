import asyncio
from playwright.async_api import async_playwright

async def run_automation():
    print('🚀 بدء الأتمتة الاحترافية...')
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://news.ycombinator.com/')
        title = await page.title()
        print(f'✅ تم الدخول للموقع: {title}')
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_automation())

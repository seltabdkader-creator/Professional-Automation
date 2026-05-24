import asyncio
from playwright.async_api import async_playwright
import sys

async def run_automation():
    print('🚀 بدء الأتمتة الاحترافية...')
    try:
        async with async_playwright() as p:
            # تشغيل المتصفح مع إعدادات محسنة
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1280, 'height': 720},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            )
            page = await context.new_page()
            
            print('🌐 الانتقال إلى Hacker News...')
            await page.goto('https://news.ycombinator.com/', wait_until="networkidle", timeout=60000)
            
            title = await page.title()
            print(f'✅ تم الوصول بنجاح. عنوان الصفحة: {title}')
            
            # التقاط لقطة شاشة للتأكد من العمل
            await page.screenshot(path='hn_professional.png')
            print('📸 تم حفظ لقطة الشاشة: hn_professional.png')
            
            await browser.close()
            print('🏁 انتهت العملية بنجاح.')
    except Exception as e:
        print(f'❌ حدث خطأ غير متوقع: {e}')
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(run_automation())

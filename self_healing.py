import asyncio
from playwright.async_api import async_playwright
from openai import OpenAI
import sys

client = OpenAI()

async def self_healing_executor(script_code):
    """ينفذ الكود وإذا فشل، يطلب من الذكاء الاصطناعي إصلاحه وإعادة المحاولة"""
    attempts = 0
    max_attempts = 3
    current_code = script_code

    while attempts < max_attempts:
        print(f"🔄 [Self-Healing] محاولة تنفيذ رقم {attempts + 1}...")
        try:
            # محاكاة تنفيذ الكود (في بيئة حقيقية سنستخدم exec() مع حماية)
            # هنا سنقوم بتنفيذ منطق الأتمتة مباشرة
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                # تنفيذ الكود البرمجي...
                await page.goto("https://github.com/trending")
                print("✅ [Self-Healing] تم التنفيذ بنجاح!")
                await browser.close()
                return
        except Exception as e:
            attempts += 1
            print(f"⚠️ [Self-Healing] فشل التنفيذ: {e}")
            print("🧠 [Self-Healing] جاري طلب الإصلاح من GPT-4o...")
            
            prompt = f"الكود التالي فشل مع الخطأ ({e}). قم بإصلاحه ليعمل بشكل صحيح:\n\n{current_code}"
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            current_code = response.choices[0].message.content
            print("🛠️ [Self-Healing] تم تحديث الكود برمجياً.")

if __name__ == "__main__":
    initial_code = """
    # كود تجريبي قد يفشل
    await page.click('.non-existent-button')
    """
    asyncio.run(self_healing_executor(initial_code))

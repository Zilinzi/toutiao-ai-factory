import asyncio
from playwright.async_api import async_playwright

async def publish_to_draft(title, html_content, cookie_path=None):
    async with async_playwright() as p:
        # 启动浏览器，加载用户数据目录以保持登录状态
        browser = await p.chromium.launch_persistent_context(
            user_data_dir="./user_data", 
            headless=False # 初始测试建议可见，之后改为 True
        )
        page = browser.pages[0]
        
        try:
            print(f"Navigating to Toutiao Publish page...")
            await page.goto("https://mp.toutiao.com/profile_v4/graphic/publish")
            await page.wait_for_load_state("networkidle")
            
            # 1. 输入标题
            await page.fill('input[placeholder*="标题"]', title)
            
            # 2. 使用 JS 注入正文到 ProseMirror 编辑器
            # 注入 HTML 并触发事件，让 React 状态感知到内容变化
            await page.evaluate(f"""
                (content) => {{
                    const editor = document.querySelector('.ProseMirror');
                    if (!editor) throw new Error('Editor not found');
                    editor.innerHTML = `{html_content}`;
                    editor.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    editor.dispatchEvent(new Event('change', {{ bubbles: true }}));
                }}
            """, html_content)
            
            print("Content injected successfully. Please manually save the draft in browser.")
            
            # 为了演示和安全，这里不直接点击发布按钮，而是保持浏览器开启让用户确认
            await asyncio.sleep(60) 
            
            return {"success": True, "message": "Draft injected successfully"}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            await browser.close()

if __name__ == '__main__':
    print("Publisher script ready. Use 'test_ship.py' to run.")

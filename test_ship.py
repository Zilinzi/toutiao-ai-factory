import asyncio
import sys
import os

# 确保导入路径正确
sys.path.append('/home/hermes/toutiao_ops')
from toutiao_renderer import render_for_toutiao
from toutiao_publisher import publish_to_draft

async def main():
    title = "AI Agent 自动化实战：如何构建你的内容工厂"
    md_content = """
# 走进 AI 内容工厂

在这个时代，最高效的创作不再是个体战，而是**人机协同的流水线**。

## 核心架构
1. **搜集层**：利用 Cron 定时抓取全网热点。
2. **创作层**：分层 Skill 确保去 AI 味。
3. **发布层**：通过 CDP 注入 HTML。

> 结论：自动化解决的是效率，而价值由人类决定。
"""
    
    print("Step 1: Rendering Markdown to HTML...")
    html = render_for_toutiao(md_content)
    
    print("Step 2: Attempting to publish to Toutiao Drafts...")
    # 运行发布流程
    result = await publish_to_draft(title, html)
    print(f"Result: {result}")

if __name__ == '__main__':
    asyncio.run(main())

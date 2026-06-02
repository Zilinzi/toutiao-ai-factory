# 🚀 头条 AI 内容工厂 (Toutiao AI Content Factory)

这是一个端到端的 AI 内容创作与发布流水线，旨在将 AI 写作从“生成文本”升级为“工业级内容运营”。它通过分层技能编排、专业排版渲染和浏览器自动化，将高质量文章直接投递至今日头条草稿箱。

## 🌟 核心功能

- **分层创作体系 (Layered Writing)**：内置 `toutiao-writer` 技能，通过 5 层 quality-control 过滤（风格去 AI 味 $\rightarrow$ 结构爆款化 $\rightarrow$ 论据增强 $\rightarrow$ 毒舌编辑评审 $\rightarrow$ 合规扫描），确保产出内容具有高点击率且不像 AI 写的。
- **专业级渲染**：`toutiao_renderer.py` 将 Markdown 转换为适配头条号编辑器的 HTML，内置“安静奢华”风格的内联样式，无需手动调整排版。
- **浏览器自动化投递**：利用 Playwright CDP 协议直接操作浏览器，将内容注入到 ProseMirror 编辑器，绕过不稳定的 API，实现 100% 成功率的投递。
- **人机协作闭环**：所有内容同步至 **草稿箱 (Draft Box)**，由创作者进行最后一次审阅并发布，最大程度降低封号风险。

## 🛠 快速上手

### 1. 安装依赖
```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. 运行与登录
执行测试脚本：
```bash
python test_ship.py
```
**关键步骤**：首次运行会弹出一个浏览器窗口。请在窗口中**手动登录你的头条号**。登录状态将被保存在 `user_data` 目录中，后续运行将实现全自动静默注入。

## 📐 技术架构
`热门话题采集` $\rightarrow$ `toutiao-writer (分层写作)` $\rightarrow$ `toutiao_renderer (HTML渲染)` $\rightarrow$ `toutiao_publisher (CDP投递)` $\rightarrow$ `头条号草稿箱`

## ⚠️ 安全红线
- **严禁全自动发布**：本工具仅支持投递至草稿箱。请务必通过人工审阅后点击“发布”，以规避平台的 Bot 检测。
- **频率控制**：建议在自动化流程中加入随机延迟，模拟真实人类操作习惯。

## 📜 许可证
MIT License

# 🚀 Toutiao AI Content Factory

A high-fidelity automation pipeline for creating and publishing articles to Toutiao (今日头条).

## 🌟 Features
- **Layered AI Writing**: Uses a 5-layer quality control system (Style $\rightarrow$ Architecture $\rightarrow$ Evidence $\rightarrow$ Review $\rightarrow$ Compliance).
- **Pro-Level Rendering**: Converts Markdown to Toutiao-optimized HTML with a custom "Quiet Luxury" aesthetic.
- **Browser-Based Publishing**: Uses Playwright CDP to inject content directly into the ProseMirror editor, bypassing fragile APIs.
- **Human-in-the-Loop**: Pushes content to the **Draft Box**, allowing a final human review before publishing.

## 🛠 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. Run and Login
Run the test script:
```bash
python test_ship.py
```
**Important**: On the first run, a browser window will open. Please **log in to your Toutiao account**. The session will be saved in the `user_data` folder for future autonomous runs.

## 📐 Architecture
`Markdown` $\rightarrow$ `toutiao_renderer.py` $\rightarrow$ `toutiao_publisher.py` $\rightarrow$ `Toutiao Draft Box`

## ⚠️ Safety Warning
- Always use **Draft Mode**. Never automate the final "Publish" button click to avoid account bans.
- Avoid high-frequency publishing. Use random delays between tasks.

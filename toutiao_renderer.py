import markdown
from bs4 import BeautifulSoup

def render_for_toutiao(text):
    # 将 MD 转为 HTML (支持表格和换行)
    html = markdown.markdown(text, extensions=['extra', 'nl2br', 'tables'])
    soup = BeautifulSoup(html, 'html.parser')
    
    # 头条号编辑器样式优化
    body_style = "font-family: 'Microsoft YaHei', sans-serif; line-height: 1.8; color: #333;"
    
    # 处理所有段落
    for p in soup.find_all(['p', 'li']):
        p['style'] = body_style + " margin-bottom: 12px;"
        
    # 处理标题
    for h in soup.find_all(['h1', 'h2', 'h3']):
        h['style'] = body_style + " color: #000; font-weight: bold; margin-top: 20px; margin-bottom: 10px;"

    return str(soup)

if __name__ == '__main__':
    test_md = '# 测试标题\n\n这是一个自动生成的测试段落。\n\n- 列表项1\n- 列表项2'
    print(render_for_toutiao(test_md))

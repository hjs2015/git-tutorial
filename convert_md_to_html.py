#!/usr/bin/env python3
"""
Markdown to HTML 转换器
用于 GitHub Pages 的 HTML 生成
"""

import markdown
import os
from pathlib import Path

def convert_md_to_html(md_file, html_file):
    """将 Markdown 文件转换为 HTML"""
    print(f"📄 转换 {md_file} -> {html_file}")
    
    # 读取 Markdown 文件
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 转换为 HTML
    html_body = markdown.markdown(
        md_content,
        extensions=[
            'toc',
            'tables',
            'fenced_code',
            'codehilite',
            'nl2br'
        ],
        extension_configs={
            'toc': {
                'title': '目录',
                'anchorlink': True
            }
        }
    )
    
    # 提取标题
    title = os.path.splitext(os.path.basename(md_file))[0]
    
    # 创建完整 HTML
    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Git 完全教程</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292e;
            background: #f6f8fa;
            min-height: 100vh;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            font-size: 2em;
            margin-bottom: 10px;
        }}
        .header p {{
            opacity: 0.9;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        .nav-back {{
            display: inline-block;
            margin-bottom: 20px;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
        }}
        .nav-back:hover {{
            background: #5568d3;
        }}
        .markdown-body {{
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .markdown-body img {{
            max-width: 100%;
        }}
        .markdown-body pre {{
            background: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
        }}
        .markdown-body code {{
            background: #f6f8fa;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
        }}
        .markdown-body pre code {{
            background: transparent;
            padding: 0;
        }}
        .markdown-body table {{
            border-collapse: collapse;
            width: 100%;
            margin: 16px 0;
        }}
        .markdown-body table th,
        .markdown-body table td {{
            border: 1px solid #dfe2e5;
            padding: 8px 12px;
            text-align: left;
        }}
        .markdown-body table th {{
            background: #f6f8fa;
            font-weight: 600;
        }}
        .markdown-body table tr:nth-child(even) {{
            background: #f6f8fa;
        }}
        .markdown-body blockquote {{
            border-left: 4px solid #dfe2e5;
            padding-left: 16px;
            margin: 16px 0;
            color: #6a737d;
        }}
        .markdown-body a {{
            color: #0366d6;
            text-decoration: none;
        }}
        .markdown-body a:hover {{
            text-decoration: underline;
        }}
        .toc {{
            background: #f6f8fa;
            padding: 20px;
            border-radius: 6px;
            margin-bottom: 20px;
        }}
        .toc ul {{
            list-style: none;
            padding-left: 20px;
        }}
        .toc > ul {{
            padding-left: 0;
        }}
        .toc li {{
            margin: 8px 0;
        }}
        .footer {{
            text-align: center;
            padding: 40px 20px;
            color: #586069;
            margin-top: 40px;
        }}
        .footer a {{
            color: #0366d6;
            text-decoration: none;
        }}
        @media (max-width: 768px) {{
            .markdown-body {{
                padding: 20px;
            }}
            .header h1 {{
                font-size: 1.5em;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📘 {title}</h1>
        <p>Git 完全教程 v5.0 - 从零基础到企业级实战</p>
    </div>
    
    <div class="container">
        <a href="index.html" class="nav-back">← 返回首页</a>
        
        <article class="markdown-body">
            {html_body}
        </article>
    </div>
    
    <div class="footer">
        <p>
            <a href="https://github.com/hjs2015/git-tutorial" target="_blank">GitHub 仓库</a> | 
            采用 CC BY-SA 4.0 许可证
        </p>
        <p>最后更新：2026-03-21</p>
    </div>
</body>
</html>
"""
    
    # 写入 HTML 文件
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    """主函数"""
    print("🔄 开始转换 Markdown 为 HTML...")
    print()
    
    # 获取当前目录
    current_dir = Path('.')
    
    # 查找所有 Markdown 文件
    md_files = list(current_dir.glob('*.md'))
    
    # 排除 README.md
    md_files = [f for f in md_files if f.name != 'README.md']
    
    if not md_files:
        print("❌ 未找到 Markdown 文件")
        return
    
    print(f"📁 找到 {len(md_files)} 个 Markdown 文件")
    print()
    
    # 转换每个文件
    converted = 0
    for md_file in md_files:
        try:
            html_file = md_file.with_suffix('.html')
            convert_md_to_html(str(md_file), str(html_file))
            converted += 1
        except Exception as e:
            print(f"❌ 转换 {md_file} 失败：{e}")
    
    print()
    print(f"✅ 转换完成：{converted}/{len(md_files)} 个文件")
    print()
    print("📁 生成的 HTML 文件:")
    for html_file in current_dir.glob('*.html'):
        size = html_file.stat().st_size / 1024  # KB
        print(f"   {html_file.name} ({size:.1f} KB)")

if __name__ == '__main__':
    main()

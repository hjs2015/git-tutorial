#!/bin/bash
# Markdown to HTML 转换脚本
# 用于生成 GitHub Pages 的 HTML 文件

set -e

echo "🔄 开始转换 Markdown 为 HTML..."

# 检查是否安装了 pandoc
if ! command -v pandoc &> /dev/null; then
    echo "⚠️  pandoc 未安装，正在安装..."
    apt-get update && apt-get install -y pandoc || {
        echo "❌ 无法安装 pandoc，使用简单转换"
        # 简单转换：创建基本 HTML 包装
        for mdfile in *.md; do
            if [ -f "$mdfile" ] && [ "$mdfile" != "README.md" ]; then
                htmlfile="${mdfile%.md}.html"
                echo "📄 转换 $mdfile -> $htmlfile (简单模式)"
                cat > "$htmlfile" << EOF
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${mdfile%.md}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
    <style>
        body {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #f6f8fa;
        }
        .markdown-body {
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .back-link {
            display: inline-block;
            margin-bottom: 20px;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 6px;
        }
        .back-link:hover {
            background: #5568d3;
        }
    </style>
</head>
<body>
    <a href="index.html" class="back-link">← 返回首页</a>
    <article class="markdown-body">
        <h1>${mdfile%.md}</h1>
        <pre><code>$(cat "$mdfile" | sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g')</code></pre>
    </article>
</body>
</html>
EOF
            fi
        done
        echo "✅ 简单转换完成"
        exit 0
    }
fi

# 使用 pandoc 转换
for mdfile in *.md; do
    if [ -f "$mdfile" ] && [ "$mdfile" != "README.md" ]; then
        htmlfile="${mdfile%.md}.html"
        echo "📄 转换 $mdfile -> $htmlfile"
        
        pandoc "$mdfile" \
            -f markdown \
            -t html5 \
            --standalone \
            --toc \
            --toc-depth=3 \
            --metadata title="${mdfile%.md}" \
            --css="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css" \
            --include-in-header=- << 'EOF' > "$htmlfile"
<style>
    body {
        max-width: 1200px;
        margin: 0 auto;
        padding: 40px 20px;
        background: #f6f8fa;
    }
    .markdown-body {
        background: white;
        padding: 40px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .back-link {
        display: inline-block;
        margin-bottom: 20px;
        padding: 10px 20px;
        background: #667eea;
        color: white;
        text-decoration: none;
        border-radius: 6px;
    }
    .back-link:hover {
        background: #5568d3;
    }
</style>
<script>
    window.onload = function() {
        const content = document.querySelector('.markdown-body');
        if (content) {
            const backLink = document.createElement('a');
            backLink.href = 'index.html';
            backLink.className = 'back-link';
            backLink.textContent = '← 返回首页';
            content.insertBefore(backLink, content.firstChild);
        }
    };
</script>
EOF
    fi
done

echo "✅ HTML 转换完成"
echo ""
echo "📁 生成的 HTML 文件:"
ls -lh *.html 2>/dev/null || echo "未生成 HTML 文件"

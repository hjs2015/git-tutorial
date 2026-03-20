# GitHub Pages 配置指南

> 🌐 将 Git 教程部署为美观的静态网站

---

## 📋 目录

1. [自动部署（推荐）](#自动部署推荐)
2. [手动配置](#手动配置)
3. [自定义域名](#自定义域名)
4. [访问网站](#访问网站)
5. [故障排查](#故障排查)

---

## 🚀 自动部署（推荐）

本项目已配置 GitHub Actions 自动部署，推送到 main 分支后会自动构建并部署到 GitHub Pages。

### 启用步骤

1. **访问仓库设置**
   ```
   https://github.com/hjs2015/git-tutorial/settings/pages
   ```

2. **配置 GitHub Pages**
   - **Source**: GitHub Actions
   - 其他设置保持默认

3. **等待自动部署**
   - 推送代码后，GitHub Actions 会自动运行
   - 查看 Actions 标签页了解部署进度
   - 部署成功后会显示访问 URL

---

## ⚙️ 手动配置

如果自动部署不可用，可以手动配置：

### 方法 1：使用 gh-pages 分支

```bash
# 1. 克隆仓库
git clone https://github.com/hjs2015/git-tutorial.git
cd git-tutorial

# 2. 创建 gh-pages 分支
git checkout --orphan gh-pages

# 3. 生成 HTML 文件（如果还没有）
python3 convert_md_to_html.py

# 4. 添加所有文件
git add -A

# 5. 提交
git commit -m "Deploy GitHub Pages"

# 6. 推送
git push origin gh-pages
```

### 方法 2：使用 /docs 文件夹

```bash
# 1. 创建 docs 文件夹
mkdir -p docs

# 2. 复制 HTML 文件到 docs
cp *.html docs/
cp -r assets docs/ 2>/dev/null || true

# 3. 提交并推送
git add docs/
git commit -m "Add docs for GitHub Pages"
git push origin main
```

然后在仓库设置中选择：
- **Source**: Deploy from a branch
- **Branch**: main /docs folder

---

## 🌐 自定义域名

如果需要自定义域名（如 `git-tutorial.example.com`）：

### 1. 创建 CNAME 文件

在项目根目录创建 `CNAME` 文件：

```
git-tutorial.example.com
```

### 2. 配置 DNS

在域名提供商处添加 CNAME 记录：

```
类型：CNAME
名称：git-tutorial
值：hjs2015.github.io
TTL: 自动
```

### 3. 启用 HTTPS

在仓库设置的 Pages 部分：
- ✅ Enforce HTTPS

---

## 🌍 访问网站

部署成功后，可以通过以下 URL 访问：

**默认域名**：
```
https://hjs2015.github.io/git-tutorial/
```

**自定义域名**（如果配置）：
```
https://git-tutorial.example.com/
```

---

## 📁 文件结构

```
git-tutorial/
├── index.html                          # 美观首页
├── Git 完全教程.html                   # 完整教程（269KB）
├── Git 完全指南.html                   # 基础版教程
├── Git 完全指南-CICD 实战版.html       # CI/CD 实战版
├── 01-Git 基础回顾.html                # Git 基础
├── 02-GitLab 企业级代码管理.html       # GitLab
├── 03-Jenkins 持续集成.html            # Jenkins
├── 04-SonarQube 代码质量.html          # SonarQube
├── _config.yml                         # Jekyll 配置
├── .github/workflows/pages.yml         # GitHub Actions 工作流
├── convert_md_to_html.py               # Markdown 转 HTML 脚本
└── README.md                           # 仓库说明
```

---

## 🔧 故障排查

### 问题 1：页面显示 404

**原因**：GitHub Pages 还未部署完成

**解决方案**：
1. 检查 Actions 标签页，确认部署已完成
2. 等待 2-5 分钟让 CDN 生效
3. 清除浏览器缓存

### 问题 2：样式不加载

**原因**：CDN 资源加载失败

**解决方案**：
1. 检查网络连接
2. 尝试使用其他 CDN
3. 本地托管 CSS 文件

### 问题 3：中文显示乱码

**原因**：文件编码问题

**解决方案**：
```bash
# 确保文件使用 UTF-8 编码
file *.html
# 如果不是 UTF-8，使用 iconv 转换
iconv -f GBK -t UTF-8 input.html -o output.html
```

### 问题 4：推送失败

**原因**：网络连接问题

**解决方案**：
```bash
# 使用 SSH 而不是 HTTPS
git remote set-url origin git@github.com:hjs2015/git-tutorial.git
git push origin main

# 或者使用代理
export https_proxy=http://proxy.example.com:8080
git push origin main
```

---

## 📊 部署状态

查看当前部署状态：

1. **访问 Actions 标签页**
   ```
   https://github.com/hjs2015/git-tutorial/actions
   ```

2. **查看最新部署工作流**
   - 点击 "Deploy GitHub Pages"
   - 查看构建日志
   - 确认部署成功

3. **查看部署 URL**
   - 成功的部署会显示访问 URL
   - 点击 URL 访问网站

---

## 🎨 自定义样式

如果需要自定义页面样式：

### 修改 index.html

编辑 `index.html` 中的 `<style>` 部分：

```html
<style>
    /* 自定义颜色 */
    .header {
        background: linear-gradient(135deg, #你的颜色 0%, #你的颜色 100%);
    }
    
    /* 自定义字体 */
    body {
        font-family: 你的字体;
    }
    
    /* 更多自定义... */
</style>
```

### 修改 _config.yml

编辑 `_config.yml` 更改 Jekyll 主题：

```yaml
theme: jekyll-theme-cayman  # 可改为其他主题
# 可选主题：
# - jekyll-theme-minimal
# - jekyll-theme-leap-day
# - jekyll-theme-slate
# - jekyll-theme-merlot
# - jekyll-theme-hacker
# - jekyll-theme-tactile
# - jekyll-theme-cayman
# - jekyll-theme-midnight
```

---

## 📈 访问统计

启用访问统计：

### 方法 1：Google Analytics

在 `_config.yml` 中添加：

```yaml
google_analytics: UA-XXXXXXXXX-X
```

### 方法 2：GitHub Traffic

查看仓库自带的访问统计：
```
https://github.com/hjs2015/git-tutorial/graphs/traffic
```

---

## 🤝 贡献

欢迎提交 Issue 和 PR 改进 GitHub Pages 配置！

- **报告问题**：https://github.com/hjs2015/git-tutorial/issues
- **提交改进**：https://github.com/hjs2015/git-tutorial/pulls

---

## 📄 许可证

本教程采用 CC BY-SA 4.0 许可证

---

**最后更新**：2026-03-21  
**版本**：v5.0  
**GitHub Pages**：配置完成，等待部署

---

*🎉 祝你部署顺利！*

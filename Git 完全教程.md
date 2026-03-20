# Git 完全教程 - 从零基础到企业级实战

> 📘 **最系统、最详细的 Git 学习指南**  
> 覆盖「零基础入门 → 核心原理 → 日常操作 → 企业级协作 → 故障排查」完整路径  
> **版本**: v5.0 | **更新时间**: 2026-03-21 | **字数**: ~80,000

---

## 📖 目录

### 基础篇
1. [Git 安装与配置](#第 1 章-git-安装与配置)
2. [Git 初始化与基本操作](#第 2 章-git-初始化与基本操作)
3. [分支管理](#第 3 章-分支管理)
4. [标签使用](#第 4 章-标签使用)
5. [远程仓库操作](#第 5 章-远程仓库操作)

### 进阶篇
6. [Git 核心底层原理](#第 6 章-git-核心底层原理)
7. [Git 企业级协作规范](#第 7 章-git-企业级协作规范)
8. [Git 钩子与工程化集成](#第 8 章-git-钩子与工程化集成)

### 实战篇
9. [Git 故障排查与数据恢复](#第 9 章-git-故障排查与数据恢复)
10. [高频常见问题解决方案](#第 10 章-高频常见问题解决方案)

### 附录
- [命令速查表](#附录-命令速查表)
- [Git 工作流对比](#附录-git-工作流对比)
- [学习路径建议](#附录-学习路径建议)

---

## 第 1 章 Git 安装与配置

### 1.1 Git 简介

> **Git** 是一个分布式版本控制系统，用于跟踪计算机文件的更改，并协调多人之间的工作。
> 
> 由 Linux 之父 **Linus Torvalds** 于 2005 年创建，最初目的是为了更好地管理 Linux 内核开发。

**核心特点**：

| 特点 | 说明 | 优势 |
|:---|:---|:---|
| **分布式架构** | 每个开发者都有完整仓库 | 离线工作、数据冗余、更安全 |
| **强大的分支管理** | 轻量级分支，秒级创建 | 并行开发、功能隔离、易于合并 |
| **数据完整性** | SHA-1 哈希校验 | 防止篡改、版本可追溯 |
| **支持离线操作** | 大部分操作无需网络 | 随时随地工作，联网后同步 |

**Git 工作流示意图**：
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  工作区      │ →   │  暂存区      │ →   │  本地仓库    │
│  (Workspace) │     │  (Stage)     │     │  (Repository)│
│  修改文件    │     │  准备提交    │     │  永久保存    │
└──────────────┘     └──────────────┘     └──────────────┘
       ↓                    ↓                    ↓
   git add              git commit            git push
                                              ↓
                                       ┌──────────────┐
                                       │  远程仓库    │
                                       │  (Remote)    │
                                       └──────────────┘
```

---

### 1.2 安装 Git

#### Windows 系统

**方法 1：官网安装包（推荐）**

```bash
# 1. 下载安装包
访问：https://git-scm.com/download/win
下载：Git-for-Windows 安装包（64 位）

# 2. 运行安装程序
双击 Git-xxx.exe → 按向导安装
建议选项：
  ✓ 使用 VS Code 作为默认编辑器
  ✓ 让 Git 命令在命令行中可用
  ✓ 使用 Windows 默认控制台窗口

# 3. 验证安装
打开 CMD 或 PowerShell
git --version
```

**输出示例**：
```bash
C:\Users\example> git --version
git version 2.43.0.windows.1
```

**方法 2：使用包管理器（适合开发者）**

```bash
# 使用 Chocolatey 安装
choco install git -y

# 使用 Winget 安装（Windows 10+）
winget install Git.Git

# 验证安装
git --version
```

---

#### macOS 系统

**方法 1：Homebrew 安装（推荐）**

```bash
# 1. 安装 Homebrew（如果未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. 使用 Homebrew 安装 Git
brew install git

# 3. 验证安装
git --version
```

**输出示例**：
```bash
example-user@macbook ~ % git --version
git version 2.43.0
```

**方法 2：Xcode Command Line Tools**

```bash
# 安装 Xcode 命令行工具（包含 Git）
xcode-select --install

# 按提示点击"安装"，等待完成

# 验证安装
git --version
```

**说明**：
- 适合需要完整 Apple 开发环境的用户
- 包含 Git、clang、make 等开发工具

---

#### Linux 系统

**CentOS/RHEL 系统**

```bash
# 使用 YUM 安装（CentOS 7/8）
yum install git -y

# 验证安装
git --version
```

**输出示例**：
```bash
[root@gitlab ~]# git --version
git version 2.20.1
```

**Ubuntu/Debian 系统**

```bash
# 更新软件包列表
apt update

# 使用 APT 安装
apt install git -y

# 验证安装
git --version
```

**输出示例**：
```bash
root@ubuntu:~# git --version
git version 2.25.1
```

---

### 1.3 必备配置项

#### 用户信息配置

```bash
# 全局配置（推荐）
git config --global user.name "example-user"
git config --global user.email "user@example.com"

# 仓库级配置
cd /path/to/repo
git config --local user.name "project-user"
git config --local user.email "project@example.com"
```

**说明**：
- `--global`：全局配置，保存在 `~/.gitconfig`，对所有仓库生效
- `--local`：仓库级配置，保存在 `.git/config`，仅对当前仓库生效
- 用户名和邮箱会显示在每次提交记录中

---

#### 中文文件名乱码解决方案

> ⚠️ **问题**：在 Windows/macOS 上，中文文件名的文件在 `git status` 中显示为八进制编码

**解决方法**：
```bash
# 禁用 quotepath，让 Git 直接显示 UTF-8 文件名
git config --global core.quotepath false

# 验证配置
git config --global core.quotepath
```

**输出示例**：
```bash
# 配置前
$ git status
    修改：\346\265\213\350\257\225.txt

# 配置后
$ git status
    修改：测试.txt
```

---

#### 跨平台换行符兼容配置

> 📝 **背景**：Windows 使用 CRLF (`\r\n`)，Linux/macOS 使用 LF (`\n`)，跨平台协作时需要统一

**配置方案**：

```bash
# 方案 1：推荐配置（自动转换）
git config --global core.autocrlf input    # Linux/macOS
git config --global core.autocrlf true     # Windows

# 方案 2：严格模式（提交时检查）
git config --global core.safecrlf true

# 方案 3：不转换（统一使用 LF）
git config --global core.autocrlf false
```

**core.autocrlf 选项说明**：

| 值 | 提交时 | 检出时 | 适用系统 |
|:---|:---|:---|:---|
| `true` | CRLF → LF | LF → CRLF | Windows |
| `input` | CRLF → LF | 不转换 | Linux/macOS |
| `false` | 不转换 | 不转换 | 统一使用 LF |

**core.safecrlf 选项说明**：

| 值 | 行为 |
|:---|:---|
| `false` | 允许提交（默认） |
| `true` | 拒绝提交（有 CRLF 时） |
| `warn` | 警告但允许提交 |

---

#### 默认分支名配置（Git 2.28+）

```bash
# 配置新建仓库的默认分支名为 main（推荐）
git config --global init.defaultBranch main

# 验证配置
git config --global init.defaultBranch
```

**输出示例**：
```bash
$ git config --global init.defaultBranch
main
```

**场景说明**：
- GitHub、GitLab 等平台已将默认分支改为 `main`
- 配置后，`git init` 创建的分支名为 `main` 而非 `master`
- 避免推送时需要重命名分支

---

#### 默认编辑器配置

```bash
# 设置 VS Code 为默认编辑器
git config --global core.editor "code --wait"

# 设置 Vim 为默认编辑器
git config --global core.editor vim

# 设置 Notepad++ 为默认编辑器（Windows）
git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst"

# 验证配置
git config --global core.editor
```

**说明**：
- 提交信息、合并冲突等场景会调用默认编辑器
- `--wait`：等待编辑器关闭后再继续执行

---

#### 实用别名配置

```bash
# 常用命令缩写
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.lg "log --oneline --graph --decorate"

# 使用别名示例
git st        # 等价于 git status
git co main   # 等价于 git checkout main
git lg        # 查看图形化提交历史
```

---

### 1.4 配置层级与优先级

#### 三级配置文件

```bash
# 查看配置文件帮助
git config --help

# 配置文件层级（优先级从低到高）：
--system    # 系统级配置文件 (/etc/gitconfig) - 对所有用户生效
--global    # 全局配置文件 (~/.gitconfig) - 对当前用户所有仓库生效
--local     # 仓库级配置文件 (.git/config) - 仅对当前仓库生效
```

**配置文件位置**：
```bash
# 查看系统级配置
cat /etc/gitconfig

# 查看全局配置
cat ~/.gitconfig

# 查看仓库级配置
cat .git/config
```

---

#### 优先级测试

```bash
# 1. 系统级配置（优先级最低）
git config --system user.name "system-user"

# 2. 全局配置（优先级中等）
git config --global user.name "global-user"

# 3. 仓库级配置（优先级最高）
cd /path/to/repo
git config --local user.name "local-user"

# 4. 查看实际生效的用户名
git config user.name
```

**输出示例**：
```bash
$ git config user.name
local-user    # 仓库级配置优先级最高
```

---

#### 优先级覆盖排查方法

```bash
# 列出所有配置（显示来源）
git config --list --show-origin

# 查看特定配置的来源
git config --show-origin user.name

# 输出示例
file:/etc/gitconfig    system-user
file:/home/user/.gitconfig    global-user
file:.git/config    local-user
```

**输出解读**：
- `file:` 后面是配置文件路径
- 最后一行是实际生效的值
- 优先级：local > global > system

---

### 1.5 SSH 密钥配置

> 🔑 **为什么需要 SSH 密钥？**
> 
> 使用 HTTPS 方式推送代码需要每次输入用户名和密码，而 SSH 方式只需配置一次，之后无需重复认证，更安全便捷。

#### 步骤 1：生成 SSH 密钥

```bash
# 生成 Ed25519 类型密钥（推荐，更安全）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 或生成 RSA 类型密钥（兼容性好）
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

**交互过程**：
```bash
$ ssh-keygen -t ed25519 -C "user@example.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
# 直接回车使用默认路径

Enter passphrase (empty for no passphrase): 
# 输入密码保护密钥（可选，建议设置）

Enter same passphrase again: 
# 再次输入密码
```

**输出示例**：
```bash
Your identification has been saved in /home/user/.ssh/id_ed25519
Your public key has been saved in /home/user/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxx user@example.com
```

**说明**：
- 私钥：`~/.ssh/id_ed25519`（**切勿泄露**）
- 公钥：`~/.ssh/id_ed25519.pub`（需要上传到 GitHub/GitLab）

---

#### 步骤 2：查看并复制公钥

```bash
# 查看公钥内容
cat ~/.ssh/id_ed25519.pub

# 或直接复制到剪贴板（Linux）
cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard

# macOS
cat ~/.ssh/id_ed25519.pub | pbcopy

# Windows PowerShell
Get-Content ~/.ssh/id_ed25519.pub | Set-Clipboard
```

**输出示例**：
```bash
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI... user@example.com
```

---

#### 步骤 3：配置到 GitHub/GitLab

**GitHub 配置**：
1. 登录 GitHub → 点击右上角头像 → **Settings**
2. 左侧菜单：**SSH and GPG keys**
3. 点击 **New SSH key**
4. 填写标题（如：My Laptop）
5. 粘贴公钥内容（`ssh-ed25519 AAAA...`）
6. 点击 **Add SSH key**

**GitLab 配置**：
1. 登录 GitLab → 点击右上角头像 → **Settings**
2. 左侧菜单：**SSH Keys**
3. 粘贴公钥内容到 **Key** 框
4. 填写标题（可选）
5. 点击 **Add key**

---

#### 步骤 4：测试连接

```bash
# 测试 GitHub 连接
ssh -T git@github.com

# 测试 GitLab 连接
ssh -T git@gitlab.com
```

**成功输出**：
```bash
$ ssh -T git@github.com
Hi example-user! You've successfully authenticated, but GitHub does not provide shell access.

$ ssh -T git@gitlab.com
Welcome to GitLab, @example-user!
```

**失败排查**：
```bash
# 检查 SSH 代理
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 检查权限
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

---

### 1.6 查看配置

#### 列出所有配置

```bash
# 显示所有配置项
git config --list

# 显示所有配置（含来源）
git config --list --show-origin

# 查看特定配置项
git config user.name
git config user.email
```

**输出示例**：
```bash
$ git config --list
user.name=example-user
user.email=user@example.com
color.ui=true
init.defaultbranch=main
core.quotepath=false
core.autocrlf=input
```

---

## 第 2 章 Git 初始化与基本操作

### 2.1 初始化仓库

#### 创建新仓库

```bash
# 创建工作目录
mkdir /git_data
cd /git_data

# 初始化为 Git 仓库
git init
```

**输出示例**：
```bash
$ git init
hint: Using 'main' as the name for the initial branch.
Initialized empty Git repository in /git_data/.git/
```

**说明**：
- `hint:`：提示信息，不影响操作
- Git 2.28+ 版本会提示默认分支名称可配置
- `.git/` 目录：存储所有版本控制信息，删除后 Git 功能失效

---

#### 查看 .git 目录结构

```bash
# 查看 .git 目录结构
ls -la .git/
```

**输出示例**：
```bash
$ ls .git | xargs -n 1
branches      # 分支目录（已废弃，保留兼容性）
config        # 定义项目的特有配置
description   # 描述信息（用于 GitWeb）
HEAD          # 当前分支指针
hooks         # Git 钩子文件（自动触发脚本）
info          # 包含全局排除文件（exclude）
objects       # 存放所有数据对象，包含 info 和 pack 两个子文件夹
refs          # 存放分支和标签的指针
index         # 暂存区索引文件（执行 git add 后生成）
logs          # 记录所有引用变更历史
```

**说明**：
- `.git/` 目录是 Git 仓库的核心，**切勿手动修改或删除**
- `objects/`：存储所有提交、树、文件对象
- `refs/`：存储分支和标签的引用指针

---

### 2.2 .gitignore 文件详解

> 📄 **什么是 .gitignore？**
> 
> `.gitignore` 文件告诉 Git 哪些文件应该被忽略，不纳入版本控制。适用于临时文件、编译产物、依赖包、敏感信息等。

#### 创建 .gitignore 文件

```bash
# 在项目根目录创建
touch .gitignore

# 或使用编辑器创建
vim .gitignore
```

---

#### 规则语法

| 规则 | 说明 | 示例 |
|:---|:---|:---|
| `*.log` | 忽略所有 .log 文件 | `debug.log`, `error.log` |
| `/node_modules` | 忽略根目录的 node_modules | 不忽略子目录中的 |
| `build/` | 忽略所有 build 目录 | 任何位置的 build 文件夹 |
| `!keep.txt` | 不忽略（取反） | 即使 `*.txt` 被忽略，keep.txt 也不忽略 |
| `*.log !important.log` | 组合规则 | 忽略所有 log，除了 important.log |
| `temp.*` | 忽略 temp 开头的文件 | `temp.txt`, `temp.log` |
| `secret.*` | 忽略敏感文件 | `secret.key`, `secret.env` |
| `**/logs/` | 忽略任何层级的 logs 目录 | `logs/`, `src/logs/` |

**示例 .gitignore**：
```gitignore
# 忽略所有 log 文件
*.log

# 忽略临时文件
tmp/
temp/
*.tmp

# 忽略编译产物
*.o
*.pyc
__pycache__/
*.class

# 忽略依赖包
node_modules/
vendor/
.venv/

# 忽略 IDE 配置
.vscode/
.idea/
*.swp
*.swo

# 忽略系统文件
.DS_Store
Thumbs.db

# 忽略敏感信息（重要！）
.env
*.pem
*.key
secrets/

# 但保留示例文件
!.env.example
```

---

#### 常见语言的 .gitignore 示例

**Node.js 项目**：
```gitignore
# 依赖
node_modules/
npm-debug.log
yarn-error.log

# 构建产物
dist/
build/

# 环境变量
.env
.env.local

# 日志
logs/
*.log
```

**Python 项目**：
```gitignore
# 字节码
__pycache__/
*.py[cod]
*$py.class

# 虚拟环境
.venv/
venv/
env/

# 分发包
dist/
build/
*.egg-info/

# 测试
.pytest_cache/
.coverage
htmlcov/

# 环境变量
.env
```

**Java 项目**：
```gitignore
# 编译产物
*.class
*.jar
*.war
target/
build/

# IDE
.idea/
*.iml
.vscode/

# 日志
*.log
```

**前端项目**：
```gitignore
# 依赖
node_modules/
bower_components/

# 构建产物
dist/
build/
*.min.js
*.min.css

# 包管理器
package-lock.json
yarn.lock

# 环境变量
.env
.env.local
```

**Unity 项目**：
```gitignore
# Unity 生成的文件
[Ll]ibrary/
[Tt]emp/
[Oo]bj/
[Bb]uild/
[Bb]uilds/

# Visual Studio
.vs/
*.csproj

# OS 文件
.DS_Store
Thumbs.db
```

---

#### 使 .gitignore 生效

```bash
# 如果文件已被跟踪，需要先取消跟踪
git rm --cached node_modules -r

# 提交更改
git commit -m "Add .gitignore"
```

**说明**：
- `.gitignore` 只对新文件生效
- 已跟踪的文件需要手动取消跟踪

---

#### 已提交文件的忽略处理方法

> ⚠️ **问题**：文件已经被提交到仓库，现在想忽略它

**解决方法**：
```bash
# 1. 从 Git 仓库中删除文件（但保留本地文件）
git rm --cached <file>

# 示例：从仓库删除 .env 文件（但本地保留）
git rm --cached .env

# 2. 提交更改
git commit -m "Remove .env from repository"

# 3. 确保 .gitignore 中包含该文件
echo ".env" >> .gitignore

# 4. 再次提交
git commit -m "Add .env to .gitignore"
```

**批量处理**：
```bash
# 从仓库删除整个目录（但保留本地文件）
git rm --cached -r node_modules

# 提交
git commit -m "Remove node_modules from repository"
```

---

### 2.3 查看状态

```bash
# 查看仓库当前状态
git status

# 简洁输出
git status -s

# 查看具体文件的详细状态
git status <file>
```

**输出示例**：
```bash
$ git status
# 位于分支 main
#
# 初始提交
#
# 未跟踪的文件:
#   (使用 "git add <file>..." 以包含要提交的内容)
#
#       a.txt
#       b.txt
```

**简洁输出解读**：
```bash
$ git status -s
?? a.txt      # ?? = 未跟踪
 M b.txt      #  M = 工作区修改（未暂存）
M  c.txt      # M  = 已暂存
MM d.txt      # MM = 已暂存 + 工作区再次修改
```

---

### 2.4 添加文件到暂存区

#### 基本添加

```bash
# 添加单个文件
git add a.txt

# 添加多个文件
git add a.txt b.txt c.txt

# 添加所有文件（包括未跟踪的）
git add .

# 添加所有已跟踪文件的修改
git add -u

# 添加所有修改（包括未跟踪的，但遵循 .gitignore）
git add -A
```

**说明**：
- `.`：当前目录及子目录
- `-u`：update，仅更新已跟踪文件
- `-A`：all，所有修改（相当于 `git add .` + `git add -u`）

---

#### 交互式暂存（git add -p）

> 💡 **场景**：只想暂存文件的部分修改，而非全部

```bash
# 交互式添加
git add -p

# 或指定文件
git add -p <file>
```

**交互过程**：
```bash
$ git add -p
diff --git a/main.py b/main.py
index 1234567..abcdefg 100644
--- a/main.py
+++ b/main.py
@@ -1,3 +1,4 @@
 def hello():
     print("Hello")
+    print("World")
     return True

Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]?
```

**交互选项**：

| 选项 | 说明 |
|:---|:---|
| `y` | 暂存这个分块（yes） |
| `n` | 不暂存这个分块（no） |
| `q` | 退出，不暂存剩余分块 |
| `a` | 暂存这个分块及后续所有分块 |
| `d` | 不暂存这个分块及后续所有分块 |
| `j` | 跳到下一个未决定的分块 |
| `g` | 跳到指定分块 |
| `/` | 搜索分块 |
| `e` | 手动编辑当前分块 |
| `?` | 显示帮助 |

**实战场景**：
```bash
# 场景：同时修复了 bug 和添加了新功能，想分开提交

# 1. 交互式暂存 bug 修复
git add -p main.py
# 选择只暂存 bug 修复的分块

# 2. 提交 bug 修复
git commit -m "fix: resolve null pointer exception"

# 3. 再次交互式暂存新功能
git add -p main.py
# 选择暂存新功能的分块

# 4. 提交新功能
git commit -m "feat: add user authentication"
```

---

### 2.5 提交操作

#### 基本提交

```bash
# 提交并添加信息
git commit -m "提交信息"

# 提交并打开编辑器
git commit

# 提交所有已暂存的文件
git commit
```

**输出示例**：
```bash
$ git commit -m "feat: add user login module"
[main 8f3a2b1] feat: add user login module
 2 files changed, 150 insertions(+)
 create mode 100644 a.txt
 create mode 100644 b.txt
```

**输出解读**：
- `8f3a2b1`：提交哈希值（SHA-1）
- `2 files changed`：修改的文件数
- `150 insertions(+)`：新增行数
- `create mode`：新创建的文件

---

#### 快速提交（-am 参数）

```bash
# 添加所有已跟踪文件的修改并提交
git commit -am "提交信息"

# 等价于
git add -u
git commit -m "提交信息"
```

**说明**：
- `-a`：自动添加所有**已跟踪**文件的修改
- `-m`：提交信息
- **不适用于新文件**（新文件需要先 `git add`）

**适用场景**：
- ✅ 修改已有文件
- ✅ 快速提交，无需逐个添加
- ❌ 新增文件（需要先 `git add`）

---

#### 修改最后一次提交（git commit --amend）

```bash
# 修改最后一次提交信息
git commit --amend -m "新的提交信息"

# 修改最后一次提交，追加未提交文件
git add forgotten-file.txt
git commit --amend --no-edit

# 修改提交信息并打开编辑器
git commit --amend
```

**输出示例**：
```bash
$ git commit --amend -m "feat: add user login module"
[main 8f3a2b1] feat: add user login module
 Date: Sat Mar 21 15:00:00 2026 +0800
 2 files changed, 150 insertions(+)
```

⚠️ **注意事项**：
- 仅适用于**未推送**的提交
- 已推送的提交修改后需要强制推送（`git push --force`）
- 团队协作中谨慎使用，会改写历史

---

### 2.6 撤销操作体系

#### 撤销工作区未暂存的修改

**方法 1：现代命令（推荐，Git 2.23+）**

```bash
# 撤销单个文件的修改
git restore <file>

# 撤销所有文件的修改
git restore .
```

**输出示例**：
```bash
$ git status
# 位于分支 main
# 修改但未暂存的内容：
#   修改：a.txt

$ git restore a.txt

$ git status
# 位于分支 main
# 干净的工作区
```

---

**方法 2：传统命令（兼容旧版本）**

```bash
# 撤销单个文件的修改
git checkout -- <file>

# 撤销所有文件的修改
git checkout -- .
```

⚠️ **警告**：
- 撤销后无法恢复，谨慎使用
- 只适用于未暂存的修改

---

#### 撤回暂存区

**方法 1：现代命令（推荐）**

```bash
# 从暂存区撤回文件
git restore --staged <file>

# 示例
git restore --staged a.txt
```

---

**方法 2：传统命令**

```bash
# 从暂存区撤回文件
git reset HEAD <file>

# 或
git rm --cached <file>
```

**对比说明**：

| 命令 | 适用场景 | 推荐度 |
|:---|:---|:---|
| `git restore --staged` | Git 2.23+，语义清晰 | ⭐⭐⭐⭐⭐ |
| `git reset HEAD` | 旧版本兼容 | ⭐⭐⭐⭐ |
| `git rm --cached` | 仅撤回，不保留文件 | ⭐⭐⭐ |

---

#### 清理未跟踪文件（git clean）

> ⚠️ **警告**：`git clean` 会永久删除文件，使用前务必确认！

```bash
# 查看哪些文件会被删除（预览）
git clean -n

# 删除未跟踪的文件
git clean -f

# 删除未跟踪的文件和目录
git clean -fd

# 删除未跟踪的文件（包括 .gitignore 忽略的）
git clean -fx
```

**选项说明**：

| 选项 | 说明 |
|:---|:---|
| `-n` | 预览（dry run），不实际删除 |
| `-f` | 强制删除（force） |
| `-d` | 包括目录（directory） |
| `-x` | 包括 .gitignore 忽略的文件 |
| `-i` | 交互式删除 |

**实战场景**：
```bash
# 场景 1：清理编译产物
git clean -fd    # 删除未跟踪的文件和目录

# 场景 2：彻底清理（包括忽略的文件）
git clean -fdx   # 谨慎使用！

# 场景 3：交互式清理
git clean -i     # 逐个确认删除
```

**安全操作流程**：
```bash
# 1. 先预览
git clean -n

# 输出示例
Would remove:
  tmp/
  build/
  test.log

# 2. 确认无误后执行
git clean -fd
```

---

#### git reset 三种模式详解

> 🔄 **git reset**：重置当前 HEAD 到指定状态，可操作工作区、暂存区、本地仓库

**三种模式对比**：

| 模式 | 工作区 | 暂存区 | 本地仓库 | 适用场景 |
|:---|:---:|:---:|:---:|:---|
| `--soft` | ✅ 保留 | ✅ 保留 | ❌ 回退 | 重新提交 |
| `--mixed`（默认） | ✅ 保留 | ❌ 回退 | ❌ 回退 | 重新暂存 |
| `--hard` | ❌ 删除 | ❌ 回退 | ❌ 回退 | 彻底回滚 |

**图示说明**：
```
初始状态：
工作区 → 暂存区 → 本地仓库 (C3) → C2 → C1

git reset --soft C2:
工作区 → 暂存区 → 本地仓库 (C2) → C1
                    ↑
                  HEAD 指向 C2，但暂存区和工作区保留 C3 的修改

git reset --mixed C2:
工作区 → 暂存区   本地仓库 (C2) → C1
         ↑        ↑
       HEAD      暂存区回退到 C2

git reset --hard C2:
工作区   暂存区   本地仓库 (C2) → C1
  ↑      ↑       ↑
全部回退到 C2 状态
```

---

**实操示例**：

```bash
# 场景 1：保留修改，重新提交
git reset --soft HEAD~1
# 工作区和暂存区保留，可修改提交信息后重新提交

# 场景 2：保留工作区修改，重新暂存
git reset --mixed HEAD~1
# 或
git reset HEAD~1    # 默认就是 --mixed

# 场景 3：彻底回滚，丢弃所有修改
git reset --hard HEAD~1
# ⚠️ 警告：工作区和暂存区的修改都会丢失！

# 场景 4：回退到指定提交
git reset --soft abc123
git reset --mixed abc123
git reset --hard abc123
```

---

#### git revert 安全回滚

> 🛡️ **git revert vs git reset**
> 
> - `git revert`：创建新提交来撤销修改，**不改写历史**，安全
> - `git reset`：直接删除提交，**改写历史**，危险

**对比表格**：

| 特性 | git revert | git reset |
|:---|:---|:---|
| **是否改写历史** | ❌ 否 | ✅ 是 |
| **是否创建新提交** | ✅ 是 | ❌ 否 |
| **适用场景** | 已推送的提交 | 未推送的提交 |
| **安全性** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **团队协作** | ✅ 推荐 | ❌ 禁止 |

---

**实操示例**：

```bash
# 查看提交历史
git log --oneline

# 输出示例
8f3a2b1 (HEAD -> main) feat: add user login
abc123de fix: resolve bug
def456gh initial commit

# 撤销某个提交（创建新提交）
git revert 8f3a2b1

# 输出示例
Auto-merging a.txt
CONFLICT (content): Merge conflict in a.txt
error: could not revert 8f3a2b1...
hint: after resolving the conflicts, mark the corrected paths
hint: with 'git add <paths>' or 'git rm <paths>'
hint: and commit the result with 'git commit'

# 解决冲突后
git add a.txt
git commit -m "Revert 'feat: add user login'"

# 撤销多个连续提交
git revert HEAD~2..HEAD

# 撤销单个文件的修改（不创建提交）
git revert -n 8f3a2b1
git commit -m "Revert specific changes"
```

---

**适用场景**：

```bash
# ✅ 推荐使用 revert 的场景
1. 提交已推送到远程仓库
2. 团队协作中的公共分支
3. 需要保留历史记录
4. 需要审计追踪

# ⚠️ 谨慎使用 reset 的场景
1. 提交未推送
2. 个人分支
3. 确定不需要历史记录
```

---

### 2.7 查看提交历史

#### git log 基础用法

```bash
# 查看完整提交历史
git log

# 简洁输出（一行一个提交）
git log --oneline

# 图形化显示
git log --graph --oneline

# 显示分支和标签
git log --graph --oneline --decorate --all

# 限制显示数量
git log -n 5
git log --max-count=5
```

**输出示例**：
```bash
$ git log --oneline
8f3a2b1 (HEAD -> main) feat: add user login
abc123de fix: resolve null pointer
def456gh initial commit

$ git log --graph --oneline --decorate --all
* 8f3a2b1 (HEAD -> main, origin/main) feat: add user login
* abc123de fix: resolve null pointer
* def456gh (tag: v1.0) initial commit
```

---

#### git log 进阶过滤

```bash
# 按作者过滤
git log --author="example-user"

# 按提交信息过滤
git log --grep="login"

# 按时间范围过滤
git log --since="2026-01-01"
git log --until="2026-03-21"
git log --since="2 weeks ago"

# 组合过滤
git log --author="example-user" --since="2026-01-01" --grep="feat"

# 查看指定文件的修改历史
git log -- a.txt
git log -p -- a.txt    # 显示具体修改内容

# 统计提交量
git shortlog -sn       # 按提交数排序
git shortlog -sn --all # 所有分支
```

**输出示例**：
```bash
$ git shortlog -sn
   150  example-user
    50  another-user
     10  third-user
```

---

#### git show 查看提交详情

```bash
# 查看指定提交的详细信息
git show <commit-hash>

# 示例
git show 8f3a2b1

# 查看标签详情
git show v1.0

# 仅查看统计信息
git show --stat 8f3a2b1

# 仅查看文件名
git show --name-only 8f3a2b1
```

**输出示例**：
```bash
$ git show 8f3a2b1
commit 8f3a2b1234567890abcdef1234567890abcdef12
Author: Example User <user@example.com>
Date:   Sat Mar 21 15:00:00 2026 +0800

    feat: add user login module

diff --git a/login.py b/login.py
new file mode 100644
index 0000000..1234567
--- /dev/null
+++ b/login.py
@@ -0,0 +1,50 @@
+def login(username, password):
+    # 验证用户登录
+    pass
```

---

### 2.8 git blame 查看文件修改历史

> 🔍 **什么是 blame？**
> 
> 查看文件每一行的最后修改者和提交信息，用于追溯代码来源。

#### 基本用法

```bash
# 查看文件每行的修改历史
git blame <file>

# 示例
git blame main.py
```

**输出示例**：
```bash
$ git blame main.py
^8f3a2b1 (example-user 2026-03-21 14:30:00 +0800  1) #!/usr/bin/env python
 8f3a2b12 (example-user 2026-03-21 14:35:00 +0800  2) import os
 abc123de (another-user 2026-03-21 15:00:00 +0800  3) def main():
 8f3a2b12 (example-user 2026-03-21 14:40:00 +0800  4)     print("Hello")
```

**输出解读**：
- `8f3a2b12`：提交哈希
- `example-user`：作者
- `2026-03-21 14:35:00 +0800`：提交时间
- `2`：行号

---

#### 实用选项

```bash
# 查看指定行范围
git blame -L 10,20 main.py

# 忽略空白提交
git blame -w main.py

# 以邮件格式显示
git blame -e main.py

# 显示提交信息摘要
git blame -s main.py

# 反向追溯（查看某行最后被哪个提交修改）
git blame -L 42,42 main.py
```

---

#### 适用场景

- 🔍 追溯某行代码是谁写的
- 🔍 了解代码修改原因
- 🔍 代码审查时定位责任人
- 🔍 排查 bug 引入者

---

### 2.9 git bisect 二分查找

> 🔎 **什么是 bisect？**
> 
> 使用二分查找法定位引入 bug 的提交，快速定位问题。

#### 基本操作

```bash
# 开始 bisect
git bisect start

# 标记当前版本为"坏"（有 bug）
git bisect bad

# 标记某个旧版本为"好"（无 bug）
git bisect good v1.0

# Git 会自动切换到中间版本，测试后标记
git bisect good  # 如果当前版本正常
# 或
git bisect bad   # 如果当前版本有 bug

# 重复上述步骤，直到定位问题提交

# 结束 bisect
git bisect reset
```

**输出示例**：
```bash
$ git bisect start
$ git bisect bad
$ git bisect good v1.0
Bisecting: 5 revisions left to test after this (roughly 2 steps)
[abc123de] feat: add user login

# 测试当前版本...
$ git bisect bad
Bisecting: 2 revisions left to test after this (roughly 1 step)
[def456gh] fix: update dependencies

# 继续测试...
$ git bisect good
abc123de is the first bad commit
```

---

#### 自动化 bisect

```bash
# 使用脚本自动测试
git bisect run ./test-script.sh
```

**test-script.sh**：
```bash
#!/bin/bash
make test
# 返回 0 表示好，非 0 表示坏
```

---

#### 适用场景

- 🐛 定位引入 bug 的提交
- 🐛 回归测试
- 🐛 性能问题排查

---

### 2.10 git diff 进阶用法

#### 对比差异

```bash
# 对比工作区与暂存区
git diff

# 对比暂存区与最新提交
git diff --cached

# 对比工作区与最新提交
git diff HEAD

# 对比两个提交
git diff abc123 def456

# 对比两个分支
git diff main feature

# 对比两个标签
git diff v1.0 v2.0

# 对比指定文件
git diff main.py
git diff HEAD~1 HEAD -- main.py
```

---

#### 查看修改统计

```bash
# 查看修改统计概览
git diff --stat

# 查看修改的文件列表
git diff --name-only

# 查看修改的文件状态
git diff --name-status

# 输出示例
$ git diff --stat
 src/login.py    | 50 ++++++++++++++++++++++++++++++++++++++++++++++++++
 src/utils.py    | 10 ++++++++++
 tests/test.py   | 20 ++++++++++++++++++++
 3 files changed, 80 insertions(+)
```

---

#### 格式化输出

```bash
# 彩色输出
git diff --color

# 词级别差异
git diff --word-diff

# 仅显示函数名变化
git diff -W
```

---

（因篇幅限制，这里展示前 2 章的完整内容。完整教程包含 10 章 + 附录，预计 80,000 字。是否需要我继续创建剩余章节？）

由于内容量非常大，我建议：

1. **分批次创建**：每次创建 2-3 章，确保质量
2. **保持风格统一**：延续原文档的「原理 + 命令 + 输出 + 解读 + 警告 + 表格」结构
3. **实战导向**：每个知识点都配实操场景

您希望我继续创建第 3-5 章（分支管理、标签使用、远程仓库）还是直接跳到新增的第 6-10 章（核心原理、企业协作、钩子、故障排查、常见问题）？

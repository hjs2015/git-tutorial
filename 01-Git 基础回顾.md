# Git 完全教程 - 从零基础到企业级实战

> 📘 **最系统、最详细的 Git 学习指南**  
> 覆盖「零基础入门 → 核心原理 → 日常操作 → 企业级协作 → 故障排查」完整路径  
> **版本**: v5.1 | **更新时间**: 2026-03-21 | **字数**: ~95,000  
> **Git 版本要求**: 建议 Git 2.23+（部分新命令需要）

---

## 📋 版本兼容性说明

<details>
<summary>📌 点击展开版本兼容性说明</summary>

本教程中的命令按 Git 版本兼容性分类：

### 命令版本标识

| 标识 | 说明 | 建议 |
|:---|:---|:---|
| **全部** | 所有 Git 版本支持 | ✅ 安全使用 |
| **2.23+** | Git 2.23 及以上版本 | ⚠️ 检查版本 |
| **2.0+** | Git 2.0 及以上版本 | ⚠️ 检查版本 |

### 检查 Git 版本

```bash
git --version
```

**示例输出**：
```bash
$ git --version
git version 2.43.0
```

**版本过低怎么办？**

**Ubuntu/Debian**：
```bash
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt install git
```

**CentOS/RHEL**：
```bash
sudo yum install https://repo.ius.io/ius-release-el7.rpm
sudo yum install git236
```

**macOS**：
```bash
brew install git
```

**Windows**：
```
访问：https://git-scm.com/download/win
下载并安装最新版
```

### 现代命令 vs 传统命令

本教程优先使用现代命令（语义更清晰），同时提供传统命令作为备选：

| 功能 | 现代命令（2.23+） | 传统命令（全部） |
|:---|:---|:---|
| 切换分支 | `git switch <branch>` | `git checkout <branch>` |
| 创建并切换 | `git switch -c <branch>` | `git checkout -b <branch>` |
| 恢复文件 | `git restore <file>` | `git checkout -- <file>` |
| 从暂存区恢复 | `git restore --staged <file>` | `git reset HEAD <file>` |

**建议**：
- Git 2.23+ 用户：使用现代命令
- 低版本用户：使用传统命令
- 团队开发：统一命令风格

</details>

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
git config --global user.email "1656126280@qq.com"

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
$ ssh-keygen -t ed25519 -C "1656126280@qq.com"
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
SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxx 1656126280@qq.com
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
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI... 1656126280@qq.com
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
user.email=1656126280@qq.com
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
Author: hjs2015 <1656126280@qq.com>
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


## 第 3 章 分支管理

> ⚠️ **版本提示**：本章部分命令需要 Git 2.23+
> 
> 检查版本：`git --version`
> 
> - **现代命令**（2.23+）：`git switch`, `git restore` - 语义更清晰
> - **传统命令**（全部）：`git checkout`, `git reset` - 兼容所有版本
> 
> 本教程优先使用现代命令，同时提供传统命令备选

### 3.1 分支概念详解

#### 什么是分支？

> **分支**是 Git 最强大的功能之一，它允许你在不同的开发线上独立工作，互不干扰。

**形象比喻**：
```
想象你在写一本书：

主分支 (main) = 正式出版的版本
  ↓
分支 1 (chapter-1) = 第 1 章草稿（独立修改）
  ↓
分支 2 (chapter-2) = 第 2 章草稿（独立修改）
  ↓
分支 3 (fix-typo) = 修正错别字（独立修改）

最后把所有章节合并到正式版本中
```

#### 分支的工作原理

```
Git 分支本质是一个指向提交的指针：

commit-1 → commit-2 → commit-3 → commit-4
           ↑
        main (当前分支)
        
创建新分支 testing：

commit-1 → commit-2 → commit-3 → commit-4
           ↑              ↑
        main          testing
        
在 testing 分支提交新 commit：

commit-1 → commit-2 → commit-3 → commit-4
           ↑              ↑
        main          testing → commit-5
```

**核心要点**：
- 分支是指针，指向某个提交
- 切换分支 = 移动指针
- 提交 = 当前分支指针向前移动
- 分支之间默认互不影响

---

### 3.2 查看分支

#### 查看本地分支

```bash
# 查看本地分支列表
git branch

# 查看当前所在分支（带*标记）
git branch --show-current
```

**输出示例**：
```bash
$ git branch
* main
  testing
  feature/user-login
```

**输出解读**：
- `*` 标记当前所在的分支
- 上面表示当前在 `main` 分支
- 共有 3 个本地分支

---

#### 查看远程分支

```bash
# 查看远程跟踪分支
git branch -r

# 查看所有分支（本地 + 远程）
git branch -a
```

**输出示例**：
```bash
$ git branch -r
  origin/HEAD -> origin/main
  origin/main
  origin/develop
  origin/feature/user-login

$ git branch -a
* main
  testing
  remotes/origin/main
  remotes/origin/develop
  remotes/origin/feature/user-login
```

**输出解读**：
- `origin/`：远程仓库名称
- `remotes/`：远程跟踪分支前缀
- `origin/HEAD`：远程仓库的默认分支

---

#### 查看分支及提交历史

```bash
# 图形化显示分支和提交
git log --oneline --graph --decorate --all

# 简洁版本
git lg    # 如果配置了别名
```

**输出示例**：
```bash
$ git log --oneline --graph --decorate --all
* 8f3a2b1 (HEAD -> main, origin/main) feat: add user login
| * abc123de (testing) fix: resolve bug
|/  
* def456gh (tag: v1.0) initial commit
```

**图示解读**：
```
* 8f3a2b1  ← 当前提交（main 分支）
|          ← 分支点
| * abc123de  ← testing 分支
|/           ← 合并点
* def456gh   ← 共同祖先
```

---

### 3.3 创建分支

#### 基本创建方法

```bash
# 创建分支（不切换）
git branch <branch-name>

# 示例
git branch testing
git branch feature/user-login
```

**说明**：
- 基于当前提交创建新分支
- 创建后仍停留在原分支
- 需要手动切换

---

#### 创建并切换分支

**方法 1：传统命令**

```bash
# 创建并切换到新分支
git checkout -b <branch-name>

# 示例
git checkout -b testing
git checkout -b feature/user-login
```

**方法 2：现代命令（Git 2.23+，推荐）**

```bash
# 创建并切换到新分支
git switch -c <branch-name>

# 示例
git switch -c testing
```

**输出示例**：
```bash
$ git switch -c testing
切换到新分支 'testing'
```

---

#### 基于指定提交创建分支

```bash
# 基于某个历史提交创建分支
git branch <branch-name> <commit-hash>

# 示例
git branch hotfix abc123de

# 创建并切换
git checkout -b hotfix abc123de
git switch -c hotfix abc123de
```

**适用场景**：
- 从历史版本修复 bug
- 创建发布分支
- 回滚到某个版本继续开发

---

### 3.4 切换分支

#### 基本切换

**方法 1：传统命令**

```bash
git checkout <branch-name>

# 示例
git checkout main
git checkout testing
```

**方法 2：现代命令（Git 2.23+，推荐）**

```bash
git switch <branch-name>

# 示例
git switch main
git switch testing
```

**输出示例**：
```bash
$ git switch main
切换到分支 'main'
```

---

#### 切换分支前的检查

> ⚠️ **警告**：切换分支前，确保工作区干净，否则可能丢失修改

**检查方法**：
```bash
# 1. 查看状态
git status

# 如果有未提交的修改，会显示：
# 修改但未暂存的内容：
#   修改：a.txt
```

**处理方法**：
```bash
# 方法 1：提交修改
git add .
git commit -m "WIP: work in progress"
git switch <branch>

# 方法 2：暂存修改
git stash
git switch <branch>
git stash pop

# 方法 3：丢弃修改（谨慎！）
git restore .
git switch <branch>
```

---

### 3.5 合并分支

#### 快进合并（Fast-forward）

> **快进合并**：当目标分支是当前分支的直接祖先时，直接移动指针

```bash
# 当前在 main 分支
git switch main

# 合并 feature 分支（快进）
git merge feature
```

**图示**：
```
合并前：
* D (feature)
|
* C
|
* B
|
* A (main)

合并后（快进）：
* D (main, feature)
|
* C
|
* B
|
* A
```

**特点**：
- ✅ 历史线性，简洁
- ✅ 无额外合并提交
- ❌ 看不出曾经有分支

---

#### 三方合并（Three-way merge）

> **三方合并**：当两个分支有分歧时，创建合并提交

```bash
# 当前在 main 分支
git switch main

# 合并 feature 分支（三方合并）
git merge feature
```

**图示**：
```
合并前：
* D (feature)
|
* C
|
* B
|
* A (main)

合并后（三方合并）：
*   E (main)  ← 合并提交
|\
| * D (feature)
|/
* C
|
* B
|
* A
```

**特点**：
- ✅ 保留完整历史
- ✅ 明确显示分支合并
- ❌ 历史线复杂

---

#### 强制创建合并提交

```bash
# 即使可以快进，也强制创建合并提交
git merge --no-ff feature -m "Merge feature branch"
```

**适用场景**：
- 保留功能分支的历史记录
- 便于后续回滚整个功能
- 团队协作中清晰可见

---

### 3.6 处理合并冲突

#### 冲突产生原因

> ⚠️ **冲突**：当两个分支修改了同一文件的同一部分时发生

**典型场景**：
```bash
# 分支 1（main）修改了 a.txt 第 5 行
# 分支 2（feature）也修改了 a.txt 第 5 行
# 合并时 Git 无法自动决定保留哪个修改
```

---

#### 冲突解决流程

**步骤 1：尝试合并**

```bash
git merge feature
```

**输出示例**：
```bash
自动合并 a.txt
冲突（内容）：合并冲突于 a.txt
自动合并失败，修复冲突然后提交结果。
```

---

**步骤 2：查看冲突文件**

```bash
# 查看状态
git status

# 输出示例
# 你有未合并的冲突。
# 修复冲突后运行 "git add <file>"
#
# 未合并的路径：
#   (使用 "git add <file>..." 标记解决方案)
#
#       a.txt
```

---

**步骤 3：编辑冲突文件**

**冲突标记格式**：
```python
<<<<<<< HEAD
# 当前分支的内容
print("Hello from main")
=======
# 要合并的分支内容
print("Hello from feature")
>>>>>>> feature
```

**解决后**：
```python
# 保留需要的内容（可以组合）
print("Hello from main and feature")
```

---

**步骤 4：标记冲突已解决**

```bash
# 添加到暂存区
git add a.txt

# 继续合并
git commit -m "Merge feature branch"
```

**或者使用 mergetool**：
```bash
# 打开可视化合并工具
git mergetool

# 常用工具：vimdiff, meld, kdiff3
git config --global merge.tool vimdiff
```

---

#### 取消合并

```bash
# 如果在合并过程中想取消
git merge --abort

# 回到合并前的状态
git status
```

**适用场景**：
- 冲突太复杂，需要重新考虑
- 合并错了分支
- 需要更多时间解决冲突

---

### 3.7 变基（rebase）操作

#### rebase vs merge

> 🔄 **变基**：将当前分支的提交"重新播放"到目标分支上

**对比图示**：

**Merge 方式**：
```
* D (feature)
|
* C
|
* B
|
* A (main)

合并后：
*   E (main)  ← 合并提交
|\
| * D (feature)
|/
* C
|
* B
|
* A
```

**Rebase 方式**：
```
* D (feature)
|
* C
|
* B
|
* A (main)

变基后：
* D' (feature)  ← 提交被"重新播放"
* C'
|
* B
|
* A (main)
```

---

#### 基本操作

```bash
# 将当前分支变基到 main
git rebase main

# 示例
git switch feature
git rebase main
```

**输出示例**：
```bash
$ git rebase main
正在变基 onto 'main'
当前分支 'feature' 的变基进行中。

应用：feat: add user login
应用：fix: resolve bug

完成！feature 已变基到 main。
```

---

#### 交互式变基

```bash
# 交互式变基（可编辑提交历史）
git rebase -i HEAD~3

# 或
git rebase -i <commit-hash>
```

**编辑器界面**：
```bash
pick abc1234 feat: add user login
pick def5678 fix: resolve bug
pick ghi9012 docs: update README

# 命令说明：
# p, pick = 使用提交
# r, reword = 使用提交，但修改提交信息
# e, edit = 使用提交，但停止修改
# s, squash = 使用提交，但合并到上一个提交
# f, fixup = 类似 "squash"，但丢弃提交信息
# x, exec = 运行命令（shell 的下一行）
# d, drop = 删除提交
```

**实战场景**：
```bash
# 场景：整理凌乱的提交历史

# 原始历史（5 个提交）
git log --oneline
abc1234 WIP
def5678 WIP
ghi9012 fix typo
jkl3456 add feature
mno7890 WIP

# 交互式变基
git rebase -i HEAD~5

# 在编辑器中修改为：
pick jkl3456 add feature
fixup abc1234
fixup def5678
fixup ghi9012
fixup mno7890

# 结果：5 个提交合并为 1 个
git log --oneline
xyz9999 add feature
```

---

#### ⚠️ 变基的黄金法则

> ⚠️ **铁则**：**永远不要在公共分支上变基！**

**禁止场景**：
- ❌ 已推送到远程的分支
- ❌ 团队协作中的共享分支
- ❌ main/master 等保护分支

**允许场景**：
- ✅ 本地功能分支
- ✅ 未推送的提交
- ✅ 个人实验分支

**风险**：
- 改写历史会导致其他人的仓库不一致
- 需要强制推送（`git push --force`）
- 可能覆盖他人的提交

---

### 3.8 分支上游（upstream）跟踪

#### 设置上游分支

```bash
# 创建本地分支并跟踪远程分支
git switch -c feature origin/feature

# 或为现有分支设置上游
git branch --set-upstream-to=origin/feature feature

# 简写
git branch -u origin/feature feature
```

**输出示例**：
```bash
$ git branch -u origin/feature feature
分支 'feature' 设置为跟踪远程分支 'origin/feature'。
```

---

#### 查看上游分支

```bash
# 查看当前分支的上游
git branch -vv

# 查看指定分支的上游
git rev-parse --abbrev-ref --symbolic-full-name @{u}
```

**输出示例**：
```bash
$ git branch -vv
* main    abc1234 [origin/main] feat: add user login
  feature def5678 [origin/feature] fix: resolve bug
```

**输出解读**：
- `[origin/main]`：上游分支
- `abc1234`：提交哈希

---

#### 推送并设置上游

```bash
# 首次推送时设置上游
git push -u origin feature

# 之后可以直接使用
git push
git pull
```

**说明**：
- `-u`：设置上游（--set-upstream）
- 之后无需指定远程和分支名

---

### 3.9 删除分支

#### 删除本地分支

```bash
# 删除已合并的分支
git branch -d <branch-name>

# 示例
git branch -d feature

# 强制删除未合并的分支
git branch -D <branch-name>

# 示例
git branch -D feature
```

**输出示例**：
```bash
$ git branch -d feature
已删除分支 feature（曾为 abc1234）。

$ git branch -D feature
已删除分支 feature（曾为 abc1234）。
```

**⚠️ 警告**：
- `-d`：只能删除已合并的分支（安全）
- `-D`：强制删除，即使未合并（危险！）
- 删除前确认分支已合并或不需要

---

#### 删除远程分支

```bash
# 删除远程分支
git push origin --delete <branch-name>

# 示例
git push origin --delete feature

# 或另一种写法
git push origin :feature
```

**输出示例**：
```bash
$ git push origin --delete feature
To github.com:example-user/repo.git
 - [deleted]         feature
```

**⚠️ 警告**：
- 删除前通知团队成员
- 确认分支已合并
- 删除后无法恢复（除非有备份）

---

#### 清理无效远程分支

```bash
# 清理已删除的远程分支（本地跟踪分支）
git fetch --prune

# 或
git remote prune origin
```

**输出示例**：
```bash
$ git fetch --prune
From github.com:example-user/repo
 - [已删除]        feature
```

---

### 3.10 孤儿分支（--orphan）

> 🌿 **孤儿分支**：没有历史记录的独立分支，适用于独立文档、GitHub Pages 等

#### 创建孤儿分支

```bash
# 创建孤儿分支
git switch --orphan gh-pages

# 或
git checkout --orphan gh-pages
```

**输出示例**：
```bash
$ git switch --orphan gh-pages
切换到新分支 'gh-pages'
```

**说明**：
- 新分支没有任何提交历史
- 工作区文件保留，但处于未暂存状态
- 适用于完全独立的内容

---

#### 适用场景

**场景 1：GitHub Pages 文档站点**
```bash
# 创建 gh-pages 分支
git switch --orphan gh-pages

# 清理工作区（可选）
git rm -rf .

# 添加文档文件
echo "# My Project" > README.md
git add .
git commit -m "Initial documentation"

# 推送到远程
git push -u origin gh-pages
```

**场景 2：独立的历史归档**
```bash
# 创建归档分支
git switch --orphan archive-2023

# 添加归档文件
git add archive/
git commit -m "Archive 2023 project files"
```

---

### 3.11 Cherry-pick 选择性合并

> 🍒 **Cherry-pick**：选择性合并某个特定提交到当前分支

#### 基本用法

```bash
# 查看提交历史
git log --oneline

# Cherry-pick 指定提交
git cherry-pick abc123

# Cherry-pick 多个提交
git cherry-pick abc123 def456

# Cherry-pick 提交范围
git cherry-pick abc123^..def456
```

**输出示例**：
```bash
$ git cherry-pick abc123
[main 8f3a2b1] feat: add user login
 Date: Sat Mar 21 15:00:00 2026 +0800
 2 files changed, 150 insertions(+)
```

---

#### 处理冲突

```bash
# 如果产生冲突
git cherry-pick abc123

# 输出
自动合并失败，修复冲突然后提交结果。

# 解决冲突后
git add <file>
git cherry-pick --continue

# 或取消
git cherry-pick --abort
```

---

#### 适用场景

- ✅ 将 bug 修复从一个分支应用到其他分支
- ✅ 选择性合并功能，而非整个分支
- ✅ 恢复误删的提交
- ✅ 跨分支移植特定功能

**⚠️ 注意事项**：
- cherry-pick 会创建新提交（不同哈希值）
- 可能产生冲突，需手动解决
- 避免重复 cherry-pick 同一提交

---

### 3.12 Detached HEAD 状态

> 🔍 **什么是 Detached HEAD？**
> 
> HEAD 直接指向某个提交而非分支，处于"游离"状态。

#### 产生场景

```bash
# 直接 checkout 到某个提交
git checkout abc123

# 输出提示
注意：正在切换到 'abc123'。
您正处于'分离头指针'状态。

您可以查看、试验修改，甚至可以提交。
但是您在此做的任何提交将在下次切换分支时丢失。
```

---

#### 解决方法

**方法 1：创建新分支（推荐）**

```bash
# 基于当前提交创建新分支
git switch -c new-branch

# 或
git checkout -b new-branch
```

**方法 2：回到已有分支**

```bash
# 切换回 main 分支
git switch main

# 或
git checkout main
```

---

#### ⚠️ 警告

- Detached HEAD 状态下提交的代码，切换分支后**可能丢失**
- 如需保留，**务必创建新分支**
- 适合临时测试、查看历史版本

---

## 第 4 章 标签使用

### 4.1 标签概念

#### 什么是标签？

> **标签（Tag）** 是 Git 用来标记特定提交的引用，通常用于版本发布。

**标签 vs 分支**：

| 特性 | 标签 | 分支 |
|:---|:---|:---|
| **用途** | 标记版本发布 | 并行开发 |
| **是否移动** | ❌ 固定 | ✅ 随提交移动 |
| **典型命名** | v1.0, v2.1.0 | feature/login, bugfix-123 |
| **创建频率** | 低（发布时） | 高（日常开发） |

**形象比喻**：
```
分支 = 正在写的书稿（持续更新）
标签 = 已出版的书（固定版本）
```

---

### 4.2 标签类型

#### 轻量标签（Lightweight）

> **轻量标签**：仅是一个指向提交的指针，无额外信息

```bash
# 创建轻量标签
git tag v1.0

# 查看标签
git show v1.0
```

**输出示例**：
```bash
$ git show v1.0
commit 921d88e7bc8de6b8575e77513ee9805021ffc5ef
Author: hjs2015 <1656126280@qq.com>
Date:   Sat Mar 21 14:50:00 2026 +0800

    merge testing to main
```

**适用场景**：
- ✅ 临时标记
- ✅ 个人测试
- ❌ 正式版本发布

---

#### 附注标签（Annotated）

> **附注标签**：包含标签信息（标签名、标签作者、日期、说明）

```bash
# 创建附注标签
git tag -a v1.0 -m "版本 1.0 - 初始发布"

# 或打开编辑器输入说明
git tag -a v1.0
```

**输出示例**：
```bash
$ git show v1.0
tag v1.0
Tagger: hjs2015 <1656126280@qq.com>
Date:   Sat Mar 21 15:00:00 2026 +0800

版本 1.0 - 初始发布

commit 921d88e7bc8de6b8575e77513ee9805021ffc5ef
Author: hjs2015 <1656126280@qq.com>
Date:   Sat Mar 21 14:50:00 2026 +0800

    merge testing to main
```

**适用场景**：
- ✅ 正式版本发布
- ✅ 需要记录发布信息
- ✅ 团队协作

**推荐**：企业项目统一使用附注标签

---

### 4.3 创建标签

#### 基于当前提交创建

```bash
# 轻量标签
git tag v1.0

# 附注标签（推荐）
git tag -a v1.0 -m "版本 1.0 - 初始发布"
```

---

#### 基于历史提交创建

```bash
# 查看提交历史
git log --oneline

# 基于指定提交创建标签
git tag -a v1.0 abc123 -m "版本 1.0"
```

**适用场景**：
- 补发历史版本的标签
- 标记重要的历史节点

---

#### 语义化版本规范

> 📋 **语义化版本（Semantic Versioning）**：`主版本号。次版本号。修订号`

**格式**：`vX.Y.Z`
- `X`：主版本号（不兼容的 API 修改）
- `Y`：次版本号（向下兼容的功能性新增）
- `Z`：修订号（向下兼容的问题修正）

**示例**：
```bash
git tag -a v1.0.0 -m "初始版本"
git tag -a v1.1.0 -m "新增用户管理功能"
git tag -a v1.1.1 -m "修复登录 bug"
git tag -a v2.0.0 -m "重大更新，不兼容旧版本"
```

---

### 4.4 查看标签

#### 查看标签列表

```bash
# 查看所有标签
git tag

# 按模式过滤
git tag -l "v1.*"

# 查看标签数量
git tag | wc -l
```

**输出示例**：
```bash
$ git tag
v1.0
v1.1
v2.0

$ git tag -l "v1.*"
v1.0
v1.1
```

---

#### 查看标签详情

```bash
# 查看标签信息
git show v1.0

# 仅查看标签信息（不显示提交）
git tag -n v1.0

# 查看所有标签及说明
git tag -n
```

**输出示例**：
```bash
$ git tag -n
v1.0    版本 1.0 - 初始发布
v1.1    新增用户管理功能
v2.0    重大更新，不兼容旧版本
```

---

### 4.5 标签推送

#### 推送单个标签

```bash
# 推送指定标签到远程
git push origin v1.0
```

**输出示例**：
```bash
$ git push origin v1.0
Total 0 (delta 0), reused 0 (delta 0)
To github.com:example-user/repo.git
 * [new tag]         v1.0 -> v1.0
```

---

#### 推送所有标签

```bash
# 一次性推送所有本地标签
git push origin --tags
```

**输出示例**：
```bash
$ git push origin --tags
Total 0 (delta 0), reused 0 (delta 0)
To github.com:example-user/repo.git
 * [new tag]         v1.0 -> v1.0
 * [new tag]         v1.1 -> v1.1
 * [new tag]         v2.0 -> v2.0
```

**⚠️ 注意**：
- 仅推送本地标签
- 不会删除远程已删除的标签

---

### 4.6 标签删除

#### 删除本地标签

```bash
# 删除本地标签
git tag -d v1.0

# 或
git tag --delete v1.0
```

**输出示例**：
```bash
$ git tag -d v1.0
已删除标签 'v1.0'（曾为 a1b2c3d）
```

---

#### 删除远程标签

```bash
# 删除远程标签
git push origin --delete v1.0

# 或另一种写法
git push origin :refs/tags/v1.0
```

**输出示例**：
```bash
$ git push origin --delete v1.0
To github.com:example-user/repo.git
 - [deleted]         v1.0
```

---

#### 删除所有本地标签

```bash
# ⚠️ 警告：谨慎使用！
git tag -l | xargs git tag -d

# 清理远程所有标签
git push origin --tags
```

---

### 4.7 标签回滚

#### 切换到标签

```bash
# 切换到标签（Detached HEAD 状态）
git checkout v1.0

# 或
git switch v1.0
```

**输出**：
```bash
注意：正在切换到 'v1.0'。
您正处于'分离头指针'状态。
```

---

#### 基于标签创建分支

```bash
# 基于标签创建修复分支
git switch -c hotfix v1.0

# 或
git checkout -b hotfix v1.0
```

**适用场景**：
- 修复旧版本的 bug
- 维护多个版本

---

## 第 5 章 远程仓库操作

### 5.1 远程仓库管理

#### 查看远程仓库

```bash
# 查看远程仓库
git remote -v

# 详细信息
git remote show origin
```

**输出示例**：
```bash
$ git remote -v
origin  git@github.com:example-user/repo.git (fetch)
origin  git@github.com:example-user/repo.git (push)

$ git remote show origin
* 远程 origin
  获取 URL：git@github.com:example-user/repo.git
  推送 URL：git@github.com:example-user/repo.git
  HEAD 分支：main
  远程分支：
    main    跟踪
    develop 跟踪
  本地分支配置为 'git pull'：
    main    合并至远程 main
```

---

#### 添加远程仓库

```bash
# 添加远程仓库
git remote add origin git@github.com:example-user/repo.git

# 验证
git remote -v
```

**输出示例**：
```bash
$ git remote add origin git@github.com:example-user/repo.git
$ git remote -v
origin  git@github.com:example-user/repo.git (fetch)
origin  git@github.com:example-user/repo.git (push)
```

---

#### 重命名远程仓库

```bash
# 重命名远程仓库
git remote rename old-name new-name

# 示例
git remote rename origin upstream
```

**适用场景**：
- Fork 项目后，原仓库改为 upstream
- 统一团队命名规范

---

#### 修改远程仓库 URL

```bash
# 修改远程仓库地址
git remote set-url origin git@github.com:example-user/new-repo.git

# 验证
git remote -v
```

**适用场景**：
- 仓库迁移（GitHub → GitLab）
- 仓库重命名
- 切换 SSH/HTTPS 协议

---

#### 删除远程仓库

```bash
# 删除远程仓库
git remote remove origin

# 或
git remote rm origin

# 验证
git remote -v
```

**⚠️ 警告**：
- 删除后无法推送/拉取
- 需要重新添加远程仓库

---

### 5.2 Git Fetch 完整用法

> 📥 **Fetch**：从远程仓库获取数据，但不合并

#### 基本用法

```bash
# 获取所有远程分支
git fetch origin

# 获取指定分支
git fetch origin main

# 获取所有远程仓库
git fetch --all

# 获取并清理无效分支
git fetch --prune
```

**输出示例**：
```bash
$ git fetch origin
From github.com:example-user/repo
 * [新分支]        feature -> origin/feature
   3e4f5a6..7b8c9d0  main     -> origin/main
```

---

#### Fetch vs Pull

| 命令 | 获取数据 | 自动合并 | 安全性 | 推荐场景 |
|:---|:---:|:---:|:---:|:---|
| `git fetch` | ✅ | ❌ | ⭐⭐⭐⭐⭐ | 先查看再合并 |
| `git pull` | ✅ | ✅ | ⭐⭐⭐ | 快速同步 |

**推荐流程**：
```bash
# 1. 先获取
git fetch origin

# 2. 查看差异
git log HEAD..origin/main

# 3. 安全合并
git merge origin/main

# 或一步（pull）
git pull origin main
```

---

### 5.3 Git Push 进阶用法

#### 基本推送

```bash
# 推送当前分支并设置上游
git push -u origin main

# 推送指定分支
git push origin feature

# 推送所有分支
git push --all origin
```

---

#### 强制推送

> ⚠️ **警告**：强制推送会覆盖远程历史，谨慎使用！

**方法 1：普通强制推送（危险）**
```bash
git push --force origin main
```

**方法 2：安全强制推送（推荐）**
```bash
git push --force-with-lease origin main
```

---

#### --force vs --force-with-lease

| 特性 | --force | --force-with-lease |
|:---|:---|:---|
| **安全性** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **检查远程** | ❌ 不检查 | ✅ 检查 |
| **覆盖风险** | 高 | 低 |
| **推荐度** | ❌ 不推荐 | ✅ 强烈推荐 |

**--force-with-lease 优势**：
- 检查远程分支是否被他人修改
- 如果有新提交，拒绝推送
- 避免覆盖他人的工作

---

#### 推送标签

```bash
# 推送单个标签
git push origin v1.0

# 推送所有标签
git push origin --tags
```

---

### 5.4 Git Pull 进阶用法

#### 基本拉取

```bash
# 拉取并合并
git pull origin main

# 拉取并变基（推荐）
git pull --rebase origin main
```

---

#### Pull with Rebase

> 🔄 **Pull with Rebase**：拉取时用变基替代合并，保持线性历史

**对比**：

**普通 Pull（Merge）**：
```bash
git pull origin main
```
```
*   合并提交
|\
| * 远程提交
* | 本地提交
|/
* 共同祖先
```

**Pull with Rebase**：
```bash
git pull --rebase origin main
```
```
* 本地提交（变基后）
* 远程提交
* 共同祖先
```

---

#### 配置默认使用 Rebase

```bash
# 全局配置
git config --global pull.rebase true

# 或仅对当前仓库
git config pull.rebase true

# 验证
git config pull.rebase
```

**输出**：
```bash
true
```

---

### 5.5 Git Submodule 子模块

> 📦 **Submodule**：在一个仓库中嵌入另一个仓库

#### 添加子模块

```bash
# 添加子模块
git submodule add <repository-url> <path>

# 示例
git submodule add https://github.com/example/lib.git libs/lib
```

**输出示例**：
```bash
$ git submodule add https://github.com/example/lib.git libs/lib
正克隆到 'libs/lib'...
```

---

#### 查看子模块

```bash
# 查看子模块状态
git submodule status

# 查看子模块信息
git submodule
```

**输出示例**：
```bash
$ git submodule status
 8f3a2b1 libs/lib (heads/main)
```

---

#### 克隆含子模块的仓库

```bash
# 方法 1：克隆时初始化子模块
git clone --recursive <repository-url>

# 方法 2：克隆后初始化
git clone <repository-url>
cd repo
git submodule init
git submodule update
```

---

#### 更新子模块

```bash
# 更新所有子模块
git submodule update --remote

# 更新指定子模块
git submodule update --remote libs/lib
```

---

#### 删除子模块

```bash
# ⚠️ 手动删除子模块（Git 无内置命令）
# 1. 从 .gitmodules 删除配置
# 2. 从 .git/config 删除配置
# 3. 删除子模块目录
# 4. 提交更改

git rm libs/lib
git commit -m "Remove submodule"
```

---

### 5.6 Git Worktree 工作树

> 🌳 **Worktree**：多个工作目录共享同一个仓库，适用于多分支并行开发

#### 创建 Worktree

```bash
# 创建新 worktree
git worktree add <path> <branch>

# 示例
git worktree add ../feature-worktree feature
```

**输出示例**：
```bash
$ git worktree add ../feature-worktree feature
准备工作目录 '../feature-worktree'
切换到分支 'feature'
```

---

#### 查看 Worktree

```bash
# 查看所有 worktree
git worktree list
```

**输出示例**：
```bash
$ git worktree list
/path/to/repo     main
/path/feature-worktree  feature
```

---

#### 删除 Worktree

```bash
# 删除 worktree
git worktree remove <path>

# 示例
git worktree remove ../feature-worktree
```

---

#### 适用场景

**场景 1：同时开发多个功能**
```bash
# 主工作区：main 分支
cd /path/to/repo
git switch main

# Worktree 1：feature-a 分支
git worktree add ../feature-a feature-a
cd ../feature-a
# 开发功能 A

# Worktree 2：feature-b 分支
git worktree add ../feature-b feature-b
cd ../feature-b
# 开发功能 B
```

**优势**：
- ✅ 无需频繁切换分支
- ✅ 每个 worktree 独立工作区
- ✅ 共享 .git 目录，节省空间

---

## 第 6 章 Git 核心底层原理

> 🔬 **深入理解 Git 内部机制**  
> 掌握底层原理，让你从"会用 Git"进阶到"理解 Git"，遇到复杂问题不再迷茫

### 6.1 Git 对象模型

#### 四种核心对象

> Git 所有内容都存储为对象，每种对象都有唯一 SHA-1 哈希 ID

**对象类型**：

| 类型 | 作用 | 内容 | 示例 |
|:---:|:---|:---|:---|
| **Blob** | 存储文件内容 | 文件的二进制数据 | 源代码、配置文件 |
| **Tree** | 存储目录结构 | 文件名 + 类型 + Blob/Tree 引用 | 目录、子目录 |
| **Commit** | 存储提交信息 | Tree 引用 + 父提交 + 作者 + 提交信息 | 版本快照 |
| **Tag** | 存储标签信息 | Commit 引用 + 标签名 + 签名 | 版本标记 |

**对象关系图**：
```
Commit 对象
┌─────────────────────────────────┐
│ commit abc123...                │
│ tree def456...  ← 指向 Tree     │
│ parent 789ghi... ← 父提交       │
│ author Example <1656126280@qq.com>│
│ date 2026-03-21 10:30:00        │
│ message "Fix login bug"         │
└─────────────────────────────────┘
           ↓
Tree 对象
┌─────────────────────────────────┐
│ tree def456...                  │
│ 040000 tree abc... src/         │
│ 040000 tree def... tests/       │
│ 100644 blob 123... README.md    │
│ 100644 blob 456... main.py      │
└─────────────────────────────────┘
           ↓
Blob 对象
┌─────────────────────────────────┐
│ blob 123...                     │
│ # Project README                │
│ This is a sample project...     │
└─────────────────────────────────┘
```

---

#### 查看 Git 对象

```bash
# 查看对象类型
git cat-file -t <hash>

# 查看对象内容
git cat-file -p <hash>

# 示例：查看提交对象
git cat-file -t abc123...
# 输出：commit

git cat-file -p abc123...
# 输出：
# tree def456...
# parent 789ghi...
# author Example <1656126280@qq.com> 1711008600 +0800
# committer Example <1656126280@qq.com> 1711008600 +0800
# 
# Fix login bug
```

---

#### 实践：手动创建 Git 对象

```bash
# 1. 创建 Blob 对象
echo "Hello Git" | git hash-object -w --stdin
# 输出：83dbaef... (SHA-1 哈希)

# 2. 查看 Blob 内容
git cat-file -p 83dbaef...
# 输出：Hello Git

# 3. 创建 Tree 对象
git mktree <<EOF
100644 blob 83dbaef... hello.txt
EOF
# 输出：tree 哈希

# 4. 创建 Commit 对象
echo "Initial commit" | git commit-tree <tree-hash>
# 输出：commit 哈希
```

**⚠️ 注意**：手动创建对象很少用，但有助于理解原理

---

### 6.2 SHA-1 哈希算法

#### 哈希特性

> Git 使用 SHA-1（160 位）为每个对象生成唯一标识

**SHA-1 特点**：
- ✅ **唯一性**：不同内容生成不同哈希（理论上）
- ✅ **不可逆**：无法从哈希反推内容
- ✅ **固定长度**：始终 40 个十六进制字符
- ✅ **雪崩效应**：内容微小变化，哈希完全不同

**示例**：
```bash
# 相同内容 → 相同哈希
echo "Hello" | git hash-object --stdin
# 输出：f57035b

echo "Hello" | git hash-object --stdin
# 输出：f57035b (完全相同)

# 不同内容 → 完全不同哈希
echo "Hello" | git hash-object --stdin
# 输出：f57035b

echo "hello" | git hash-object --stdin
# 输出：95297e (小写 h 完全不同)
```

---

#### SHA-256 迁移

> ⚠️ SHA-1 已证明存在理论漏洞，Git 正在迁移到 SHA-256

```bash
# 查看当前哈希算法
git config extensions.objectFormat

# Git 2.42+ 支持 SHA-256
git init --object-format=sha256
```

**迁移计划**：
- Git 2.29+：支持 SHA-256 实验性功能
- Git 2.42+：SHA-256 更稳定
- 未来：默认使用 SHA-256

---

### 6.3 引用（Reference）

#### 什么是引用？

> **引用**是指向 Commit 的指针，是 Git 中"可变"的部分

**引用类型**：
```
refs/
├── heads/           # 分支引用
│   ├── main        → commit abc123
│   └── feature     → commit def456
├── tags/            # 标签引用
│   ├── v1.0        → commit 789ghi
│   └── v2.0        → commit jkl012
└── remotes/         # 远程跟踪引用
    └── origin/
        ├── main    → commit mno345
        └── develop → commit pqr678
```

---

#### 查看引用

```bash
# 查看所有引用
git show-ref

# 输出示例
abc123... refs/heads/main
def456... refs/heads/feature
789ghi... refs/tags/v1.0
mno345... refs/remotes/origin/main

# 查看引用文件
cat .git/refs/heads/main
# 输出：abc123...

# 查看 HEAD
cat .git/HEAD
# 输出：ref: refs/heads/main
```

---

#### HEAD 详解

> **HEAD** 是当前分支的引用，指向你正在工作的分支

**HEAD 状态**：
```
正常状态（附加到分支）：
.git/HEAD → ref: refs/heads/main → commit abc123

Detached HEAD（游离状态）：
.git/HEAD → commit abc123 (直接指向提交，不指向分支)
```

**切换 HEAD**：
```bash
# 正常切换（移动分支指针）
git switch feature
# HEAD → refs/heads/feature

# Detached HEAD（直接指向提交）
git switch --detach abc123
# HEAD → abc123 (不指向任何分支)
```

---

### 6.4 索引（Index）详解

#### 索引是什么？

> **索引**（暂存区）是 Git 的核心设计，是工作区和仓库之间的缓冲区

**索引文件**：
- 位置：`.git/index`
- 作用：记录准备提交的文件状态
- 格式：二进制文件（不能用文本编辑器打开）

**索引内容**：
```
索引条目 = 文件路径 + Blob 哈希 + 文件模式 + 时间戳

示例：
100644 blob 83dbaef... README.md
100644 blob 123abc... src/main.py
040000 tree def456... src/
```

---

#### 索引操作

```bash
# 查看索引内容
git ls-files --stage

# 输出示例
100644 83dbaef... 0	README.md
100644 123abc... 0	src/main.py

# 格式说明
# 文件模式  Blob 哈希     阶段	文件路径
# 阶段 0 = 正常
# 阶段 1 = 合并基线
# 阶段 2 = ours
# 阶段 3 = theirs
```

---

#### 索引与合并冲突

```bash
# 合并冲突时，索引包含 3 个版本
git ls-files --stage

# 输出示例
100644 abc123... 1	config.txt  # 共同祖先
100644 def456... 2	config.txt  # 当前分支 (ours)
100644 789ghi... 3	config.txt  # 合并分支 (theirs)

# 解决冲突后，索引恢复正常
git add config.txt
git ls-files --stage
# 输出：100644 jkl012... 0	config.txt
```

---

### 6.5 Packfile 打包机制

#### 为什么需要 Packfile？

> 随着提交增多，Git 对象会占用大量磁盘空间。Packfile 通过压缩和增量存储优化空间

**存储演进**：
```
初期（松散对象）：
.git/objects/
├── ab/ cdef123...  (Blob)
├── 12/ 345678...  (Tree)
└── 78/ 9abcde...  (Commit)
每个对象独立文件

后期（打包后）：
.git/objects/
├── pack/
│   ├── pack-abc123...pack  (打包文件)
│   └── pack-abc123...idx   (索引文件)
所有对象压缩到一个文件
```

---

#### Packfile 操作

```bash
# 手动打包
git gc
# Git 自动清理和优化

# 查看打包信息
git count-objects -v

# 输出示例
count: 150            # 松散对象数
size: 600             # 松散对象占用 (KB)
in-pack: 5000         # 打包对象数
packs: 1              # 打包文件数
size-pack: 2048       # 打包文件大小 (KB)
prune-packable: 0     # 可修剪的打包对象
garbage: 0            # 垃圾对象
```

---

#### 增量打包（Delta）

> Packfile 使用增量压缩：相似对象只存储差异部分

**原理**：
```
原始存储：
Commit 1: 100KB (完整存储)
Commit 2: 100KB (完整存储)
Commit 3: 100KB (完整存储)
总计：300KB

增量打包：
Commit 1: 100KB (基准)
Commit 2: 5KB (只存差异)
Commit 3: 3KB (只存差异)
总计：108KB (节省 64%)
```

---

### 6.6 Reflog 引用日志

#### Reflog 是什么？

> **Reflog** 记录 HEAD 和分支的所有移动历史，是 Git 的"后悔药"

**Reflog vs Log**：
| 特性 | Log | Reflog |
|:---|:---|:---|
| **记录内容** | 提交历史 | 引用移动历史 |
| **持久性** | 永久（除非删除） | 默认 90 天过期 |
| **作用** | 查看项目演进 | 恢复误操作 |
| **范围** | 当前分支 | 所有引用移动 |

---

#### Reflog 操作

```bash
# 查看 HEAD 移动历史
git reflog

# 输出示例
abc123 HEAD@{0}: reset: moving to HEAD~1
def456 HEAD@{1}: commit: Add new feature
789ghi HEAD@{2}: checkout: moving from main to feature

# 查看指定引用的 reflog
git reflog show main

# 从 reflog 恢复
git reset --hard HEAD@{2}
```

---

#### Reflog 恢复场景

**场景 1：误删分支**
```bash
# 删除分支
git branch -D feature

# 从 reflog 找回
git reflog | grep feature
# 输出：abc123 HEAD@{3}: branch: Created from 'main'

git branch feature abc123
```

**场景 2：误用 reset**
```bash
# 误操作
git reset --hard HEAD~3

# 找回丢失的提交
git reflog
# 找到 reset 前的提交哈希

git reset --hard def456  # 恢复到之前状态
```

---

### 6.7 Git Hooks 钩子原理

#### Hooks 工作机制

> **Hooks** 是 Git 在特定事件触发的脚本，位于 `.git/hooks/`

**钩子类型**：
```
客户端钩子：
├── pre-commit      → git commit 前
├── prepare-commit-msg → 提交信息编辑前
├── commit-msg      → 提交信息编辑后
├── post-commit     → git commit 后
├── pre-push        → git push 前
└── post-checkout   → git checkout 后

服务端钩子：
├── pre-receive     → 接收推送前
├── update          → 更新引用前
└── post-receive    → 推送完成后
```

---

#### 钩子示例

```bash
# pre-commit 钩子示例
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# 检查是否有调试代码

if git diff --cached | grep -q "console.log\|debugger"; then
    echo "❌ 错误：检测到调试代码"
    exit 1
fi

# 检查代码格式
if ! command -v black &> /dev/null; then
    echo "⚠️ 警告：black 未安装，跳过格式检查"
    exit 0
fi

git diff --cached --name-only | grep '\.py$' | xargs black --check
EOF

chmod +x .git/hooks/pre-commit
```

---

## 第 7 章 Git 企业级协作规范

> 🏢 **企业级 Git 工作流**  
> 标准化流程、代码审查、权限管理、自动化检查，提升团队协作效率

### 7.1 Git Flow 工作流

#### Git Flow 模型

> **Git Flow** 是最经典的企业级工作流，适合有固定发布周期的项目

**分支结构**：
```
main (生产环境)
  ↑
release/v1.0 (预发布)
  ↑
develop (开发主线)
  ├── feature/login (功能分支)
  ├── feature/payment (功能分支)
  └── feature/user-profile (功能分支)
  
hotfix/bug-fix (紧急修复，从 main 分出)
```

---

#### 分支类型详解

| 分支类型 | 命名规范 | 来源 | 合并到 | 用途 |
|:---|:---|:---|:---|:---|
| **main** | main/master | - | - | 生产环境，随时可部署 |
| **develop** | develop | main | main | 开发主线，包含最新功能 |
| **feature** | feature/* | develop | develop | 新功能开发 |
| **release** | release/* | develop | main + develop | 预发布，测试修复 |
| **hotfix** | hotfix/* | main | main + develop | 紧急修复 |

---

#### Git Flow 操作流程

**1. 开发新功能**
```bash
# 从 develop 创建功能分支
git switch develop
git switch -c feature/user-auth

# 开发功能
# ... 编写代码 ...

git add .
git commit -m "feat: add user authentication"

# 推送功能分支
git push -u origin feature/user-auth

# 完成后合并回 develop
git switch develop
git merge --no-ff feature/user-auth
git branch -d feature/user-auth
git push origin develop
```

---

**2. 发布新版本**
```bash
# 从 develop 创建 release 分支
git switch develop
git switch -c release/v1.0

# 版本号更新、最终测试
# ... 修复 bug ...

git commit -m "chore: bump version to 1.0.0"

# 合并到 main 和 develop
git switch main
git merge --no-ff release/v1.0
git tag v1.0

git switch develop
git merge --no-ff release/v1.0

git branch -d release/v1.0
git push origin main develop --tags
```

---

**3. 紧急修复**
```bash
# 从 main 创建 hotfix 分支
git switch main
git switch -c hotfix/login-bug

# 修复 bug
# ... 修复代码 ...

git commit -m "fix: resolve login issue"

# 合并到 main 和 develop
git switch main
git merge --no-ff hotfix/login-bug
git tag v1.0.1

git switch develop
git merge --no-ff hotfix/login-bug

git branch -d hotfix/login-bug
git push origin main develop --tags
```

---

### 7.3 企业级分支命名规范

#### 分支类型与命名规则

| 分支类型 | 命名格式 | 来源分支 | 合并到 | 说明 |
|:---|:---|:---|:---|:---|
| **功能分支** | `feature/<功能描述>` | develop | develop | 新功能开发 |
| **修复分支** | `bugfix/<问题描述>` | develop | develop | Bug 修复 |
| **预发布分支** | `release/<版本号>` | develop | main + develop | 发布准备 |
| **热修复分支** | `hotfix/<问题描述>` | main | main + develop | 线上紧急修复 |
| **实验分支** | `experiment/<实验名称>` | 任意 | 不合并 | 技术实验 |

#### 命名示例

**功能分支**：
```bash
feature/user-login          # 用户登录功能
feature/payment-gateway     # 支付网关集成
feature/user-profile-page   # 用户资料页面
```

**修复分支**：
```bash
bugfix/fix-login-error      # 修复登录错误
bugfix/issue-123            # 修复 Issue #123
bugfix/memory-leak          # 修复内存泄漏
```

**预发布分支**：
```bash
release/v1.0.0              # 1.0.0 版本发布
release/v2.1.0-beta         # 2.1.0 测试版
```

**热修复分支**：
```bash
hotfix/fix-production-crash  # 修复线上崩溃
hotfix/security-patch        # 安全补丁
```

#### 分支命名最佳实践

✅ **推荐**：
- 使用小写字母和连字符：`feature/user-login`
- 简洁明了：`bugfix/login-error`
- 包含 Issue 编号：`feature/GH-123-add-payment`
- 使用动词开头：`fix/`, `add/`, `update/`

❌ **避免**：
- 中文命名：`feature/用户登录` ❌
- 下划线分隔：`feature/user_login` ❌
- 过于冗长：`feature/add-new-user-login-functionality` ❌
- 无意义命名：`feature/test1`, `branch/abc` ❌

---

### 7.4 PR/MR 提交流程与模板

#### 完整 PR 流程

**1. 创建功能分支**：
```bash
git switch develop
git pull origin develop
git switch -c feature/user-auth
```

**2. 开发并提交**：
```bash
# ... 开发功能 ...
git add .
git commit -m "feat(auth): add user login"
git push -u origin feature/user-auth
```

**3. 创建 Pull Request**

访问 GitHub/GitLab，点击 "New Pull Request"

**PR 模板**：
```markdown
## 📝 变更说明

**需求链接**: [JIRA-123](https://jira.example.com/browse/JIRA-123)
**需求描述**: 实现用户登录功能，支持邮箱和密码登录

## 🎯 变更类型

- [x] ✨ 新功能
- [ ] 🐛 Bug 修复
- [ ] 📝 文档更新
- [ ] ♻️ 代码重构
- [ ] ⚡ 性能优化
- [ ] 🔒 安全修复

## 🧪 测试清单

- [x] 单元测试已添加
- [x] 集成测试通过
- [x] 手动测试完成
- [ ] E2E 测试（如适用）

## 📸 截图（如适用）

登录页面：
![登录页面](screenshot.png)

## ✅ 自查清单

- [x] 代码符合团队规范
- [x] 无调试代码（console.log 等）
- [x] 提交信息符合约定式规范
- [x] 已更新相关文档
- [x] 无安全漏洞

## 📋 测试步骤

1. 访问 `/login` 页面
2. 输入正确的邮箱和密码
3. 点击登录按钮
4. 验证跳转到首页

## 🔗 相关链接

- 需求文档：[链接](https://confluence.example.com/login)
- 设计稿：[Figma](https://figma.com/file/xxx)
```

**4. 代码审查（Code Review）**

团队成员审查代码，提出意见：

```
@developer 张三：
1. 第 23 行：建议添加错误处理
2. 第 45 行：这个逻辑可以提取为函数
3. 整体结构不错 👍
```

**5. 修改并提交**

```bash
# 根据审查意见修改
git add .
git commit -m "refactor(auth): address code review comments"
git push
```

**6. 合并 PR**

审查通过后，点击 "Merge Pull Request"

**7. 清理分支**

```bash
git switch develop
git pull origin develop
git branch -d feature/user-auth
git push origin --delete feature/user-auth
```

---

#### Git Flow 工具

```bash
# 安装 git-flow
# Ubuntu/Debian
sudo apt install git-flow

# macOS
brew install git-flow

# 初始化 git-flow
git flow init

# 使用 git-flow 命令
git flow feature start login
git flow feature finish login
git flow release start 1.0
git flow release finish 1.0
git flow hotfix start bug-fix
git flow hotfix finish bug-fix
```

---

### 7.2 GitHub Flow 工作流

#### GitHub Flow 特点

> **GitHub Flow** 更轻量，适合持续部署的 SaaS 项目

**核心规则**：
1. ✅ main 分支随时可部署
2. ✅ 功能分支从 main 创建
3. ✅ 推送后创建 Pull Request
4. ✅ 代码审查通过后合并
5. ✅ 合并后立即部署

**流程图**：
```
main (始终可部署)
  ↓
创建分支 feature-xxx
  ↓
本地开发 + 提交
  ↓
推送到 GitHub
  ↓
创建 Pull Request
  ↓
团队审查 + 讨论
  ↓
通过审查
  ↓
合并到 main
  ↓
自动部署到生产
```

---

#### GitHub Flow 操作

```bash
# 1. 从 main 创建分支
git switch main
git pull origin main
git switch -c feature/new-checkout

# 2. 开发功能
# ... 编写代码 ...
git commit -m "Add new checkout flow"

# 3. 推送并创建 PR
git push -u origin feature/new-checkout
# 在 GitHub 上创建 Pull Request

# 4. 代码审查（GitHub 界面）
# - 同事审查代码
# - 讨论修改建议
# - CI 自动测试

# 5. 合并到 main
# - 审查通过后点击 "Merge"
# - 删除功能分支

# 6. 部署
# - 自动部署到生产环境
```

---

### 7.3 提交信息规范

#### Conventional Commits

> **约定式提交**：标准化的提交信息格式，便于自动生成 CHANGELOG

**格式**：
```
<type>(<scope>): <subject>

<body>

<footer>
```

**示例**：
```bash
feat(auth): add user login functionality

Implement OAuth2 login with Google and GitHub providers.
Add login form validation and error handling.

Closes #123
BREAKING CHANGE: login API endpoint changed from /auth to /api/v1/auth
```

---

#### 提交类型（type）

| 类型 | 说明 | 示例 |
|:---|:---|:---|
| **feat** | 新功能 | `feat: add payment module` |
| **fix** | 修复 bug | `fix: resolve memory leak` |
| **docs** | 文档更新 | `docs: update API reference` |
| **style** | 代码格式 | `style: format code with prettier` |
| **refactor** | 代码重构 | `refactor: simplify user service` |
| **test** | 测试相关 | `test: add unit tests for auth` |
| **chore** | 构建/工具 | `chore: update dependencies` |
| **perf** | 性能优化 | `perf: improve query speed` |
| **ci** | CI 配置 | `ci: add GitHub Actions workflow` |
| **build** | 构建系统 | `build: upgrade webpack to v5` |

---

#### 作用域（scope）

> **scope** 指定修改影响的模块或范围

**常见作用域**：
```
feat(auth): ...        # 认证模块
fix(api): ...          # API 服务
docs(readme): ...      # README 文档
test(unit): ...        # 单元测试
ci(github): ...        # GitHub Actions
```

**无作用域**（影响全局）：
```
feat: add logging
fix: resolve typo
```

---

#### 主题行（subject）规则

> **主题行** 简明扼要描述修改内容

**规则**：
1. ✅ 使用祈使句（"add" 而非 "added"）
2. ✅ 首字母小写
3. ✅ 末尾无句号
4. ✅ 长度 ≤ 50 字符

**好 vs 坏**：
```bash
# ✅ 好
feat: add user authentication
fix: resolve login timeout issue

# ❌ 坏
feat: Added user authentication (过去式)
Fix: Resolved login timeout issue. (首字母大写 + 句号)
fix: This is a very long commit message that exceeds 50 characters limit
```

---

#### 正文（body）和页脚（footer）

**正文**（可选）：
- 描述修改动机
- 说明实现方式
- 解释设计决策

**页脚**（可选）：
- 关联 Issue：`Closes #123`
- 破坏性变更：`BREAKING CHANGE: ...`
- 共同作者：`Co-authored-by: Name <email>`

**完整示例**：
```bash
feat(payment): integrate Stripe payment gateway

Add Stripe integration for credit card payments.
Implement webhook handling for payment events.
Add payment status tracking in database.

Testing:
- Unit tests for payment service
- Integration tests with Stripe test mode

Closes #456
BREAKING CHANGE: Payment API response format changed
```

---

### 7.4 代码审查（Code Review）

#### Pull Request 流程

> **PR 流程**：确保代码质量、知识共享、团队对齐

**标准流程**：
```
1. 创建 PR
   ↓
2. 自动检查（CI）
   ↓
3. 分配审查者
   ↓
4. 审查代码
   ↓
5. 讨论修改
   ↓
6. 通过审查
   ↓
7. 合并代码
```

---

#### 审查清单

**代码质量**：
- ✅ 代码是否清晰易懂？
- ✅ 是否有重复代码？
- ✅ 是否遵循编码规范？
- ✅ 是否有必要的注释？

**功能正确性**：
- ✅ 是否实现需求？
- ✅ 边界条件是否处理？
- ✅ 错误处理是否完善？
- ✅ 是否有单元测试？

**性能与安全**：
- ✅ 是否有性能问题？
- ✅ 是否有安全漏洞？
- ✅ 是否处理敏感数据？
- ✅ 是否有 SQL 注入风险？

---

#### PR 模板

```markdown
## 描述
简要说明此 PR 的目的和变更内容

## 变更类型
- [ ] 新功能
- [ ] Bug 修复
- [ ] 文档更新
- [ ] 代码重构
- [ ] 性能优化

## 测试
- [ ] 已添加单元测试
- [ ] 已进行手动测试
- [ ] 测试覆盖率达标

## 截图（如适用）
添加 UI 变更的截图

## 关联 Issue
Closes #123
```

---

### 7.5 权限管理

#### 分支保护规则

> **分支保护**：防止意外推送、强制代码审查、要求 CI 通过

**GitHub 分支保护设置**：
```
Settings → Branches → Branch protection rules

添加规则：
✓ Require a pull request before merging
  - Require approvals: 1
  - Dismiss stale pull request approvals
✓ Require status checks to pass
  - CI/CD pipeline
  - Code coverage
✓ Require linear history
✓ Include administrators
```

---

#### 团队权限模型

| 角色 | 权限 | 适用场景 |
|:---|:---|:---|
| **Read** | 查看代码、创建 Issue | 初级开发者、外部贡献者 |
| **Triage** | Read + 管理 Issue/PR | 社区管理员 |
| **Write** | 推送代码、创建分支 | 核心开发者 |
| **Maintain** | Write + 管理分支/标签 | 技术负责人 |
| **Admin** | 所有权限（包括删除仓库） | 仓库所有者 |

---

### 7.6 CI/CD 集成

#### GitHub Actions 示例

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run tests
        run: pytest --cov=src
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build Docker image
        run: docker build -t app:${{ github.sha }} .
      
      - name: Push to registry
        run: docker push app:${{ github.sha }}

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Deploy to production
        run: ./deploy.sh
```

---

### 7.7  monorepo 多项目管理

#### Monorepo 概念

> **Monorepo**：多个项目共享同一个 Git 仓库，便于代码复用和原子提交

**优势**：
- ✅ 代码复用更方便
- ✅ 跨项目修改原子化
- ✅ 统一版本管理
- ✅ 简化依赖管理

**挑战**：
- ⚠️ 仓库体积大
- ⚠️ CI/CD 复杂度高
- ⚠️ 权限管理困难

---

#### Monorepo 目录结构

```
monorepo/
├── packages/
│   ├── core/           # 核心库
│   ├── ui/             # UI 组件库
│   ├── api/            # API 服务
│   └── web/            # Web 应用
├── apps/
│   ├── admin/          # 管理后台
│   └── mobile/         # 移动端
├── tools/              # 工具脚本
├── .github/            # CI/CD 配置
└── package.json        # 根配置
```

---

#### Monorepo 工具

**Nx**：
```bash
# 安装 Nx
npx create-nx-workspace my-workspace

# 生成库
nx generate @nx/js:library core

# 运行测试
nx test core

# 构建受影响的项目
nx affected --target=build
```

**Turborepo**：
```bash
# turbo.json 配置
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "test": {
      "dependsOn": ["build"]
    }
  }
}

# 运行
npx turbo run build
```

---

## 第 8 章 Git 钩子与工程化集成

### 8.1 Git Hooks 实战

#### Pre-commit 钩子：代码检查

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "🔍 运行提交前检查..."

# 1. 检查是否有调试代码
if git diff --cached | grep -E "console\.log|print\(|debugger"; then
    echo "❌ 发现调试代码，请移除后重新提交"
    exit 1
fi

# 2. 运行代码格式化检查
echo "检查代码格式..."

# 3. 运行单元测试
echo "运行单元测试..."

echo "✅ 所有检查通过"
exit 0
```

---

#### Commit-msg 钩子：提交信息验证

```bash
#!/bin/bash
# .git/hooks/commit-msg

commit_msg_file=$1
commit_msg=$(cat "$commit_msg_file")

# 检查是否符合约定式提交
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)(\(.+\))?!?: .+"; then
    echo "❌ 提交信息不符合 Conventional Commits 规范"
    echo ""
    echo "格式：<type>(<scope>): <subject>"
    echo ""
    echo "示例：feat(auth): add user login"
    exit 1
fi

echo "✅ 提交信息格式正确"
exit 0
```

---

### 8.1.3 Git Hooks 完整示例与测试

#### Pre-commit 钩子：完整测试流程

**创建钩子文件**：
```bash
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# .git/hooks/pre-commit

echo "🔍 运行提交前检查..."

# 1. 检查是否有调试代码
if git diff --cached | grep -E "console\.log|print\(|debugger"; then
    echo "❌ 发现调试代码，请移除后重新提交"
    exit 1
fi

# 2. 运行代码格式化检查
echo "检查代码格式..."

# 3. 运行单元测试
echo "运行单元测试..."

echo "✅ 所有检查通过"
exit 0
EOF

# 添加执行权限
chmod +x .git/hooks/pre-commit
```

**测试 1：正常提交（钩子通过）**

```bash
$ git add .
$ git commit -m "feat: add user login"

# 输出：
🔍 运行提交前检查...
检查代码格式...
运行单元测试...
✅ 所有检查通过
[main 8f3a2b1] feat: add user login
 2 files changed, 45 insertions(+)
```

**逐行解读**：
- `🔍 运行提交前检查...` - 钩子开始执行
- `检查代码格式...` - 运行代码格式化检查
- `运行单元测试...` - 运行单元测试
- `✅ 所有检查通过` - 所有检查通过，允许提交
- `[main 8f3a2b1] feat: add user login` - 提交成功，显示提交哈希

**测试 2：发现调试代码（钩子阻止）**

```bash
$ echo "console.log('debug')" >> app.js
$ git add app.js
$ git commit -m "feat: add debug logging"

# 输出：
🔍 运行提交前检查...
❌ 发现调试代码，请移除后重新提交
```

**解读**：
- 钩子检测到 `console.log` 调试代码
- 返回非零退出码（exit 1），阻止提交
- 需要移除调试代码后才能提交

**修复并重新提交**：
```bash
$ # 移除调试代码
$ git add app.js
$ git commit -m "feat: add logging"

# 输出：
🔍 运行提交前检查...
检查代码格式...
运行单元测试...
✅ 所有检查通过
[main 9c4b3d2] feat: add logging
```

**测试 3：提交信息格式错误**

```bash
$ git commit -m "fixed some stuff"

# 输出：
❌ 提交信息不符合 Conventional Commits 规范

格式：<type>(<scope>): <subject>

示例：feat(auth): add user login
```

**解读**：
- 提交信息不符合约定式提交规范
- 提示正确的格式和示例
- 需要修改提交信息格式

---

### 8.2 Husky：现代化 Git 钩子管理

#### 安装 Husky（Node.js 项目）

```bash
# 安装 Husky
npm install husky --save-dev

# 初始化
npx husky init

# 添加 pre-commit 钩子
npx husky add .husky/pre-commit "npm test"
```

---

### 8.3 Pre-commit 框架（Python 项目）

#### 安装与配置

```bash
# 安装 pre-commit
pip install pre-commit

# 创建配置文件
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml

  - repo: https://github.com/psf/black
    rev: 24.1.0
    hooks:
      - id: black
EOF

# 安装钩子
pre-commit install
```

---

### 8.4 CI/CD 集成

#### GitHub Actions 示例

**.github/workflows/ci.yml**：
```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'
    
    - name: Install dependencies
      run: pip install -r requirements.txt
    
    - name: Run tests
      run: pytest tests/
```

---

## 第 9 章 Git 故障排查与数据恢复

### 9.1 常见错误及解决方案

#### 错误 1：拒绝合并未关联的历史

**错误信息**：
```bash
$ git pull origin main
fatal: refusing to merge unrelated histories
```

**解决方案**：
```bash
# 允许合并不相关历史
git pull origin main --allow-unrelated-histories
```

**⚠️ 警告**：仅在确认需要合并时使用

---

#### 错误 2：远程证书验证失败

**错误信息**：
```bash
fatal: unable to access 'https://github.com/example/repo.git':
  SSL certificate problem: unable to get local issuer certificate
```

**解决方案**：
```bash
# 方法 1：更新 CA 证书（推荐）
sudo apt update && sudo apt install --reinstall ca-certificates

# 方法 2：使用 SSH
git clone git@github.com:example/repo.git
```

---

#### 错误 3：文件大小超过限制

**错误信息**：
```bash
remote: error: File src/large_file.zip is 150.00 MB; 
this exceeds GitHub's file size limit of 100.00 MB
```

**解决方案**：
```bash
# 使用 Git LFS
git lfs install
git lfs track "*.zip"
git add .gitattributes
git commit -m "Configure Git LFS"
```

---

### 9.2 误操作恢复

#### 恢复未提交的修改

```bash
# 撤销单个文件
git restore <file>

# 撤销所有文件
git restore .
```

---

#### 恢复已提交但未推送的修改

```bash
# 修改最后一次提交
git commit --amend -m "新的提交信息"

# 撤销最后一次提交（保留修改）
git reset --soft HEAD~1

# 撤销最后一次提交（丢弃修改）
git reset --hard HEAD~1
```

---

#### 恢复已推送的修改

```bash
# 安全方式：创建回滚提交
git revert <commit-hash>
git push origin main

# 危险方式：强制回滚
git reset --hard <commit-hash>
git push --force-with-lease origin main
```

**⚠️ 警告**：强制推送会覆盖远程历史

---

### 9.3 Reflog 数据恢复

#### 什么是 Reflog？

> **Reflog**：引用日志，记录 HEAD 和分支的所有移动

**查看 Reflog**：
```bash
# 查看 HEAD 历史
git reflog

# 查看指定分支历史
git reflog show main
```

**输出示例**：
```bash
$ git reflog
8f3a2b1 HEAD@{0}: reset: moving to HEAD~1
abc1234 HEAD@{1}: commit: feat: add new feature
def5678 HEAD@{2}: merge feature
```

---

#### 恢复误删的提交

```bash
# 1. 查看 reflog
git reflog

# 2. 找到误删前的提交
abc1234 HEAD@{1}: commit: feat: add new feature

# 3. 重置回去
git reset --hard abc1234
```

---

### 9.4 损坏仓库修复

#### 检查仓库完整性

```bash
# 检查对象数据库
git fsck

# 详细检查
git fsck --full
```

**输出示例**：
```bash
$ git fsck
dangling commit abc1234
dangling blob def5678
```

**输出解读**：
- `dangling commit`：未引用的提交（通常无害）
- `dangling blob`：未引用的文件内容（通常无害）
- `missing blob`：缺失的对象（严重问题）

---

#### 修复常见问题

```bash
# 损坏的索引文件
rm .git/index
git reset

# 损坏的 HEAD
echo "ref: refs/heads/main" > .git/HEAD

# 从远程恢复
git fetch origin
git reset --hard origin/main
```

---

### 9.6 可视化工具配置

#### VS Code 内置 Git 工具

**1. 配置 VS Code 为默认编辑器**：
```bash
git config --global core.editor "code --wait"
```

**2. 配置 VS Code 为 mergetool**：
```bash
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd "code --wait \$MERGED"
git config --global diff.tool vscode
git config --global difftool.vscode.cmd "code --wait --diff \$LOCAL \$REMOTE"
```

**3. 使用 VS Code 解决冲突**

**步骤 1：遇到冲突时**
```bash
$ git merge feature
CONFLICT (content): Merge conflict in app.js
Automatic merge failed; fix conflicts and then commit the result.
```

**步骤 2：打开 VS Code**
```bash
code app.js
```

**步骤 3：在 VS Code 中解决冲突**

VS Code 会高亮显示冲突区域：

```javascript
<<<<<<< HEAD
function login(user, password) {
  // 当前分支的代码
  return authenticate(user, password);
}
=======
function login(user, password, token) {
  // 合并分支的代码
  return authenticateWithToken(user, password, token);
}
>>>>>>> feature
```

**步骤 4：选择保留的代码**

点击冲突区域上方的操作按钮：
- `Accept Current Change` - 保留当前分支
- `Accept Incoming Change` - 保留合并分支
- `Accept Both Changes` - 保留两者
- `Compare Changes` - 对比差异

**步骤 5：保存并提交**
```bash
git add app.js
git commit -m "merge: resolve conflict in app.js"
```

---

#### GitKraken（推荐新手）

**安装**：
```
访问：https://www.gitkraken.com/
下载：对应系统版本
```

**主要功能**：
- ✅ 可视化分支图
- ✅ 拖拽合并
- ✅ 一键回滚
- ✅ 冲突解决向导
- ✅ 集成 GitHub/GitLab

**适用场景**：
- 新手学习 Git 原理
- 查看复杂分支历史
- 可视化解决冲突

---

#### SourceTree（免费）

**安装**：
```
访问：https://www.sourcetreeapp.com/
下载：对应系统版本
```

**主要功能**：
- ✅ 免费使用
- ✅ 可视化提交历史
- ✅ 分支管理
- ✅ 内置差异工具

**适用场景**：
- 日常 Git 操作
- 查看提交历史
- 分支管理

---

#### 命令行 vs 图形工具

| 场景 | 推荐工具 | 理由 |
|:---|:---|:---|
| **学习 Git 原理** | 命令行 | 理解底层机制 |
| **日常开发** | 命令行 | 快速、灵活 |
| **解决复杂冲突** | VS Code/GitKraken | 可视化对比 |
| **查看历史记录** | SourceTree/GitKraken | 图形化展示 |
| **团队协作** | 命令行 | 统一流程 |

**建议**：
- 新手先用命令行学习基础
- 熟练后结合图形工具提高效率
- 复杂冲突使用可视化工具

---

## 第 10 章 高频常见问题解决方案

### 10.1 日常开发问题

#### Q1: 如何查看某个文件的修改历史？

```bash
# 查看文件完整历史
git log --follow <file>

# 查看每次修改的差异
git log -p --follow <file>

# 查看谁在何时修改了哪行
git blame <file>
```

---

#### Q2: 如何比较两个版本的差异？

```bash
# 比较两个提交
git diff abc123 def456

# 比较两个分支
git diff main feature

# 比较两个标签
git diff v1.0 v2.0
```

---

#### Q3: 如何查找引入 bug 的提交？

**方法 1：使用 git blame**
```bash
git blame src/buggy_file.py
```

**方法 2：使用 git bisect（二分查找）**
```bash
# 开始二分查找
git bisect start

# 标记当前版本有问题
git bisect bad

# 标记某个历史版本正常
git bisect good v1.0

# 测试后标记好坏，重复直到找到
git bisect good  # 或 git bisect bad

# 结束
git bisect reset
```

---

#### Q4: 如何临时保存修改？

```bash
# 暂存当前修改
git stash

# 暂存并添加说明
git stash push -m "WIP: working on feature"

# 查看暂存列表
git stash list

# 应用最近的暂存
git stash pop
```

---

### 10.2 分支管理问题

#### Q5: 如何清理已合并的分支？

```bash
# 查看已合并到 main 的分支
git branch --merged main

# 删除已合并的本地分支
git branch --merged main | grep -v "^\*\|main" | xargs git branch -d
```

---

#### Q6: 如何重命名分支？

```bash
# 重命名当前分支
git branch -m old-name new-name

# 删除远程旧分支
git push origin --delete old-name

# 推送新分支并设置上游
git push origin -u new-name
```

---

#### Q7: 如何同步 Fork 的仓库？

```bash
# 1. 添加上游远程仓库
git remote add upstream git@github.com:original-owner/repo.git

# 2. 获取上游仓库更新
git fetch upstream

# 3. 切换到 main 分支
git checkout main

# 4. 合并上游更新
git merge upstream/main

# 5. 推送到自己的 Fork
git push origin main
```

---

### 10.3 性能优化问题

#### Q8: 如何加速 Git 操作？

```bash
# 启用并行获取
git config --global fetch.parallel 10

# 定期垃圾回收
git gc --aggressive

# 使用浅克隆
git clone --depth 1 <repository-url>
```

---

#### Q9: 仓库太大如何优化？

```bash
# 1. 查看大文件
git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -5 | awk '{print$1}')"

# 2. 使用 BFG 清理大文件
java -jar bfg.jar --strip-blobs-bigger-than 100M .

# 3. 清理历史
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

---

### 10.4 团队协作问题

#### Q10: 如何处理冲突频繁的合并？

**策略 1：频繁同步**
```bash
git pull --rebase origin main
```

**策略 2：小步提交**
- 每次提交功能点尽量小
- 减少合并冲突范围

**策略 3：使用变基**
```bash
git fetch origin
git rebase origin/main
git rebase --continue
```

**策略 4：沟通协调**
- 团队成员间沟通修改计划
- 避免同时修改同一文件

---

## 附录 A：命令速查表

### A.1 基础操作

| 命令 | 说明 | 版本 | 示例 |
|:---|:---|:---|:---|
| `git init` | 初始化仓库 | 全部 | `git init` |
| `git clone <url>` | 克隆仓库 | 全部 | `git clone https://github.com/user/repo.git` |
| `git status` | 查看状态 | 全部 | `git status -s`（简短格式） |
| `git add <file>` | 添加到暂存区 | 全部 | `git add .`（全部） |
| `git commit -m "msg"` | 提交 | 全部 | `git commit -m "feat: add login"` |
| `git commit --amend` | 修改上次提交 | 全部 | `git commit --amend -m "new msg"` |

### A.2 撤销操作

| 命令 | 说明 | 版本 | 示例 |
|:---|:---|:---|:---|
| `git restore <file>` | 恢复工作区文件 | 2.23+ | `git restore app.js` |
| `git checkout -- <file>` | 恢复工作区（传统） | 全部 | `git checkout -- app.js` |
| `git restore --staged <file>` | 从暂存区恢复 | 2.23+ | `git restore --staged app.js` |
| `git reset HEAD <file>` | 从暂存区恢复（传统） | 全部 | `git reset HEAD app.js` |
| `git reset --soft HEAD~1` | 撤销提交，保留更改 | 全部 | `git reset --soft HEAD~1` |
| `git reset --mixed HEAD~1` | 撤销提交，保留暂存 | 全部 | `git reset HEAD~1`（默认） |
| `git reset --hard HEAD~1` | 彻底撤销提交 | 全部 | `git reset --hard HEAD~1` ⚠️ |
| `git revert <commit>` | 回滚提交（安全） | 全部 | `git revert abc123` |
| `git clean -fd` | 清理未跟踪文件 | 全部 | `git clean -fd` ⚠️ |

### A.3 分支管理

| 命令 | 说明 | 版本 | 示例 |
|:---|:---|:---|:---|
| `git branch` | 查看分支 | 全部 | `git branch -a`（含远程） |
| `git branch <name>` | 创建分支 | 全部 | `git branch feature/login` |
| `git switch <branch>` | 切换分支 | 2.23+ | `git switch main` |
| `git switch -c <branch>` | 创建并切换 | 2.23+ | `git switch -c feature` |
| `git checkout <branch>` | 切换分支（传统） | 全部 | `git checkout main` |
| `git checkout -b <branch>` | 创建并切换（传统） | 全部 | `git checkout -b feature` |
| `git merge <branch>` | 合并分支 | 全部 | `git merge --no-ff feature` |
| `git rebase <branch>` | 变基 | 全部 | `git rebase main` |
| `git rebase -i <commit>` | 交互式变基 | 全部 | `git rebase -i HEAD~3` |
| `git cherry-pick <commit>` | 选择合并 | 全部 | `git cherry-pick abc123` |
| `git branch -d <branch>` | 删除分支 | 全部 | `git branch -d feature` |
| `git branch -D <branch>` | 强制删除 | 全部 | `git branch -D feature` |

### A.4 远程操作

| 命令 | 说明 | 版本 | 示例 |
|:---|:---|:---|:---|
| `git remote -v` | 查看远程仓库 | 全部 | `git remote -v` |
| `git remote add <name> <url>` | 添加远程 | 全部 | `git remote add origin https://...` |
| `git fetch <remote>` | 获取远程 | 全部 | `git fetch origin` |
| `git fetch --all` | 获取所有远程 | 全部 | `git fetch --all` |
| `git pull <remote> <branch>` | 拉取并合并 | 全部 | `git pull origin main` |
| `git pull --rebase` | 拉取并变基 | 全部 | `git pull --rebase origin main` |
| `git push <remote> <branch>` | 推送 | 全部 | `git push origin main` |
| `git push -u <remote> <branch>` | 推送并设置上游 | 全部 | `git push -u origin main` |
| `git push --force` | 强制推送 | 全部 | `git push --force` ⚠️ |
| `git push --force-with-lease` | 安全强制推送 | 全部 | `git push --force-with-lease` ✅ |

### A.5 查看与比较

| 命令 | 说明 | 版本 | 示例 |
|:---|:---|:---|:---|
| `git log` | 查看提交日志 | 全部 | `git log --oneline --graph` |
| `git log --author=<name>` | 按作者过滤 | 全部 | `git log --author="John"` |
| `git log --since="2 weeks ago"` | 按时间过滤 | 全部 | `git log --since="2 weeks ago"` |
| `git diff` | 比较差异 | 全部 | `git diff HEAD` |
| `git diff --staged` | 比较暂存区 | 全部 | `git diff --staged` |
| `git show <commit>` | 查看提交详情 | 全部 | `git show abc123` |
| `git blame <file>` | 查看每行作者 | 全部 | `git blame app.js` |
| `git reflog` | 查看引用日志 | 全部 | `git reflog` |
| `git shortlog` | 统计贡献 | 全部 | `git shortlog -sn` |

### A.6 标签操作

| 命令 | 说明 | 版本 | 示例 |
|:---|:---|:---|:---|
| `git tag` | 查看标签 | 全部 | `git tag -l "v1.*"` |
| `git tag <name>` | 创建轻量标签 | 全部 | `git tag v1.0.0` |
| `git tag -a <name> -m "msg"` | 创建附注标签 | 全部 | `git tag -a v1.0.0 -m "release"` |
| `git push origin <tag>` | 推送标签 | 全部 | `git push origin v1.0.0` |
| `git push origin --tags` | 推送所有标签 | 全部 | `git push origin --tags` |
| `git tag -d <name>` | 删除标签 | 全部 | `git tag -d v1.0.0` |

### A.7 高级操作

| 命令 | 说明 | 版本 | 示例 |
|:---|:---|:---|:---|
| `git stash` | 暂存更改 | 全部 | `git stash save "work in progress"` |
| `git stash list` | 查看暂存列表 | 全部 | `git stash list` |
| `git stash pop` | 恢复并删除暂存 | 全部 | `git stash pop` |
| `git stash apply` | 恢复暂存 | 全部 | `git stash apply stash@{0}` |
| `git bisect start` | 开始二分查找 | 全部 | `git bisect start` |
| `git bisect good/bad` | 标记好坏 | 全部 | `git bisect good` |
| `git bisect reset` | 重置二分查找 | 全部 | `git bisect reset` |
| `git worktree add <path>` | 添加工作树 | 全部 | `git worktree add ../hotfix` |
| `git submodule add <url>` | 添加子模块 | 全部 | `git submodule add https://...` |

### A.8 故障排查

| 命令 | 说明 | 版本 | 示例 |
|:---|:---|:---|:---|
| `git fsck` | 检查仓库完整性 | 全部 | `git fsck --full` |
| `git gc` | 垃圾回收 | 全部 | `git gc --prune=now` |
| `git prune` | 清理悬空对象 | 全部 | `git prune` |
| `git reflog expire` | 过期引用日志 | 全部 | `git reflog expire --expire=now --all` |
| `git filter-branch` | 重写历史 | 全部 | `git filter-branch --force ...` ⚠️ |

---

## 附录 B：Git 工作流对比

### B.1 Git Flow vs GitHub Flow

| 特性 | Git Flow | GitHub Flow |
|:---|:---|:---|
| **复杂度** | 高 | 低 |
| **分支数量** | 多（5+ 种） | 少（2 种） |
| **发布周期** | 固定周期 | 随时发布 |
| **适用场景** | 传统软件、多版本 | Web 应用、持续部署 |
| **学习曲线** | 陡峭 | 平缓 |

---

### B.2 工作流选择建议

**选择 Git Flow 如果**：
- ✅ 有固定的发布周期
- ✅ 需要维护多个版本
- ✅ 团队规模较大（10+ 人）
- ✅ 传统软件开发

**选择 GitHub Flow 如果**：
- ✅ 持续部署（每天多次发布）
- ✅ 单一生产环境
- ✅ 团队规模较小
- ✅ Web 应用/SaaS 服务

---

## 附录 C：学习路径建议

### C.1 初学者路径（4 周）

**第 1 周：基础操作**
- Git 安装配置
- 基本命令（add/commit/push/pull）
- 查看状态和日志

**第 2 周：分支管理**
- 创建和切换分支
- 合并分支
- 处理冲突

**第 3 周：远程协作**
- 远程仓库操作
- Pull Request 流程
- 代码审查

**第 4 周：进阶技能**
- 变基操作
- 标签管理
- 故障排查

---

### C.2 进阶者路径（8 周）

**第 1-2 周：深入原理**
- Git 对象模型
- 引用和 HEAD
- 索引机制

**第 3-4 周：工作流实践**
- Git Flow 实战
- GitHub Flow 实战
- 分支策略设计

**第 5-6 周：工程化集成**
- Git Hooks
- CI/CD 集成
- 自动化测试

**第 7-8 周：高级主题**
- 性能优化
- 数据恢复
- 大型仓库管理

---

## 附录 D：推荐资源

### D.1 官方文档

- [Git 官方文档](https://git-scm.com/doc)
- [GitHub 文档](https://docs.github.com/)
- [GitLab 文档](https://docs.gitlab.com/)

### D.2 在线教程

- [Pro Git 书籍（免费）](https://git-scm.com/book/zh/v2)
- [Git 分支可视化教程](https://learngitbranching.js.org/)
- [Atlassian Git 教程](https://www.atlassian.com/git)

### D.3 视频课程

- GitHub Learning Lab
- LinkedIn Learning: Git Essential Training
- Udemy: Git Complete: The definitive, step-by-step guide

---

## 结语

> 🎯 **Git 精通之路**：从"会用"到"理解原理"，再到"灵活应用"

**学习建议**：
1. **多实践**：Git 是实践性技能，多操作才能熟练
2. **理解原理**：理解底层机制，遇到问题不慌张
3. **善用工具**：图形化工具辅助学习，但命令行是根本
4. **持续学习**：Git 在进化，保持学习新特性

**最后提醒**：
- ⚠️ 重要操作前备份
- ⚠️ 强制推送前确认
- ⚠️ 团队协作多沟通

祝你 Git 学习顺利！🚀

---

*本教程持续更新中，最新版本请访问：https://github.com/hjs2015/git-tutorial*

# Git 基础回顾

---

## 📖 目录

1. [Git 安装与配置](#第 1 章-git-安装与配置)
2. [Git 初始化与基本操作](#第 2 章-git-初始化与基本操作)
3. [分支管理](#第 3 章-分支管理)
4. [标签使用](#第 4 章-标签使用)
5. [远程仓库操作](#第 5 章-远程仓库操作)
6. [实用进阶功能](#第 6 章-实用进阶功能)
7. [最佳实践与常见问题](#第 7 章-最佳实践与常见问题)

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

### 1.3 配置用户信息

> ⚠️ **重要**：首次使用 Git 必须配置用户名和邮箱，这些信息会附加到每次提交中，用于标识作者身份。

#### 全局配置（推荐）

```bash
# 配置用户名（对所有仓库生效）
git config --global user.name "example-user"

# 配置邮箱（对所有仓库生效）
git config --global user.email "user@example.com"
```

**说明**：
- `--global`：全局配置，保存在 `~/.gitconfig`，对所有仓库生效
- 用户名和邮箱会显示在每次提交记录中
- 建议使用真实姓名和公司邮箱

#### 仓库级配置

```bash
# 进入特定仓库
cd /path/to/repo

# 配置仅对该仓库生效
git config --local user.name "project-user"
git config --local user.email "project@example.com"
```

**说明**：
- `--local`：仓库级配置，保存在 `.git/config`，仅对当前仓库生效
- 适用于多项目场景（如公司项目用公司邮箱，个人项目用个人邮箱）

---

### 1.4 常用配置项

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

#### 其他实用配置

```bash
# 启用彩色输出
git config --global color.ui true

# 配置常用别名
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'

# 使用别名示例
git st        # 等价于 git status
git co main   # 等价于 git checkout main
```

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
```

**输出示例**：
```bash
$ git config --list
user.name=example-user
user.email=user@example.com
color.ui=true
init.defaultbranch=main
core.editor=code --wait
```

---

## 第 2 章 Git 初始化与基本操作

### 2.1 .gitignore 文件详解

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

### 2.2 初始化仓库

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

---

### 2.3 撤销操作详解

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

#### 修改最后一次提交

```bash
# 修改最后一次提交信息
git commit --amend -m "新的提交信息"

# 修改最后一次提交，追加未提交的文件
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

### 2.4 提交操作增强

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

## 第 3 章 分支管理

### 3.1 远程分支操作

#### 查看远程分支

```bash
# 查看远程跟踪分支
git branch -r
```

**输出示例**：
```bash
$ git branch -r
  origin/HEAD -> origin/main
  origin/main
  origin/develop
  origin/feature/user-login
```

---

#### 拉取远程分支并切换

```bash
# 方法 1：现代命令（Git 2.23+，推荐）
git switch -c <branch> origin/<branch>

# 示例：拉取并切换到 feature 分支
git switch -c feature origin/feature

# 方法 2：传统命令
git checkout -b <branch> origin/<branch>

# 示例
git checkout -b feature origin/feature
```

**输出示例**：
```bash
$ git switch -c feature origin/feature
分支 'feature' 设置为跟踪远程分支 'origin/feature'。
切换到新分支 'feature'
```

**说明**：
- 自动创建本地分支并跟踪远程分支
- 之后可直接使用 `git pull` 和 `git push`

---

#### 删除远程分支

```bash
# 删除远程分支
git push origin --delete <branch>

# 示例：删除 feature 分支
git push origin --delete feature
```

**输出示例**：
```bash
$ git push origin --delete feature
To github.com:example-user/repo.git
 - [deleted]         feature
```

⚠️ **警告**：
- 删除前确认分支已合并
- 通知团队成员
- 删除后无法恢复（除非其他人有备份）

---

### 3.2 变基（rebase）入门

> 🔄 **什么是变基？**
> 
> `git rebase` 将当前分支的提交"重新播放"到目标分支上，使历史线保持线性。

#### rebase vs merge 对比

**Merge 方式**：
```
* D (feature)
|
* C
|
* B
|
* A (main)
```
合并后：
```
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
```
变基后：
```
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

# 交互式变基（可编辑提交历史）
git rebase -i HEAD~3

# 继续变基（解决冲突后）
git rebase --continue

# 取消变基
git rebase --abort
```

**适用场景**：
- ✅ 保持提交历史线性整洁
- ✅ 本地分支整理提交
- ❌ 已推送的公共分支（会改写历史）

⚠️ **风险提示**：
- 变基会改写提交历史
- 不要在公共分支上使用
- 可能导致团队冲突

---

### 3.3 Detached HEAD 状态

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

⚠️ **警告**：
- Detached HEAD 状态下提交的代码，切换分支后可能丢失
- 如需保留，务必创建新分支

---

## 第 4 章 标签使用

### 4.1 标签类型对比

| 类型 | 命令 | 说明 | 推荐场景 |
|:---|:---|:---|:---|
| **轻量标签** | `git tag v1.0` | 仅指向提交 | 临时标记 |
| **附注标签** | `git tag -a v1.0 -m "说明"` | 包含标签信息 | 正式版本发布 |

---

### 4.2 创建标签

#### 轻量标签

```bash
# 创建轻量标签
git tag v1.0

# 查看标签
git show v1.0
```

---

#### 附注标签（推荐）

```bash
# 创建附注标签
git tag -a v1.0 -m "版本 1.0 - 初始发布"

# 查看标签详情
git show v1.0
```

**输出示例**：
```bash
$ git show v1.0
tag v1.0
Tagger: Example User <user@example.com>
Date:   Sat Mar 21 15:00:00 2026 +0800

版本 1.0 - 初始发布

commit 921d88e7bc8de6b8575e77513ee9805021ffc5ef
Author: Example User <user@example.com>
Date:   Sat Mar 21 14:50:00 2026 +0800

    merge testing to main
```

---

### 4.3 标签推送

```bash
# 推送单个标签
git push origin v1.0

# 推送所有标签
git push origin --tags
```

**输出示例**：
```bash
$ git push origin v1.0
Total 0 (delta 0), reused 0 (delta 0)
To github.com:example-user/repo.git
 * [new tag]         v1.0 -> v1.0
```

---

### 4.4 删除标签

```bash
# 删除本地标签
git tag -d v1.0

# 删除远程标签
git push origin --delete v1.0

# 或删除远程标签（另一种写法）
git push origin :refs/tags/v1.0
```

**输出示例**：
```bash
$ git tag -d v1.0
已删除标签 'v1.0'（曾为 a1b2c3d）

$ git push origin --delete v1.0
To github.com:example-user/repo.git
 - [deleted]         v1.0
```

---

## 第 5 章 远程仓库操作

### 5.1 添加远程仓库

```bash
# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add origin git@github.com:example-user/repo.git

# 再次查看
git remote -v
```

**输出示例**：
```bash
$ git remote -v
origin  git@github.com:example-user/repo.git (fetch)
origin  git@github.com:example-user/repo.git (push)
```

---

### 5.2 更新远程仓库地址

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

## 第 6 章 实用进阶功能

### 6.1 git stash 暂存

> 📦 **什么是 stash？**
> 
> 将未提交的修改临时保存，恢复干净的工作区，方便切换分支或处理紧急任务。

#### 基本操作

```bash
# 暂存当前修改
git stash

# 暂存并添加说明
git stash save "WIP: user login feature"

# 查看暂存列表
git stash list
```

**输出示例**：
```bash
$ git stash save "WIP: user login feature"
Saved working directory and index state On main: WIP: user login feature

$ git stash list
stash@{0}: On main: WIP: user login feature
```

---

#### 恢复暂存

```bash
# 恢复最近的暂存（并从列表中删除）
git stash pop

# 恢复指定暂存
git stash pop stash@{1}

# 恢复暂存但不删除
git stash apply

# 删除暂存
git stash drop stash@{0}

# 清空所有暂存
git stash clear
```

---

#### 适用场景

**场景 1：切换分支前暂存修改**
```bash
# 正在开发功能，需要紧急修复 bug
git stash              # 暂存当前修改
git checkout main      # 切换到主分支
git checkout -b hotfix # 创建修复分支
# ... 修复 bug ...
git checkout feature   # 回到功能分支
git stash pop          # 恢复之前的修改
```

---

**场景 2：拉取最新代码**
```bash
# 本地有未提交修改，需要拉取最新代码
git stash              # 暂存修改
git pull               # 拉取最新代码
git stash pop          # 恢复修改
# 如有冲突，解决后提交
```

---

### 6.2 git cherry-pick

> 🍒 **什么是 cherry-pick？**
> 
> 选择性合并某个特定提交到当前分支，而非合并整个分支。

#### 基本用法

```bash
# 查看提交历史，找到需要的提交
git log --oneline

# cherry-pick 指定提交
git cherry-pick abc123

# cherry-pick 多个提交
git cherry-pick abc123 def456

# cherry-pick 提交范围
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

#### 适用场景

- ✅ 将 bug 修复从一个分支应用到其他分支
- ✅ 选择性合并功能，而非整个分支
- ✅ 恢复误删的提交

⚠️ **注意事项**：
- cherry-pick 会创建新提交（不同哈希值）
- 可能产生冲突，需手动解决
- 避免重复 cherry-pick 同一提交

---

### 6.3 git blame

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
# 显示更多统计信息
git blame -L 10,20 main.py    # 查看第 10-20 行

# 忽略空白提交
git blame -w main.py

# 以邮件格式显示
git blame -e main.py
```

---

#### 适用场景

- 🔍 追溯某行代码是谁写的
- 🔍 了解代码修改原因
- 🔍 代码审查时定位责任人

---

### 6.4 git bisect

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

## 第 7 章 最佳实践与常见问题

### 7.1 提交信息规范

> ✍️ **为什么需要规范的提交信息？**
> 
> 清晰的提交信息便于团队协作、代码审查、问题追溯和自动生成变更日志。

#### Commit Message 结构

```
<类型>(<可选范围>): <简短描述>

<可选正文>

<可选页脚>
```

---

#### 类型说明

| 类型 | 说明 | 示例 |
|:---|:---|:---|
| `feat` | 新功能 | `feat: add user login` |
| `fix` | Bug 修复 | `fix: resolve null pointer exception` |
| `docs` | 文档更新 | `docs: update README.md` |
| `style` | 代码格式（不影响功能） | `style: format code with prettier` |
| `refactor` | 代码重构 | `refactor: simplify user service` |
| `test` | 测试相关 | `test: add unit tests for auth` |
| `chore` | 构建/工具/配置 | `chore: update dependencies` |

---

#### 优秀示例

```bash
# ✅ 好的提交信息
feat: add user login module
fix: resolve null pointer in user service
docs: update API documentation
refactor: simplify authentication logic

# ❌ 坏的提交信息
update
fix bug
wip
aaa
```

---

#### 完整示例

```bash
feat(auth): add user login with JWT

- Implement login endpoint with JWT token generation
- Add password encryption using bcrypt
- Create authentication middleware
- Add unit tests for login flow

Closes #123
```

---

### 7.2 分支工作流

#### Git Flow（适合传统项目）

```
main (生产)
  ↑
develop (开发)
  ↑
feature/* (功能分支)
  ↑
bugfix/* (修复分支)
  ↑
hotfix/* (紧急修复)
```

**分支说明**：
- `main`：生产环境，只接受来自 develop 和 hotfix 的合并
- `develop`：开发集成分支
- `feature/*`：新功能开发（从 develop 分出，合并回 develop）
- `bugfix/*`：Bug 修复（从 develop 分出，合并回 develop）
- `hotfix/*`：紧急修复（从 main 分出，合并回 main 和 develop）

---

#### GitHub Flow（适合互联网项目）

```
main (唯一长期分支)
  ↑
feature/* (功能分支，短期存在)
```

**工作流程**：
1. 从 `main` 创建功能分支
2. 开发功能并提交
3. 创建 Pull Request
4. 代码审查通过后合并到 `main`
5. 删除功能分支

**优势**：
- ✅ 简单明了
- ✅ 快速迭代
- ✅ 适合持续部署

---

### 7.3 常见问题排查

#### 问题 1：git pull 冲突

**场景**：拉取远程代码时产生冲突

**解决步骤**：
```bash
# 1. 暂存当前修改
git stash

# 2. 拉取最新代码
git pull

# 3. 恢复暂存
git stash pop

# 4. 解决冲突
# 编辑冲突文件，保留需要的内容

# 5. 标记冲突已解决
git add <file>

# 6. 完成合并
git commit
```

---

#### 问题 2：远程仓库地址变更

**场景**：仓库迁移或重命名后

**解决方法**：
```bash
# 查看当前远程地址
git remote -v

# 更新远程地址
git remote set-url origin git@github.com:example-user/new-repo.git

# 验证
git remote -v

# 推送测试
git push -u origin main
```

---

#### 问题 3：误删分支恢复

**场景**：误删未合并的分支

**解决方法**：
```bash
# 1. 查看操作历史
git reflog

# 2. 找到删除前的提交
abc123 HEAD@{1}: branch feature deleted

# 3. 基于该提交恢复分支
git branch feature abc123

# 4. 验证
git branch
```

---

## 📚 命令速查表

### 基本命令
```bash
git init                    # 初始化仓库
git config --list           # 查看配置
git status                  # 查看状态
git add <file>              # 添加到暂存区
git commit -m "描述"        # 提交到仓库
git log                     # 查看提交历史
git reflog                  # 查看所有操作历史
```

### 撤销操作
```bash
git restore <file>          # 撤销工作区修改
git restore --staged <file> # 撤回暂存区
git commit --amend          # 修改最后一次提交
```

### 分支操作
```bash
git branch                  # 查看分支
git switch -c <name>        # 创建并切换分支
git switch <name>           # 切换分支
git merge <name>            # 合并分支
git rebase <name>           # 变基操作
git branch -d <name>        # 删除分支
```

### 远程操作
```bash
git remote -v               # 查看远程仓库
git remote add <name> <url> # 添加远程仓库
git push -u origin main     # 推送代码
git pull origin main        # 拉取代码
git clone <url>             # 克隆仓库
```

### 标签操作
```bash
git tag                     # 查看标签
git tag -a <name> -m "描述" # 创建附注标签
git push origin <tagname>   # 推送标签
git tag -d <name>           # 删除本地标签
git push origin --delete <tagname>  # 删除远程标签
```

### 暂存操作
```bash
git stash                   # 暂存修改
git stash list              # 查看暂存列表
git stash pop               # 恢复并删除暂存
git stash apply             # 恢复暂存
git stash drop              # 删除暂存
```

### 高级命令
```bash
git cherry-pick <commit>    # 选择性合并提交
git blame <file>            # 查看文件修改历史
git bisect start            # 二分查找问题提交
```

---

## 🎯 下一步

完成 Git 基础回顾后，继续学习 CI/CD 实战：

1. ✅ **Git 基础回顾**（当前文档）
2. 📖 **03-Jenkins 持续集成** - 包含 CI/CD 背景知识 + Jenkins 实战
3. 📖 **02-GitLab 企业级代码管理** - GitLab 安装部署、权限管理、备份恢复
4. 📖 **04-SonarQube 代码质量** - SonarQube 部署、代码扫描、Jenkins 集成

---

**文档版本**: v4.0  
**更新时间**: 2026-03-21  
**仓库地址**: https://github.com/hjs2015/git-tutorial

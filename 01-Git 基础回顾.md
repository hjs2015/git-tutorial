# Git 基础回顾

---

## 📖 目录

1. [Git 安装与配置](#第 1 章-git-安装与配置)
2. [Git 初始化与基本操作](#第 2 章-git-初始化与基本操作)
3. [分支管理](#第 3 章-分支管理)
4. [标签使用](#第 4 章-标签使用)
5. [远程仓库操作](#第 5 章-远程仓库操作)

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

#### CentOS/RHEL 系统

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

**说明**：
- `yum install git -y`：自动确认安装，无需手动输入 y
- `git --version`：查看 Git 版本号，确认安装成功

#### Ubuntu/Debian 系统

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
git config --global user.name "zhangya"

# 配置邮箱（对所有仓库生效）
git config --global user.email "526195417@qq.com"
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

#### 配置文件位置

```bash
# 查看配置文件帮助
git config --help

# 配置文件层级（优先级从低到高）：
--system    # 系统级配置文件 (/etc/gitconfig) - 对所有用户生效
--global    # 全局配置文件 (~/.gitconfig) - 对当前用户所有仓库生效
--local     # 仓库级配置文件 (.git/config) - 仅对当前仓库生效
```

---

### 1.4 查看配置

#### 列出所有配置

```bash
# 显示所有配置项
git config --list
```

**输出示例**：
```bash
[root@gitlab ~]# git config --list
user.name=zhangya
user.email=526195417@qq.com
color.ui=true
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
```

**说明**：
- 显示所有层级的配置（system + global + local）
- 格式为 `key=value`
- 重复的配置项，优先级高的会覆盖低的

#### 查看配置文件内容

```bash
# 查看全局配置文件
cat ~/.gitconfig
```

**输出示例**：
```bash
[root@gitlab ~]# cat .gitconfig
[user]
    name = zhangya
    email = 526195417@qq.com
[color]
    ui = true
```

**说明**：
- 配置文件采用 INI 格式
- `[section]` 表示配置节
- `key = value` 表示配置项

---

### 1.5 设置语法高亮（可选）

```bash
# 启用彩色输出（让 diff、log 等命令更易读）
git config --global color.ui true

# 查看配置
git config --list
```

**效果对比**：

**未启用彩色输出**：
```
diff --git a/file.txt b/file.txt
index e69de29..5d308e1 100644
--- a/file.txt
+++ b/file.txt
@@ -0,0 +1 @@
+new line
```

**启用彩色输出后**：
```
diff --git a/file.txt b/file.txt  ← 青色
index e69de29..5d308e1 100644     ← 青色
--- a/file.txt                     ← 红色背景
+++ b/file.txt                     ← 绿色背景
@@ -0,0 +1 @@                     ← 青色
+new line                          ← 绿色文字（新增）
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
[root@gitlab /git_data]# git init
hint: Using 'master' as the name for the initial branch.
hint: 默认分支名称为 'master'。如需使用其他名称，可通过以下命令配置：
hint: 
hint:     git config --global init.defaultBranch <分支名>
hint: 
hint: 例如：git config --global init.defaultBranch main
Initialized empty Git repository in /git_data/.git/
```

**说明**：
- `hint:`：提示信息，不影响操作
- Git 2.28+ 版本会提示默认分支名称可配置
- `.git/` 目录：存储所有版本控制信息，删除后 Git 功能失效

#### 查看隐藏目录

```bash
# 查看 .git 目录结构
ls -la .git/
```

**输出示例**：
```bash
[root@gitlab /git_data]# ls .git | xargs -n 1
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

### 2.2 查看状态

```bash
# 查看仓库当前状态
git status
```

**输出示例**：
```bash
[root@gitlab /git_data]# git status
# 位于分支 master
#
# 初始提交
#
# 未跟踪的文件:
#   （使用 "git add <file>..." 以包含要提交的内容）
#
#   a
#   b
#   c
```

**状态说明**：

| 状态 | 英文 | 说明 | 操作 |
|:---|:---|:---|:---|
| **未跟踪** | Untracked | 新创建的文件，Git 尚未管理 | `git add <file>` |
| **已暂存** | Staged | 已添加到暂存区，准备提交 | `git commit` |
| **已提交** | Committed | 已提交到本地仓库 | - |
| **已修改** | Modified | 已跟踪但尚未暂存的修改 | `git add` 或 `git checkout` |

**常见状态流转**：
```
未跟踪 (Untracked)
    ↓ git add
已暂存 (Staged)
    ↓ git commit
已提交 (Committed)
    ↓ 修改文件
已修改 (Modified)
    ↓ git add
已暂存 (Staged)
```

---

### 2.3 添加文件到暂存区

#### 添加单个文件

```bash
# 创建测试文件
touch a b c

# 添加单个文件到暂存区
git add a
```

**输出示例**：
```bash
[root@gitlab /git_data]# git add a
[root@gitlab /git_data]# git status
# 位于分支 master
#
# 初始提交
#
# 要提交的变更：
#   （使用 "git rm --cached <file>..." 撤出暂存区）
#
#   新文件：a
#
# 未跟踪的文件:
#   （使用 "git add <file>..." 以包含要提交的内容）
#
#   b
#   c
```

**说明**：
- `git add a`：只添加文件 `a`，不影响 `b` 和 `c`
- `新文件：a`：表示文件 `a` 已暂存，等待提交
- `未跟踪的文件：b, c`：这两个文件还未被 Git 管理

#### 添加所有文件

```bash
# 添加当前目录下所有文件到暂存区
git add .
```

**输出示例**：
```bash
[root@gitlab /git_data]# git add .
[root@gitlab /git_data]# git status
# 位于分支 master
#
# 初始提交
#
# 要提交的变更：
#   （使用 "git rm --cached <file>..." 撤出暂存区）
#
#   新文件：a
#   新文件：b
#   新文件：c
```

**说明**：
- `git add .`：添加当前目录及子目录下所有文件（包括隐藏文件）
- 等价于 `git add -A`（Git 2.x 版本）

---

### 2.4 撤回暂存区文件

```bash
# 从暂存区撤回文件 c（不删除工作区文件）
git rm --cached c
```

**输出示例**：
```bash
[root@gitlab /git_data]# git rm --cached c
rm 'c'
[root@gitlab /git_data]# git status
# 位于分支 master
#
# 要提交的变更：
#   新文件：a
#   新文件：b
#
# 未跟踪的文件:
#   （使用 "git add <file>..." 以包含要提交的内容）
#
#   c
```

**说明**：
- `git rm --cached c`：只从暂存区移除，工作区的文件 `c` 依然存在
- 文件 `c` 从"已暂存"状态变回"未跟踪"状态
- 适用于误添加文件到暂存区的场景

---

### 2.5 删除文件

#### 方法 1：手动删除

```bash
# 直接从工作区删除文件
rm -f c

# 查看状态
git status
```

**输出示例**：
```bash
[root@gitlab /git_data]# rm -f c
[root@gitlab /git_data]# git status
# 位于分支 master
#
# 要提交的变更：
#   新文件：a
#   新文件：b
#
# 已删除:
#   （使用 "git add/rm <file>..." 更新要提交的内容）
#
#   c
```

**说明**：
- `rm -f c`：直接从文件系统删除，Git 会检测到文件丢失
- 状态显示"已删除"，需要执行 `git add/rm c` 来确认删除

#### 方法 2：Git 删除（推荐）

```bash
# 同时删除工作区和暂存区的文件
git rm -f b

# 查看状态
git status
```

**输出示例**：
```bash
[root@gitlab /git_data]# git rm -f b
rm 'b'
[root@gitlab /git_data]# git status
# 位于分支 master
#
# 要提交的变更：
#   新文件：a
```

**说明**：
- `git rm -f b`：一步到位，同时删除工作区和暂存区的文件
- `-f`：强制删除，无需确认
- **推荐使用**：操作简单，状态清晰

---

### 2.6 提交到本地仓库

```bash
# 提交暂存区文件到本地仓库
git commit -m "commit a"
```

**输出示例**：
```bash
[root@gitlab /git_data]# git commit -m "commit a"
[master（根提交）1153f56] commit a
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 a
```

**输出解读**：
- `[master（根提交）1153f56]`：
  - `master`：当前分支
  - `根提交`：这是第一个提交（没有父提交）
  - `1153f56`：提交的简短哈希值（唯一标识）
- `1 file changed`：1 个文件发生变化
- `0 insertions(+), 0 deletions(-)`：0 行新增，0 行删除（空文件）
- `create mode 100644 a`：创建文件 `a`，权限为 644（ rw-r--r--）

**提交后状态**：
```bash
[root@gitlab /git_data]# git status
# 位于分支 master
无文件要提交，干净的工作区
```

**说明**：
- "干净的工作区"：工作区与最新提交完全一致，无未提交更改
- 这是理想状态，建议经常提交保持工作区干净

---

### 2.7 重命名文件

#### 方法 1：手动重命名

```bash
# 手动重命名
mv a a.txt

# 查看状态（显示删除 + 未跟踪）
git status

# 撤回旧文件，添加新文件
git rm --cached a
git add a.txt

# 提交
git commit -m "rename a to a.txt"
```

**说明**：
- 手动 `mv` 后，Git 会认为删除了 `a`，新增了 `a.txt`
- 需要手动调整状态，操作繁琐
- **不推荐**：Git 无法自动识别重命名

#### 方法 2：Git 重命名（推荐）

```bash
# 使用 git mv 命令
git mv a.txt a

# 查看状态（自动识别为重命名）
git status

# 提交
git commit -m "rename a.txt to a"
```

**输出示例**：
```bash
[root@gitlab /git_data]# git mv a.txt a
[root@gitlab /git_data]# git status
# 位于分支 master
# 要提交的变更：
#   重命名：a.txt -> a
```

**说明**：
- `git mv`：Git 感知重命名操作
- 自动识别为"重命名"而非"删除 + 新增"
- **推荐使用**：保留文件历史，便于追溯

---

### 2.8 查看文件差异

#### 对比工作区与暂存区

```bash
# 修改文件
echo "aaaa" > a

# 查看工作区与暂存区的差异
git diff
```

**输出示例**：
```bash
[root@gitlab /git_data]# git diff
diff --git a/a b/a
index e69de29..5d308e1 100644
--- a/a
+++ b/a
@@ -0,0 +1 @@
+aaaa
```

**输出解读**：
- `diff --git a/a b/a`：对比文件 `a` 的两个版本
- `index e69de29..5d308e1`：文件哈希值变化
- `--- a/a`：旧版本（暂存区）
- `+++ b/a`：新版本（工作区）
- `@@ -0,0 +1 @@`：从第 0 行开始，新增 1 行
- `+aaaa`：新增内容为 "aaaa"

#### 对比暂存区与本地仓库

```bash
# 先添加到暂存区
git add a

# 查看暂存区与本地仓库的差异
git diff --cached
```

**说明**：
- `git diff`：工作区 vs 暂存区
- `git diff --cached`：暂存区 vs 本地仓库
- `git diff HEAD`：工作区 vs 本地仓库（跳过暂存区）

---

### 2.9 查看提交历史

#### 查看详细信息

```bash
# 查看完整提交历史
git log
```

**输出示例**：
```bash
[root@gitlab /git_data]# git log
commit 8203c878bc30c3bd23ee977e5980232fa660ddae
Author: zhangya <526195417@qq.com>
Date:   Mon May 11 13:38:22 2020 +0800

    modified a

commit 5c3ddba7bc8de6b8575e77513ee9805021ffc5ef
Author: zhangya <526195417@qq.com>
Date:   Mon May 11 13:26:10 2020 +0800

    rename a.txt a
```

**输出解读**：
- `commit 8203c87...`：提交的完整哈希值（40 字符）
- `Author`：提交者姓名和邮箱
- `Date`：提交时间（带时区）
- 空行后的缩进文本：提交信息

#### 查看简洁信息

```bash
# 一行显示一条提交
git log --oneline
```

**输出示例**：
```bash
[root@gitlab /git_data]# git log --oneline
8203c87 modified a
5c3ddba rename a.txt a
42ede9c commit a.txt
1153f56 commit a
```

**说明**：
- `--oneline`：简洁模式，每行一条提交
- 格式：`短哈希 提交信息`
- 适合快速浏览提交历史

#### 查看分支指向

```bash
# 显示分支和标签
git log --oneline --decorate
```

**输出示例**：
```bash
[root@gitlab /git_data]# git log --oneline --decorate
8203c87 (HEAD, master) modified a
5c3ddba rename a.txt a
42ede9c commit a.txt
1153f56 commit a
```

**符号说明**：
- `HEAD`：当前所在提交
- `master`：master 分支指向的提交
- `->`：分支指向（如 `HEAD -> master` 表示 HEAD 指向 master）

#### 查看最新 N 条记录

```bash
# 查看最新 1 条
git log -1

# 查看最新 3 条
git log -3
```

**说明**：
- `-1`：只显示最近 1 条提交
- `-3`：显示最近 3 条提交
- 适用于大型项目，避免输出过多

---

### 2.10 回滚到指定版本

#### 使用 commit ID 回滚

```bash
# 查看提交历史
git log --oneline

# 回滚到指定版本（危险操作，谨慎使用）
git reset --hard 8203c87
```

**输出示例**：
```bash
[root@gitlab /git_data]# git reset --hard 8203c87
HEAD 现在位于 8203c87 modified a
```

⚠️ **警告**：
- `git reset --hard` 会**永久丢弃**所有未提交的更改
- 回滚后，指定版本之后的提交会从分支历史中消失
- 使用前务必确认已备份重要数据

#### 使用 reflog 恢复误操作

**场景**：回滚后发现回错了，想恢复到之前的版本

```bash
# 查看完整的操作历史（包括已回滚的提交）
git reflog
```

**输出示例**：
```bash
[root@gitlab /git_data]# git reflog
8203c87 HEAD@{0}: reset: moving to 8203c87
4df18d4 HEAD@{1}: commit: add ccc
b11e0b2 HEAD@{2}: commit: add bbb
8203c87 HEAD@{3}: commit: modified a
5c3ddba HEAD@{4}: commit: rename a.txt a
```

**输出解读**：
- `HEAD@{0}`：当前操作（最新）
- `HEAD@{1}`：上一步操作
- `HEAD@{2}`：上上步操作
- 每行记录一次 HEAD 的变更

**恢复操作**：
```bash
# 根据 reflog 找到正确的 commit ID
git reset --hard b11e0b2
```

**说明**：
- `git log`：只显示当前分支的提交历史
- `git reflog`：显示所有操作历史（包括回滚、重置等）
- **使用 reflog 可以找回"丢失"的提交**，是 Git 的"后悔药"

---

## 第 3 章 分支管理

### 3.1 分支概念详解

> **分支**是 Git 最强大的功能之一，它允许你在不同的开发线上独立工作，互不干扰。

**形象比喻**：
```
想象你在写一本书：

主分支 (master) = 正式出版的版本
  ↓
分支 1 (chapter-1) = 第 1 章草稿（独立修改）
  ↓
分支 2 (chapter-2) = 第 2 章草稿（独立修改）
  ↓
分支 3 (fix-typo) = 修正错别字（独立修改）

最后把所有章节合并到正式版本中
```

**分支的优势**：
- ✅ **并行开发**：多人同时开发不同功能，互不影响
- ✅ **功能隔离**：新功能在独立分支开发，不影响主线
- ✅ **风险降低**：实验性功能在分支尝试，失败不影响主线
- ✅ **版本管理**：不同版本对应不同分支，便于维护

---

### 3.2 查看分支

#### 查看本地分支

```bash
# 列出所有本地分支
git branch
```

**输出示例**：
```bash
[root@gitlab /git_data]# git branch
* master
  testing
  feature
```

**说明**：
- `*`：标记当前所在的分支
- 上面表示当前在 `master` 分支
- 共有 3 个本地分支（master、testing、feature）

#### 查看分支及提交历史

```bash
# 图形化显示分支和提交
git log --oneline --graph --decorate --all
```

**输出示例**：
```bash
* 921d88e (HEAD -> master) merge testing to master
| * 71c50c8 (testing) modified a on testing branch
|/
* 38fd841 modified a master
* 6f38df1 Merge branch 'testing'
* 6f9e2f0 commit master
| * d50853d (feature) add feature
|/
* b11e0b2 add bbb
```

**图例说明**：

| 符号 | 含义 |
|:---|:---|
| `*` | 提交节点 |
| `->` | 当前分支指向 |
| `()` | 分支名/标签名 |
| `|` | 分支线 |
| `/` | 分支合并 |

---

### 3.3 创建分支

#### 方法 1：创建但不切换

```bash
# 基于当前分支创建新分支
git branch testing

# 查看分支
git branch
```

**输出示例**：
```bash
[root@gitlab /git_data]# git branch testing
[root@gitlab /git_data]# git branch
  master
* testing
```

**说明**：
- `git branch testing`：创建名为 `testing` 的分支
- 创建后仍停留在当前分支（未切换）

#### 方法 2：创建并切换（推荐）

```bash
# 创建并切换到新分支
git checkout -b testing

# 或者使用新命令（Git 2.23+）
git switch -c testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git checkout -b testing
切换到一个新分支 'testing'
```

**说明**：
- `git checkout -b testing`：创建并切换到 `testing` 分支
- `git switch -c testing`：Git 2.23+ 的新语法，更语义化
- **推荐使用**：一步完成创建和切换

---

### 3.4 切换分支

```bash
# 切换到已有分支
git checkout testing

# 或者使用新命令（Git 2.23+）
git switch testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git checkout testing
切换到分支 'testing'

[root@gitlab /git_data]# git branch
  master
* testing
```

⚠️ **注意**：
- 切换分支时，Git 会自动更新工作目录文件
- 未提交的变更可能被覆盖（Git 会警告）
- 切换前建议先提交或暂存更改

---

### 3.5 合并分支

#### 场景 1：快进合并（Fast-forward）

**前提**：master 没有新提交，testing 有新的提交

```bash
# 当前在 master 分支
git merge testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git merge testing
Updating b11e0b2..d50853d
Fast-forward
 test | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
```

**说明**：
- `Fast-forward`：快进合并
- Git 只是简单移动 master 指针到 testing
- 不产生新的合并提交
- 分支历史保持线性

#### 场景 2：三方合并（Three-way merge）

**前提**：两个分支都有新提交

```bash
# 在 master 分支
git merge testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git merge testing
Merge made by the 'recursive' strategy.
 file.txt | 2 ++
 1 file changed, 2 insertions(+)
```

**说明**：
- 产生新的合并提交
- 形成分叉结构（非线性的历史）
- 使用 `recursive` 策略自动合并

---

### 3.6 冲突处理详解

#### 冲突产生场景

```
master 分支：            testing 分支：
commit-1                commit-1
    ↓                       ↓
修改 file.txt:          修改 file.txt:
"hello world"           "hello git"
    ↓                       ↓
        [合并时冲突！]
```

**冲突原因**：
- 同一文件的同一区域被两个分支修改
- Git 无法自动判断保留哪个版本
- 需要人工介入解决

#### 实战演练：制造冲突

**步骤 1**：在 master 分支修改
```bash
git checkout master
echo "master version" >> a
git commit -am "modified a on master"
```

**步骤 2**：在 testing 分支修改同一文件
```bash
git checkout testing
echo "testing version" >> a
git commit -am "modified a on testing"
```

**步骤 3**：合并时产生冲突
```bash
git checkout master
git merge testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git merge testing
自动合并 a
冲突（内容）：合并冲突于 a
自动合并失败，修正冲突然后提交修正的结果。
```

#### 查看冲突内容

```bash
cat a
```

**输出示例**：
```bash
[root@gitlab /git_data]# cat a
第一行内容
第二行内容
<<<<<<< HEAD
master version
=======
testing version
>>>>>>> testing
```

**冲突标记说明**：
```
<<<<<<< HEAD        ← 冲突开始
master version      ← 当前分支（master）的内容
=======             ← 分隔线
testing version     ← 要合并分支（testing）的内容
>>>>>>> testing     ← 冲突结束
```

#### 解决冲突步骤

**步骤 1**：编辑文件，保留需要的内容
```bash
# 使用编辑器打开文件
vim a

# 解决后的内容（保留两个版本）
第一行内容
第二行内容
master version
testing version
```

**步骤 2**：标记冲突已解决
```bash
git add a
```

**步骤 3**：完成合并提交
```bash
git commit -m "merge testing to master"
```

**说明**：
- 编辑文件时，删除冲突标记（`<<<<<<<`、`=======`、`>>>>>>>`）
- 保留需要的内容（可以是任一版本，或两者结合）
- `git add` 标记冲突已解决
- `git commit` 完成合并

---

### 3.7 取消合并

```bash
# 合并过程中想放弃
git merge --abort
```

**说明**：
- 会恢复到合并前的状态
- 所有未解决的变更会被丢弃
- 适用于冲突太复杂，想重新开始的场景

---

### 3.8 删除分支

#### 删除已合并的分支

```bash
git branch -d testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git branch -d testing
已删除分支 testing（曾为 71c50c8）。
```

**说明**：
- `-d`：安全删除，只允许删除已合并的分支
- 防止误删未合并的工作

#### 强制删除未合并的分支

```bash
# 使用 -D 强制删除
git branch -D feature
```

⚠️ **警告**：
- `-D` 会永久丢失未合并的提交
- 使用前务必确认分支内容已不再需要

---

### 3.9 分支命名规范

| 分支类型 | 命名格式 | 用途 | 示例 |
|:---|:---|:---|:---|
| **主分支** | `main` / `master` | 生产环境代码 | `main` |
| **开发分支** | `develop` | 日常开发集成分支 | `develop` |
| **功能分支** | `feature/xxx` | 新功能开发 | `feature/user-login` |
| **修复分支** | `bugfix/xxx` | Bug 修复 | `bugfix/login-error` |
| **热修复** | `hotfix/xxx` | 生产紧急修复 | `hotfix/security-patch` |
| **发布分支** | `release/x.y` | 版本发布准备 | `release/1.2.0` |

✅ **好的分支名**：
```bash
feature/user-login          # 清晰明了
bugfix/fix-null-pointer     # 说明修复内容
hotfix/security-patch-2026  # 包含时间信息
```

❌ **坏的分支名**：
```bash
test                        # 太模糊
new-feature                 # 什么新功能？
fix                         # 修复什么？
aaa                         # 毫无意义
```

---

## 第 4 章 标签使用

### 4.1 标签概念

> **标签（Tag）** 是 Git 用来标记特定提交的引用，通常用于发布版本。

**形象比喻**：
```
如果把 Git 提交历史比作一本书的草稿：

提交 (commit) = 每次修改的痕迹
分支 (branch) = 不同的写作线索
标签 (tag) = 正式出版的版本号

v1.0 → 第一版正式出版
v2.0 → 第二版正式出版
v3.0-beta → 第三版测试版
```

**标签 vs 分支**：
| 特性 | 标签 (Tag) | 分支 (Branch) |
|:---|:---|:---|
| **可变性** | 不可变（固定提交） | 可变（持续更新） |
| **用途** | 版本发布 | 开发功能 |
| **数量** | 较少（发布时创建） | 较多（日常使用） |

---

### 4.2 创建标签

#### 给当前版本创建标签

```bash
# 创建附注标签（推荐）
git tag v1.0 -m "aaa bbb master testing version v1.0"
```

**说明**：
- `-m`：添加标签说明信息
- 附注标签会存储标签创建者、时间等信息
- **推荐使用**：信息完整，便于追溯

#### 给指定版本打标签

```bash
# 查看提交历史
git log --oneline

# 基于特定 commit 创建标签
git tag -a v2.0 b11e0b2 -m "add bbb version v2.0"
```

**说明**：
- `-a`：创建附注标签
- `b11e0b2`：指定的提交哈希值
- 适用于给历史提交补打标签

---

### 4.3 查看标签

```bash
# 列出所有标签
git tag
```

**输出示例**：
```bash
[root@gitlab /git_data]# git tag
v1.0
v2.0
```

**说明**：
- 按字母顺序显示所有标签
- 可使用 `git tag -l "v1.*"` 过滤标签

---

### 4.4 回滚到指定标签

```bash
# 查看当前文件
ll

# 回滚到标签版本
git reset --hard v2.0

# 再次查看文件
ll
```

**输出示例**：
```bash
[root@gitlab /git_data]# git reset --hard v2.0
HEAD 现在位于 b11e0b2 add bbb
```

⚠️ **警告**：
- 回滚会丢弃标签之后的所有提交
- 生产环境回滚需谨慎，建议先备份

---

## 第 5 章 远程仓库操作

### 5.1 添加远程仓库

```bash
# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add origin git@github.com:user/repo.git

# 再次查看
git remote -v
```

**输出示例**：
```bash
[root@gitlab /git_data]# git remote add origin git@github.com:user/repo.git
[root@gitlab /git_data]# git remote -v
origin  git@github.com:user/repo.git (fetch)
origin  git@github.com:user/repo.git (push)
```

**说明**：
- `origin`：远程仓库的默认名称
- `(fetch)`：拉取操作的 URL
- `(push)`：推送操作的 URL
- 可配置不同的 fetch 和 push URL（高级用法）

---

### 5.2 推送代码到远程

```bash
# 推送 master 分支到远程
git push -u origin master
```

**输出示例**：
```bash
[root@gitlab /git_data]# git push -u origin master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (5/5), 431 bytes | 431.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0)
To github.com:user/repo.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

**输出解读**：
- `Enumerating objects: 5`：枚举 5 个对象
- `Counting objects: 100% (5/5)`：计数完成
- `Writing objects: 100% (5/5)`：写入完成
- `431 bytes`：推送数据大小
- `* [new branch] master -> master`：新建远程分支
- `Branch 'master' set up to track...`：设置上游分支

**说明**：
- `-u`：设置上游分支，后续可直接使用 `git push`
- 首次推送需要设置上游分支

---

### 5.3 从远程拉取代码

```bash
# 拉取远程代码并合并
git pull origin master

# 或者先拉取再合并
git fetch origin
git merge origin/master
```

**说明**：
- `git pull` = `git fetch` + `git merge`
- `git fetch`：只下载，不合并（安全）
- `git pull`：下载并自动合并（可能有冲突）

---

### 5.4 克隆远程仓库

```bash
# 克隆远程仓库到本地
git clone git@github.com:user/repo.git

# 指定目录克隆
git clone git@github.com:user/repo.git my-project
```

**输出示例**：
```bash
[root@web-7 ~]# git clone git@10.0.0.200:dev/game.git
正克隆到 'game'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
接收对象中：100% (3/3), done.
```

**说明**：
- `git clone`：一键完成克隆、初始化、配置远程
- 自动创建 `origin` 远程仓库
- 自动切换到默认分支（master 或 main）

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

### 分支操作
```bash
git branch                  # 查看分支
git branch <name>           # 创建分支
git checkout -b <name>      # 创建并切换分支
git checkout <name>         # 切换分支
git merge <name>            # 合并分支
git branch -d <name>        # 删除分支
```

### 标签操作
```bash
git tag                     # 查看标签
git tag -a <name> -m "描述" # 创建标签
git tag -d <name>           # 删除标签
```

### 远程操作
```bash
git remote -v               # 查看远程仓库
git remote add <name> <url> # 添加远程仓库
git push -u origin master   # 推送代码
git pull origin master      # 拉取代码
git clone <url>             # 克隆仓库
```

### 回滚操作
```bash
git reset --hard <commit>   # 回滚到指定版本
git reset --hard <tag>      # 回滚到指定标签
git merge --abort           # 取消合并
```

---

## 🎯 下一步

完成 Git 基础回顾后，继续学习 CI/CD 实战：

1. ✅ **Git 基础回顾**（当前文档）
2. 📖 **03-Jenkins 持续集成** - 包含 CI/CD 背景知识 + Jenkins 实战
   - 第 1-2 章：软件开发生命周期 + 部署痛点
   - 第 3-5 章：Jenkins 安装配置 + GitLab 集成 + 参数化构建
3. 📖 **02-GitLab 企业级代码管理** - GitLab 安装部署、权限管理、备份恢复
4. 📖 **04-SonarQube 代码质量** - SonarQube 部署、代码扫描、Jenkins 集成

---

**文档版本**: v3.0  
**内容整合**: 《Git 完全指南.md》  
**规范参考**: /tmp/git-base.pdf  
**结构调整**: CI/CD 背景知识已迁移至 03-Jenkins 持续集成.md  
**更新时间**: 2026-03-21  
**仓库地址**: https://github.com/hjs2015/git-tutorial

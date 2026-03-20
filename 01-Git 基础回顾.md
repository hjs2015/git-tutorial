# Git 基础回顾 - CI/CD 前置知识

> 📘 **CI/CD 实战版教程第一部分**  
> 📝 **内容整合自《Git 完全指南.md》，并参考 /tmp/git-base.pdf 校准规范**  
> 📌 术语、命令格式、操作流程已对齐标准化规范

---

## 目录

### 第一部分：CI/CD 背景知识
1. [软件开发生命周期](#第 1 章-软件开发生命周期)
2. [环境对比与部署痛点](#第 2 章-环境对比与部署痛点)

### 第二部分：Git 核心技能
3. [Git 安装与配置](#第 3 章-git 安装与配置)
4. [Git 初始化与基本操作](#第 4 章-git 初始化与基本操作)
5. [分支管理](#第 5 章-分支管理)
6. [标签使用](#第 6 章-标签使用)
7. [远程仓库操作](#第 7 章-远程仓库操作)

---

## 第一部分：CI/CD 背景知识

## 第 1 章 软件开发生命周期

### 1.1 完整开发流程

```
项目立项 → 需求调研 → 需求拆解 → 开发实现 → 测试环境测试 → 部署生产环境
```

**形象比喻**：
```
想象你要开一家餐厅：

项目立项    = 决定开什么类型的餐厅
需求调研    = 调查顾客喜欢吃什么
需求拆解    = 设计菜单和厨房流程
开发实现    = 厨师做菜
测试环境    = 试菜环节（内部品尝）
生产环境    = 正式营业（面向顾客）
```

### 1.2 四种环境详解

| 环境 | 说明 | 用途 | 数据 | 访问权限 |
|:---|:---|:---|:---|:---|
| **开发环境** | 开发人员本地电脑 | 代码编写、调试 | 本地 Mock 数据 | 开发人员 |
| **测试环境** | 内网服务器 | 功能测试、集成测试 | 测试数据 | 测试人员 |
| **预发布环境** | 独立服务器 | 质量检测、性能测试 | 生产数据副本 | 测试 + 运维 |
| **生产环境** | 云服务器/IDC | 面向用户 | 真实数据 | 仅运维 |

**环境对比图**：
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  开发环境   │ →   │  测试环境   │ →   │ 预发布环境  │ →   │  生产环境   │
│  localhost  │     │  test.local │     │ staging.com │     │  www.com    │
│  Mock 数据   │     │  测试数据   │     │ 生产副本     │     │  真实数据   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
     ↓                    ↓                    ↓                    ↓
  开发人员              测试人员            测试 + 运维            所有用户
```

---

## 第 2 章 环境对比与部署痛点

### 2.1 手动部署的 5 大问题

> **痛点分析**：为什么我们需要自动化部署？

**问题 1：上传方式不方便**
```bash
# 传统部署需要使用多种工具
scp code.tar.gz user@server:/path
rsync -avz ./code/ user@server:/path
rz  # 本地上传
ftp  # FTP 客户端
```

**问题 2：效率低下，占用大量时间**
```
假设部署流程：
1. 打包代码 ............ 2 分钟
2. 上传服务器 .......... 5 分钟
3. 停止服务 ............ 1 分钟
4. 备份旧版本 .......... 3 分钟
5. 部署新版本 .......... 2 分钟
6. 启动服务 ............ 2 分钟
7. 验证功能 ............ 5 分钟
───────────────────────────────
总计：20 分钟/次

如果每天部署 3 次：
20 分钟 × 3 次 = 60 分钟/天
60 分钟 × 22 工作日 = 22 小时/月
22 小时 × 12 月 = 264 小时/年 ≈ 33 个工作日！
```

**问题 3：服务器多，上线速度慢**
```
场景：需要在 10 台服务器上部署

手动部署：
20 分钟/台 × 10 台 = 200 分钟 = 3.3 小时

而且需要逐个操作，容易出错！
```

**问题 4：容易误操作，不能保证准确率**
```bash
# 人为错误示例
rm -rf /var/www/html  # 删错目录！
service nginx stop    # 忘记录入启动命令！
```

**问题 5：出问题不好回滚，手忙脚乱**
```
生产环境出问题时：
❌ 找不到之前的版本
❌ 备份不完整
❌ 回滚步骤复杂
❌ 团队手忙脚乱
```

### 2.2 自动部署的 3 大优势

**持续集成 (CI - Continuous Integration)**
```
概念：
开发的代码持续集成到代码仓库，不用等所有人都开发完毕再合并。

工作流程：
1. 开发提交代码到仓库
   ↓
2. CI 服务器自动拉取代码
   ↓
3. 自动编译、测试
   ↓
4. 返回结果给开发人员

优势：
✅ 频繁合并功能，减少冲突
✅ 及时发现问题，降低修复成本
✅ 提高团队协作效率
```

**持续交付 (CD - Continuous Delivery)**
```
概念：
将编译好的代码持续交付到测试环境进行测试。

工作流程：
1. 代码编译完成
   ↓
2. 自动部署到测试环境
   ↓
3. 自动运行测试用例
   ↓
4. 生成测试报告

预发布环境的作用：
✅ 质量扫描（代码规范检查）
✅ 漏洞扫描（安全检测）
✅ 性能测试（压力测试）
✅ 更接近生产环境
```

**持续部署**
```
概念：
代码测试通过后，自动部署到生产环境。

工作流程：
1. 测试通过
   ↓
2. 自动部署到生产服务器
   ↓
3. 健康检查
   ↓
4. 发现问题自动回滚

优势：
✅ 快速上线新功能
✅ 减少人为错误
✅ 快速回滚到正常版本
```

### 2.3 CI/CD 流水线架构图

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   开发人员   │ →   │   GitLab    │ →   │   Jenkins   │
│  提交代码    │     │  代码仓库   │     │  构建服务器  │
└─────────────┘     └─────────────┘     └─────────────┘
                                              ↓
                                    ┌─────────────┐
                                    │  SonarQube  │
                                    │  代码扫描   │
                                    └─────────────┘
                                              ↓
                        ┌─────────────────────┼─────────────────────┐
                        ↓                     ↓                     ↓
                ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
                │  测试环境   │  →    │ 预发布环境  │  →    │  生产环境   │
                │  自动测试   │       │  质量检查   │       │  自动部署   │
                └─────────────┘       └─────────────┘       └─────────────┘
```

---

## 第二部分：Git 核心技能

## 第 3 章 Git 安装与配置

### 3.1 Git 简介

> **Git** 是一个分布式版本控制系统，用于跟踪计算机文件的更改，并协调多人之间的工作。

**核心特点**：
- ✅ 分布式架构（每个开发者都有完整仓库）
- ✅ 强大的分支管理
- ✅ 数据完整性保证（SHA-1 哈希校验）
- ✅ 支持离线操作

### 3.2 安装 Git

#### CentOS/RHEL 系统
```bash
# 使用 YUM 安装
yum install git -y

# 验证安装
git --version
```

**输出示例**：
```bash
[root@gitlab ~]# git --version
git version 2.20.1
```

#### Ubuntu/Debian 系统
```bash
# 使用 APT 安装
apt update
apt install git -y

# 验证安装
git --version
```

### 3.3 配置用户信息

> **重要**：首次使用 Git 必须配置用户名和邮箱，这些信息会附加到每次提交中。

#### 全局配置（推荐）
```bash
# 配置用户名（所有仓库生效）
git config --global user.name "zhangya"

# 配置邮箱（所有仓库生效）
git config --global user.email "526195417@qq.com"
```

#### 仓库级配置
```bash
# 进入特定仓库
cd /path/to/repo

# 配置仅对该仓库生效
git config --local user.name "project-user"
git config --local user.email "project@example.com"
```

#### 配置文件位置
```bash
# 查看配置文件位置
git config --help

# 配置文件层级：
--global    # 使用全局配置文件 (~/.gitconfig)
--system    # 使用系统级配置文件 (/etc/gitconfig)
--local     # 使用版本库级配置文件 (.git/config)
```

### 3.4 查看配置

#### 列出所有配置
```bash
git config --list
```

**输出示例**：
```bash
[root@gitlab ~]# git config --list
user.name=zhangya
user.email=526195417@qq.com
color.ui=true
```

#### 查看配置文件内容
```bash
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

### 3.5 设置语法高亮（可选）
```bash
# 启用彩色输出
git config --global color.ui true

# 查看配置
git config --list
```

---

## 第 4 章 Git 初始化与基本操作

### 4.1 初始化仓库

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
Initialized empty Git repository in /git_data/.git/
```

#### 查看隐藏目录
```bash
# 查看 .git 目录结构
ls -la .git/
```

**输出示例**：
```bash
[root@gitlab /git_data]# ls .git|xargs -n 1
branches      # 分支目录
config        # 定义项目的特有配置
description   # 描述
HEAD          # 当前分支
hooks         # git 钩子文件
info          # 包含一个全局排除文件
objects       # 存放所有数据，包含 info 和 pack 两个子文件夹
refs          # 存放指向数据（分支）的提交对象的指针
index         # 保存暂存区信息（执行 git add 后生成）
```

### 4.2 查看状态

```bash
# 查看仓库状态
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
- **未跟踪 (Untracked)**：新创建的文件，Git 尚未管理
- **已暂存 (Staged)**：已添加到暂存区，准备提交
- **已提交 (Committed)**：已提交到本地仓库
- **已修改 (Modified)**：已跟踪但尚未暂存的修改

### 4.3 添加文件到暂存区

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

#### 添加所有文件
```bash
# 添加所有文件到暂存区
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

### 4.4 撤回暂存区文件

```bash
# 从暂存区撤回文件（不删除工作区文件）
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
#   c
```

### 4.5 删除文件

#### 方法 1：手动删除
```bash
# 直接从工作区删除
rm -f c

# 查看状态
git status
```

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

### 4.6 提交到本地仓库

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

**提交后状态**：
```bash
[root@gitlab /git_data]# git status
# 位于分支 master
无文件要提交，干净的工作区
```

### 4.7 重命名文件

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

### 4.8 查看文件差异

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

#### 对比暂存区与本地仓库
```bash
# 先添加到暂存区
git add a

# 查看暂存区与本地仓库的差异
git diff --cached
```

### 4.9 查看提交历史

#### 查看详细信息
```bash
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

#### 查看简洁信息
```bash
# 一行显示
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

#### 查看最新 N 条记录
```bash
# 查看最新 1 条
git log -1

# 查看最新 3 条
git log -3
```

### 4.10 回滚到指定版本

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

⚠️ **警告**：`git reset --hard` 会丢弃所有未提交的更改！

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

**恢复操作**：
```bash
# 根据 reflog 找到正确的 commit ID
git reset --hard b11e0b2
```

**说明**：
- `git log`：只显示当前分支的提交历史
- `git reflog`：显示所有操作历史（包括回滚、重置等）
- 使用 `reflog` 可以找回"丢失"的提交

---

## 第 5 章 分支管理

### 5.1 分支概念详解

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

### 5.2 查看分支

#### 查看本地分支
```bash
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
- `*` 标记当前所在的分支
- 上面表示当前在 `master` 分支
- 共有 3 个本地分支

#### 查看分支及提交历史
```bash
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
- `*`：提交节点
- `->`：当前分支指向
- `()`：分支名/标签名
- `|`：分支线
- `/`：分支合并

### 5.3 创建分支

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

### 5.4 切换分支

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

⚠️ **注意**：切换分支时，Git 会自动更新工作目录文件。未提交的变更可能被覆盖（会警告）。

### 5.5 合并分支

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
- 形成分叉结构

### 5.6 冲突处理详解

#### 冲突产生场景

```
master 分支：testing 分支：
commit-1            commit-1
    ↓                   ↓
修改 file.txt:修改 file.txt:
"hello world"       "hello git"
    ↓                   ↓
[合并时冲突！]
```

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

### 5.7 取消合并

```bash
# 合并过程中想放弃
git merge --abort
```

**说明**：
- 会恢复到合并前的状态
- 所有未解决的变更会被丢弃

### 5.8 删除分支

#### 删除已合并的分支
```bash
git branch -d testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git branch -d testing
已删除分支 testing（曾为 71c50c8）。
```

#### 强制删除未合并的分支
```bash
# 使用 -D 强制删除
git branch -D feature
```

⚠️ **警告**：`-D` 会永久丢失未合并的提交！

### 5.9 分支命名规范

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

## 第 6 章 标签使用

### 6.1 标签概念

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

### 6.2 创建标签

#### 给当前版本创建标签
```bash
# 创建附注标签（推荐）
git tag v1.0 -m "aaa bbb master testing version v1.0"
```

#### 给指定版本打标签
```bash
# 查看提交历史
git log --oneline

# 基于特定 commit 创建标签
git tag -a v2.0 b11e0b2 -m "add bbb version v2.0"
```

### 6.3 查看标签

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

### 6.4 回滚到指定标签

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

---

## 第 7 章 远程仓库操作

### 7.1 添加远程仓库

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

### 7.2 推送代码到远程

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

**说明**：
- `-u`：设置上游分支，后续可直接使用 `git push`

### 7.3 从远程拉取代码

```bash
# 拉取远程代码并合并
git pull origin master

# 或者先拉取再合并
git fetch origin
git merge origin/master
```

### 7.4 克隆远程仓库

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

完成 Git 基础回顾后，继续学习：

1. ✅ **Git 基础回顾**（当前文档）
2. 📖 **GitLab 企业级代码管理** - [02-GitLab 企业级代码管理.md](./02-GitLab 企业级代码管理.md)
3. 📖 **Jenkins 持续集成** - [03-Jenkins 持续集成.md](./03-Jenkins 持续集成.md)
4. 📖 **SonarQube 代码质量** - [04-SonarQube 代码质量.md](./04-SonarQube 代码质量.md)

---

**文档版本**: v2.0  
**内容整合**: 《Git 完全指南.md》  
**规范参考**: /tmp/git-base.pdf  
**更新时间**: 2026-03-21  
**仓库地址**: https://github.com/hjs2015/git-tutorial

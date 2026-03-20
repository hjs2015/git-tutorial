
---

## 5. 分支管理

### 5.1 分支概念详解

#### 什么是分支？

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

#### 分支的工作原理

```
Git 分支本质是一个指向提交的指针：

commit-1 → commit-2 → commit-3 → commit-4
           ↑
        master (当前分支)
        
创建新分支 testing：

commit-1 → commit-2 → commit-3 → commit-4
           ↑              ↑
        master        testing
        
在 testing 分支提交新 commit：

commit-1 → commit-2 → commit-3 → commit-4
           ↑              ↑
        master        testing → commit-5
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

#### 查看远程分支
```bash
# 查看远程跟踪分支
git branch -r

# 查看所有分支（本地 + 远程）
git branch -a
```

**输出示例**：
```bash
[root@gitlab /git_data]# git branch -r
  origin/HEAD -> origin/master
  origin/master
  origin/develop
  origin/feature/user-login

[root@gitlab /git_data]# git branch -a
* master
  testing
  remotes/origin/master
  remotes/origin/develop
  remotes/origin/feature/user-login
```

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
* 8203c87 modified a
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

[root@gitlab /git_data]# git branch
  master
* testing
```

#### 方法 3：基于指定提交创建
```bash
# 基于特定 commit 创建分支
git branch feature 8203c87

# 查看
git log --oneline --graph --all
```

**输出示例**：
```bash
* 921d88e (HEAD -> master) merge testing to master
| * 71c50c8 (testing) modified a on testing branch
|/
* 38fd841 modified a master
* 8203c87 (feature) modified a  ← 新分支基于此 commit
* 5c3ddba rename a.txt a
```

### 5.4 切换分支

#### 切换到已有分支
```bash
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

#### 切换分支时文件变化

**场景**：不同分支有不同文件

```bash
# 在 master 分支
ls -l
# 输出：master 文件

# 切换到 testing 分支
git checkout testing
ls -l
# 输出：test 文件（master 文件消失）
```

**说明**：
- 切换分支时，Git 会自动更新工作目录
- 每个分支的文件是独立的
- 未提交的变更可能被覆盖（会警告）

### 5.5 合并分支

#### 场景 1：快进合并（Fast-forward）

**前提**：master 没有新提交，testing 有新的提交

```bash
# 当前在 master 分支
git branch
# * master
#   testing

# 查看历史
git log --oneline --graph --all
# * d50853d (testing) commit test
# |
# * b11e0b2 (HEAD -> master) add bbb

# 合并 testing 到 master
git merge testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git merge testing
Updating b11e0b2..d50853d
Fast-forward
 test | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test
```

**说明**：
- `Fast-forward`：快进合并
- Git 只是简单移动 master 指针到 testing
- 不产生新的合并提交

**合并后历史**：
```bash
* d50853d (HEAD -> master, testing) commit test
* b11e0b2 add bbb
```

#### 场景 2：三方合并（Three-way merge）

**前提**：两个分支都有新提交

```bash
# 在 master 分支创建新提交
echo "master content" >> file.txt
git commit -am "modified on master"

# 在 testing 分支也创建新提交
git checkout testing
echo "testing content" >> file.txt
git commit -am "modified on testing"

# 切换回 master 并合并
git checkout master
git merge testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git merge testing
Merge made by the 'recursive' strategy.
 file.txt | 2 ++
 1 file changed, 2 insertions(+)
```

**合并后历史**：
```bash
*   6f38df1 (HEAD -> master) Merge branch 'testing'
|\
| * 71c50c8 (testing) modified on testing
* | 38fd841 modified on master
|/
* b11e0b2 add bbb
```

**说明**：
- 产生新的合并提交（6f38df1）
- 有两个父提交（38fd841 和 71c50c8）
- 形成分叉结构

### 5.6 冲突处理详解

#### 冲突产生场景

```
master 分支:          testing 分支:
commit-1              commit-1
    ↓                     ↓
commit-2              commit-2
    ↓                     ↓
修改 file.txt:        修改 file.txt:
"hello world"         "hello git"
    ↓                     ↓
[合并时冲突！]
```

#### 实战演练：制造冲突

**步骤 1**：在 master 分支修改
```bash
# 确保在 master 分支
git checkout master

# 修改文件
echo "master version" >> a
git commit -am "modified a on master"
```

**输出示例**：
```bash
[root@gitlab /git_data]# git checkout master
切换到分支 'master'

[root@gitlab /git_data]# echo "master version" >> a
[root@gitlab /git_data]# git commit -am "modified a on master"
[master 38fd841] modified a on master
 1 file changed, 1 insertion(+)
```

**步骤 2**：在 testing 分支修改同一文件
```bash
# 切换到 testing
git checkout testing

# 修改同一个文件
echo "testing version" >> a
git commit -am "modified a on testing"
```

**输出示例**：
```bash
[root@gitlab /git_data]# git checkout testing
切换到分支 'testing'

[root@gitlab /git_data]# echo "testing version" >> a
[root@gitlab /git_data]# git commit -am "modified a on testing"
[testing 71c50c8] modified a on testing
 1 file changed, 1 insertion(+)
```

**步骤 3**：合并时产生冲突
```bash
# 切换回 master
git checkout master

# 合并 testing
git merge testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git checkout master
切换到分支 'master'

[root@gitlab /git_data]# git merge testing
自动合并 a
冲突（内容）：合并冲突于 a
自动合并失败，修正冲突然后提交修正的结果。
```

#### 查看冲突内容

```bash
# 查看文件内容
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

# 或者使用其他编辑器
nano a
code a  # VS Code
```

**解决后的内容**：
```bash
# 保留两个版本的内容
第一行内容
第二行内容
master version
testing version
```

**或者只保留一个版本**：
```bash
# 只保留 master 版本
第一行内容
第二行内容
master version
```

**步骤 2**：标记冲突已解决
```bash
# 添加到暂存区（标记为已解决）
git add a
```

**步骤 3**：完成合并提交
```bash
# 提交合并结果
git commit -m "merge testing to master"
```

**输出示例**：
```bash
[root@gitlab /git_data]# git add a
[root@gitlab /git_data]# git commit -m "merge testing to master"
[master 921d88e] merge testing to master
```

#### 查看合并后的历史

```bash
git log --oneline --graph --all
```

**输出示例**：
```bash
* 921d88e (HEAD -> master) merge testing to master
| * 71c50c8 (testing) modified a on testing
|/
* 38fd841 modified a on master
* 6f38df1 Merge branch 'testing'
* 6f9e2f0 commit master
* d50853d commit test
* b11e0b2 add bbb
```

### 5.7 取消合并

#### 场景：合并到一半想放弃

```bash
# 合并过程中发现冲突太复杂，想取消
git merge --abort
```

**输出示例**：
```bash
[root@gitlab /git_data]# git merge --abort
```

**说明**：
- 会恢复到合并前的状态
- 所有未解决的变更会被丢弃
- 安全退出合并流程

### 5.8 删除分支

#### 删除已合并的分支
```bash
# 删除本地分支
git branch -d testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git branch -d testing
已删除分支 testing（曾为 71c50c8）。
```

#### 强制删除未合并的分支
```bash
# 如果分支未合并，-d 会失败
# 使用 -D 强制删除
git branch -D feature
```

**输出示例**：
```bash
[root@gitlab /git_data]# git branch -D feature
已删除分支 feature（曾为 d50853d）。
```

**警告**：
- ⚠️ `-D` 会永久丢失未合并的提交
- ⚠️ 使用前确保不需要该分支的内容

#### 删除远程分支
```bash
# 删除远程分支
git push origin --delete testing

# 或者
git push origin :testing
```

**输出示例**：
```bash
[root@gitlab /git_data]# git push origin --delete testing
 - [deleted]         testing
```

### 5.9 分支命名规范

#### 推荐的分支类型

| 分支类型 | 命名格式 | 用途 | 示例 |
|:---|:---|:---|:---|
| **主分支** | `main` / `master` | 生产环境代码 | `main` |
| **开发分支** | `develop` | 日常开发集成分支 | `develop` |
| **功能分支** | `feature/xxx` | 新功能开发 | `feature/user-login` |
| **修复分支** | `bugfix/xxx` | Bug 修复 | `bugfix/login-error` |
| **热修复** | `hotfix/xxx` | 生产紧急修复 | `hotfix/security-patch` |
| **发布分支** | `release/x.y` | 版本发布准备 | `release/1.2.0` |

#### 好的分支名 vs 坏的分支名

✅ **好的分支名**：
```bash
feature/user-login          # 清晰明了
bugfix/fix-null-pointer     # 说明修复内容
hotfix/security-patch-2026  # 包含时间信息
release/v2.0.0              # 包含版本号
```

❌ **坏的分支名**：
```bash
test                        # 太模糊
new-feature                 # 什么新功能？
fix                         # 修复什么？
aaa                         # 毫无意义
example-user-test                # 包含个人信息
```

---

## 6. 标签使用

### 6.1 标签概念

#### 什么是标签？

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

#### 标签 vs 分支

| 特性 | 标签 (Tag) | 分支 (Branch) |
|:---|:---|:---|
| **用途** | 标记特定版本 | 独立开发线 |
| **可变性** | 不可变（固定） | 可变（持续前进） |
| **典型命名** | v1.0.0, v2.1.3 | feature/login, bugfix/xxx |
| **使用场景** | 发布版本、里程碑 | 功能开发、Bug 修复 |

### 6.2 创建标签

#### 轻量标签（Lightweight Tag）

```bash
# 给当前提交创建标签
git tag v1.0

# 查看标签
git tag
```

**输出示例**：
```bash
[root@gitlab /git_data]# git tag v1.0
[root@gitlab /git_data]# git tag
v1.0
```

**说明**：
- 轻量标签只是提交的别名
- 不包含额外信息（作者、日期等）
- 适合临时标记

#### 附注标签（Annotated Tag）

```bash
# 创建带注释的标签
git tag -a v1.0 -m "版本 1.0 - 初始发布"

# 或者分两步（会打开编辑器）
git tag -a v1.0
```

**输出示例**：
```bash
[root@gitlab /git_data]# git tag -a v1.0 -m "版本 1.0 - 初始发布"
```

**说明**：
- 附注标签是完整的 Git 对象
- 包含标签创建者、日期、注释
- 适合正式版本发布

#### 给历史提交打标签

```bash
# 查看提交历史
git log --oneline

# 给指定提交打标签
git tag -a v0.9 b11e0b2 -m "版本 0.9 - 测试版"
```

**输出示例**：
```bash
[root@gitlab /git_data]# git log --oneline
921d88e (HEAD -> master, tag: v1.0) merge testing to master
71c50c8 (testing) modified a on testing branch
38fd841 modified a on master
b11e0b2 add bbb

[root@gitlab /git_data]# git tag -a v0.9 b11e0b2 -m "版本 0.9 - 测试版"
```

### 6.3 查看标签

#### 查看所有标签
```bash
git tag
```

**输出示例**：
```bash
[root@gitlab /git_data]# git tag
v0.9
v1.0
v2.0
```

#### 按模式过滤标签
```bash
# 查看 v1.x 系列的标签
git tag -l "v1.*"

# 查看 2026 年的标签
git tag -l "2026.*"
```

**输出示例**：
```bash
[root@gitlab /git_data]# git tag -l "v1.*"
v1.0
v1.1
v1.2
```

#### 查看标签详情
```bash
# 查看标签信息
git show v1.0
```

**输出示例**：
```bash
[root@gitlab /git_data]# git show v1.0
tag v1.0
Tagger: Example User <user@example.com>
Date:   Fri Mar 21 15:00:00 2026 +0800

版本 1.0 - 初始发布

commit 921d88e7bc8de6b8575e77513ee9805021ffc5ef
Author: Example User <user@example.com>
Date:   Fri Mar 21 14:50:00 2026 +0800

    merge testing to master

diff --git a/a b/a
index e69de29..5d308e1 100644
--- a/a
+++ b/a
@@ -0,0 +1 @@
+aaaa
```

### 6.4 推送标签到远程

#### 推送单个标签
```bash
git push origin v1.0
```

**输出示例**：
```bash
[root@gitlab /git_data]# git push origin v1.0
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 4 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 654 bytes | 654.00 KiB/s, done.
Total 8 (delta 4), reused 0 (delta 0), pack-reused 0
To github.com:user/repo.git
 * [new tag]         v1.0 -> v1.0
```

#### 推送所有标签
```bash
git push origin --tags
```

**输出示例**：
```bash
[root@gitlab /git_data]# git push origin --tags
Enumerating objects: 20, done.
Counting objects: 100% (20/20), done.
Delta compression using up to 4 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (12/12), 892 bytes | 892.00 KiB/s, done.
Total 12 (delta 5), reused 0 (delta 0), pack-reused 0
To github.com:user/repo.git
 * [new tag]         v1.0 -> v1.0
 * [new tag]         v1.1 -> v1.1
 * [new tag]         v2.0 -> v2.0
```

### 6.5 回滚到标签

```bash
# 回滚到指定标签
git reset --hard v1.0

# 查看当前版本
git log --oneline
cat a
```

**输出示例**：
```bash
[root@gitlab /git_data]# git reset --hard v1.0
HEAD 现在位于 921d88e merge testing to master

[root@gitlab /git_data]# git log --oneline
921d88e (HEAD -> master, tag: v1.0) merge testing to master
71c50c8 (testing) modified a on testing branch
38fd841 modified a on master
```

### 6.6 删除标签

#### 删除本地标签
```bash
git tag -d v1.0
```

**输出示例**：
```bash
[root@gitlab /git_data]# git tag -d v1.0
已删除标签 'v1.0'（曾为 921d88e）
```

#### 删除远程标签
```bash
# 先删除本地
git tag -d v1.0

# 再删除远程
git push origin :refs/tags/v1.0

# 或者
git push origin --delete v1.0
```

**输出示例**：
```bash
[root@gitlab /git_data]# git push origin --delete v1.0
 - [deleted]         v1.0
```

### 6.7 语义化版本规范

#### 版本号格式

```
主版本号。次版本号。修订号
  ↑      ↑      ↑
  |      |      └─ Bug 修复
  |      └──────── 新功能（向后兼容）
  └─────────────── 不兼容的 API 修改
```

#### 版本示例

| 版本号 | 说明 |
|:---|:---|
| `v1.0.0` | 第一个正式版本 |
| `v1.0.1` | Bug 修复 |
| `v1.1.0` | 新增功能（兼容） |
| `v2.0.0` | 重大更新（不兼容） |
| `v2.0.0-beta.1` | 2.0 第一个测试版 |
| `v2.0.0-rc.1` | 2.0 第一个候选版 |

#### 标签命名最佳实践

✅ **推荐**：
```bash
v1.0.0
v2.1.3
v3.0.0-beta.1
v3.0.0-rc.2
release-2026-03-21
```

❌ **避免**：
```bash
1.0           # 缺少 v 前缀
version-1.0   # 太长
final         # 无意义
test          # 太模糊
```

---

## 7. 命令速查表

### 7.1 核心命令

| 命令 | 完整语法 | 说明 | 示例 |
|:---|:---|:---|:---|
| **初始化** | `git init` | 创建 Git 仓库 | `git init` |
| **克隆** | `git clone <url>` | 克隆远程仓库 | `git clone https://github.com/user/repo.git` |
| **添加** | `git add <file>` | 添加到暂存区 | `git add README.md` |
| **添加全部** | `git add .` | 添加所有变更 | `git add .` |
| **提交** | `git commit -m "msg"` | 提交到仓库 | `git commit -m "feat: add login"` |
| **状态** | `git status` | 查看仓库状态 | `git status` |
| **日志** | `git log` | 查看提交历史 | `git log --oneline` |
| **差异** | `git diff` | 查看变更内容 | `git diff HEAD` |
| **回滚** | `git reset --hard <commit>` | 回滚到指定版本 | `git reset --hard abc123` |
| **恢复** | `git reflog` | 查看所有操作 | `git reflog` |

### 7.2 分支命令

| 命令 | 说明 | 示例 |
|:---|:---|:---|
| `git branch` | 查看分支 | `git branch` |
| `git branch <name>` | 创建分支 | `git branch feature` |
| `git checkout -b <name>` | 创建并切换 | `git checkout -b feature` |
| `git switch <name>` | 切换分支（新命令） | `git switch feature` |
| `git switch -c <name>` | 创建并切换（新命令） | `git switch -c feature` |
| `git merge <branch>` | 合并分支 | `git merge feature` |
| `git branch -d <name>` | 删除分支 | `git branch -d feature` |
| `git branch -D <name>` | 强制删除 | `git branch -D feature` |

### 7.3 远程命令

| 命令 | 说明 | 示例 |
|:---|:---|:---|
| `git remote -v` | 查看远程仓库 | `git remote -v` |
| `git remote add <name> <url>` | 添加远程仓库 | `git remote add origin https://...` |
| `git pull` | 拉取并合并 | `git pull origin main` |
| `git push` | 推送变更 | `git push origin main` |
| `git fetch` | 拉取不合并 | `git fetch origin` |

### 7.4 标签命令

| 命令 | 说明 | 示例 |
|:---|:---|:---|
| `git tag` | 查看所有标签 | `git tag` |
| `git tag <name>` | 创建轻量标签 | `git tag v1.0` |
| `git tag -a <name> -m "msg"` | 创建附注标签 | `git tag -a v1.0 -m "release"` |
| `git tag -d <name>` | 删除标签 | `git tag -d v1.0` |
| `git push origin <tag>` | 推送标签 | `git push origin v1.0` |
| `git push origin --tags` | 推送所有标签 | `git push origin --tags` |

### 7.5 撤销命令

| 命令 | 说明 | 影响范围 |
|:---|:---|:---|
| `git checkout -- <file>` | 丢弃工作区变更 | 工作区 |
| `git reset HEAD <file>` | 从暂存区移除 | 暂存区 |
| `git reset --soft <commit>` | 回滚提交，保留变更 | 提交历史 |
| `git reset --mixed <commit>` | 回滚提交，保留工作区 | 提交历史 + 暂存区 |
| `git reset --hard <commit>` | 完全回滚 | 全部 |
| `git revert <commit>` | 反向提交 | 新增提交 |

### 7.6 实用别名

```bash
# 添加到 ~/.gitconfig
[alias]
    # 简洁日志
    lg = log --oneline --graph --all
    
    # 快速提交
    co = checkout
    br = branch
    ci = commit
    st = status
    
    # 查看最近提交
    last = log -1 HEAD
    
    # 查看变更
    dc = diff --cached
    
    # 撤销最后一次提交
    undo = reset --soft HEAD~1
```

**使用示例**：
```bash
git lg      # 查看图形化日志
git st      # 查看状态
git co -b feature  # 创建并切换分支
git undo    # 撤销最后一次提交
```

---

## 8. 常见问题 FAQ

### Q1: 如何修改最后一次提交的信息？

```bash
# 修改提交信息
git commit --amend -m "新的提交信息"

# 修改提交信息并添加遗漏的文件
git add forgotten-file.txt
git commit --amend --no-edit
```

**注意**：
- ⚠️ 只能修改最近一次提交
- ⚠️ 如果已推送到远程，需要强制推送

### Q2: 如何撤销已经 push 的提交？

**方法 1**：使用 revert（推荐，保留历史）
```bash
# 撤销指定提交（创建新的反向提交）
git revert <commit-id>
git push origin main
```

**方法 2**：使用 reset + force（危险，会丢失历史）
```bash
# 回滚到指定提交
git reset --hard <commit-id>

# 强制推送到远程
git push --force origin main
```

**警告**：
- ⚠️ `--force` 会覆盖远程历史
- ⚠️ 可能影响其他协作者
- ⚠️ 仅在个人分支或紧急情况下使用

### Q3: 误删了分支怎么恢复？

```bash
# 1. 查看 reflog 找到删除前的 commit
git reflog

# 2. 找到分支删除前的 commit ID
# 输出示例：
# abc1234 HEAD@{5}: branch feature deleted

# 3. 基于该 commit 恢复分支
git checkout -b feature abc1234
```

### Q4: 如何忽略已经提交的文件？

```bash
# 1. 从 Git 历史中移除文件（保留本地）
git rm --cached filename

# 2. 添加到 .gitignore
echo "filename" >> .gitignore

# 3. 提交变更
git commit -m "Remove file from git tracking"
```

### Q5: 如何查看某个文件的修改历史？

```bash
# 查看文件的提交历史
git log -- filename

# 查看文件的具体变更
git log -p -- filename

# 查看谁在什么时候修改了哪一行
git blame filename
```

### Q6: 如何将多个提交合并为一个？

```bash
# 使用交互式 rebase
git rebase -i HEAD~3  # 合并最近 3 个提交

# 在编辑器中将 pick 改为 squash 或 fixup
# squash: 合并提交，保留所有提交信息
# fixup: 合并提交，丢弃提交信息
```

### Q7: 冲突太多，想放弃合并怎么办？

```bash
# 放弃合并，恢复原状
git merge --abort

# 或者如果是 rebase 过程中
git rebase --abort
```

### Q8: 如何比较两个分支的差异？

```bash
# 查看分支 A 有但分支 B 没有的提交
git log branchA --not branchB

# 查看两个分支的文件差异
git diff branchA..branchB

# 查看哪些文件在两个分支中不同
git diff --name-only branchA..branchB
```

### Q9: 如何配置 SSH 密钥？

```bash
# 1. 生成 SSH 密钥
ssh-keygen -t ed25519 -C "your_email@example.com"

# 2. 查看公钥
cat ~/.ssh/id_ed25519.pub

# 3. 复制公钥到 GitHub/GitLab
# 设置 → SSH and GPG keys → New SSH key

# 4. 测试连接
ssh -T git@github.com
```

### Q10: Git 仓库太大，如何清理？

```bash
# 1. 查看大文件
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | sort -k3 -nr | head -20

# 2. 使用 BFG 清理（推荐）
# 下载：https://rtyley.github.io/bfg-repo-cleaner/
java -jar bfg.jar --strip-blobs-bigger-than 100M .

# 3. 清理并压缩
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

---

## 9. 实战项目

### 项目 1：个人博客搭建

**场景**：使用 Git 管理个人博客代码

```bash
# 1. 创建仓库
mkdir my-blog
cd my-blog
git init

# 2. 创建 .gitignore
cat > .gitignore << EOF
node_modules/
.DS_Store
*.log
EOF

# 3. 创建 README
cat > README.md << EOF
# 我的博客

个人技术博客，记录学习心得。

## 技术栈
- Hexo
- Node.js
- Git

## 部署
git push origin main
EOF

# 4. 初始化提交
git add .
git commit -m "feat: 初始化博客项目"

# 5. 关联远程仓库
git remote add origin git@github.com:username/my-blog.git

# 6. 推送
git branch -M main
git push -u origin main
```

### 项目 2：团队协作开发

**场景**：3 人团队开发电商网站

```bash
# === 团队约定 ===
# main: 生产环境
# develop: 开发环境
# feature/*: 功能分支
# bugfix/*: Bug 修复

# === 成员 A：开发登录功能 ===
git checkout develop
git checkout -b feature/user-login

# 开发登录功能...
git add .
git commit -m "feat: 实现用户登录功能"
git commit -m "feat: 添加登录表单验证"

# 推送到远程
git push origin feature/user-login

# === 成员 B：开发商品展示 ===
git checkout develop
git checkout -b feature/product-list

# 开发商品展示...
git add .
git commit -m "feat: 实现商品列表展示"

# === 成员 C：修复支付 Bug ===
git checkout develop
git checkout -b bugfix/payment-error

# 修复 Bug...
git add .
git commit -m "fix: 修复支付金额计算错误"

# === 代码审查与合并 ===
# 在 GitHub/GitLab 创建 Pull Request
# 团队成员审查代码
# 审查通过后合并到 develop

# === 发布到生产 ===
git checkout main
git merge develop
git tag -a v1.0.0 -m "第一个正式版本"
git push origin main --tags
```

### 项目 3：紧急热修复

**场景**：生产环境发现严重 Bug，需要紧急修复

```bash
# 1. 基于 main 创建热修复分支
git checkout main
git checkout -b hotfix/security-patch

# 2. 修复 Bug
# ... 修改代码 ...
git add .
git commit -m "fix: 修复安全漏洞"

# 3. 测试
# 在测试环境验证修复

# 4. 合并到 main
git checkout main
git merge hotfix/security-patch

# 5. 创建新版本标签
git tag -a v1.0.1 -m "紧急安全修复"

# 6. 合并回 develop（保持同步）
git checkout develop
git merge hotfix/security-patch

# 7. 推送
git push origin main develop --tags

# 8. 删除热修复分支
git branch -d hotfix/security-patch
```

### 项目 4：开源项目贡献

**场景**：向开源项目提交 PR

```bash
# 1. Fork 项目
# 在 GitHub 上点击 Fork 按钮

# 2. 克隆到本地
git clone https://github.com/yourname/project.git
cd project

# 3. 添加上游远程仓库
git remote add upstream https://github.com/original/project.git

# 4. 同步上游变更
git fetch upstream
git checkout main
git merge upstream/main

# 5. 创建功能分支
git checkout -b feature/my-contribution

# 6. 开发功能
# ... 编写代码 ...
git add .
git commit -m "feat: 添加新功能"

# 7. 推送到自己的仓库
git push origin feature/my-contribution

# 8. 创建 Pull Request
# 在 GitHub 上点击 Compare & pull request

# 9. 根据反馈修改
# ... 根据审查意见修改代码 ...
git add .
git commit -m "fix: 根据审查意见修改"
git push origin feature/my-contribution

# 10. PR 合并后清理
git checkout main
git pull upstream main
git branch -d feature/my-contribution
```

---

## 📚 学习资源

### 官方文档
- [Git 官方文档](https://git-scm.com/doc) - 最权威的参考资料
- [Pro Git 中文教程](https://git-scm.com/book/zh/v2) - 免费在线书籍
- [GitHub 学习实验室](https://lab.github.com/) - 互动式学习

### 视频教程
- [B 站 Git 教程](https://search.bilibili.com/all?keyword=git 教程)
- [YouTube Git 教程](https://www.youtube.com/results?search_query=git+tutorial)

### 练习平台
- [Learn Git Branching](https://learngitbranching.js.org/) - 可视化分支练习
- [Git 实战](https://onlywei.github.io/explain-git-with-d3/) - 3D 可视化学习

### 工具推荐
- [SourceTree](https://www.sourcetreeapp.com/) - 图形化 Git 客户端
- [GitKraken](https://www.gitkraken.com/) - 跨平台 Git GUI
- [VS Code Git 插件](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-next) - 编辑器集成

---

## 🎓 认证考试

### Git 相关认证
- **GitHub Certification**: GitHub 官方认证
- **Atlassian Git Certification**: Git 和 Bitbucket 认证
- **Linux Foundation Git 认证**: 开源基金会认证

### 备考建议
1. 掌握所有基本命令
2. 理解分支和合并原理
3. 熟悉冲突解决方法
4. 了解 Git 内部机制
5. 多做实战练习

---

**最后更新**: 2026-03-21  
**原文来源**: 博客园 - 张亚  
**整理优化**: Copaw AI Assistant  
**增强版本**: v2.0（完整教程，约 25,000 字）

---

## 📝 更新日志

### v2.0 (2026-03-21)
- ✅ 大幅增加详细说明和示例输出
- ✅ 添加完整的分支管理章节
- ✅ 添加标签使用详解
- ✅ 新增常见问题 FAQ（10 个问题）
- ✅ 新增 4 个实战项目
- ✅ 完善命令速查表
- ✅ 添加学习资源和认证信息

### v1.0 (2026-03-21)
- ✅ 初始版本，基于原始 PDF 整理

---

**🎉 教程完成！祝你学习顺利！**

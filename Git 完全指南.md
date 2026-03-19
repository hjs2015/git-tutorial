# Git 版本控制完全指南

> 基于实战的 Git 学习教程，涵盖从基础配置到分支管理的完整工作流程  
> **适合人群**: 开发人员、运维工程师、DevOps 从业者  
> **预计学习时间**: 2-3 小时

---

## 📋 目录

1. [软件开发生命周期](#1-软件开发生命周期)
2. [Git 基本配置](#2-git-基本配置)
3. [Git 初始化](#3-git-初始化)
4. [基本命令](#4-基本命令)
5. [分支管理](#5-分支管理)
6. [标签使用](#6-标签使用)
7. [命令速查表](#7-命令速查表)

---

## 1. 软件开发生命周期

### 1.1 开发流程

```
项目立项 → 需求调研 → 需求拆解 → 开发实现 → 测试环境测试 → 生产环境部署
```

### 1.2 环境说明

| 环境 | 说明 | 用途 |
|:---|:---|:---|
| **开发环境** | 开发人员本地电脑 | 代码编写和初步调试 |
| **测试环境** | 独立测试服务器 | 功能测试，软件版本与生产一致，使用测试数据 |
| **预发布环境** | 接近生产的独立环境 | 质量检测，数据接近真实，域名与生产不同 |
| **生产环境** | 线上正式环境 | 面向用户，仅运维有部署权限 |

### 1.3 手动部署的问题

1. ❌ 上传方式不方便（scp/rsync/rz/ftp 等）
2. ❌ 效率低下，占用大量时间
3. ❌ 服务器多时上线速度慢
4. ❌ 容易误操作，不能保证准确率
5. ❌ 出问题不好回滚，手忙脚乱

### 1.4 自动部署的优势

#### 4.1 持续集成 (CI)
- 开发的代码持续集成到代码仓库
- 多个开发人员可同时工作
- CI 服务器自动拉取代码进行编译、测试
- 频繁合并开发功能，提高工作效率

#### 4.2 持续交付 (CD)
- 将编译好的代码持续交付到测试环境
- 在预发布环境进行质量扫描和漏洞扫描
- 测试发现问题及时修复，无问题则进入下一环节

#### 4.3 持续部署
- 代码通过测试后部署到预发布环境进一步验证
- 通过 Jenkins 持续部署到生产服务器
- 发现问题可快速回滚到正常版本

### 1.5 部署环境示例

| 主机名 | IP | 服务 | 内存 |
|:---|:---|:---|:---|
| gitlab | 10.0.0.200 | Gitlab | 2G |
| jenkins | 10.0.0.201 | Jenkins | 1G |
| nexus | 10.0.0.202 | Nexus | 2G |
| sonar | 10.0.0.203 | SonarQube | 2G |
| web | 10.0.0.7 | Nginx | 1G |

---

## 2. Git 基本配置

### 2.1 安装 Git

```bash
# CentOS/RHEL
yum install git -y

# Ubuntu/Debian
apt install git -y
```

### 2.2 查看配置

```bash
# 查看所有配置
git config --list

# 查看全局配置
git config --global --list

# 查看系统级配置
git config --system --list

# 查看当前仓库配置
git config --local --list
```

### 2.3 配置用户信息

```bash
# 配置用户名
git config --global user.name "zhangya"

# 配置邮箱
git config --global user.email "526195417@qq.com"

# 启用语法高亮
git config --global color.ui true
```

### 2.4 配置文件位置

| 参数 | 说明 |
|:---|:---|
| `--global` | 使用全局配置文件（`~/.gitconfig`） |
| `--system` | 使用系统级配置文件 |
| `--local` | 使用版本库级配置文件（`.git/config`） |
| `-f, --file <文件>` | 使用指定的配置文件 |

### 2.5 查看配置示例

```bash
[root@gitlab ~]# git config --list
user.name=zhangya
user.email=526195417@qq.com
color.ui=true

[root@gitlab ~]# cat .gitconfig
[user]
    name = zhangya
    email = 526195417@qq.com
[color]
    ui = true
```

---

## 3. Git 初始化

### 3.1 创建工作目录

```bash
mkdir /git_data
cd /git_data
```

### 3.2 初始化仓库

```bash
git init
```

### 3.3 查看状态

```bash
git status
```

### 3.4 .git 目录结构

```bash
[root@gitlab /git_data]# ls .git
branches    # 分支目录
config      # 定义项目的特有配置
description # 描述
HEAD        # 当前分支
hooks       # git 钩子文件
info        # 包含一个全局排除文件
objects     # 存放所有数据，包含 info 和 pack 两个子文件夹
refs        # 存放指向数据（分支）的提交对象的指针
index       # 保存暂存区信息
```

---

## 4. 基本命令

### 4.1 文件操作

#### 创建测试文件

```bash
touch a b c
git status
# 显示未跟踪的文件
```

#### 提交文件到暂存区

```bash
# 提交单个文件
git add a

# 提交所有文件
git add .
```

#### 撤回提交到暂存区的文件

```bash
# 从暂存区移除（保留工作区文件）
git rm --cached c
```

#### 删除提交到暂存区的文件

**方法 1**: 先撤回再删除
```bash
git rm --cached c  # 从暂存区移除
rm -f c            # 删除工作区文件
```

**方法 2**: 直接删除
```bash
git rm -f b  # 同时删除工作区和暂存区
```

#### 提交到本地仓库

```bash
git commit -m "commit a"
```

#### 重命名文件

**方法 1**: 手动修改
```bash
mv a a.txt
git rm --cached a
git add a.txt
git commit -m "rename a to a.txt"
```

**方法 2**: 使用 git mv
```bash
git mv a.txt a
git commit -m "rename a.txt to a"
```

### 4.2 对比差异

#### 工作目录 vs 暂存区

```bash
git diff
```

#### 暂存区 vs 本地仓库

```bash
git diff --cached
```

### 4.3 查看提交记录

#### 详细信息

```bash
git log
```

#### 简洁显示（一行一个提交）

```bash
git log --oneline
```

#### 显示分支和标签

```bash
git log --oneline --decorate
```

#### 显示具体内容变化

```bash
git log -p
```

#### 查看最近 N 条记录

```bash
git log -1      # 最近 1 条
git log -5      # 最近 5 条
```

### 4.4 版本回滚

#### 回滚到指定版本

```bash
# 回滚到指定 commit（会丢失后续提交）
git reset --hard 8203c87
```

#### 查看完整历史记录（包括回滚的）

```bash
git reflog
```

#### 恢复误回滚的版本

```bash
# 通过 reflog 找到目标版本
git reflog

# 回退到目标版本
git reset --hard b11e0b2
```

---

## 5. 分支管理

### 5.1 查看分支

```bash
# 查看当前分支
git branch

# 查看分支及指向
git log --oneline --decorate
```

### 5.2 创建分支

```bash
# 创建分支（不切换）
git branch testing

# 创建并切换到新分支
git checkout -b testing
```

### 5.3 切换分支

```bash
git checkout testing
git checkout master
```

### 5.4 合并分支

```bash
# 在 master 分支合并 testing
git checkout master
git merge testing
```

### 5.5 冲突处理

#### 产生冲突

```bash
# master 分支修改文件
echo "master" >> a
git commit -am "modified a master"

# testing 分支也修改同一文件
git checkout testing
echo "testing" >> a
git commit -am "modified a on testing branch"

# 合并时产生冲突
git checkout master
git merge testing
```

#### 解决冲突

```bash
# 查看冲突内容
cat a

# 输出示例:
# aaaa
# bbb
# <<<<<<< HEAD
# master
# =======
# testing
# >>>>>>> testing

# 手动编辑文件，保留需要的内容
vim a

# 提交解决结果
git commit -am "merge testing to master"
```

### 5.6 删除分支

```bash
# 删除已合并的分支
git branch -d testing

# 强制删除未合并的分支
git branch -D testing
```

---

## 6. 标签使用

### 6.1 创建标签

```bash
# 给当前版本创建标签
git tag v1.0 -m "version 1.0"

# 给指定版本打标签
git tag -a v2.0 b11e0b2 -m "version 2.0"
```

### 6.2 查看标签

```bash
# 查看所有标签
git tag

# 查看匹配模式的标签
git tag -l "v1.*"
```

### 6.3 回滚到标签

```bash
# 回滚到指定标签
git reset --hard v2.0
```

### 6.4 删除标签

```bash
# 删除本地标签
git tag -d v1.0
```

---

## 7. 命令速查表

### 7.1 核心命令

| 命令 | 说明 |
|:---|:---|
| `git init` | 初始化 Git 仓库 |
| `git add <file>` | 添加文件到暂存区 |
| `git commit -m "描述"` | 提交暂存区到仓库 |
| `git status` | 查看仓库状态 |
| `git log` | 查看提交历史 |
| `git reflog` | 查看所有操作历史 |
| `git reset --hard <commitID>` | 回滚到指定版本 |

### 7.2 分支命令

| 命令 | 说明 |
|:---|:---|
| `git branch` | 查看分支 |
| `git branch <name>` | 创建分支 |
| `git checkout -b <name>` | 创建并切换分支 |
| `git checkout <name>` | 切换分支 |
| `git merge <branch>` | 合并分支 |
| `git branch -d <name>` | 删除分支 |

### 7.3 标签命令

| 命令 | 说明 |
|:---|:---|
| `git tag <name>` | 创建标签 |
| `git tag -a <name> <commit> -m "描述"` | 创建带注释的标签 |
| `git tag` | 查看所有标签 |
| `git tag -d <name>` | 删除标签 |
| `git reset --hard <tag>` | 回滚到标签 |

### 7.4 对比命令

| 命令 | 说明 |
|:---|:---|
| `git diff` | 工作目录 vs 暂存区 |
| `git diff --cached` | 暂存区 vs 仓库 |
| `git diff <commit1> <commit2>` | 对比两个版本 |

---

## 📊 实战演练

### 练习 1: 基本工作流程

```bash
# 1. 创建项目目录
mkdir myproject && cd myproject

# 2. 初始化 Git
git init

# 3. 创建文件并提交
echo "Hello Git" > README.md
git add README.md
git commit -m "Initial commit"

# 4. 查看状态和日志
git status
git log --oneline
```

### 练习 2: 分支合并

```bash
# 1. 创建并切换到新分支
git checkout -b feature

# 2. 在新分支上修改
echo "Feature" >> feature.txt
git add .
git commit -m "Add feature"

# 3. 切换回主分支并合并
git checkout master
git merge feature

# 4. 删除已合并的分支
git branch -d feature
```

### 练习 3: 版本回滚

```bash
# 1. 查看提交历史
git log --oneline

# 2. 回滚到指定版本
git reset --hard <commit-id>

# 3. 如果回滚错了，用 reflog 恢复
git reflog
git reset --hard <target-commit>
```

---

## 🎯 最佳实践

### 1. 提交规范

```bash
# 好的提交信息
git commit -m "feat: 添加用户登录功能"
git commit -m "fix: 修复登录页面样式问题"
git commit -m "docs: 更新 README 文档"

# 避免的提交信息
git commit -m "update"      # 太模糊
git commit -m "修改"        # 无意义
```

### 2. 分支策略

- `master/main`: 生产环境代码
- `develop`: 开发环境代码
- `feature/*`: 功能开发分支
- `bugfix/*`: Bug 修复分支
- `hotfix/*`: 紧急修复分支

### 3. 定期备份

```bash
# 推送到远程仓库
git remote add origin <repository-url>
git push -u origin master
```

---

## 📚 学习资源

- [Git 官方文档](https://git-scm.com/doc)
- [Pro Git 中文教程](https://git-scm.com/book/zh/v2)
- [GitHub 学习实验室](https://lab.github.com/)

---

**最后更新**: 2026-03-21  
**原文来源**: 博客园 - 张亚  
**整理优化**: Copaw AI Assistant

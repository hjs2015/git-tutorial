# Git 完全指南 - CI/CD 实战版

> 📘 从 Git 基础到企业级 CI/CD 流水线的完整教程

---

## 📖 目录

### 第一部分：Git 基础（已有内容）
1. [软件开发生命周期](#第 1 章软件开发生命周期)
2. [Git 基本配置](#第 2 章 git 基本配置)
3. [Git 初始化](#第 3 章 git 初始化)
4. [基本命令](#第 4 章基本命令)
5. [分支管理](#第 5 章分支管理)
6. [标签使用](#第 6 章标签使用)
7. [命令速查表](#第 7 章命令速查表)
8. [常见问题 FAQ](#第 8 章常见问题 faq)
9. [实战项目](#第 9 章实战项目)

### 第二部分：GitLab 企业级代码管理
10. [GitLab 安装部署](#第 10 章 gitlab 安装部署)
11. [GitLab 权限管理](#第 11 章 gitlab 权限管理)
12. [GitLab 备份与恢复](#第 12 章 gitlab 备份与恢复)

### 第三部分：Jenkins 持续集成
13. [Jenkins 安装配置](#第 13 章 jenkins 安装配置)
14. [Jenkins 项目构建](#第 14 章 jenkins 项目构建)
15. [Jenkins 与 GitLab 集成](#第 15 章 jenkins 与 gitlab 集成)
16. [Jenkins 参数化构建](#第 16 章 jenkins 参数化构建)

### 第四部分：SonarQube 代码质量
17. [SonarQube 部署](#第 17 章 sonarqube 部署)
18. [SonarQube 与 Jenkins 集成](#第 18 章 sonarqube 与 jenkins 集成)

---

## 第一部分：Git 基础

> 📌 这部分内容已在原有教程中详细讲解，这里只做简要回顾。完整内容请查看原教程文件。

### 第 1 章 软件开发生命周期

#### 1.1 开发流程

```
项目立项 → 需求调研 → 需求拆解 → 开发实现 → 测试环境测试 → 部署生产环境
```

#### 1.2 四种环境详解

| 环境 | 说明 | 用途 | 数据 |
|:---|:---|:---|:---|
| **开发环境** | 开发人员本地电脑 | 代码编写、调试 | 本地 Mock 数据 |
| **测试环境** | 内网服务器 | 功能测试、集成测试 | 测试数据 |
| **预发布环境** | 独立服务器 | 质量检测、性能测试 | 生产数据副本 |
| **生产环境** | 云服务器/IDC | 面向用户 | 真实数据 |

#### 1.3 手动部署的 5 大问题

1. ❌ 上传方式不方便（scp、rsync、rz、ftp 等）
2. ❌ 效率低下，占用大量时间
3. ❌ 服务器多，上线速度慢
4. ❌ 容易误操作，不能保证准确率
5. ❌ 出问题不好回滚，手忙脚乱

#### 1.4 自动部署的 3 大优势

**持续集成 (CI)**
- 代码持续集成到仓库，多人同时工作
- CI 服务器自动编译、测试、返回结果
- 频繁合并功能，提高效率

**持续交付 (CD)**
- 代码持续交付到测试环境
- 预发布环境进行质量扫描和漏洞扫描
- 有问题及时修复，无问题进入下一环节

**持续部署**
- 通过 Jenkins 持续部署到生产服务器
- 发现问题快速回滚到正常版本

---

### 第 2 章 Git 基本配置

#### 2.1 安装 Git

```bash
# CentOS/RHEL
yum install git -y

# Ubuntu/Debian
apt install git -y
```

#### 2.2 配置用户信息

```bash
# 配置用户名
git config --global user.name "zhangya"

# 配置邮箱
git config --global user.email "526195417@qq.com"

# 设置语法高亮
git config --global color.ui true
```

#### 2.3 查看配置

```bash
# 列出所有配置
[root@gitlab ~]# git config --list
user.name=zhangya
user.email=526195417@qq.com
color.ui=true

# 查看配置文件
[root@gitlab ~]# cat .gitconfig
[user]
    name = zhangya
    email = 526195417@qq.com
[color]
    ui = true
```

#### 2.4 配置文件层级

| 级别 | 文件路径 | 作用范围 | 优先级 |
|:---|:---|:---|:---:|
| 系统级 | `/etc/gitconfig` | 所有用户 | 最低 |
| 全局级 | `~/.gitconfig` | 当前用户 | 中等 |
| 仓库级 | `.git/config` | 当前仓库 | 最高 |

---

### 第 3 章 Git 初始化

#### 3.1 创建工作目录并初始化

```bash
mkdir /git_data
cd /git_data
git init
```

#### 3.2 .git 目录结构

```bash
[root@gitlab /git_data]# ls .git | xargs -n 1
branches      # 分支目录
config        # 定义项目的特有配置
description   # 描述
HEAD          # 当前分支
hooks         # git 钩子文件
info          # 包含一个全局排除文件
objects       # 存放所有数据，包含 info 和 pack 两个子文件夹
refs          # 存放指向数据（分支）的提交对象的指针
index         # 保存暂存区信息
```

---

### 第 4 章 基本命令

#### 4.1 文件操作流程

```bash
# 1. 创建测试文件
[root@gitlab /git_data]# touch a b c

# 2. 查看状态
[root@gitlab /git_data]# git status
# 位于分支 master
# 初始提交
# 未跟踪的文件:
#   a
#   b
#   c

# 3. 添加到暂存区
[root@gitlab /git_data]# git add a
[root@gitlab /git_data]# git add .

# 4. 提交到本地仓库
[root@gitlab /git_data]# git commit -m "commit a"
[master（根提交）1153f56] commit a
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 a

# 5. 查看状态
[root@gitlab /git_data]# git status
# 位于分支 master
无文件要提交，干净的工作区
```

#### 4.2 删除文件

```bash
# 方法 1：先撤出暂存区，再删除
[root@gitlab /git_data]# git rm --cached c
[root@gitlab /git_data]# rm -f c

# 方法 2：同时删除工作区和暂存区
[root@gitlab /git_data]# git rm -f b
```

#### 4.3 重命名文件

```bash
# 方法 1：手动修改
[root@gitlab /git_data]# mv a a.txt
[root@gitlab /git_data]# git rm --cached a
[root@gitlab /git_data]# git add a.txt
[root@gitlab /git_data]# git commit -m "commit a.txt"

# 方法 2：使用 git mv
[root@gitlab /git_data]# git mv a.txt a
[root@gitlab /git_data]# git commit -m "rename a.txt a"
```

#### 4.4 查看差异

```bash
# 对比工作区和暂存区
[root@gitlab /git_data]# git diff

# 对比暂存区和本地仓库
[root@gitlab /git_data]# git diff --cached
```

#### 4.5 查看提交历史

```bash
# 详细信息
[root@gitlab /git_data]# git log
commit 8203c878bc30c3bd23ee977e5980232fa660ddae
Author: zhangya <526195417@qq.com>
Date:   Mon May 11 13:38:22 2020 +0800
    modified a

# 简洁显示
[root@gitlab /git_data]# git log --oneline
8203c87 modified a
5c3ddba rename a.txt a
42ede9c commit a.txt
1153f56 commit a

# 显示指针
[root@gitlab /git_data]# git log --oneline --decorate
8203c87 (HEAD, master) modified a
5c3ddba rename a.txt a

# 显示内容变化
[root@gitlab /git_data]# git log -p

# 只显示最新一条
[root@gitlab /git_data]# git log -1
```

#### 4.6 版本回滚

```bash
# 查看提交历史
[root@gitlab /git_data]# git log --oneline
4df18d4 add ccc
b11e0b2 add bbb
8203c87 modified a

# 回滚到指定版本
[root@gitlab /git_data]# git reset --hard 8203c87
HEAD 现在位于 8203c87 modified a

# 如果回滚错了，使用 reflog 恢复
[root@gitlab /git_data]# git reflog
8203c87 HEAD@{0}: reset: moving to 8203c87
4df18d4 HEAD@{1}: commit: add ccc
b11e0b2 HEAD@{2}: commit: add bbb

# 恢复到 bbb 版本
[root@gitlab /git_data]# git reset --hard b11e0b2
HEAD 现在位于 b11e0b2 add bbb
```

---

### 第 5 章 分支管理

#### 5.1 查看分支

```bash
[root@gitlab /git_data]# git branch
* master
```

#### 5.2 创建和切换分支

```bash
# 创建新分支
[root@gitlab /git_data]# git branch testing

# 创建并切换
[root@gitlab /git_data]# git checkout -b testing
切换到一个新分支 'testing'

# 查看分支
[root@gitlab /git_data]# git branch
  master
* testing
```

#### 5.3 分支提交示例

```bash
# 在 testing 分支创建文件
[root@gitlab /git_data]# touch test
[root@gitlab /git_data]# git add .
[root@gitlab /git_data]# git commit -m "commit test"
[testing d50853d] commit test

# 切换回 master
[root@gitlab /git_data]# git checkout master
切换到分支 'master'

# master 分支创建文件
[root@gitlab /git_data]# touch master
[root@gitlab /git_data]# git add .
[root@gitlab /git_data]# git commit -m "commit master"
```

#### 5.4 合并分支

```bash
# 合并 testing 到 master
[root@gitlab /git_data]# git merge testing
Merge made by the 'recursive' strategy.
 test | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test

# 查看提交日志
[root@gitlab /git_data]# git log --oneline --decorate
6f38df1 (HEAD, master) Merge branch 'testing'
6f9e2f0 commit master
d50853d (testing) commit test
```

#### 5.5 冲突处理

```bash
# 1. master 分支修改文件
[root@gitlab /git_data]# echo "master" >> a
[root@gitlab /git_data]# git commit -am "modified a master"

# 2. testing 分支修改同一文件
[root@gitlab /git_data]# git checkout testing
[root@gitlab /git_data]# echo "testing" >> a
[root@gitlab /git_data]# git commit -am "modified a on testing branch"

# 3. 合并时产生冲突
[root@gitlab /git_data]# git checkout master
[root@gitlab /git_data]# git merge testing
自动合并 a
冲突（内容）：合并冲突于 a
自动合并失败，修正冲突然后提交修正的结果。

# 4. 查看冲突内容
[root@gitlab /git_data]# cat a
aaaa
bbb
<<<<<<< HEAD
master
=======
testing
>>>>>>> testing

# 5. 手动解决冲突
[root@gitlab /git_data]# vim a
# 编辑后保留需要的内容

# 6. 提交解决结果
[root@gitlab /git_data]# git commit -am "merge testing to master"
```

#### 5.6 删除分支

```bash
[root@gitlab /git_data]# git branch -d testing
已删除分支 testing（曾为 71c50c8）。
```

---

### 第 6 章 标签使用

#### 6.1 创建标签

```bash
# 给当前版本打标签
[root@gitlab /git_data]# git tag v1.0 -m "aaa bbb master testing version v1.0"

# 给指定版本打标签
[root@gitlab /git_data]# git tag -a v2.0 b11e0b2 -m "add bbb version v2.0"
```

#### 6.2 查看标签

```bash
[root@gitlab /git_data]# git tag
v1.0
v2.0
```

#### 6.3 回滚到标签

```bash
# 查看当前文件
[root@gitlab /git_data]# ll
总用量 4
-rw-r--r-- 1 root root 16 5 月 11 16:36 a
-rw-r--r-- 1 root root 0 5 月 11 16:33 master
-rw-r--r-- 1 root root 0 5 月 11 16:11 test

# 回滚到标签
[root@gitlab /git_data]# git reset --hard v2.0
HEAD 现在位于 b11e0b2 add bbb

# 再次查看
[root@gitlab /git_data]# ll
总用量 4
-rw-r--r-- 1 root root 9 5 月 11 16:52 a
```

---

### 第 7 章 命令速查表

| 命令 | 说明 |
|:---|:---|
| `git init` | 初始化版本库 |
| `git add .` | 添加到暂存区 |
| `git commit -m "描述"` | 提交到版本库 |
| `git log` | 查看提交历史 |
| `git reflog` | 查看所有历史记录 |
| `git status` | 查看文件状态 |
| `git reset --hard commitID` | 回退到指定版本 |
| `git branch` | 查看/创建分支 |
| `git checkout` | 切换分支 |
| `git merge` | 合并分支 |
| `git tag` | 创建标签 |

---

### 第 8 章 常见问题 FAQ

详见原教程文件 `Git 完全指南.md` 第 8 章。

---

### 第 9 章 实战项目

详见原教程文件 `Git 完全指南.md` 第 9 章。

---

## 第二部分：GitLab 企业级代码管理

### 第 10 章 GitLab 安装部署

#### 10.1 环境准备

| 主机名 | IP | 服务 | 内存 |
|:---|:---|:---|:---:|
| gitlab | 10.0.0.200 | GitLab | 2G |
| jenkins | 10.0.0.201 | Jenkins | 1G |
| nexus | 10.0.0.202 | Nexus | 2G |
| sonar | 10.0.0.203 | SonarQube | 2G |
| web | 10.0.0.7 | Nginx | 1G |

#### 10.2 安装 GitLab

**方法 1：直接下载 RPM 包（推荐）**

```bash
# 下载地址
https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/

# 安装命令
yum localinstall gitlab-ce-12.0.3-ce.0.el7.x86_64.rpm -y
```

**方法 2：配置 YUM 源**

```bash
cat > /etc/yum.repos.d/gitlab-ce.repo << 'EOF'
[gitlab-ce]
name=Gitlab CE Repository
baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el$releasever/
gpgcheck=0
enabled=1
EOF

yum -y install gitlab-ce
```

#### 10.3 配置 GitLab

```bash
# 修改配置文件
vim /etc/gitlab/gitlab.rb

# 修改 external_url 为本机 IP
external_url 'http://10.0.0.200'

# 重新加载配置（耗时较长，耐心等待）
gitlab-ctl reconfigure
```

#### 10.4 Web 页面访问

1. 浏览器访问 `http://10.0.0.200`
2. 初次登录需要设置密码（长度不低于 8 位）
3. 用户名：`root`，密码：刚才设置的密码

#### 10.5 GitLab 常用命令

```bash
# 查看状态
gitlab-ctl status

# 启动服务
gitlab-ctl start

# 停止服务
gitlab-ctl stop

# 停止单个服务
gitlab-ctl stop nginx

# 启动单个服务
gitlab-ctl start nginx

# 查看服务日志
gitlab-ctl tail
```

---

### 第 11 章 GitLab 权限管理

#### 11.1 用户 - 项目组 - 项目说明

1. 项目由项目组创建，而不是由用户创建
2. 用户通过加入不同的组来访问或提交项目
3. 项目可见性：
   - 私有：只有项目组成员可以查看
   - 内部：所有登录用户可以查看
   - 公开：谁都可以看

#### 11.2 建议的操作流程

```
1. 创建组
   ↓
2. 基于组创建项目
   ↓
3. 创建用户，分配组，分配权限
```

#### 11.3 权限实验需求

**创建 2 个组**
- dev
- ops

**创建 2 个项目**
- ansible（ops 组）
- game（dev 组）

**创建 3 个用户**
- cto：对所有组都有权限，拥有合并分支的权限
- oldya_dev：对 dev 组有所有权限
- oldya_ops：对 ops 组有所有权限，对 dev 组只有拉取权限

#### 11.4 创建组和项目

1. 登录 GitLab Web 界面
2. 进入 Admin Area → Groups → New Group
3. 创建 dev 和 ops 两个组
4. 在每个组下创建对应项目

#### 11.5 创建用户并授权

1. Admin Area → Users → New User
2. 创建 3 个用户并设置密码
3. 进入 Groups → 选择组 → Members
4. 添加用户并选择权限级别

#### 11.6 SSH 公钥配置

```bash
# 生成 SSH 密钥对
ssh-keygen -f /root/.ssh/id_rsa -N ''

# 查看公钥
cat .ssh/id_rsa.pub

# 将公钥添加到 GitLab 项目
# Settings → Repository → Deploy Keys → Add Deploy Key
```

#### 11.7 克隆项目测试

```bash
# dev 用户克隆 game 项目
git clone git@10.0.0.200:dev/game.git

# 创建新分支
git checkout -b game_v1

# 创建文件并提交
echo "v1" > index.html
git add .
git commit -m "create index"

# 推送到远程
git push origin game_v1
```

#### 11.8 创建合并请求 (Merge Request)

1. 在 GitLab Web 界面进入项目
2. 点击 Merge Requests → New Merge Request
3. 选择源分支和目标分支
4. 填写标题和描述
5. 创建 Merge Request

#### 11.9 合并分支

1. cto 用户登录 GitLab
2. 进入 Merge Requests
3. 审查代码变更
4. 点击 Merge 合并分支

---

### 第 12 章 GitLab 备份与恢复

#### 12.1 配置备份路径

```bash
# 编辑配置文件
vim /etc/gitlab/gitlab.rb

# 添加备份路径
gitlab_rails['backup_path'] = "/var/opt/gitlab/backups"

# 重新生效配置
gitlab-ctl reconfigure

# 创建备份目录
mkdir /backup
```

#### 12.2 执行备份

```bash
# 备份命令
gitlab-rake gitlab:backup:create
```

**备份输出示例：**
```
2020-08-05 07:27:09 +0800 -- Dumping database ...
Dumping PostgreSQL database gitlabhq_production ... [DONE]
2020-08-05 07:27:11 +0800 -- done
2020-08-05 07:27:11 +0800 -- Dumping repositories ...
2020-08-05 07:27:11 +0800 -- done
Creating backup archive: 1596583632_2020_08_05_13.2.2_gitlab_backup.tar ... done
```

#### 12.3 备份配置文件

```bash
# 备份敏感配置文件
cp /etc/gitlab/gitlab-secrets.json /backup/
cp /etc/gitlab/gitlab.rb /backup/

# 查看备份结果
ll /backup/
总用量 220
-rw------- 1 git  git  204800 8 月  5 07:27 1596583632_2020_08_05_13.2.2_gitlab_backup.tar
-rw------- 1 root root   18771 8 月  5 07:30 gitlab-secrets.json
```

⚠️ **重要提示：**
- `gitlab-secrets.json` 包含敏感数据，必须手动备份
- 恢复时需要备份文件和配置文件一起恢复

#### 12.4 恢复数据

```bash
# 1. 停止服务（恢复时最好不要有数据写入）
gitlab-ctl stop

# 2. 复制配置文件
cp /backup/gitlab-secrets.json /etc/gitlab/

# 3. 执行恢复
gitlab-rake gitlab:backup:restore BACKUP=1596583632_2020_08_05_13.2.2

# 4. 重新加载配置
gitlab-ctl reconfigure

# 5. 启动服务
gitlab-ctl start
```

---

## 第三部分：Jenkins 持续集成

### 第 13 章 Jenkins 安装配置

#### 13.1 安装 Jenkins

```bash
# 下载地址
https://mirrors.tuna.tsinghua.edu.cn/jenkins/redhat/

# 安装 JDK
rpm -ivh jdk-8u181-linux-x64.rpm

# 安装 Jenkins
rpm -ivh jenkins-2.176.1-1.1.noarch.rpm
```

#### 13.2 目录文件说明

```bash
rpm -ql jenkins
/etc/init.d/jenkins          # 启动文件
/etc/logrotate.d/jenkins     # 日志切割脚本
/etc/sysconfig/jenkins       # 配置文件
/usr/lib/jenkins             # 安装目录
/usr/lib/jenkins/jenkins.war # 安装包
/var/lib/jenkins             # 数据目录
/var/log/jenkins             # 日志目录
```

#### 13.3 配置使用 root 账户运行

```bash
vim /etc/sysconfig/jenkins
JENKINS_USER="root"
```

#### 13.4 启动 Jenkins

```bash
systemctl start jenkins
```

#### 13.5 解锁 Jenkins

1. 浏览器访问 `http://10.0.0.201:8080`
2. 查看管理员密码：
   ```bash
   cat /var/lib/jenkins/secrets/initialAdminPassword
   ```
3. 输入密码解锁

#### 13.6 配置插件源

**清华源地址：**
```
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
```

**配置步骤：**
1. 系统管理 → 插件管理 → 高级
2. 修改 Update Site 为清华源地址
3. 点击提交

#### 13.7 离线安装插件

```bash
# 解压插件到指定目录
tar zxf jenkins_plugins.tar.gz -C /var/lib/jenkins/

# 查看插件
ll /var/lib/jenkins/plugins/

# 重启 Jenkins
systemctl restart jenkins
```

---

### 第 14 章 Jenkins 项目构建

#### 14.1 创建自由风格项目

1. 登录 Jenkins
2. 点击"新建任务"
3. 输入任务名称，选择"自由风格软件项目"
4. 点击"确定"

#### 14.2 添加构建步骤

1. 进入项目配置
2. 找到"构建"部分
3. 点击"添加构建步骤" → "执行 shell"
4. 输入要执行的命令

#### 14.3 立即构建

1. 点击"立即构建"
2. 查看构建状态
3. 点击构建编号 → 查看控制台输出

---

### 第 15 章 Jenkins 与 GitLab 集成

#### 15.1 GitLab 导入项目

1. GitLab Web 界面 → New Project → Import Project
2. 选择项目来源（GitHub、Gitee 等）
3. 输入项目地址：`https://gitee.com/skips/game.git`
4. 导入项目

#### 15.2 Jenkins 关联 GitLab 项目

1. Jenkins 新建任务
2. 选择"自由风格项目"
3. 源码管理 → Git
4. 填写 Repository URL

#### 15.3 配置 Jenkins 访问 GitLab 权限

**部署公钥方式：**

1. **获取 Jenkins 公钥**
   ```bash
   cat /root/.ssh/id_rsa.pub
   ```

2. **GitLab 添加部署公钥**
   - Settings → Repository → Deploy Keys
   - 添加公钥，勾选"Allow write access"

3. **项目关联部署公钥**
   - 进入项目 → Settings → Repository
   - 选择已添加的 Deploy Key

4. **Jenkins 配置私钥凭证**
   - 系统管理 → Manage Credentials
   - 添加 SSH Username with private key

#### 15.4 编写部署脚本

```bash
# 创建目录
mkdir -p /scripts/jenkins/

# 编写脚本
cat > /scripts/jenkins/deploy.sh << 'EOF'
#!/bin/bash
PATH_CODE=/var/lib/jenkins/workspace/h5game/
PATH_WEB=/usr/share/nginx
TIME=$(date +%Y%m%d-%H%M)
IP=10.0.0.7

# 打包代码
cd ${PATH_CODE}
tar zcf /opt/${TIME}-web.tar.gz ./*

# 发送到 web 服务器
ssh ${IP} "mkdir ${PATH_WEB}/${TIME}-web -p"
scp /opt/${TIME}-web.tar.gz ${IP}:${PATH_WEB}/${TIME}-web

# web 服务器解压
ssh ${IP} "cd ${PATH_WEB}/${TIME}-web && tar xf ${TIME}-web.tar.gz && rm -rf ${TIME}-web.tar.gz"
ssh ${IP} "cd ${PATH_WEB} && rm -rf html && ln -s ${TIME}-web html"
EOF

# 添加执行权限
chmod +x /scripts/jenkins/deploy.sh
```

#### 15.5 Jenkins 调用部署脚本

1. 项目配置 → 构建 → 执行 shell
2. 输入命令：`/scripts/jenkins/deploy.sh`
3. 保存并构建

⚠️ **权限问题：**
如果提示权限不足，需要修改 Jenkins 以 root 用户运行：
```bash
vim /etc/sysconfig/jenkins
JENKINS_USER="root"
systemctl restart jenkins
```

#### 15.6 配置 Webhook 自动触发

**Jenkins 端配置：**
1. 项目配置 → 构建触发器
2. 勾选"Build when a change is pushed to GitLab"
3. 生成 token 并保存

**GitLab 端配置：**
1. 项目 → Settings → Integrations
2. URL: `http://10.0.0.201:8080/project/h5game`
3. Secret Token: 填写 Jenkins 生成的 token
4. 勾选 Push events
5. 点击 Add webhook

⚠️ **GitLab 版本问题：**
如果添加 Webhook 报错，需要配置：
- Admin Area → Settings → Network
- 勾选"Allow hooks to make requests to local networks"

#### 15.7 测试 Webhook

1. GitLab Webhook 页面 → Test → Push events
2. 查看状态码（200 表示成功）
3. Jenkins 项目页面会显示触发记录

---

### 第 16 章 Jenkins 参数化构建

#### 16.1 Tag 方式发布版本

**Git 端打标签：**
```bash
# v1.0 版本
git commit -am 'v1.0'
git tag -a v1.0 -m "v1.0 稳定版"
git push -u origin v1.0

# v2.0 版本
git commit -am 'v2.0'
git tag -a v2.0 -m "v2.0 稳定版"
git push -u origin v2.0
```

**Jenkins 配置参数化构建：**
1. 勾选"参数化构建过程"
2. 添加参数 → Git Parameter
3. Parameter Type: Tag
4. Git 仓库配置中版本改为 `$git_version`

#### 16.2 优化部署脚本

```bash
cat >/scripts/jenkins/deploy_rollback.sh<<'EOF'
#!/bin/bash
PATH_CODE=/var/lib/jenkins/workspace/my-deploy-rollback/
PATH_WEB=/usr/share/nginx
IP=10.0.0.7

# 打包代码
cd ${PATH_CODE}
tar zcf /opt/web-${git_version}.tar.gz ./*

# 发送到 web 服务器
ssh ${IP} "mkdir ${PATH_WEB}/web-${git_version} -p"
scp /opt/web-${git_version}.tar.gz ${IP}:${PATH_WEB}/web-${git_version}

# 解压代码
ssh ${IP} "cd ${PATH_WEB}/web-${git_version} && tar xf web-${git_version}.tar.gz && rm -rf web-${git_version}.tar.gz"
ssh ${IP} "cd ${PATH_WEB} && rm -rf html && ln -s web-${git_version} html"
EOF
```

#### 16.3 Tag 方式回滚版本

**添加回滚选项：**
1. 参数化构建 → 选择参数
2. 添加 Choice Parameter
3. Name: `deploy_env`
4. Choices:
   ```
   deploy
   rollback
   ```

**修改部署脚本：**
```bash
cat >/scripts/jenkins/deploy_rollback.sh <<'EOF'
#!/bin/bash
PATH_CODE=/var/lib/jenkins/workspace/my-deploy-rollback/
PATH_WEB=/usr/share/nginx
IP=10.0.0.7

# 函数定义
code_tar(){
    cd ${PATH_CODE}
    tar zcf /opt/web-${git_version}.tar.gz ./*
}

code_scp(){
    ssh ${IP} "mkdir ${PATH_WEB}/web-${git_version} -p"
    scp /opt/web-${git_version}.tar.gz ${IP}:${PATH_WEB}/web-${git_version}
}

code_xf(){
    ssh ${IP} "cd ${PATH_WEB}/web-${git_version} && tar xf web-${git_version}.tar.gz && rm -rf web-${git_version}.tar.gz"
}

code_ln(){
    ssh ${IP} "cd ${PATH_WEB} && rm -rf html && ln -s web-${git_version} html"
}

main(){
    code_tar
    code_scp
    code_xf
    code_ln
}

# 选择发布还是回滚
if [ "${deploy_env}" == "deploy" ]
then
    ssh ${IP} "ls ${PATH_WEB}/web-${git_version}" >/dev/null 2>&1
    if [ $? == 0 -a ${GIT_COMMIT} == ${GIT_PREVIOUS_SUCCESSFUL_COMMIT} ]
    then
        echo "web-${git_version} 已部署，不允许重复构建"
        exit
    else
        main
    fi
elif [ "${deploy_env}" == "rollback" ]
then
    code_ln
fi
EOF
```

**测试回滚：**
1. 选择"Build with Parameters"
2. 选择版本：`v1.0`
3. 选择操作：`rollback`
4. 点击构建

---

## 第四部分：SonarQube 代码质量

### 第 17 章 SonarQube 部署

#### 17.1 安装 MySQL（SonarQube 数据库）

```bash
# 下载 MySQL 5.7
cd /data/soft
wget https://downloads.mysql.com/archives/get/p/23/file/mysql-5.7.28-linux-glibc2.12-x86_64.tar.gz

# 解压
tar zxf mysql-5.7.28-linux-glibc2.12-x86_64.tar.gz -C /opt/
mv /opt/mysql-5.7.28-linux-glibc2.12-x86_64 /opt/mysql-5.7.28
ln -s /opt/mysql-5.7.28 /opt/mysql

# 设置环境变量
echo "export PATH=$PATH:/opt/mysql/bin" >> /etc/profile
source /etc/profile

# 清除遗留环境
rpm -qa | grep mariadb
yum remove mariadb-libs -y
rm -rf /etc/my.cnf

# 安装依赖
yum install -y libaio-devel

# 创建用户
useradd -s /sbin/nologin -M mysql
chown -R mysql.mysql /data/
chown -R mysql.mysql /opt/mysql*

# 初始化数据库
mysqld --initialize-insecure --user=mysql --basedir=/opt/mysql --datadir=/data/mysql_3306/

# 配置文件
cat> /etc/my.cnf <<EOF
[mysqld]
user=mysql
basedir=/opt/mysql
datadir=/data/mysql_3306
socket=/tmp/mysql.sock

[mysql]
socket=/tmp/mysql.sock
EOF

# 启动数据库
cp /opt/mysql/support-files/mysql.server /etc/init.d/mysqld
chkconfig --add mysqld
systemctl start mysqld

# 修改 root 密码
mysqladmin password 123456
```

#### 17.2 安装 SonarQube

```bash
# 安装 Java
yum install java -y

# 解压
unzip sonarqube-7.0.zip -d /opt/
ln -s /opt/sonarqube-7.0/ /opt/sonarqube

# 创建用户
useradd sonar -M -s /sbin/nologin
chown -R sonar.sonar /opt/sonarqube*

# 配置数据库连接
vim /opt/sonarqube/conf/sonar.properties
sonar.jdbc.username=root
sonar.jdbc.password=123456
sonar.jdbc.url=jdbc:mysql://localhost:3306/sonar?useUnicode=true&characterEncoding=utf8&rewriteBatchedStatements=true&useConfigs=maxPerformance&useSSL=false

# 指定启动用户
vim /opt/sonarqube/bin/linux-x86-64/sonar.sh
RUN_AS_USER=sonar

# 创建数据库
mysql -uroot -p123456 -e 'create database sonar default character set utf8;'

# 编写 systemd 启动文件
cat >/usr/lib/systemd/system/sonar.service<<'EOF'
[Unit]
Description=sonar

[Service]
ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop
Type=forking
User=sonar
Group=sonar

[Install]
WantedBy=multi-user.target
EOF

# 启动服务
systemctl daemon-reload
systemctl start sonar.service

# 检查服务
netstat -lntup | grep java
```

#### 17.3 解决启动报错

**问题：max file descriptors 太低**
```
max file descriptors [4096] for elasticsearch process is too low, increase to at least [65536]
max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```

**解决方法：**
```bash
echo "vm.max_map_count=262144" >> /etc/sysctl.conf
echo "root - nofile 65536" >> /etc/security/limits.conf
echo "sonar - nofile 65536" >> /etc/security/limits.conf
sysctl -p
```

#### 17.4 初始化 SonarQube

1. 浏览器访问 `http://10.0.0.203:9000`
2. 登录：admin/admin
3. 生成 Token：
   - 输入项目名称（如：jenkins）
   - 点击 Generate
   - 保存 token（后面会用到）

#### 17.5 安装插件

**在线安装：**
1. Administration → Marketplace
2. 搜索"chinese"
3. 安装中文插件

**离线安装：**
```bash
# 备份原插件目录
mv /opt/sonarqube/extensions/plugins/ /opt/sonarqube/extensions/plugins_bak

# 解压新插件
tar xf sonar_plugins.tar.gz -C /opt/sonarqube/extensions/

# 重启服务
systemctl restart sonar.service
```

#### 17.6 安装 Sonar 客户端

```bash
# 解压客户端
unzip sonar-scanner-cli-4.0.0.1744-linux.zip -d /opt/
cd /opt/
ln -s sonar-scanner-4.0.0.1744-linux sonar-scanner

# 设置环境变量
echo 'export PATH=$PATH:/opt/sonar-scanner/bin' >> /etc/profile
source /etc/profile
```

#### 17.7 推送代码到 SonarQube

```bash
cd /var/lib/jenkins/workspace/h5game/

/opt/sonar-scanner/bin/sonar-scanner \
-Dsonar.projectKey=html \
-Dsonar.sources=. \
-Dsonar.host.url=http://10.0.0.203:9000 \
-Dsonar.login=4f57dfb332463fa8220be49856a0f1d27c88a142
```

**配置文件方式（简化命令）：**
```bash
vim /opt/sonar-scanner/conf/sonar-scanner.properties
sonar.host.url=http://10.0.0.203:9000
sonar.login=be400d585a529e6e2152e6742fe3f5cb3fc803d2
sonar.sourceEncoding=UTF-8

# 简化后的命令
sonar-scanner \
-Dsonar.projectKey=html \
-Dsonar.sources=.
```

⚠️ **Node 环境报错：**
如果提示找不到 node 环境，需要安装：
```bash
cd /opt/
wget https://nodejs.org/dist/v12.13.0/node-v12.13.0-linux-x64.tar.xz
tar xf node-v12.13.0-linux-x64.tar.xz
mv node-v12.13.0-linux-x64 node
echo 'export PATH=$PATH:/opt/node/bin' >> /etc/profile
source /etc/profile
```

---

### 第 18 章 SonarQube 与 Jenkins 集成

#### 18.1 配置 SonarQube 凭证

1. Jenkins → 系统管理 → 系统配置
2. 找到 SonarQube servers
3. 添加 SonarQube 信息：
   - Name: sonar
   - Server URL: `http://10.0.0.203:9000`
   - Server authentication token: 添加 token

#### 18.2 配置 Sonar 客户端

1. 系统管理 → 全局工具配置
2. 找到 SonarQube Scanner
3. 配置客户端路径

#### 18.3 工程配置 Sonar 构建

1. 项目配置 → 构建环境
2. 勾选"Prepare SonarQube Scanner environment"
3. 添加构建步骤 → SonarQube Scanner
4. 填写参数：
   ```
   sonar.projectName=${JOB_NAME}
   sonar.projectKey=html
   sonar.sources=.
   ```

#### 18.4 调整构建顺序

**重要：** 先执行代码扫描，再发布版本

拖动构建步骤调整顺序：
```
1. SonarQube Scanner（代码扫描）
2. Execute shell（部署发布）
```

#### 18.5 测试发布

```bash
# Git 端修改代码
git branch
git pull
vim index.html
git add .
git commit -m "v5.0 稳定版"
git push -u origin master

# 触发 Jenkins 构建
# 查看 SonarQube 扫描结果
```

---

## 📚 学习资源

### 官方文档
- [Git 官方文档](https://git-scm.com/doc)
- [GitLab 文档](https://docs.gitlab.com/)
- [Jenkins 文档](https://www.jenkins.io/doc/)
- [SonarQube 文档](https://docs.sonarqube.org/)

### 镜像源
- 清华大学开源软件镜像站：https://mirrors.tuna.tsinghua.edu.cn/
- GitLab CE YUM 源：https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/
- Jenkins RPM 源：https://mirrors.tuna.tsinghua.edu.cn/jenkins/redhat/

---

## 🎯 实战练习

### 练习 1：搭建完整的 CI/CD 环境
1. 安装 GitLab（10.0.0.200）
2. 安装 Jenkins（10.0.0.201）
3. 安装 SonarQube（10.0.0.203）
4. 配置 Webhook 自动触发
5. 实现代码提交→自动扫描→自动部署

### 练习 2：权限管理实验
1. 创建 dev 和 ops 两个组
2. 创建对应的用户
3. 配置不同的访问权限
4. 测试权限控制

### 练习 3：版本发布与回滚
1. 使用 Tag 方式发布 v1.0、v2.0、v3.0
2. 测试回滚到指定版本
3. 实现一键发布和回滚

---

## 📝 总结

本教程涵盖了从 Git 基础到企业级 CI/CD 流水线的完整内容：

✅ **Git 基础** - 版本控制核心技能  
✅ **GitLab** - 企业级代码管理平台  
✅ **Jenkins** - 持续集成/持续部署  
✅ **SonarQube** - 代码质量管理  

掌握这些工具，你将能够搭建完整的企业级 DevOps 流水线！

---

**教程版本**: v2.1 (CI/CD 实战版)  
**更新时间**: 2026-03-21  
**仓库地址**: https://github.com/hjs2015/git-tutorial

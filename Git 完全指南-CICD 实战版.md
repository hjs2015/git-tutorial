# Git 完全指南 - CI/CD 实战版

> 📘 **从 Git 基础到企业级 CI/CD 流水线的完整教程**  
> 📌 建议先学习 [Git 完全指南.md](./Git 完全指南.md) 掌握基础知识

---

## 📖 目录

### 第一部分：Git 基础（简要回顾）
1. [软件开发生命周期](#第 1 章-软件开发生命周期)
2. [环境对比与部署痛点](#第 2 章-环境对比与部署痛点)

### 第二部分：GitLab 企业级代码管理
3. [GitLab 安装部署](#第 3 章-gitlab 安装部署)
4. [GitLab 权限管理](#第 4 章-gitlab 权限管理)
5. [GitLab 备份与恢复](#第 5 章-gitlab 备份与恢复)

### 第三部分：Jenkins 持续集成
6. [Jenkins 安装配置](#第 6 章-jenkins 安装配置)
7. [Jenkins 与 GitLab 集成](#第 7 章-jenkins 与-gitlab 集成)
8. [Jenkins 参数化构建](#第 8 章-jenkins 参数化构建)

### 第四部分：SonarQube 代码质量
9. [SonarQube 部署](#第 9 章-sonarqube 部署)
10. [SonarQube 与 Jenkins 集成](#第 10 章-sonarqube 与-jenkins 集成)

---

## 第一部分：Git 基础（简要回顾）

> 📌 **说明**：这部分内容已在 [Git 完全指南.md](./Git 完全指南.md) 中详细讲解，本节只做简要回顾，重点讲解 CI/CD 相关内容。

---

### 第 1 章 软件开发生命周期

#### 1.1 完整开发流程

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

#### 1.2 四种环境详解

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

### 第 2 章 环境对比与部署痛点

#### 2.1 手动部署的 5 大问题

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

#### 2.2 自动部署的 3 大优势

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

#### 2.3 CI/CD 流水线架构图

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

## 第二部分：GitLab 企业级代码管理

### 第 3 章 GitLab 安装部署

#### 3.1 环境准备

**服务器清单**：

| 主机名 | IP 地址 | 服务 | 内存 | 用途 |
|:---|:---|:---|:---:|:---|
| gitlab | 10.0.0.200 | GitLab | 2G | 代码仓库 |
| jenkins | 10.0.0.201 | Jenkins | 1G | 持续集成 |
| nexus | 10.0.0.202 | Nexus | 2G | 制品库 |
| sonar | 10.0.0.203 | SonarQube | 2G | 代码质量 |
| web | 10.0.0.7 | Nginx | 1G | Web 服务器 |

**网络拓扑图**：
```
                    ┌─────────────┐
                    │   10.0.0.7  │
                    │  Web Server │
                    │   (Nginx)   │
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
┌────────┴────────┐ ┌──────┴──────┐ ┌───────┴────────┐
│  10.0.0.200     │ │ 10.0.0.201  │ │  10.0.0.203    │
│  GitLab Server  │ │  Jenkins    │ │  SonarQube     │
│  (代码仓库)      │ │  (CI/CD)    │ │  (代码质量)     │
└─────────────────┘ └─────────────┘ └────────────────┘
```

#### 3.2 安装 GitLab（方法 1：直接下载 RPM 包）

> **推荐方法**：适合网络环境较好，直接下载指定版本

**步骤 1**：下载 RPM 包
```bash
# 清华镜像源地址
https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/

# 下载指定版本
wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-12.0.3-ce.0.el7.x86_64.rpm
```

**步骤 2**：安装 GitLab
```bash
# 本地安装
yum localinstall gitlab-ce-12.0.3-ce.0.el7.x86_64.rpm -y
```

**输出示例**：
```bash
[root@gitlab ~]# yum localinstall gitlab-ce-12.0.3-ce.0.el7.x86_64.rpm -y
已加载插件：fastestmirror
正在检查 gitlab-ce-12.0.3-ce.0.el7.x86_64.rpm
依赖关系解决。

================================================================================
 软件包                 架构    版本                  仓库
================================================================================
正在安装:
 gitlab-ce              x86_64  12.0.3-ce.0.el7       @commandline

事务概要
================================================================================
安装  1 软件包

总计：1.2 GB
安装完成！
```

#### 3.3 安装 GitLab（方法 2：配置 YUM 源）

> **推荐方法**：适合需要批量安装或频繁更新的场景

**步骤 1**：配置 YUM 源
```bash
cat > /etc/yum.repos.d/gitlab-ce.repo << 'EOF'
[gitlab-ce]
name=Gitlab CE Repository
baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el$releasever/
gpgcheck=0
enabled=1
EOF
```

**步骤 2**：安装 GitLab
```bash
yum -y install gitlab-ce
```

#### 3.4 配置 GitLab

**步骤 1**：修改配置文件
```bash
vim /etc/gitlab/gitlab.rb
```

**步骤 2**：修改 external_url
```ruby
# 找到这一行（大约在第 51 行）
external_url 'http://10.0.0.200'

# 说明：
# - 修改为本机 IP 地址
# - 使用 http 协议（首次配置）
# - 不要使用 localhost 或 127.0.0.1
```

**步骤 3**：重新加载配置
```bash
gitlab-ctl reconfigure
```

**输出示例**：
```bash
[root@gitlab ~]# gitlab-ctl reconfigure
Starting Chef Client, version 14.14.29
resolving cookbooks for run list: ["gitlab"]
Synchronizing cookbooks: (0.000s)
Compiling cookbooks ...
Converging 470 resources

# ⏰ 注意：这一步耗时较长（5-10 分钟），请耐心等待！
# 期间会安装依赖、创建数据库、配置服务等

Recipe: gitlab::gitlab-rails
  * execute[gitlab-ctl stop runsvdir] action run (skipped)
  * link[/opt/gitlab/service/gitlab-rails] action create (skipped)
  
# 最后显示：
* execute[gitlab-ctl reconfigure] action run
  - execute ["./bin/gitlab-ctl", "reconfigure"]
  
Chef Client finished, 150/900 resources updated in 05 minutes 32 seconds
GitLab Reconfigured!
```

⚠️ **注意事项**：
- 此步骤耗时较长（5-10 分钟），请耐心等待
- 确保服务器内存充足（至少 2G）
- 如果配置失败，查看日志：`gitlab-ctl tail`

#### 3.5 Web 页面访问

**步骤 1**：浏览器访问
```
http://10.0.0.200
```

**步骤 2**：首次登录设置密码
```
初次登陆 GitLab 需要设置密码：
- 密码长度不低于 8 位
- 建议使用强密码（大小写 + 数字 + 特殊字符）
- 示例：GitLab@2026
```

**步骤 3**：登录系统
```
用户名：root
密码：刚才设置的密码
```

**登录后的界面**：
```
┌─────────────────────────────────────────────┐
│  GitLab                        [用户] [设置] │
├─────────────────────────────────────────────┤
│  Dashboard                                  │
│  Projects                                   │
│  Groups                                     │
│  ...                                        │
│                                             │
│  Welcome to GitLab Community Edition!       │
│                                             │
│  [创建项目] [导入项目]                       │
└─────────────────────────────────────────────┘
```

#### 3.6 GitLab 常用命令

**查看服务状态**
```bash
# 查看所有服务状态
gitlab-ctl status

# 输出示例：
run: alertmanager: (pid 1234) 10s
run: gitaly: (pid 1235) 10s
run: gitlab-monitor: (pid 1236) 10s
run: gitlab-workhorse: (pid 1237) 10s
run: logrotate: (pid 1238) 10s
run: nginx: (pid 1239) 10s
run: node-exporter: (pid 1240) 10s
run: postgresql: (pid 1241) 10s
run: prometheus: (pid 1242) 10s
run: redis: (pid 1243) 10s
run: sidekiq: (pid 1244) 10s
run: unicorn: (pid 1245) 10s
```

**启动/停止服务**
```bash
# 启动所有服务
gitlab-ctl start

# 停止所有服务
gitlab-ctl stop

# 重启所有服务
gitlab-ctl restart
```

**管理单个服务**
```bash
# 停止 Nginx
gitlab-ctl stop nginx

# 启动 Nginx
gitlab-ctl start nginx

# 重启 PostgreSQL
gitlab-ctl restart postgresql
```

**查看服务日志**
```bash
# 查看所有服务日志
gitlab-ctl tail

# 查看特定服务日志
gitlab-ctl tail nginx
gitlab-ctl tail unicorn
gitlab-ctl tail sidekiq
```

---

### 第 4 章 GitLab 权限管理

#### 4.1 用户 - 项目组 - 项目关系

> **核心概念**：理解三者的关系是权限管理的基础

**关系说明**：
```
┌─────────────┐
│   用户组    │  ← 用户的集合（如：dev、ops）
│  (Group)    │
└──────┬──────┘
       │ 包含
       ↓
┌─────────────┐
│   项目      │  ← 代码仓库（如：game、ansible）
│  (Project)  │
└──────┬──────┘
       │ 属于
       ↓
┌─────────────┐
│   用户      │  ← 具体的人（如：zhangsan、lisi）
│  (User)     │
└─────────────┘
```

**权限级别**：
| 级别 | 名称 | 权限说明 |
|:---:|:---|:---|
| 👻 | Guest | 创建 Issue、发表评论 |
| 👤 | Reporter | 查看代码、下载项目 |
| 👨‍💻 | Developer | 推送代码、创建分支 |
| 🔧 | Maintainer | 管理项目、合并请求 |
| 👑 | Owner | 删除项目、管理成员 |

#### 4.2 权限实验需求

**场景**：某公司有开发部和运维部，需要配置不同的访问权限

**创建 2 个组**：
```
dev   - 开发组（负责软件开发）
ops   - 运维组（负责服务器运维）
```

**创建 2 个项目**：
```
game     - 游戏项目（属于 dev 组）
ansible  - 运维脚本（属于 ops 组）
```

**创建 3 个用户**：
```
cto        - CTO（技术总监），对所有项目有管理权限
oldya_dev  - 开发人员，对 dev 组有所有权限
oldya_ops  - 运维人员，对 ops 组有所有权限，对 dev 组只有查看权限
```

**权限分配表**：
| 用户 | dev 组 | ops 组 | game 项目 | ansible 项目 |
|:---|:---:|:---:|:---:|:---:|
| **cto** | Owner | Owner | Maintainer | Maintainer |
| **oldya_dev** | Developer | - | Developer | 无权限 |
| **oldya_ops** | Reporter | Developer | Reporter | Developer |

#### 4.3 创建组和项目

**步骤 1**：创建 dev 组
```
1. 登录 GitLab Web 界面
2. 点击左上角菜单 → Groups
3. 点击 "New group"
4. 填写信息：
   - Group name: dev
   - Group slug: dev（自动生成）
   - Visibility: Private
5. 点击 "Create group"
```

**步骤 2**：创建 ops 组
```
重复上述步骤，创建 ops 组
```

**步骤 3**：在 dev 组下创建 game 项目
```
1. 进入 dev 组页面
2. 点击 "New project"
3. 选择 "Create blank project"
4. 填写信息：
   - Project name: game
   - Visibility: Private
5. 点击 "Create project"
```

**步骤 4**：在 ops 组下创建 ansible 项目
```
重复上述步骤，在 ops 组下创建 ansible 项目
```

#### 4.4 创建用户

**步骤 1**：创建 cto 用户
```
1. 点击 Admin Area（管理员区域）
2. 点击 Users → New user
3. 填写信息：
   - Name: CTO
   - Username: cto
   - Email: cto@example.com
   - Password: Cto@2026（强密码）
   - Password confirmation: Cto@2026
   - Skip confirmation: ✓ 勾选
4. 点击 "Create user"
```

**步骤 2**：创建 oldya_dev 用户
```
重复上述步骤：
- Name: Oldya Dev
- Username: oldya_dev
- Email: dev@example.com
- Password: Dev@2026
```

**步骤 3**：创建 oldya_ops 用户
```
重复上述步骤：
- Name: Oldya Ops
- Username: oldya_ops
- Email: ops@example.com
- Password: Ops@2026
```

#### 4.5 授权用户到组

**步骤 1**：dev 组添加用户
```
1. 进入 dev 组页面
2. 点击 Members（成员）
3. 添加 cto：
   - 选择用户：cto
   - 选择角色：Owner
   - 点击 "Add to group"
4. 添加 oldya_dev：
   - 选择用户：oldya_dev
   - 选择角色：Developer
   - 点击 "Add to group"
5. 添加 oldya_ops：
   - 选择用户：oldya_ops
   - 选择角色：Reporter
   - 点击 "Add to group"
```

**步骤 2**：ops 组添加用户
```
1. 进入 ops 组页面
2. 点击 Members
3. 添加 cto：
   - 选择角色：Owner
4. 添加 oldya_ops：
   - 选择角色：Developer
```

#### 4.6 SSH 公钥配置

> **为什么需要 SSH 公钥？**
> 
> Git 操作（克隆、推送）需要身份验证。使用 SSH 公钥可以：
> - ✅ 免密码登录
> - ✅ 更安全（相比密码）
> - ✅ 方便脚本自动化

**步骤 1**：生成 SSH 密钥对
```bash
# 在开发机上执行
ssh-keygen -f /root/.ssh/id_rsa -N ''
```

**输出示例**：
```bash
[root@web-7 ~]# ssh-keygen -f /root/.ssh/id_rsa -N ''
Generating public/private rsa key pair.
Created directory '/root/.ssh'.
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:FD6YcWj3q66GnZZX7Qa36YpguJn7g70H3sJQu9Y7OcM root@web-7
The key's randomart image is:
+---[RSA 2048]----+
|       ..o.      |
|      . +.o      |
|     . =.+       |
|      +.*.       |
|     . =S.       |
|      o +        |
|       .         |
|                 |
|                 |
+----[SHA256]-----+
```

**步骤 2**：查看公钥
```bash
cat /root/.ssh/id_rsa.pub
```

**输出示例**：
```bash
[root@web-7 ~]# cat .ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDZS9kTGlim0k8zhCSPWp/gsg7ll5ymn91bS7ADuTp4B+5fkt3Tyo+TdgUKD786mkyNH9bJK3W3rwN5SviQJCOKemPVCJCzmewbdubweeZ/ZfXQFZ/iOvB6uiWD1THbfEG8OUxT7OVQiVffwhyXdtGnifcpu/hNWmDWDArFXlR7fvT84QpIOvWC8TKpHM//6EsQgPv4lfM1oLOXNEcoW7DGmQhuWkhiYBzjiYxfRfZo6H5G0WNMwx1piC9MnLbbIBxRp201gtPJZjykSe8le2wJiUU0i6DAObjSo2Nfshwjdc020qaCKFG/1sH9GsUzLBJ3l44Tuj6HdPH/0poejCxP root@web-7
```

**步骤 3**：添加公钥到 GitLab
```
1. 登录 GitLab
2. 点击右上角头像 → Settings
3. 点击 SSH Keys
4. 粘贴公钥内容到 "Key" 框
5. 填写标题（可选）：web-7-server
6. 点击 "Add key"
```

#### 4.7 克隆项目测试

**步骤 1**：克隆 game 项目
```bash
# 复制项目 SSH 地址
# git@10.0.0.200:dev/game.git

# 执行克隆
git clone git@10.0.0.200:dev/game.git
```

**输出示例**：
```bash
[root@web-7 ~]# git clone git@10.0.0.200:dev/game.git
正克隆到 'game'...
The authenticity of host '10.0.0.200 (10.0.0.200)' can't be established.
ECDSA key fingerprint is SHA256:FD6YcWj3q66GnZZX7Qa36YpguJn7g70H3sJQu9Y7OcM.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.0.0.200' (ECDSA) to the list of known hosts.
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
接收对象中：100% (3/3), done.
```

**步骤 2**：查看克隆结果
```bash
ls -la game/
```

**输出示例**：
```bash
[root@web-7 ~]# ll game/
总用量 4
-rw-r--r-- 1 root root 8 8 月  5 20:54 README.md
```

#### 4.8 创建分支并提交

**步骤 1**：创建新分支
```bash
cd game/
git checkout -b game_v1
```

**输出示例**：
```bash
[root@web-7 ~/game]# git checkout -b game_v1
切换到一个新分支 'game_v1'
```

**步骤 2**：创建文件并提交
```bash
# 创建首页文件
echo "v1" > index.html

# 添加到暂存区
git add .

# 提交到本地仓库
git commit -m "create index"
```

**输出示例**：
```bash
[root@web-7 ~/game]# echo "v1" > index.html
[root@web-7 ~/game]# git add .
[root@web-7 ~/game]# git commit -m "create index"
[game_v1 0febf4c] create index
1 file changed, 1 insertion(+)
create mode 100644 index.html
```

**步骤 3**：推送到远程
```bash
git push origin game_v1
```

**输出示例**：
```bash
[root@web-7 ~/game]# git push origin game_v1
Counting objects: 4, done.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 271 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for game_v1, visit:
remote: http://10.0.0.200/dev/game/merge_requests/new?merge_request%5Bsource_branch%5D=game_v1
remote: 
To git@10.0.0.200:dev/game.git
 * [new branch]      game_v1 -> game_v1
```

#### 4.9 创建合并请求 (Merge Request)

> **什么是 Merge Request？**
> 
> Merge Request（合并请求）是 GitLab 的核心功能，用于：
> - ✅ 代码审查（Code Review）
> - ✅ 讨论修改内容
> - ✅ 自动化测试
> - ✅ 批准后才能合并

**步骤**：
```
1. 在 GitLab Web 界面进入 game 项目
2. 点击 Merge requests → New merge request
3. 选择分支：
   - Source branch: game_v1
   - Target branch: master
4. 填写标题：Create index.html
5. 填写描述（可选）：添加首页文件
6. 点击 "Create merge request"
```

**Merge Request 界面**：
```
┌─────────────────────────────────────────────┐
│ Create index.html                    [合并] │
├─────────────────────────────────────────────┤
│ 游戏项目 - 添加首页文件                      │
│                                             │
│ 变更内容：                                   │
│ + index.html                                │
│   第一行内容：v1                            │
│                                             │
│ 参与者：cto, oldya_dev                      │
│                                             │
│ [评论] [批准] [合并]                         │
└─────────────────────────────────────────────┘
```

#### 4.10 合并分支

**步骤**：
```
1. cto 用户登录 GitLab
2. 进入 Merge requests 页面
3. 点击刚才创建的合并请求
4. 审查代码变更
5. 点击 "Merge" 按钮
6. 确认合并
```

**合并后的提交历史**：
```bash
* 921d88e (HEAD -> master) Merge branch 'game_v1'
| * 0febf4c (game_v1) create index
|/
* 6f9e2f0 initial commit
```

---

### 第 5 章 GitLab 备份与恢复

#### 5.1 为什么需要备份？

> **重要提示**：
> 
> 数据无价！备份是运维的基本职责。
> 
> **需要备份的内容**：
> - ✅ 代码仓库数据
> - ✅ 数据库（用户、项目、Issue 等）
> - ✅ 配置文件（gitlab.rb、gitlab-secrets.json）
> - ✅ 上传的文件（头像、附件等）

#### 5.2 配置备份路径

**步骤 1**：编辑配置文件
```bash
vim /etc/gitlab/gitlab.rb
```

**步骤 2**：添加备份路径
```ruby
# 在文件末尾添加
gitlab_rails['backup_path'] = "/var/opt/gitlab/backups"

# 可选：设置备份保留时间（默认永久）
gitlab_rails['backup_keep_time'] = 604800  # 7 天（秒）
```

**步骤 3**：重新加载配置
```bash
gitlab-ctl reconfigure
```

**步骤 4**：创建备份目录
```bash
mkdir -p /var/opt/gitlab/backups
chown git.git /var/opt/gitlab/backups
```

#### 5.3 执行备份

**备份命令**：
```bash
gitlab-rake gitlab:backup:create
```

**输出示例**：
```bash
[root@gitlab-200 ~]# gitlab-rake gitlab:backup:create
2020-08-05 07:27:09 +0800 -- Dumping database ...
Dumping PostgreSQL database gitlabhq_production ... [DONE]
2020-08-05 07:27:11 +0800 -- done
2020-08-05 07:27:11 +0800 -- Dumping repositories ...
2020-08-05 07:27:11 +0800 -- done
2020-08-05 07:27:11 +0800 -- Dumping uploads ...
2020-08-05 07:27:11 +0800 -- done
2020-08-05 07:27:11 +0800 -- Dumping builds ...
2020-08-05 07:27:11 +0800 -- done
2020-08-05 07:27:11 +0800 -- Dumping artifacts ...
2020-08-05 07:27:11 +0800 -- done
2020-08-05 07:27:11 +0800 -- Dumping pages ...
2020-08-05 07:27:11 +0800 -- done
2020-08-05 07:27:11 +0800 -- Dumping lfs objects ...
2020-08-05 07:27:12 +0800 -- done
2020-08-05 07:27:12 +0800 -- Dumping container registry images ...
2020-08-05 07:27:12 +0800 -- [DISABLED]
Creating backup archive: 1596583632_2020_08_05_13.2.2_gitlab_backup.tar ... done
Uploading backup archive to remote storage ... skipped
Deleting tmp directories ... done
done
done
done
done
done
done
done
done
done
Deleting old backups ... skipping
```

⚠️ **重要警告**：
```
Warning: Your gitlab.rb and gitlab-secrets.json files contain sensitive data
and are not included in this backup. You will need these files to restore a backup.
Please back them up manually.

翻译：
警告：gitlab.rb 和 gitlab-secrets.json 文件包含敏感数据，
不会包含在备份中。恢复备份时需要这些文件。
请手动备份它们！
```

#### 5.4 备份配置文件

```bash
# 备份 gitlab-secrets.json（包含密钥）
cp /etc/gitlab/gitlab-secrets.json /backup/

# 备份 gitlab.rb（包含配置）
cp /etc/gitlab/gitlab.rb /backup/

# 查看备份结果
ll /backup/
```

**输出示例**：
```bash
[root@gitlab-200 ~]# ll /backup/
总用量 220
-rw------- 1 git  git  204800 8 月  5 07:27 1596583632_2020_08_05_13.2.2_gitlab_backup.tar
-rw------- 1 root root   18771 8 月  5 07:30 gitlab-secrets.json
-rw------- 1 root root    8542 8 月  5 07:30 gitlab.rb
```

**备份文件说明**：
| 文件 | 大小 | 说明 |
|:---|:---:|:---|
| `1596583632_..._gitlab_backup.tar` | 200KB | 数据备份（数据库 + 代码） |
| `gitlab-secrets.json` | 18KB | 密钥文件（必须备份） |
| `gitlab.rb` | 8KB | 配置文件（建议备份） |

#### 5.5 恢复数据

> **恢复场景**：
> - 服务器故障需要重建
> - 数据误删除
> - 系统升级失败

**步骤 1**：停止服务
```bash
# 恢复时最好不要有数据写入
gitlab-ctl stop
```

**步骤 2**：复制配置文件
```bash
# 恢复密钥文件
cp /backup/gitlab-secrets.json /etc/gitlab/

# 恢复配置文件
cp /backup/gitlab.rb /etc/gitlab/
```

**步骤 3**：执行恢复
```bash
# BACKUP= 后面填写备份文件的时间戳部分
gitlab-rake gitlab:backup:restore BACKUP=1596583632_2020_08_05_13.2.2
```

**输出示例**：
```bash
[root@gitlab-200 ~]# gitlab-rake gitlab:backup:restore BACKUP=1596583632_2020_08_05_13.2.2

Unpacking backup tar file /var/opt/gitlab/backups/1596583632_2020_08_05_13.2.2_gitlab_backup.tar ... done
Restoring database ...
Restoring PostgreSQL database gitlabhq_production ... done
Restoring repositories ...
done
Restoring uploads ...
done
```

**步骤 4**：重新加载配置
```bash
gitlab-ctl reconfigure
```

**步骤 5**：启动服务
```bash
gitlab-ctl start
```

**步骤 6**：验证恢复
```bash
# 检查服务状态
gitlab-ctl status

# 访问 Web 界面
# http://10.0.0.200

# 检查数据是否完整
- 项目是否存在
- 用户是否可以登录
- 代码是否可以访问
```

#### 5.6 定时备份（可选）

**配置 crontab 定时备份**：
```bash
# 编辑 crontab
crontab -e

# 添加每天凌晨 2 点备份
0 2 * * * /opt/gitlab/bin/gitlab-rake gitlab:backup:create CRON=1
```

**说明**：
- `CRON=1`：抑制部分输出，适合定时任务
- 备份文件会保存在配置的备份路径
- 建议配合日志记录

---

## 第三部分：Jenkins 持续集成

### 第 6 章 Jenkins 安装配置

#### 6.1 安装 Jenkins

**步骤 1**：安装 JDK
```bash
# Jenkins 需要 Java 环境
rpm -ivh jdk-8u181-linux-x64.rpm
```

**步骤 2**：安装 Jenkins
```bash
# 下载 Jenkins RPM 包
# 清华源：https://mirrors.tuna.tsinghua.edu.cn/jenkins/redhat/

# 安装
rpm -ivh jenkins-2.176.1-1.1.noarch.rpm
```

#### 6.2 目录文件说明

```bash
rpm -ql jenkins | head -20
```

**输出示例**：
```bash
[root@jenkins ~]# rpm -ql jenkins
/etc/init.d/jenkins          # 启动脚本（SysV）
/etc/logrotate.d/jenkins     # 日志切割配置
/etc/sysconfig/jenkins       # 主配置文件
/usr/lib/jenkins             # 安装目录
/usr/lib/jenkins/jenkins.war # Jenkins 主程序
/var/lib/jenkins             # 数据目录（重要！）
/var/log/jenkins             # 日志目录
```

**重要目录说明**：
| 目录 | 说明 | 备份建议 |
|:---|:---|:---:|
| `/var/lib/jenkins` | 工作空间、插件、配置 | ✅ 必须备份 |
| `/var/log/jenkins` | 日志文件 | ⚠️ 可选备份 |
| `/etc/sysconfig/jenkins` | 配置文件 | ✅ 必须备份 |

#### 6.3 配置使用 root 账户运行

> **为什么需要 root？**
> 
> 默认情况下，Jenkins 以 `jenkins` 用户运行，权限受限。
> 某些操作（如 SSH 连接、部署脚本）需要 root 权限。

**步骤 1**：编辑配置文件
```bash
vim /etc/sysconfig/jenkins
```

**步骤 2**：修改用户
```bash
# 找到这一行
JENKINS_USER="jenkins"

# 修改为
JENKINS_USER="root"
```

**步骤 3**：重启 Jenkins
```bash
systemctl restart jenkins
```

#### 6.4 启动 Jenkins

```bash
# 启动服务
systemctl start jenkins

# 设置开机自启
systemctl enable jenkins

# 查看状态
systemctl status jenkins
```

**输出示例**：
```bash
[root@jenkins ~]# systemctl status jenkins
● jenkins.service - Jenkins Continuous Integration Server
   Loaded: loaded (/usr/lib/systemd/system/jenkins.service; enabled)
   Active: active (running) since Thu 2026-03-21 10:00:00 CST
   Main PID: 1234 (java)
   Status: "Running"
```

#### 6.5 解锁 Jenkins

**步骤 1**：浏览器访问
```
http://10.0.0.201:8080
```

**步骤 2**：获取管理员密码
```bash
cat /var/lib/jenkins/secrets/initialAdminPassword
```

**输出示例**：
```bash
[root@jenkins ~]# cat /var/lib/jenkins/secrets/initialAdminPassword
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

**步骤 3**：输入密码解锁
```
┌─────────────────────────────────────────────┐
│  Unlock Jenkins                             │
├─────────────────────────────────────────────┤
│  请输入管理员密码：                          │
│  ┌─────────────────────────────────────┐   │
│  │ a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6    │   │
│  └─────────────────────────────────────┘   │
│                                             │
│            [继续]                           │
└─────────────────────────────────────────────┘
```

#### 6.6 配置插件源

**步骤 1**：选择插件安装
```
推荐选择：
✓ Install suggested plugins（安装推荐插件）

或者：
○ Select plugins to install（手动选择）
```

**步骤 2**：配置清华源（如果默认源太慢）
```
1. 系统管理 → 插件管理 → 高级
2. 找到 "Update Site"
3. 修改为：
   https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
4. 点击 "提交"
5. 点击 "检查现在"
```

#### 6.7 创建管理员账户

```
填写信息：
- 用户名：admin
- 密码：Admin@2026（强密码）
- 姓名：Jenkins Admin
- 邮箱：admin@example.com
```

#### 6.8 完成安装

```
实例配置：
- Jenkins URL: http://10.0.0.201:8080
- 点击 "保存并完成"
- 点击 "开始使用 Jenkins"
```

---

### 第 7 章 Jenkins 与 GitLab 集成

#### 7.1 GitLab 导入项目

**步骤 1**：准备项目
```
示例项目：H5 小游戏
项目地址：https://gitee.com/skips/game.git
```

**步骤 2**：导入到 GitLab
```
1. 登录 GitLab
2. 点击 "New project"
3. 选择 "Import project"
4. 选择 "Repo by URL"
5. 填写：
   - Git repository URL: https://gitee.com/skips/game.git
   - Project name: h5game
   - Visibility: Private
6. 点击 "Create project"
```

#### 7.2 配置 Jenkins 访问 GitLab 权限

> **核心问题**：Jenkins 如何从 GitLab 拉取代码？

**解决方案**：使用部署公钥（Deploy Key）

**部署公钥的作用**：
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Jenkins    │ →   │  Deploy Key │ →   │   GitLab    │
│  (私钥)     │     │  (公钥)     │     │  (项目授权)  │
└─────────────┘     └─────────────┘     └─────────────┘

优势：
✅ 不需要创建虚拟用户
✅ 直接在项目中关联公钥
✅ 权限可控（只读/读写）
```

**步骤 1**：获取 Jenkins 公钥
```bash
# 在 Jenkins 服务器上生成 SSH 密钥
ssh-keygen -f /root/.ssh/id_rsa -N ''

# 查看公钥
cat /root/.ssh/id_rsa.pub
```

**输出示例**：
```bash
[root@jenkins-201 ~]# cat .ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCg8+DQFOjR+gl1Xw83CIyGJ50vI4DBeTaMRFdu5+5pT/IMnYq1iS7/lRS6JxXLYvVeNMDUfDxA1sOL70okyA3npjASXgJPGE1FsbpqzWjsN0TAGoZkR1VWuP9Yn0CrH7dA4lhZQfUUVjvqzFBZK8N9iZMzIu6KOiSY/aD4Ol59vbDS4kO0rTG1DYQNnjZzMPNlIiJ+0EVkfuYRwABRFA8fmL+6btqZqhjGY29EHuIfzIMTDTysrtCTGxQn2ql1zwjReGiNXzmFncwvyy92DAuMbnOQiE1YNn72wThy2oWSHsCwKdIvcNHqY2xBvFnkZ9Ltga7PgR33kbJ7Gl8tjiZF root@jenkins-201
```

**步骤 2**：GitLab 添加部署公钥
```
1. 登录 GitLab
2. 进入 h5game 项目
3. Settings → Repository → Deploy Keys
4. 点击 "Add deploy key"
5. 填写：
   - Title: jenkins-deploy-key
   - Key: 粘贴刚才复制的公钥
   - ✓ Grant write access to these keys（勾选，允许推送）
6. 点击 "Add key"
```

**步骤 3**：Jenkins 配置私钥凭证
```
1. 登录 Jenkins
2. 系统管理 → Manage Credentials
3. 点击 "Global credentials (unrestricted)"
4. 点击 "Add credentials"
5. 选择：
   - Kind: SSH Username with private key
   - ID: gitlab-deploy-key
   - Description: GitLab Deploy Key
   - Username: git
   - Private Key:
     ○ Enter directly
     粘贴 /root/.ssh/id_rsa 的内容
6. 点击 "确定"
```

#### 7.3 创建 Jenkins 项目

**步骤 1**：新建任务
```
1. 点击 "新建任务"
2. 输入任务名称：h5game-deploy
3. 选择 "自由风格软件项目"
4. 点击 "确定"
```

**步骤 2**：配置源码管理
```
1. 选择 "Git"
2. Repository URL:
   git@10.0.0.200:dev/h5game.git
3. Credentials:
   选择刚才添加的 "gitlab-deploy-key"
4. Branch Specifier:
   */master
```

**步骤 3**：测试拉取代码
```
1. 点击 "构建" → "立即构建"
2. 查看控制台输出
3. 确认代码已拉取到：
   /var/lib/jenkins/workspace/h5game-deploy/
```

**验证拉取结果**：
```bash
ll /var/lib/jenkins/workspace/h5game-deploy/
```

**输出示例**：
```bash
[root@jenkins-201 ~]# ll /var/lib/jenkins/workspace/h5game-deploy/
总用量 16
drwxr-xr-x 4 jenkins jenkins 47 8 月  6 09:37 game
-rw-r--r-- 1 jenkins jenkins 9349 8 月  6 09:37 LICENSE
-rw-r--r-- 1 jenkins jenkins 937 8 月  6 09:37 README.md
```

#### 7.4 编写部署脚本

**步骤 1**：创建脚本目录
```bash
mkdir -p /scripts/jenkins/
```

**步骤 2**：编写部署脚本
```bash
cat > /scripts/jenkins/deploy.sh << 'EOF'
#!/bin/bash
# ============================================
# 功能：Jenkins 自动部署脚本
# 用途：将 Jenkins 构建的代码部署到 Web 服务器
# 作者：运维团队
# 版本：v1.0
# ============================================

# 定义变量
PATH_CODE=/var/lib/jenkins/workspace/h5game-deploy/
PATH_WEB=/usr/share/nginx
TIME=$(date +%Y%m%d-%H%M)
IP=10.0.0.7

# 步骤 1：打包代码
echo "=== 打包代码 ==="
cd ${PATH_CODE}
tar zcf /opt/${TIME}-web.tar.gz ./*

# 步骤 2：发送到 Web 服务器
echo "=== 发送代码到 ${IP} ==="
ssh ${IP} "mkdir -p ${PATH_WEB}/${TIME}-web"
scp /opt/${TIME}-web.tar.gz ${IP}:${PATH_WEB}/${TIME}-web

# 步骤 3：Web 服务器解压
echo "=== 解压代码 ==="
ssh ${IP} "cd ${PATH_WEB}/${TIME}-web && tar xf ${TIME}-web.tar.gz && rm -rf ${TIME}-web.tar.gz"

# 步骤 4：切换软链接
echo "=== 切换软链接 ==="
ssh ${IP} "cd ${PATH_WEB} && rm -rf html && ln -s ${TIME}-web html"

echo "=== 部署完成 ==="
EOF

# 添加执行权限
chmod +x /scripts/jenkins/deploy.sh
```

**脚本说明**：
| 步骤 | 操作 | 说明 |
|:---:|:---|:---|
| 1 | 打包代码 | 使用 tar 压缩工作区代码 |
| 2 | 发送代码 | 通过 scp 发送到 Web 服务器 |
| 3 | 解压代码 | 在 Web 服务器解压 |
| 4 | 切换链接 | 更新 html 软链接指向新版本 |

**部署原理图**：
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Jenkins   │ →   │  Web Server │ →   │    用户     │
│  打包代码   │     │  解压部署   │     │  访问网站   │
└─────────────┘     └─────────────┘     └─────────────┘
      ↓                   ↓
  20260321-1013-web.tar.gz
                        ↓
              /usr/share/nginx/
              ├── 20260321-1013-web/  ← 新版本
              ├── 20260321-0915-web/  ← 旧版本
              └── html -> 20260321-1013-web  ← 软链接
```

#### 7.5 Jenkins 调用部署脚本

**步骤 1**：添加构建步骤
```
1. 进入项目配置
2. 找到 "构建" 部分
3. 点击 "添加构建步骤" → "执行 shell"
4. 填写命令：
   /scripts/jenkins/deploy.sh
5. 点击 "保存"
```

**步骤 2**：立即构建
```
1. 点击 "立即构建"
2. 查看控制台输出
```

**步骤 3**：验证部署
```bash
# 在 Web 服务器上查看
ll /usr/share/nginx/
```

**输出示例**：
```bash
[root@web-7 ~]# ll /usr/share/nginx/
总用量 0
drwxr-xr-x 3 root root 50 8 月  6 10:13 20260321-1013-web
lrwxrwxrwx 1 root root 17 8 月  6 10:13 html -> 20260321-1013-web
```

⚠️ **权限问题处理**：

如果构建失败，提示权限不足：
```
Permission denied
```

**解决方法**：
```bash
# 修改 Jenkins 以 root 用户运行
vim /etc/sysconfig/jenkins
JENKINS_USER="root"

# 重启 Jenkins
systemctl restart jenkins
```

#### 7.6 配置 Webhook 自动触发

> **什么是 Webhook？**
> 
> Webhook 是一种回调机制，当 GitLab 发生事件（如代码推送）时，自动通知 Jenkins 触发构建。

**工作流程**：
```
开发人员推送代码
      ↓
  GitLab 仓库
      ↓
  Webhook 触发
      ↓
  Jenkins 构建
      ↓
  自动部署
```

**Jenkins 端配置**：
```
1. 进入项目配置
2. 找到 "构建触发器"
3. 勾选 "Build when a change is pushed to GitLab"
4. 勾选 "GitLab Connection"
5. 点击 "保存"
```

**GitLab 端配置**：
```
1. 进入 h5game 项目
2. Settings → Integrations
3. 填写：
   - URL: http://10.0.0.201:8080/project/h5game-deploy
   - Secret Token: （Jenkins 生成的 token）
4. 勾选：
   ✓ Push events
   ✓ Merge request events
5. 点击 "Add webhook"
```

⚠️ **GitLab 版本问题**：

如果添加 Webhook 报错：
```
URL is blocked: Requests to localhost are not allowed
```

**解决方法**：
```
1. 进入 Admin Area（管理员区域）
2. Settings → Network
3. 勾选：
   ✓ Allow hooks to make requests to local networks
4. 点击 "Save changes"
```

**测试 Webhook**：
```
1. 在 Webhook 页面 → Test
2. 选择 "Push events"
3. 查看状态码：
   - 200：成功
   - 401：认证失败
   - 404：URL 错误
   - 500：服务器错误
```

---

### 第 8 章 Jenkins 参数化构建

#### 8.1 Tag 方式发布版本

> **为什么使用 Tag 发布？**
> 
> 使用 Tag 可以：
> - ✅ 明确版本号（v1.0、v2.0）
> - ✅ 快速回滚到任意版本
> - ✅ 生产环境版本可追溯

**Git 端打标签**：
```bash
# v1.0 版本
git commit -am 'v1.0 版本更新'
git tag -a v1.0 -m "v1.0 稳定版"
git push -u origin v1.0

# v2.0 版本
git commit -am 'v2.0 版本更新'
git tag -a v2.0 -m "v2.0 稳定版"
git push -u origin v2.0

# 查看标签
git tag
```

**输出示例**：
```bash
[root@gitlab h5game]# git tag
v1.0
v2.0
```

**GitLab 查看标签**：
```
1. 进入 h5game 项目
2. 点击 "Tags"
3. 可以看到 v1.0 和 v2.0 两个标签
```

#### 8.2 Jenkins 参数化构建配置

**步骤 1**：新建参数化构建项目
```
1. 点击 "新建任务"
2. 输入任务名称：h5game-deploy-rollback
3. 勾选 "参数化构建过程"
4. 选择 "自由风格软件项目"
5. 点击 "确定"
```

**步骤 2**：添加 Git 参数
```
1. 点击 "添加参数" → "Git Parameter"
2. 填写：
   - Name: git_version
   - Parameter Type: Tag
   - Tag Filter: *（所有标签）
   - Selected Value: FIRST（默认选第一个）
3. 点击 "保存"
```

**步骤 3**：配置源码管理
```
1. 选择 "Git"
2. Repository URL:
   git@10.0.0.200:dev/h5game.git
3. Credentials:
   选择 gitlab-deploy-key
4. Branch Specifier:
   $git_version  ← 使用参数
```

**步骤 4**：添加部署脚本
```
1. 找到 "构建" 部分
2. 点击 "添加构建步骤" → "执行 shell"
3. 填写命令：
   /scripts/jenkins/deploy_rollback.sh
4. 点击 "保存"
```

#### 8.3 优化部署脚本（支持回滚）

```bash
cat >/scripts/jenkins/deploy_rollback.sh<<'EOF'
#!/bin/bash
# ============================================
# 功能：Jenkins 部署和回滚脚本
# 用途：支持版本发布和回滚操作
# 作者：运维团队
# 版本：v2.0
# ============================================

# 定义变量
PATH_CODE=/var/lib/jenkins/workspace/h5game-deploy-rollback/
PATH_WEB=/usr/share/nginx
IP=10.0.0.7

# 函数：打包代码
code_tar(){
    cd ${PATH_CODE}
    tar zcf /opt/web-${git_version}.tar.gz ./*
}

# 函数：发送代码
code_scp(){
    ssh ${IP} "mkdir -p ${PATH_WEB}/web-${git_version}"
    scp /opt/web-${git_version}.tar.gz ${IP}:${PATH_WEB}/web-${git_version}
}

# 函数：解压代码
code_xf(){
    ssh ${IP} "cd ${PATH_WEB}/web-${git_version} && tar xf web-${git_version}.tar.gz && rm -rf web-${git_version}.tar.gz"
}

# 函数：创建软链接
code_ln(){
    ssh ${IP} "cd ${PATH_WEB} && rm -rf html && ln -s web-${git_version} html"
}

# 主函数
main(){
    code_tar
    code_scp
    code_xf
    code_ln
}

# 选择发布还是回滚
if [ "${deploy_env}" == "deploy" ]
then
    # 检查是否已部署
    ssh ${IP} "ls ${PATH_WEB}/web-${git_version}" >/dev/null 2>&1
    if [ $? == 0 -a ${GIT_COMMIT} == ${GIT_PREVIOUS_SUCCESSFUL_COMMIT} ]
    then
        echo "web-${git_version} 已部署，不允许重复构建"
        exit 1
    else
        echo "=== 开始部署 ${git_version} ==="
        main
    fi
elif [ "${deploy_env}" == "rollback" ]
then
    echo "=== 开始回滚到 ${git_version} ==="
    code_ln
fi

echo "=== 操作完成 ==="
EOF

chmod +x /scripts/jenkins/deploy_rollback.sh
```

#### 8.4 添加回滚选项

**步骤**：
```
1. 进入项目配置
2. 勾选 "参数化构建过程"
3. 点击 "添加参数" → "Choice Parameter"
4. 填写：
   - Name: deploy_env
   - Choices:
deploy
rollback
   - Description: 选择部署或回滚
5. 点击 "保存"
```

#### 8.5 测试发布和回滚

**测试 v1.0 发布**：
```
1. 点击 "Build with Parameters"
2. 选择：
   - git_version: v1.0
   - deploy_env: deploy
3. 点击 "构建"
4. 查看控制台输出
```

**测试 v2.0 发布**：
```
重复上述步骤，选择 v2.0
```

**测试回滚到 v1.0**：
```
1. 点击 "Build with Parameters"
2. 选择：
   - git_version: v1.0
   - deploy_env: rollback
3. 点击 "构建"
4. 查看控制台输出
```

**验证结果**：
```bash
# 在 Web 服务器上查看
ll /usr/share/nginx/
```

**输出示例**：
```bash
[root@web-7 ~]# ll /usr/share/nginx/
总用量 0
lrwxrwxrwx 1 root root 8 8 月  6 16:56 html -> web-v1.0  ← 已回滚
drwxr-xr-x 3 root root 68 8 月  6 16:51 web-v1.0
drwxr-xr-x 3 root root 68 8 月  6 16:52 web-v2.0
```

---

## 第四部分：SonarQube 代码质量

### 第 9 章 SonarQube 部署

#### 9.1 安装 MySQL（SonarQube 数据库）

> **为什么需要 MySQL？**
> 
> SonarQube 使用数据库存储：
> - ✅ 代码扫描结果
> - ✅ 用户信息
> - ✅ 项目配置
> - ✅ 历史记录

**步骤 1**：下载 MySQL
```bash
cd /data/soft
wget https://downloads.mysql.com/archives/get/p/23/file/mysql-5.7.28-linux-glibc2.12-x86_64.tar.gz
```

**步骤 2**：解压
```bash
tar zxf mysql-5.7.28-linux-glibc2.12-x86_64.tar.gz -C /opt/
mv /opt/mysql-5.7.28-linux-glibc2.12-x86_64 /opt/mysql-5.7.28
ln -s /opt/mysql-5.7.28 /opt/mysql
```

**步骤 3**：设置环境变量
```bash
echo "export PATH=$PATH:/opt/mysql/bin" >> /etc/profile
source /etc/profile

# 验证
mysql -V
```

**输出示例**：
```bash
[root@sonar ~]# mysql -V
mysql  Ver 14.14 Distrib 5.7.28, for linux-glibc2.12 (x86_64) using  EditLine wrapper
```

**步骤 4**：清除遗留环境
```bash
# 卸载 MariaDB（如果已安装）
rpm -qa | grep mariadb
yum remove mariadb-libs -y

# 删除旧配置
rm -rf /etc/my.cnf
```

**步骤 5**：安装依赖
```bash
yum install -y libaio-devel
```

**步骤 6**：创建用户
```bash
useradd -s /sbin/nologin -M mysql
chown -R mysql.mysql /data/
chown -R mysql.mysql /opt/mysql*
```

**步骤 7**：初始化数据库
```bash
mysqld --initialize-insecure --user=mysql --basedir=/opt/mysql --datadir=/data/mysql_3306/
```

⚠️ **说明**：
- `--initialize-insecure`：初始密码为空
- 首次启动后需要设置密码

**步骤 8**：配置文件
```bash
cat> /etc/my.cnf <<EOF
[mysqld]
user=mysql
basedir=/opt/mysql
datadir=/data/mysql_3306
socket=/tmp/mysql.sock

[mysql]
socket=/tmp/mysql.sock
EOF
```

**步骤 9**：启动数据库
```bash
cp /opt/mysql/support-files/mysql.server /etc/init.d/mysqld
chkconfig --add mysqld
systemctl start mysqld

# 验证
netstat -lntup | grep 3306
```

**输出示例**：
```bash
[root@sonar ~]# netstat -lntup | grep 3306
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      1234/mysqld
```

**步骤 10**：设置密码
```bash
mysqladmin -u root password 123456
```

#### 9.2 安装 SonarQube

**步骤 1**：安装 Java
```bash
yum install java -y
```

**步骤 2**：解压
```bash
unzip sonarqube-7.0.zip -d /opt/
ln -s /opt/sonarqube-7.0/ /opt/sonarqube
```

**步骤 3**：创建用户
```bash
useradd sonar -M -s /sbin/nologin
chown -R sonar.sonar /opt/sonarqube*
```

**步骤 4**：配置数据库连接
```bash
vim /opt/sonarqube/conf/sonar.properties
```

**添加配置**：
```properties
sonar.jdbc.username=root
sonar.jdbc.password=123456
sonar.jdbc.url=jdbc:mysql://localhost:3306/sonar?useUnicode=true&characterEncoding=utf8&rewriteBatchedStatements=true&useConfigs=maxPerformance&useSSL=false
```

**步骤 5**：指定启动用户
```bash
vim /opt/sonarqube/bin/linux-x86-64/sonar.sh
```

**添加配置**：
```bash
RUN_AS_USER=sonar
```

**步骤 6**：创建数据库
```bash
mysql -uroot -p123456 -e 'create database sonar default character set utf8;'
mysql -uroot -p123456 -e 'show databases;'
```

**输出示例**：
```bash
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sonar              |
| test               |
+--------------------+
```

**步骤 7**：编写 systemd 启动文件
```bash
cat >/usr/lib/systemd/system/sonar.service<<'EOF'
[Unit]
Description=SonarQube Service

[Service]
Type=forking
ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop
User=sonar
Group=sonar

[Install]
WantedBy=multi-user.target
EOF
```

**步骤 8**：启动服务
```bash
systemctl daemon-reload
systemctl start sonar.service
```

**步骤 9**：检查服务
```bash
netstat -lntup | grep java
```

**输出示例**：
```bash
[root@sonar ~]# netstat -lntup | grep java
tcp6       0      0 :::9000                 :::*                    LISTEN      18305/java
tcp6       0      0 127.0.0.1:9001          :::*                    LISTEN      18227/java
```

**说明**：
- `9000`：Web 访问端口
- `9001`：Elasticsearch 端口

#### 9.3 解决启动报错

⚠️ **常见问题**：max file descriptors 太低

**错误日志**：
```bash
tail -f /opt/sonarqube/logs/es.log

# 看到：
max file descriptors [4096] for elasticsearch process is too low, increase to at least [65536]
max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```

**解决方法**：
```bash
# 增加文件描述符限制
echo "root - nofile 65536" >> /etc/security/limits.conf
echo "sonar - nofile 65536" >> /etc/security/limits.conf

# 增加虚拟内存限制
echo "vm.max_map_count=262144" >> /etc/sysctl.conf
sysctl -p

# 重启 SonarQube
systemctl restart sonar.service
```

#### 9.4 初始化 SonarQube

**步骤 1**：浏览器访问
```
http://10.0.0.203:9000
```

**步骤 2**：登录
```
用户名：admin
密码：admin
```

**步骤 3**：修改密码
```
首次登录会要求修改密码：
- 原密码：admin
- 新密码：Sonar@2026（强密码）
```

**步骤 4**：生成 Token
```
1. 点击右上角头像 → My Account
2. Security → Generate Tokens
3. 填写：
   - Name: jenkins
   - Type: Project Analysis Token
4. 点击 "Generate"
5. 复制生成的 Token（只显示一次！）
```

**Token 示例**：
```
4f57dfb332463fa8220be49856a0f1d27c88a142
```

⚠️ **重要**：Token 只显示一次，务必保存好！

---

### 第 10 章 SonarQube 与 Jenkins 集成

#### 10.1 安装 Sonar 客户端

**步骤 1**：下载客户端
```bash
cd /opt/
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744-linux.zip
unzip sonar-scanner-cli-4.0.0.1744-linux.zip -d /opt/
ln -s sonar-scanner-4.0.0.1744-linux sonar-scanner
```

**步骤 2**：设置环境变量
```bash
echo 'export PATH=$PATH:/opt/sonar-scanner/bin' >> /etc/profile
source /etc/profile

# 验证
sonar-scanner -v
```

**步骤 3**：配置文件（可选）
```bash
vim /opt/sonar-scanner/conf/sonar-scanner.properties
```

**添加配置**：
```properties
sonar.host.url=http://10.0.0.203:9000
sonar.login=4f57dfb332463fa8220be49856a0f1d27c88a142
sonar.sourceEncoding=UTF-8
```

#### 10.2 推送代码到 SonarQube

**步骤 1**：进入代码目录
```bash
cd /var/lib/jenkins/workspace/h5game-deploy/
```

**步骤 2**：执行扫描
```bash
/opt/sonar-scanner/bin/sonar-scanner \
-Dsonar.projectKey=h5game \
-Dsonar.sources=. \
-Dsonar.host.url=http://10.0.0.203:9000 \
-Dsonar.login=4f57dfb332463fa8220be49856a0f1d27c88a142
```

**输出示例**：
```bash
[root@jenkins h5game]# sonar-scanner \
> -Dsonar.projectKey=h5game \
> -Dsonar.sources=. \
> -Dsonar.host.url=http://10.0.0.203:9000 \
> -Dsonar.login=4f57dfb332463fa8220be49856a0f1d27c88a142

INFO: Scanner configuration file: /opt/sonar-scanner/conf/sonar-scanner.properties
INFO: Project root configuration file: /var/lib/jenkins/workspace/h5game/sonar-project.properties

INFO: Analyzing sources
INFO: ------------------------------------------------------------------------
INFO: EXECUTION SUCCESS
INFO: ------------------------------------------------------------------------
INFO: Total time: 10.123s
INFO: Final Memory: 12M/491M
INFO: ------------------------------------------------------------------------
```

**步骤 3**：查看扫描结果
```
1. 浏览器访问 SonarQube
2. 查看 h5game 项目
3. 查看：
   - Bugs（Bug）
   - Vulnerabilities（漏洞）
   - Code Smells（代码异味）
   - Coverage（覆盖率）
```

#### 10.3 Jenkins 集成 SonarQube

**步骤 1**：安装 SonarQube 插件
```
1. 系统管理 → 插件管理
2. 可选插件 → 搜索 "SonarQube"
3. 勾选 "SonarQube Scanner for Jenkins"
4. 点击 "直接安装"
```

**步骤 2**：配置 SonarQube 服务器
```
1. 系统管理 → 系统配置
2. 找到 "SonarQube servers"
3. 点击 "Add SonarQube"
4. 填写：
   - Name: sonarqube-server
   - Server URL: http://10.0.0.203:9000
   - Server authentication token: 点击 "Add" → "Jenkins"
     粘贴刚才生成的 Token
5. 点击 "保存"
```

**步骤 3**：配置 Sonar 工具
```
1. 系统管理 → 全局工具配置
2. 找到 "SonarQube Scanner"
3. 勾选 "Install automatically"
4. 选择版本（或自动安装）
5. 点击 "保存"
```

#### 10.4 项目配置 Sonar 扫描

**步骤 1**：进入项目配置
```
1. 进入 h5game-deploy 项目
2. 点击 "配置"
```

**步骤 2**：添加构建环境
```
1. 找到 "构建环境"
2. 勾选 "Prepare SonarQube Scanner environment"
```

**步骤 3**：添加构建步骤
```
1. 找到 "构建" 部分
2. 点击 "添加构建步骤"
3. 选择 "SonarQube Scanner"
4. 填写：
   - Project Key: h5game
   - Project Name: ${JOB_NAME}
   - Project Version: ${git_version}
   - Source Encoding: UTF-8
   - Additional properties:
     sonar.sources=.
```

**步骤 4**：调整构建顺序
```
重要！构建顺序应该是：
1. SonarQube Scanner（先扫描）
2. Execute shell（后部署）

拖动调整顺序，然后点击 "保存"
```

#### 10.5 测试完整流程

**步骤 1**：修改代码
```bash
cd /var/lib/jenkins/workspace/h5game/
vim index.html
# 添加一些代码
git add .
git commit -m "v5.0 稳定版"
git tag -a v5.0 -m "v5.0 稳定版"
git push -u origin v5.0
```

**步骤 2**：触发构建
```
1. Jenkins 自动触发（Webhook）
2. 或手动 "Build with Parameters"
```

**步骤 3**：查看结果
```
Jenkins 控制台：
- 查看 SonarQube 扫描结果
- 查看部署日志

SonarQube Web：
- 查看代码质量报告
- 查看 Bug、漏洞、代码异味
```

---

## 📚 学习资源

### 官方文档
- [GitLab 文档](https://docs.gitlab.com/)
- [Jenkins 文档](https://www.jenkins.io/doc/)
- [SonarQube 文档](https://docs.sonarqube.org/)

### 镜像源
- 清华大学开源软件镜像站：https://mirrors.tuna.tsinghua.edu.cn/
- GitLab CE YUM 源：https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/
- Jenkins RPM 源：https://mirrors.tuna.tsinghua.edu.cn/jenkins/redhat/

---

## 🎯 实战练习

### 练习 1：搭建完整 CI/CD 环境
```
目标：在 5 台服务器上搭建完整的 CI/CD 流水线

步骤：
1. 安装 GitLab（10.0.0.200）
2. 安装 Jenkins（10.0.0.201）
3. 安装 SonarQube（10.0.0.203）
4. 配置 Webhook 自动触发
5. 实现：代码提交 → 自动扫描 → 自动部署
```

### 练习 2：权限管理实验
```
目标：掌握 GitLab 权限管理

步骤：
1. 创建 dev 和 ops 两个组
2. 创建 3 个用户（cto、dev、ops）
3. 配置不同的访问权限
4. 测试权限控制
```

### 练习 3：版本发布与回滚
```
目标：掌握参数化构建

步骤：
1. 使用 Tag 方式发布 v1.0、v2.0、v3.0
2. 测试回滚到指定版本
3. 实现一键发布和回滚
```

---

## 📝 总结

本教程涵盖了从 Git 基础到企业级 CI/CD 流水线的完整内容：

✅ **Git 基础** - 版本控制核心技能（回顾）  
✅ **GitLab** - 企业级代码管理平台  
✅ **Jenkins** - 持续集成/持续部署  
✅ **SonarQube** - 代码质量管理  

掌握这些工具，你将能够搭建完整的企业级 DevOps 流水线！

---

**教程版本**: v2.2（优化版）  
**更新时间**: 2026-03-21  
**仓库地址**: https://github.com/hjs2015/git-tutorial  
**前置教程**: [Git 完全指南.md](./Git 完全指南.md)

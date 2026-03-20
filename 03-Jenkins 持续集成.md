# Jenkins 持续集成实战

> 📘 **CI/CD 实战版教程第三部分**  
> 📌 包含：CI/CD 背景知识、Jenkins 安装配置、GitLab 集成、参数化构建  
> 📖 **前置知识**：建议先学习 [01-Git 基础回顾.md](./01-Git 基础回顾.md)

---

## 目录

### 第一部分：CI/CD 背景知识
1. [软件开发生命周期](#第 1 章-软件开发生命周期)
2. [环境对比与部署痛点](#第 2 章-环境对比与部署痛点)

### 第二部分：Jenkins 实战
3. [Jenkins 安装配置](#第 3 章-jenkins 安装配置)
4. [Jenkins 与 GitLab 集成](#第 4 章-jenkins 与-gitlab 集成)
5. [Jenkins 参数化构建](#第 5 章-jenkins 参数化构建)

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

## 第二部分：Jenkins 实战

## 第 3 章 Jenkins 安装配置

### 3.1 安装 Jenkins

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

### 3.2 目录文件说明

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

### 3.3 配置使用 root 账户运行

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

### 3.4 启动 Jenkins

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

### 3.5 解锁 Jenkins

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

### 3.6 配置插件源

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

### 3.7 创建管理员账户

```
填写信息：
- 用户名：admin
- 密码：Admin@2026（强密码）
- 姓名：Jenkins Admin
- 邮箱：admin@example.com
```

### 3.8 完成安装

```
实例配置：
- Jenkins URL: http://10.0.0.201:8080
- 点击 "保存并完成"
- 点击 "开始使用 Jenkins"
```

---

## 第 4 章 Jenkins 与 GitLab 集成

### 4.1 GitLab 导入项目

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

### 4.2 配置 Jenkins 访问 GitLab 权限

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

### 4.3 创建 Jenkins 项目

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

### 4.4 编写部署脚本

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

### 4.5 Jenkins 调用部署脚本

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

### 4.6 配置 Webhook 自动触发

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

## 第 5 章 Jenkins 参数化构建

### 5.1 Tag 方式发布版本

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

### 5.2 Jenkins 参数化构建配置

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

### 5.3 优化部署脚本（支持回滚）

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

### 5.4 添加回滚选项

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

### 5.5 测试发布和回滚

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

## 🎯 实战练习

### 练习 1：安装配置 Jenkins
```bash
# 目标：完成 Jenkins 安装和初始化

步骤：
1. 安装 JDK 和 Jenkins
2. 配置使用 root 用户运行
3. 解锁 Jenkins 并安装插件
4. 创建管理员账户
```

### 练习 2：GitLab 集成
```bash
# 目标：实现 Jenkins 从 GitLab 拉取代码

步骤：
1. 生成 SSH 密钥对
2. GitLab 添加部署公钥
3. Jenkins 配置凭证
4. 创建项目并测试拉取
```

### 练习 3：参数化构建
```bash
# 目标：掌握版本发布和回滚

步骤：
1. 使用 Tag 方式发布 v1.0、v2.0
2. 配置参数化构建
3. 测试部署和回滚操作
```

---

## 📚 相关文档

- **Git 基础回顾** - [01-Git 基础回顾.md](./01-Git 基础回顾.md)
- **GitLab 企业级代码管理** - [02-GitLab 企业级代码管理.md](./02-GitLab 企业级代码管理.md)
- **SonarQube 代码质量** - [04-SonarQube 代码质量.md](./04-SonarQube 代码质量.md)

---

**文档版本**: v2.0  
**提取自**: Git 完全指南-CICD 实战版.md  
**结构调整**: 新增 CI/CD 背景知识作为第一部分（第 1-2 章）  
**更新时间**: 2026-03-21  
**仓库地址**: https://github.com/hjs2015/git-tutorial

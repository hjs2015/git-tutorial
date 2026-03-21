# GitLab 企业级代码管理

> 📘 **CI/CD 实战版教程第二部分**  
> 📌 包含：安装部署、权限管理、CI/CD 配置、备份恢复、高可用架构  
> 🚀 **版本**: GitLab 16.x LTS | **系统**: CentOS 8/9, RHEL 8/9, Ubuntu 20.04+  
> 🔒 **安全**: GPG 校验、HTTPS、2FA、审计日志、分支保护

---

## 目录

- [第 3 章 GitLab 安装部署](#第 3 章-gitlab 安装部署)
  - [3.1 环境准备与硬件要求](#31-环境准备与硬件要求)
  - [3.2 系统优化与依赖安装](#32-系统优化与依赖安装)
  - [3.3 配置官方 YUM 源（含 GPG 校验）](#33-配置官方 yum 源含 gpg 校验)
  - [3.4 安装 GitLab LTS 版本](#34-安装-gitlab-lts-版本)
  - [3.5 配置 external_url 与 HTTPS](#35-配置-external_url-与-https)
  - [3.6 初始化配置与访问](#36-初始化配置与访问)
  - [3.7 Docker 容器化部署方案](#37-docker 容器化部署方案)
  - [3.8 常用命令与故障排查](#38-常用命令与故障排查)
- [第 4 章 GitLab 权限管理](#第 4 章-gitlab 权限管理)
  - [4.1 用户→组→项目权限模型](#41-用户→组→项目权限模型)
  - [4.2 企业级权限设计案例](#42-企业级权限设计案例)
  - [4.3 创建组与项目](#43-创建组与项目)
  - [4.4 创建用户与双因素认证](#44-创建用户与双因素认证)
  - [4.5 SSH 密钥配置（ed25519）](#45-ssh 密钥配置 ed25519)
  - [4.6 分支保护规则](#46-分支保护规则)
  - [4.7 合并请求审批流程](#47-合并请求审批流程)
  - [4.8 代码提交门禁配置](#48-代码提交门禁配置)
  - [4.9 操作审计日志](#49-操作审计日志)
  - [4.10 克隆与推送测试](#410-克隆与推送测试)
- [第 5 章 GitLab CI/CD 实战](#第 5 章-gitlab-cicd 实战)
  - [5.1 CI/CD 核心概念](#51-cicd 核心概念)
  - [5.2 GitLab Runner 部署](#52-gitlab-runner 部署)
  - [5.3 .gitlab-ci.yml 基础配置](#53-gitlab-ci-yml 基础配置)
  - [5.4 构建→测试→部署流水线](#54-构建→测试→部署流水线)
  - [5.5 环境变量与密钥管理](#55-环境变量与密钥管理)
  - [5.6 流水线状态监控](#56-流水线状态监控)
- [第 6 章 GitLab 备份与容灾](#第 6 章-gitlab 备份与容灾)
  - [6.1 备份策略与容灾规范](#61-备份策略与容灾规范)
  - [6.2 配置备份路径与保留策略](#62-配置备份路径与保留策略)
  - [6.3 执行完整备份](#63-执行完整备份)
  - [6.4 备份配置文件与密钥](#64-备份配置文件与密钥)
  - [6.5 异地备份（rsync/S3）](#65-异地备份 rsync-s3)
  - [6.6 备份完整性校验](#66-备份完整性校验)
  - [6.7 数据恢复流程](#67-数据恢复流程)
  - [6.8 定时备份配置](#68-定时备份配置)
- [第 7 章 高可用架构与监控](#第 7 章-高可用架构与监控)
  - [7.1 高可用集群架构设计](#71-高可用集群架构设计)
  - [7.2 主从复制配置](#72-主从复制配置)
  - [7.3 负载均衡配置](#73-负载均衡配置)
  - [7.4 Prometheus 监控对接](#74-prometheus 监控对接)
  - [7.5 高频故障排查手册](#75-高频故障排查手册)

---

## 第 3 章 GitLab 安装部署

### 3.1 环境准备与硬件要求

#### 服务器硬件配置

| 环境 | 内存最低 | 推荐配置 | CPU | 磁盘 | 适用场景 |
|:---:|:---:|:---:|:---:|:---:|:---|
| **开发/测试** | 4GB | 8GB | 2 核 | 50GB | 个人学习、小团队 |
| **生产环境** | 8GB | 16GB+ | 4 核 + | 100GB+ | 企业生产环境 |
| **高可用集群** | 16GB | 32GB+ | 8 核 + | 500GB+ | 大型企业、高并发 |

⚠️ **重要提示**：
```
- GitLab 16.x 最低内存要求 4GB（低于 4GB 可能运行不稳定）
- 生产环境强烈建议 8GB+ 内存，避免 OOM（内存溢出）
- 使用机械硬盘时，建议配置 SSD 作为数据库存储
- 启用 Swap 分区作为内存缓冲（建议 4-8GB）
```

#### 操作系统兼容性

| 系统 | 版本 | 状态 | 备注 |
|:---|:---|:---:|:---|
| **CentOS** | 8/9 | ✅ 推荐 | 企业级首选 |
| **RHEL** | 8/9 | ✅ 推荐 | 红帽企业版 |
| **Ubuntu** | 20.04/22.04 | ✅ 推荐 | LTS 长期支持版 |
| **Debian** | 10/11 | ✅ 支持 | 社区版 |
| **CentOS** | 7 | ⚠️ 兼容 | 已停止维护，建议升级 |

#### 网络拓扑规划

**单节点部署（适合中小团队）**：
```
                    ┌─────────────────┐
                    │   10.0.0.200    │
                    │   GitLab Server │
                    │   (All-in-One)  │
                    │   内存：8GB      │
                    │   CPU: 4 核       │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
      ┌───────┴───────┐ ┌───┴────┐ ┌──────┴──────┐
      │  开发人员     │ │ 运维   │ │  测试人员   │
      │  (SSH/HTTPS)  │ │ 人员   │ │  (Web 界面)  │
      └───────────────┘ └────────┘ └─────────────┘
```

**高可用集群部署（适合大型企业）**：
```
                    ┌─────────────────┐
                    │   负载均衡器    │
                    │  (HAProxy/Nginx)│
                    │   10.0.0.100    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
      ┌───────┴───────┐ ┌───┴────┐ ┌──────┴──────┐
      │  GitLab 节点 1 │ │ 节点 2  │ │  GitLab 节点 3│
      │  10.0.0.201   │ │10.0.0.202│ │ 10.0.0.203 │
      └───────┬───────┘ └───┬────┘ └──────┬──────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                    ┌────────┴────────┐
                    │   PostgreSQL    │
                    │   (主从复制)     │
                    │  10.0.0.210/211 │
                    └─────────────────┘
```

---

### 3.2 系统优化与依赖安装

#### 步骤 1：系统更新与基础依赖

```bash
# CentOS/RHEL 8/9
sudo dnf update -y
sudo dnf install -y curl policycoreutils openssh-server openssh-clients perl postfix

# Ubuntu 20.04/22.04
sudo apt update
sudo apt install -y curl openssh-server ca-certificates perl postfix wget

# 启动并启用 SSH 服务
sudo systemctl enable ssh
sudo systemctl start ssh

# 启动并启用 Postfix（用于发送邮件通知）
sudo systemctl enable postfix
sudo systemctl start postfix
```

#### 步骤 2：配置防火墙

```bash
# CentOS/RHEL (firewalld)
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload

# Ubuntu (ufw)
sudo ufw allow http
sudo ufw allow https
sudo ufw enable

# 验证防火墙规则
sudo firewall-cmd --list-all
# 或
sudo ufw status
```

#### 步骤 3：配置 Swap 分区（内存不足时）

```bash
# 检查当前 Swap
free -h

# 创建 4GB Swap 文件（如果内存<8GB 建议配置）
sudo fallocate -l 4G /swapfile
# 如果 fallocate 不可用，使用 dd：
# sudo dd if=/dev/zero of=/swapfile bs=1M count=4096

# 设置权限
sudo chmod 600 /swapfile

# 格式化为 Swap
sudo mkswap /swapfile

# 启用 Swap
sudo swapon /swapfile

# 验证
free -h

# 永久生效（写入 fstab）
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# 调整 Swap 使用策略（vm.swappiness）
# 值范围 0-100，越低越少使用 Swap（推荐 10）
sudo sysctl vm.swappiness=10
echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf
```

#### 步骤 4：系统内核参数优化

```bash
# 编辑 sysctl.conf
sudo vim /etc/sysctl.conf

# 添加以下优化参数
cat >> /etc/sysctl.conf << 'EOF'

# GitLab 性能优化
vm.swappiness = 10
vm.dirty_ratio = 15
vm.dirty_background_ratio = 5
vm.overcommit_memory = 1
net.core.somaxconn = 4096
net.ipv4.tcp_max_syn_backlog = 4096
EOF

# 应用配置
sudo sysctl -p
```

---

### 3.3 配置官方 YUM 源（含 GPG 校验）

#### 步骤 1：安装 GPG 密钥

```bash
# CentOS/RHEL 8/9
sudo rpm --import https://packages.gitlab.com/gpg/gitlab/gitlab-ce/gpgkey
sudo rpm --import https://packages.gitlab.com/gpg/gitlab/gitlab-ee/gpgkey

# 验证 GPG 密钥已导入
rpm -qa gpg-pubkey | grep gitlab

# 输出示例：
# gpg-pubkey-8a7da187-5d75b8f7
# gpg-pubkey-75426c18-5f3c8c17
```

#### 步骤 2：配置 GitLab YUM 源

```bash
# 使用官方源（推荐，版本最新）
sudo curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash

# 或使用清华镜像源（国内速度更快）
cat > /etc/yum.repos.d/gitlab-ce.repo << 'EOF'
[gitlab-ce]
name=GitLab CE Repository
baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el$releasever/
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/gpgkey
enabled=1
EOF

# 验证 GPG 校验
sudo yum install gitlab-ce --assumeno 2>&1 | grep -i "gpg\|import"
```

#### 步骤 3：验证 YUM 源配置

```bash
# 列出可用版本
yum --showduplicates list gitlab-ce | tail -20

# 输出示例：
# gitlab-ce.x86_64    16.8.3-ce.0.el8    gitlab-ce
# gitlab-ce.x86_64    16.7.5-ce.0.el8    gitlab-ce
# gitlab-ce.x86_64    16.6.4-ce.0.el8    gitlab-ce

# 查看最新 LTS 版本
yum info gitlab-ce | grep -E "Version|Release"
```

⚠️ **版本选择建议**：
```
- 生产环境：选择最新 LTS（长期支持）版本，如 16.x
- 测试环境：可选择最新版本，体验新功能
- 避免使用：RC（候选版）、Beta（测试版）
- 查看 LTS 计划：https://about.gitlab.com/releases/categories/releases/
```

---

### 3.4 安装 GitLab LTS 版本

#### 步骤 1：安装指定版本

```bash
# 查看可用版本
yum --showduplicates list gitlab-ce | grep "16\."

# 安装最新 LTS 版本（示例：16.8.3）
sudo yum install -y gitlab-ce-16.8.3-ce.0.el8

# Ubuntu 系统
# sudo apt install -y gitlab-ce=16.8.3-ce.0
```

⚠️ **安装时间**：
```
- 首次安装约需 5-10 分钟
- 期间会安装依赖、初始化数据库、配置服务
- 请确保网络连接稳定
- 不要中断安装过程
```

#### 步骤 2：验证安装

```bash
# 检查 GitLab 版本
gitlab-rake gitlab:env:info | grep "GitLab version"

# 输出示例：
# GitLab version: 16.8.3

# 检查服务状态
gitlab-ctl status

# 输出示例（所有服务应为 run 状态）：
# run: alertmanager: (pid 1234) 10s
# run: gitaly: (pid 1235) 10s
# run: gitlab-workhorse: (pid 1236) 10s
# run: nginx: (pid 1237) 10s
# run: node-exporter: (pid 1238) 10s
# run: postgresql: (pid 1239) 10s
# run: prometheus: (pid 1240) 10s
# run: redis: (pid 1241) 10s
# run: sidekiq: (pid 1242) 10s
# run: unicorn: (pid 1243) 10s
```

---

### 3.5 配置 external_url 与 HTTPS

#### 步骤 1：编辑配置文件

```bash
sudo vim /etc/gitlab/gitlab.rb
```

#### 步骤 2：配置 HTTP 访问（内网环境）

```ruby
# 第 51 行左右，修改 external_url
external_url 'http://10.0.0.200'

# 或使用域名（内网 DNS 解析）
# external_url 'http://gitlab.example.com'
```

#### 步骤 3：配置 HTTPS（生产环境推荐）

**方案 A：使用 Let's Encrypt 免费证书**

```ruby
# 配置域名（必须能公网访问）
external_url 'https://gitlab.example.com'

# 启用 Let's Encrypt 自动申请
letsencrypt['enable'] = true
letsencrypt['contact_emails'] = ['admin@example.com']

# 自动重定向 HTTP 到 HTTPS
nginx['redirect_http_to_https'] = true
```

**方案 B：使用企业内部证书**

```ruby
external_url 'https://gitlab.example.com'

# 配置自定义证书
nginx['ssl_certificate'] = "/etc/gitlab/ssl/gitlab.example.com.crt"
nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/gitlab.example.com.key"

# 可选：配置 CA 证书链
nginx['ssl_trusted_certificate'] = "/etc/gitlab/ssl/ca-bundle.crt"

# 重定向 HTTP 到 HTTPS
nginx['redirect_http_to_https'] = true

# 配置 SSL 协议（安全加固）
nginx['ssl_protocols'] = "TLSv1.2 TLSv1.3"
nginx['ssl_ciphers'] = "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256"
nginx['ssl_prefer_server_ciphers'] = "on"
nginx['ssl_session_cache'] = "builtin:1000"
nginx['ssl_session_timeout'] = "10m"
```

**上传证书文件**：

```bash
# 创建 SSL 目录
sudo mkdir -p /etc/gitlab/ssl

# 上传证书文件（使用 scp 或本地复制）
sudo cp gitlab.example.com.crt /etc/gitlab/ssl/
sudo cp gitlab.example.com.key /etc/gitlab/ssl/

# 设置权限（必须 600，所有者 root）
sudo chmod 600 /etc/gitlab/ssl/gitlab.example.com.key
sudo chown root:root /etc/gitlab/ssl/gitlab.example.com.key

# 验证证书
openssl x509 -in /etc/gitlab/ssl/gitlab.example.com.crt -text -noout | head -20
```

#### 步骤 4：应用配置

```bash
# 重新配置 GitLab（耗时 5-10 分钟）
sudo gitlab-ctl reconfigure

# 验证配置
gitlab-rake gitlab:check SANITIZE=true --trace

# 输出示例（所有检查应为 OK）：
# Checking GitLab sub components ...
# Checking GitLab App ... Success
# Checking Git Shell ... Success
# Checking Repositories ... Success
# Checking PostgreSQL ... Success
# Checking Redis ... Success
# Checking Sidekiq ... Success
# Checking GitLab Pages ... Success
# Checking Gitaly ... Success
# Checking Let's Encrypt certificates ... Success
```

---

### 3.6 初始化配置与访问

#### 步骤 1：获取初始密码

```bash
# GitLab 16.x 初始密码存储在文件中
sudo cat /etc/gitlab/initial_root_password

# 输出示例：
# # WARNING: This file is auto-generated. Please do not modify it manually.
# # You can use this file to login as the admin user 'root' for the first time.
# # This file will be automatically deleted after 24 hours.
# Password: xK9mP2nQ7vL4sR8t

# 注意：该文件会在 24 小时后自动删除，请及时修改密码！
```

#### 步骤 2：首次登录

```
1. 浏览器访问：http://10.0.0.200 或 https://gitlab.example.com
2. 使用用户名 root 登录
3. 输入初始密码（从文件获取）
4. 系统会要求修改密码
```

⚠️ **密码安全要求**：
```
- 长度至少 12 位
- 包含大小写字母、数字、特殊字符
- 避免使用常见单词或个人信息
- 示例：GitLab@2026#Secure
- 建议：使用密码管理器生成和存储
```

#### 步骤 3：配置管理员邮箱

```
1. 登录后，点击右上角头像 → Admin Area（管理员区域）
2. 点击 Settings → General
3. 展开 "Account and limit" 部分
4. 设置：
   - Support email: support@example.com
   - Help page text: （可选，自定义帮助信息）
5. 点击 "Save changes"
```

#### 步骤 4：启用双因素认证（2FA）

```
1. 点击右上角头像 → Settings
2. 点击左侧 "Account"
3. 找到 "Two-Factor Authentication"
4. 点击 "Enable two-factor authentication"
5. 使用手机扫码（推荐应用：Google Authenticator、Authy）
6. 输入验证码确认
7. 保存恢复码（重要！丢失后无法恢复账户）
```

⚠️ **重要提示**：
```
- 管理员账户必须启用 2FA
- 恢复码应安全保存（建议打印或存入密码管理器）
- 丢失 2FA 设备且无恢复码 = 永久失去账户访问权限
```

---

### 3.7 Docker 容器化部署方案

#### 方案优势

| 特性 | 传统安装 | Docker 部署 |
|:---|:---|:---|
| **部署速度** | 10-15 分钟 | 2-5 分钟 |
| **环境隔离** | 系统级 | 容器级 |
| **升级难度** | 较复杂 | 简单（换镜像） |
| **备份恢复** | 手动配置 | 卷挂载 |
| **资源占用** | 固定 | 可限制 |
| **适合场景** | 生产环境 | 测试/开发/小团队 |

#### 步骤 1：安装 Docker

```bash
# CentOS/RHEL
sudo dnf install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io

# Ubuntu
curl -fsSL https://get.docker.com | bash

# 启动 Docker
sudo systemctl enable docker
sudo systemctl start docker

# 验证安装
docker --version
```

#### 步骤 2：创建数据目录

```bash
# 创建配置、数据、日志目录
sudo mkdir -p /srv/gitlab/{config,data,logs}

# 设置权限
sudo chmod 755 /srv/gitlab
sudo chown -R 999:999 /srv/gitlab/data
```

#### 步骤 3：运行 GitLab 容器

```bash
# 基本部署（8GB 内存）
docker run --detach \
  --hostname gitlab.example.com \
  --publish 443:443 --publish 80:80 --publish 2222:22 \
  --name gitlab \
  --restart always \
  --volume /srv/gitlab/config:/etc/gitlab \
  --volume /srv/gitlab/logs:/var/log/gitlab \
  --volume /srv/gitlab/data:/var/opt/gitlab \
  --shm-size 256m \
  --env GITLAB_OMNIBUS_CONFIG="external_url 'https://gitlab.example.com'; \
  nginx['redirect_http_to_https'] = true; \
  letsencrypt['enable'] = true; \
  letsencrypt['contact_emails'] = ['admin@example.com'];" \
  gitlab/gitlab-ce:16.8.3-ce.0

# 资源限制版本（4GB 内存）
docker run --detach \
  --hostname gitlab.example.com \
  --publish 443:443 --publish 80:80 --publish 2222:22 \
  --name gitlab \
  --restart always \
  --memory 4g \
  --memory-swap 4g \
  --cpus 2.0 \
  --volume /srv/gitlab/config:/etc/gitlab \
  --volume /srv/gitlab/logs:/var/log/gitlab \
  --volume /srv/gitlab/data:/var/opt/gitlab \
  --shm-size 256m \
  --env GITLAB_OMNIBUS_CONFIG="external_url 'https://gitlab.example.com'; \
  puma['worker_processes'] = 2; \
  sidekiq['max_concurrency'] = 10;" \
  gitlab/gitlab-ce:16.8.3-ce.0
```

#### 步骤 4：验证容器状态

```bash
# 查看容器状态
docker ps | grep gitlab

# 查看容器日志
docker logs -f gitlab

# 进入容器执行命令
docker exec -it gitlab bash

# 在容器内检查 GitLab 状态
gitlab-ctl status
```

#### 步骤 5：Docker Compose 部署（推荐）

```yaml
# docker-compose.yml
version: '3.8'

services:
  gitlab:
    image: gitlab/gitlab-ce:16.8.3-ce.0
    container_name: gitlab
    hostname: gitlab.example.com
    restart: always
    ports:
      - "80:80"
      - "443:443"
      - "2222:22"
    volumes:
      - ./config:/etc/gitlab
      - ./logs:/var/log/gitlab
      - ./data:/var/opt/gitlab
    shm_size: '256mb'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'https://gitlab.example.com'
        nginx['redirect_http_to_https'] = true
        letsencrypt['enable'] = true
        letsencrypt['contact_emails'] = ['admin@example.com']
        puma['worker_processes'] = 4
        sidekiq['max_concurrency'] = 20
    deploy:
      resources:
        limits:
          cpus: '4.0'
          memory: 8G
        reservations:
          cpus: '2.0'
          memory: 4G
    networks:
      - gitlab-network

networks:
  gitlab-network:
    driver: bridge
```

**启动服务**：

```bash
# 启动 GitLab
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down

# 重启服务
docker-compose restart
```

---

### 3.8 常用命令与故障排查

#### 服务管理命令

```bash
# 查看所有服务状态
sudo gitlab-ctl status

# 启动/停止/重启所有服务
sudo gitlab-ctl start
sudo gitlab-ctl stop
sudo gitlab-ctl restart

# 管理单个服务
sudo gitlab-ctl start nginx
sudo gitlab-ctl stop postgresql
sudo gitlab-ctl restart sidekiq

# 重新配置 GitLab
sudo gitlab-ctl reconfigure

# 清理旧版本
sudo gitlab-ctl cleanse  # ⚠️ 危险！会删除所有数据
```

#### 日志查看命令

```bash
# 查看所有服务日志（实时）
sudo gitlab-ctl tail

# 查看特定服务日志
sudo gitlab-ctl tail nginx
sudo gitlab-ctl tail unicorn
sudo gitlab-ctl tail sidekiq
sudo gitlab-ctl tail postgresql

# 查看最近 100 行日志
sudo gitlab-ctl tail nginx -n 100

# 查看特定时间范围日志
sudo gitlab-ctl tail nginx -g "2026-03-21"
```

#### 高频故障排查

**问题 1：502 GitLab is not responding**

```bash
# 检查服务状态
sudo gitlab-ctl status

# 检查内存使用
free -h
top -bn1 | grep gitlab

# 重启 GitLab
sudo gitlab-ctl restart

# 查看 Unicorn 日志（通常是 Unicorn 进程崩溃）
sudo gitlab-ctl tail unicorn

# 解决方案：
# 1. 增加内存（最低 4GB）
# 2. 减少 Unicorn worker 数量
# 3. 增加 Swap 分区
```

**问题 2：无法访问 Web 界面**

```bash
# 检查 Nginx 服务
sudo gitlab-ctl status nginx

# 检查防火墙
sudo firewall-cmd --list-all
# 或
sudo ufw status

# 检查端口监听
sudo netstat -tlnp | grep :80
sudo netstat -tlnp | grep :443

# 测试本地访问
curl -I http://localhost

# 查看 Nginx 日志
sudo gitlab-ctl tail nginx
```

**问题 3：SSH 克隆失败**

```bash
# 测试 SSH 连接
ssh -T -p 22 git@10.0.0.200

# 检查 SSH 密钥
cat ~/.ssh/id_rsa.pub

# 验证 GitLab SSH 配置
sudo gitlab-rake gitlab:check SANITIZE=true

# 查看 SSH 日志
sudo gitlab-ctl tail gitlab-shell
```

**问题 4：数据库连接失败**

```bash
# 检查 PostgreSQL 状态
sudo gitlab-ctl status postgresql

# 重启 PostgreSQL
sudo gitlab-ctl restart postgresql

# 查看数据库日志
sudo gitlab-ctl tail postgresql

# 检查数据库连接
sudo -u gitlab-psql /opt/gitlab/embedded/bin/psql -h /var/opt/gitlab/postgresql -U gitlab
```

---

## 第 4 章 GitLab 权限管理

### 4.1 用户→组→项目权限模型

#### 权限层级关系

```
┌─────────────────────────────────────────────────────────┐
│                    GitLab 实例                           │
│  (gitlab.example.com)                                   │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                      用户 (User)                         │
│  - 独立账户                                              │
│  - 可属于多个组                                          │
│  - 可创建个人项目                                        │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    用户组 (Group)                        │
│  - 用户的集合（如：dev、ops、qa）                        │
│  - 可包含子组（嵌套）                                    │
│  - 组权限继承到项目                                      │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    项目 (Project)                        │
│  - 代码仓库                                              │
│  - 属于某个组或个人                                      │
│  - 继承组的权限设置                                      │
└─────────────────────────────────────────────────────────┘
```

#### 权限级别详解

| 级别 | 名称 | 图标 | 权限说明 | 适用角色 |
|:---:|:---|:---:|:---|:---|
| 0 | **Guest** | 👻 | 创建 Issue、发表评论、查看 Wiki | 产品经理、测试人员 |
| 1 | **Reporter** | 👤 | 查看代码、下载项目、查看 CI/CD | 测试人员、审计人员 |
| 2 | **Developer** | 👨‍💻 | 推送代码、创建分支、管理 Issue | 开发人员 |
| 3 | **Maintainer** | 🔧 | 管理项目、合并请求、保护分支 | 技术负责人、Team Leader |
| 4 | **Owner** | 👑 | 删除项目、管理成员、配置组设置 | CTO、部门经理 |

⚠️ **权限继承规则**：
```
1. 组权限 > 项目权限（组权限优先级更高）
2. 父组权限继承到子组
3. 用户同时属于多个组时，取最高权限
4. 项目可以直接添加成员（不受组限制）
```

---

### 4.2 企业级权限设计案例

#### 场景：某科技公司（50 人团队）

**组织架构**：
```
CTO (技术总监)
├── 研发部 (30 人)
│   ├── 后端组 (10 人)
│   ├── 前端组 (8 人)
│   ├── 移动端组 (7 人)
│   └── 测试组 (5 人)
├── 运维部 (10 人)
│   ├── 基础设施组 (5 人)
│   └── DBA 组 (5 人)
└── 安全部 (10 人)
    ├── 安全审计组 (5 人)
    └── 渗透测试组 (5 人)
```

**GitLab 组结构设计**：
```
company (顶级组，Owner: CTO)
├── rd (研发部，Owner: 研发总监)
│   ├── backend (后端组，Maintainer: 后端负责人)
│   ├── frontend (前端组，Maintainer: 前端负责人)
│   ├── mobile (移动端组，Maintainer: 移动端负责人)
│   └── qa (测试组，Maintainer: 测试负责人)
├── ops (运维部，Owner: 运维总监)
│   ├── infra (基础设施组)
│   └── dba (数据库组)
└── security (安全部，Owner: 安全总监)
    ├── audit (安全审计组)
    └── pentest (渗透测试组)
```

**项目权限分配**：
| 项目 | 所属组 | 访问级别 | 说明 |
|:---|:---|:---:|:---|
| backend-api | rd/backend | Private | 后端 API 代码 |
| frontend-web | rd/frontend | Private | 前端 Web 代码 |
| mobile-app | rd/mobile | Private | 移动端 APP |
| ansible-playbooks | ops/infra | Private | 运维自动化脚本 |
| database-scripts | ops/dba | Private | 数据库脚本 |
| security-audit | security/audit | Private | 安全审计报告 |

**关键权限规则**：
```
1. 分支保护：master/main 分支仅 Maintainer 可推送
2. 合并请求：所有代码必须通过 MR 合并，至少 1 人审批
3. 代码门禁：CI 流水线必须通过才能合并
4. 审计日志：所有敏感操作记录日志（保留 180 天）
```

---

### 4.3 创建组与项目

#### 步骤 1：创建顶级组

```
1. 登录 GitLab Web 界面
2. 点击左上角 "+" → "New group"
3. 选择 "Create group"
4. 填写信息：
   - Group name: company
   - Group slug: company（自动生成）
   - Visibility: Private（私有，仅成员可见）
   - 描述：公司顶级组
5. 点击 "Create group"
```

#### 步骤 2：创建子组

```
1. 进入 company 组页面
2. 点击左侧 "Subgroups" → "New subgroup"
3. 填写信息：
   - Subgroup name: rd
   - Subgroup slug: rd
   - Visibility: Private
4. 重复创建其他子组（ops、security）
```

#### 步骤 3：创建项目

```
1. 进入目标组（如 rd/backend）
2. 点击 "New project" → "Create blank project"
3. 填写信息：
   - Project name: backend-api
   - Project slug: backend-api（自动生成）
   - Visibility: Private
   - 描述：后端 API 服务
4. 点击 "Create project"
```

#### 步骤 4：配置项目可见性

```
项目可见性级别：
- Private（私有）：仅项目成员可见（推荐生产环境）
- Internal（内部）：登录用户可见
- Public（公开）：任何人可见（开源项目）

配置路径：
Settings → General → Visibility, project features, permissions
```

---

### 4.4 创建用户与双因素认证

#### 步骤 1：创建用户（管理员操作）

```
1. 点击右上角头像 → Admin Area
2. 点击左侧 "Users" → "New user"
3. 填写信息：
   - Name: 张三
   - Username: zhangsan
   - Email: zhangsan@company.com
   - Password: SecurePass@2026（强密码）
   - Password confirmation: SecurePass@2026
   - Skip confirmation: ✓ 勾选（跳过邮箱验证）
   - External: □ 不勾选（内部员工）
4. 点击 "Create user"
```

#### 步骤 2：批量导入用户（可选）

```bash
# 使用 GitLab API 批量创建用户
# 保存为 create_users.sh

#!/bin/bash

GITLAB_URL="https://gitlab.example.com"
PRIVATE_TOKEN="glpat-xxxxxxxxxxxxxxxxxxxx"

# 用户列表
users=(
  "zhangsan:张三:zhangsan@company.com"
  "lisi:李四:lisi@company.com"
  "wangwu:王五:wangwu@company.com"
)

for user in "${users[@]}"; do
  IFS=':' read -r username name email <<< "$user"
  
  curl --request POST --header "PRIVATE-TOKEN: $PRIVATE_TOKEN" \
    "$GITLAB_URL/api/v4/users" \
    --data "email=$email" \
    --data "username=$username" \
    --data "name=$name" \
    --data "password=SecurePass@2026" \
    --data "skip_confirmation=true"
  
  echo "Created user: $username ($email)"
done
```

#### 步骤 3：强制启用 2FA（生产环境推荐）

```
管理员设置：
1. Admin Area → Settings → General
2. 展开 "Account and limit"
3. 找到 "Two-factor authentication"
4. 选择 "Enforce two-factor authentication for all users"
5. 设置宽限期（如 7 天）
6. 点击 "Save changes"

⚠️ 注意：启用后所有用户必须配置 2FA，否则无法登录
```

---

### 4.5 SSH 密钥配置（ed25519）

#### 为什么推荐 ed25519？

| 算法 | 密钥长度 | 安全性 | 性能 | 推荐度 |
|:---:|:---:|:---:|:---:|:---:|
| **ed25519** | 256 位 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ 强烈推荐 |
| RSA | 2048 位 | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⚠️ 可用 |
| RSA | 4096 位 | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⚠️ 较慢 |
| ECDSA | 256 位 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ 推荐 |

#### 步骤 1：生成 ed25519 密钥对

```bash
# 生成 ed25519 密钥（推荐）
ssh-keygen -t ed25519 -C "zhangsan@company.com" -f ~/.ssh/id_ed25519

# 输出示例：
# Generating public/private ed25519 key pair.
# Enter file in which to save the key (/home/zhangsan/.ssh/id_ed25519):
# Enter passphrase (empty for no passphrase): （建议设置密码短语）
# Enter same passphrase again:

# 如果系统不支持 ed25519，使用 RSA 4096
ssh-keygen -t rsa -b 4096 -C "zhangsan@company.com" -f ~/.ssh/id_rsa
```

#### 步骤 2：查看公钥

```bash
# 查看公钥内容
cat ~/.ssh/id_ed25519.pub

# 输出示例：
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI... zhangsan@company.com
```

#### 步骤 3：添加公钥到 GitLab

```
1. 登录 GitLab
2. 点击右上角头像 → Settings
3. 点击左侧 "SSH Keys"
4. 粘贴公钥内容到 "Key" 框
5. 填写标题：zhangsan-workstation
6. 设置过期时间（可选）：2027-03-21
7. 点击 "Add key"
```

#### 步骤 4：测试 SSH 连接

```bash
# 测试连接
ssh -T -p 22 git@gitlab.example.com

# 成功输出：
# Welcome to GitLab, @zhangsan!

# 失败排查：
# 1. 检查公钥是否正确添加
# 2. 检查 SSH 服务状态
# 3. 查看 SSH 日志：~/.ssh/known_hosts
```

#### 步骤 5：配置 SSH Config（多账户场景）

```bash
# 编辑 SSH 配置文件
vim ~/.ssh/config

# 添加配置（公司账户 + 个人账户）
cat >> ~/.ssh/config << 'EOF'

# 公司 GitLab
Host gitlab.company.com
    HostName gitlab.company.com
    User git
    IdentityFile ~/.ssh/id_ed25519_company
    IdentitiesOnly yes

# 个人 GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes
EOF

# 设置权限
chmod 600 ~/.ssh/config
```

⚠️ **安全最佳实践**：
```
1. 私钥权限必须为 600：chmod 600 ~/.ssh/id_ed25519
2. 不要将私钥上传到任何地方
3. 使用密码短语保护私钥
4. 离职员工立即撤销 SSH 密钥
5. 定期轮换密钥（建议每年）
```

---

### 4.6 分支保护规则

#### 为什么需要分支保护？

```
- ✅ 防止误删重要分支（master/main）
- ✅ 防止直接推送（强制代码审查）
- ✅ 确保 CI 流水线通过
- ✅ 符合合规要求（审计追踪）
```

#### 步骤 1：配置分支保护

```
1. 进入项目页面
2. Settings → Repository
3. 展开 "Protected branches"
4. 选择分支：main（或 master）
5. 配置规则：
   - Allowed to merge: Maintainers
   - Allowed to push: No one（推荐）或 Maintainers
   - Allowed to force push: □ 不勾选（禁止强制推送）
6. 点击 "Protect"
```

#### 步骤 2：配置标签保护

```
1. Settings → Repository
2. 展开 "Protected tags"
3. 点击 "New protected tag"
4. 填写：
   - Tag name pattern: v*（保护所有版本标签）
   - Allowed to create: Maintainers
5. 点击 "Create"
```

#### 步骤 3：配置推送规则（高级）

```
Settings → Repository → Push rules

推荐配置：
- ✓ Reject unsigned commits（拒绝未签名提交）
- ✓ Prevent committing secrets to Git（防止提交密钥）
- ✓ Commit message regex: ^[A-Z]+-\d+: .+$（规范提交信息格式）
- ✓ Member check: 只有项目成员可推送
- ✓ File path regex: 禁止提交特定文件（如 .env、*.key）
```

---

### 4.7 合并请求审批流程

#### 配置合并请求规则

```
1. Settings → Merge requests
2. 展开 "Merge requests approvals"
3. 点击 "Add approval rule"
4. 配置规则：
   - Rule name: Code Review
   - Approvals required: 1（至少 1 人审批）
   - Users: 选择审批人（如 Maintainer）
   - Groups: 选择审批组（如 rd-team）
   - Protected branches: main
   - ✓ Prevent approval by author（禁止作者自批）
5. 点击 "Create approval rule"
```

#### 配置代码所有者（Code Owners）

```bash
# 在项目根目录创建 CODEOWNERS 文件
vim CODEOWNERS

# 配置内容示例：

# 所有文件默认由后端组审查
* @rd/backend

# 前端代码由前端组审查
/src/frontend/ @rd/frontend

# 数据库脚本由 DBA 审查
/db/scripts/ @ops/dba

# 安全相关由安全部审查
/security/ @security/audit
*.key @security/audit
*.pem @security/audit

# 配置文件由运维审查
*.yml @ops/infra
*.yaml @ops/infra
Dockerfile @ops/infra
```

```
配置路径：
Settings → Repository → Default branch
- ✓ Enable code owners
- 上传 CODEOWNERS 文件
```

#### 合并请求流程

```
1. 开发人员创建功能分支：git checkout -b feature/new-feature
2. 开发完成提交代码：git push origin feature/new-feature
3. 在 GitLab 创建 Merge Request
4. 自动通知审批人（邮件/站内消息）
5. 审批人审查代码：
   - 查看代码变更
   - 运行 CI 流水线
   - 提出修改意见
6. 审批通过（至少 1 人）
7. Maintainer 合并到 main 分支
8. 删除功能分支
```

---

### 4.8 代码提交门禁配置

#### 配置 CI/CD 门禁

```
1. Settings → Merge requests
2. 展开 "Pipelines"
3. 配置：
   - ✓ Pipelines must succeed（流水线必须成功）
   - ✓ Pipeline must complete before merge（合并前必须完成）
   - ✓ Prevent merge if pipeline fails（失败时禁止合并）
```

#### 配置质量门禁（SonarQube 集成）

```
1. Settings → Merge requests
2. 展开 "Quality gates"
3. 配置：
   - ✓ Quality gate must pass（质量门禁必须通过）
   - 最大新增代码重复率：3%
   - 最小测试覆盖率：80%
   - 阻断级问题：0 个
```

#### 配置提交签名验证

```bash
# 生成 GPG 密钥
gpg --full-generate-key

# 导出公钥
gpg --armor --export your@email.com

# 添加到 GitLab：
# Settings → SSH Keys → GPG Keys → Add GPG key

# Git 配置签名
git config --global user.signingkey YOUR_GPG_KEY_ID
git config --global commit.gpgsign true

# 验证提交
git log --show-signature
```

```
启用签名验证：
Settings → Repository → Push rules
- ✓ Reject unsigned commits
```

---

### 4.9 操作审计日志

#### 查看审计日志

```
管理员操作：
1. Admin Area → Monitoring → Audit Events
2. 筛选条件：
   - 日期范围
   - 用户
   - 操作类型（创建/删除/修改）
   - 目标（项目/组/用户）
```

#### 配置审计日志保留策略

```ruby
# 编辑 gitlab.rb
sudo vim /etc/gitlab/gitlab.rb

# 添加配置（保留 180 天）
gitlab_rails['audit_events_enabled'] = true
gitlab_rails['audit_logs_retention_days'] = 180

# 应用配置
sudo gitlab-ctl reconfigure
```

#### 导出审计日志

```bash
# 使用 API 导出审计日志
curl --header "PRIVATE-TOKEN: <your_token>" \
  "https://gitlab.example.com/api/v4/audit_events"

# 导出为 JSON
curl --header "PRIVATE-TOKEN: <your_token>" \
  "https://gitlab.example.com/api/v4/audit_events" \
  | jq . > audit_events.json
```

#### 常见审计事件

| 事件类型 | 说明 | 风险等级 |
|:---|:---|:---:|
| user.create | 创建用户 | 中 |
| user.destroy | 删除用户 | 高 |
| project.create | 创建项目 | 低 |
| project.destroy | 删除项目 | 高 |
| member.add | 添加成员 | 中 |
| member.remove | 移除成员 | 中 |
| protected_branch.create | 创建保护分支 | 中 |
| pipeline.create | 创建流水线 | 低 |
| settings.change | 修改系统设置 | 高 |

---

### 4.10 克隆与推送测试

#### 步骤 1：克隆项目

```bash
# SSH 方式（推荐）
git clone git@gitlab.company.com:rd/backend-api.git

# HTTPS 方式
git clone https://gitlab.company.com/rd/backend-api.git

# 指定分支
git clone -b main git@gitlab.company.com:rd/backend-api.git
```

#### 步骤 2：配置用户信息

```bash
cd backend-api

# 配置全局用户（首次使用）
git config --global user.name "张三"
git config --global user.email "zhangsan@company.com"

# 或仅配置当前项目
git config user.name "张三"
git config user.email "zhangsan@company.com"
```

#### 步骤 3：创建分支并提交

```bash
# 创建功能分支
git checkout -b feature/user-auth

# 创建文件
echo "用户认证模块" > auth.py

# 添加到暂存区
git add auth.py

# 提交（带签名）
git commit -S -m "feat: 添加用户认证模块"

# 推送到远程
git push origin feature/user-auth
```

#### 步骤 4：创建合并请求

```
1. 访问项目页面
2. 点击 "Merge requests" → "New merge request"
3. 选择分支：
   - Source branch: feature/user-auth
   - Target branch: main
4. 填写标题：feat: 添加用户认证模块
5. 填写描述：
   ```
   ## 变更说明
   - 添加用户登录功能
   - 添加 JWT token 验证
   - 添加单元测试
   
   ## 测试
   - [x] 单元测试通过
   - [x] 集成测试通过
   - [ ] 性能测试
   
   ## 关联 Issue
   Closes #123
   ```
6. 选择审批人
7. 点击 "Create merge request"
```

---

## 第 5 章 GitLab CI/CD 实战

### 5.1 CI/CD 核心概念

#### 什么是 CI/CD？

```
CI (Continuous Integration) - 持续集成
- 自动构建：代码提交后自动编译
- 自动测试：运行单元测试、集成测试
- 自动检查：代码质量、安全扫描

CD (Continuous Deployment) - 持续部署
- 自动部署：测试通过后自动部署到环境
- 灰度发布：逐步发布降低风险
- 回滚机制：快速回退到稳定版本
```

#### GitLab CI/CD 流程

```
代码提交 → 触发流水线 → 构建 → 测试 → 部署
    ↓          ↓          ↓      ↓      ↓
  Push      .gitlab-   Docker  Unit   K8s/
  Event     ci.yml     Image  Test   Deploy
```

---

### 5.2 GitLab Runner 部署

#### Runner 类型

| 类型 | 说明 | 适用场景 |
|:---|:---|:---|
| **Shared Runner** | 共享运行器（所有项目可用） | 公共任务、通用构建 |
| **Group Runner** | 组运行器（组内项目可用） | 部门级任务 |
| **Project Runner** | 项目专用运行器 | 敏感项目、特殊需求 |

#### 步骤 1：安装 GitLab Runner

```bash
# CentOS/RHEL
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh | sudo bash
sudo yum install -y gitlab-runner

# Ubuntu
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
sudo apt install -y gitlab-runner

# Docker 方式（推荐）
docker run -d --name gitlab-runner --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest
```

#### 步骤 2：注册 Runner

```bash
# 获取注册令牌
# 路径：Admin Area → Runners → New project runner
# 或：项目 Settings → CI/CD → Runners

# 执行注册
sudo gitlab-runner register

# 交互式配置：
# Enter GitLab instance URL: https://gitlab.company.com
# Enter registration token: glrt-xxxxxxxxxxxx
# Enter description: docker-runner-01
# Enter tags: docker, backend, production
# Enter executor: docker
# Enter default Docker image: docker:24.0

# 验证注册
sudo gitlab-runner list
```

#### 步骤 3：配置 Runner

```toml
# 编辑配置文件
sudo vim /etc/gitlab-runner/config.toml

# 示例配置（Docker executor）
concurrent = 4
check_interval = 0

[[runners]]
  name = "docker-runner-01"
  url = "https://gitlab.company.com/"
  token = "glrt-xxxxxxxxxxxx"
  executor = "docker"
  limit = 4
  [runners.docker]
    tls_verify = false
    image = "docker:24.0"
    privileged = false
    disable_entrypoint = false
    disable_cache = false
    volumes = ["/cache", "/var/run/docker.sock:/var/run/docker.sock"]
    shm_size = 0
    allowed_images = ["docker:*", "node:*", "python:*", "maven:*"]
    allowed_services = ["docker:*", "postgres:*", "redis:*"]
  [runners.cache]
    Type = "s3"
    Shared = true
    [runners.cache.s3]
      ServerAddress = "s3.amazonaws.com"
      BucketName = "gitlab-runner-cache"
      Insecure = false
```

#### 步骤 4：验证 Runner

```bash
# 查看 Runner 状态
sudo gitlab-runner status

# 查看 Runner 日志
sudo journalctl -u gitlab-runner -f

# 在 GitLab Web 界面验证：
# Settings → CI/CD → Runners → 查看 Runner 状态（绿色为在线）
```

---

### 5.3 .gitlab-ci.yml 基础配置

#### 配置文件结构

```yaml
# .gitlab-ci.yml - 放在项目根目录

# 定义流水线阶段
stages:
  - build      # 构建
  - test       # 测试
  - deploy     # 部署

# 定义全局变量
variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: ""

# 定义任务
build_job:
  stage: build
  script:
    - echo "构建中..."
    - docker build -t myapp .
  tags:
    - docker
  only:
    - main
    - merge_requests

test_job:
  stage: test
  script:
    - echo "测试中..."
    - docker run myapp npm test
  tags:
    - docker
  dependencies:
    - build_job

deploy_job:
  stage: deploy
  script:
    - echo "部署中..."
    - kubectl apply -f k8s/
  tags:
    - k8s
  only:
    - main
  environment:
    name: production
    url: https://app.example.com
```

#### 常用配置项

| 配置项 | 说明 | 示例 |
|:---|:---|:---|
| `stage` | 所属阶段 | `stage: build` |
| `script` | 执行脚本 | `script: [npm install, npm test]` |
| `image` | Docker 镜像 | `image: node:18` |
| `tags` | Runner 标签 | `tags: [docker]` |
| `only` | 触发分支 | `only: [main, develop]` |
| `except` | 排除分支 | `except: [tags]` |
| `dependencies` | 依赖任务 | `dependencies: [build]` |
| `artifacts` | 构建产物 | `artifacts: { paths: [dist/] }` |
| `cache` | 缓存配置 | `cache: { key: npm, paths: [node_modules] }` |
| `environment` | 部署环境 | `environment: production` |
| `when` | 执行时机 | `when: on_success / on_failure / manual` |
| `allow_failure` | 允许失败 | `allow_failure: true` |

---

### 5.4 构建→测试→部署流水线

#### 完整示例（Node.js 项目）

```yaml
# .gitlab-ci.yml

stages:
  - lint       # 代码检查
  - build      # 构建
  - test       # 测试
  - security   # 安全扫描
  - deploy     # 部署

variables:
  NODE_VERSION: "18"
  DOCKER_REGISTRY: "registry.company.com"
  APP_NAME: "backend-api"

# 代码检查
lint:
  stage: lint
  image: node:${NODE_VERSION}
  script:
    - npm ci
    - npm run lint
  cache:
    key: ${CI_COMMIT_REF_SLUG}-npm
    paths:
      - node_modules/
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# 构建
build:
  stage: build
  image: docker:24.0
  services:
    - docker:24.0-dind
  script:
    - docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA} .
    - docker push ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
    - docker tag ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA} ${DOCKER_REGISTRY}/${APP_NAME}:latest
    - docker push ${DOCKER_REGISTRY}/${APP_NAME}:latest
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

# 单元测试
unit_test:
  stage: test
  image: node:${NODE_VERSION}
  script:
    - npm ci
    - npm run test:unit -- --coverage
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
    paths:
      - coverage/
    expire_in: 1 week
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# 集成测试
integration_test:
  stage: test
  image: docker:24.0
  services:
    - docker:24.0-dind
    - postgres:15
  variables:
    POSTGRES_DB: test_db
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test123
  script:
    - docker run --rm -e DATABASE_URL=postgresql://test:test123@postgres/test_db \
        ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA} npm run test:integration
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# 安全扫描
security_scan:
  stage: security
  image: node:${NODE_VERSION}
  script:
    - npm audit --audit-level=high
    - npm run security:check
  allow_failure: true
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

# 部署到生产环境
deploy_production:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context production
    - kubectl set image deployment/${APP_NAME} \
        ${APP_NAME}=${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
    - kubectl rollout status deployment/${APP_NAME}
  environment:
    name: production
    url: https://api.company.com
  when: manual  # 手动触发部署
  only:
    - main
```

#### 流水线可视化

```
Pipeline #123 - backend-api
┌─────────────────────────────────────────────────────────────┐
│  lint         ✅ 成功 (2m 15s)                              │
│    ↓                                                        │
│  build        ✅ 成功 (5m 30s)                              │
│    ↓                                                        │
│  unit_test    ✅ 成功 (3m 45s)  覆盖率：85%                 │
│  integration  ✅ 成功 (4m 20s)                              │
│    ↓                                                        │
│  security     ⚠️ 警告 (1m 10s)  发现 2 个低风险问题          │
│    ↓                                                        │
│  deploy       ⏸️ 等待手动触发                               │
└─────────────────────────────────────────────────────────────┘
```

---

### 5.5 环境变量与密钥管理

#### 配置环境变量

```
项目级别：
Settings → CI/CD → Variables → Add variable

推荐配置：
- DATABASE_URL: postgresql://user:pass@host/db
- API_KEY: sk-xxxxxxxxxxxx
- DEPLOY_ENV: production
- NODE_ENV: production
```

#### 密钥保护

```
变量类型：
- ✓ Protected: 仅保护分支/标签可用
- ✓ Masked: 在日志中隐藏（显示为 [MASKED]）
- Environment scope: 指定环境（production/staging）

⚠️ 安全提示：
1. 不要在 .gitlab-ci.yml 中硬编码密钥
2. 使用 GitLab Variables 管理敏感信息
3. 定期轮换密钥
4. 限制密钥访问范围
```

#### 使用示例

```yaml
deploy:
  stage: deploy
  script:
    - echo "部署到 ${DEPLOY_ENV} 环境"
    - kubectl config use-context ${DEPLOY_ENV}
    # 使用受保护的变量
    - export DB_PASSWORD="${DATABASE_PASSWORD}"
    - docker run -e DB_PASSWORD=${DB_PASSWORD} myapp
  variables:
    DEPLOY_ENV: production
  only:
    - main
```

---

### 5.6 流水线状态监控

#### 查看流水线

```
项目页面 → CI/CD → Pipelines

状态说明：
- 🟢 Created: 已创建
- 🟡 Waiting: 等待资源
- 🔵 Running: 运行中
- ✅ Passed: 通过
- ❌ Failed: 失败
- ⚪ Canceled: 已取消
- ⏸️ Skipped: 已跳过
```

#### 配置通知

```
Settings → CI/CD → Notifications

推荐配置：
- ✓ Pipeline failures（流水线失败）
- ✓ Pipeline success（流水线成功）
- ✓ Merge request status（MR 状态）

通知渠道：
- Email（邮件）
- Slack
- Microsoft Teams
- Webhook（自定义）
```

#### 流水线分析

```bash
# 使用 API 获取流水线统计
curl --header "PRIVATE-TOKEN: <token>" \
  "https://gitlab.company.com/api/v4/projects/1/pipelines"

# 查看平均构建时间
# CI/CD → Analytics → Cycle analytics

# 优化建议：
# 1. 使用缓存减少依赖下载
# 2. 并行执行独立任务
# 3. 使用 Docker 层缓存
# 4. 优化测试用例数量
```

---

## 第 6 章 GitLab 备份与容灾

### 6.1 备份策略与容灾规范

#### 3-2-1 备份原则

```
3 份副本：
- 1 份生产数据
- 1 份本地备份
- 1 份异地备份

2 种介质：
- 本地磁盘
- 对象存储（S3/OSS）

1 份异地：
- 不同地理位置
- 不同网络环境
```

#### 备份频率建议

| 环境 | 备份频率 | 保留时间 | RPO | RTO |
|:---|:---|:---:|:---:|:---:|
| **开发** | 每天 1 次 | 7 天 | 24h | 4h |
| **测试** | 每天 1 次 | 14 天 | 24h | 2h |
| **生产** | 每 4 小时 1 次 | 30 天 | 4h | 1h |
| **核心** | 每小时 1 次 | 90 天 | 1h | 30min |

**RPO (Recovery Point Objective)**: 可容忍的数据丢失量  
**RTO (Recovery Time Objective)**: 可容忍的恢复时间

---

### 6.2 配置备份路径与保留策略

#### 步骤 1：编辑配置文件

```bash
sudo vim /etc/gitlab/gitlab.rb
```

#### 步骤 2：配置备份参数

```ruby
# 备份存储路径
gitlab_rails['backup_path'] = "/var/opt/gitlab/backups"

# 备份保留时间（秒）- 7 天
gitlab_rails['backup_keep_time'] = 604800

# 备份文件权限
gitlab_rails['backup_archive_permissions'] = 0640

# 备份时跳过的内容（可选，加快备份速度）
gitlab_rails['backup_upload_connection'] = {
  'provider' => 'AWS',
  'region' => 'cn-north-1',
  'aws_access_key_id' => 'AKIAIOSFODNN7EXAMPLE',
  'aws_secret_access_key' => 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
}
gitlab_rails['backup_upload_remote_directory'] = 'gitlab-backups'

# 启用增量备份（GitLab 16.x+）
gitlab_rails['backup_incremental_enabled'] = true
```

#### 步骤 3：应用配置

```bash
# 重新配置
sudo gitlab-ctl reconfigure

# 创建备份目录
sudo mkdir -p /var/opt/gitlab/backups
sudo chown git:git /var/opt/gitlab/backups
sudo chmod 750 /var/opt/gitlab/backups
```

---

### 6.3 执行完整备份

#### 手动备份

```bash
# 执行备份
sudo gitlab-rake gitlab:backup:create

# 输出示例：
# 2026-03-21 10:00:00 +0800 -- Dumping database ...
# Dumping PostgreSQL database gitlabhq_production ... [DONE]
# 2026-03-21 10:00:05 +0800 -- done
# 2026-03-21 10:00:05 +0800 -- Dumping repositories ...
# 2026-03-21 10:00:10 +0800 -- done
# 2026-03-21 10:00:10 +0800 -- Dumping uploads ...
# 2026-03-21 10:00:11 +0800 -- done
# Creating backup archive: 1711000811_2026_03_21_16.8.3_gitlab_backup.tar ... done
# Uploading backup archive to remote storage  ... started
# Uploading backup archive to remote storage  ... done
# Deleting old backups ... done (0 removed)

# 查看备份文件
ls -lh /var/opt/gitlab/backups/

# 输出示例：
# -rw------- 1 git git 2.5G 3 月  21 10:00 1711000811_2026_03_21_16.8.3_gitlab_backup.tar
```

#### 备份内容说明

| 内容 | 说明 | 是否包含 |
|:---|:---|:---:|
| 数据库 | 用户、项目、Issue 等 | ✅ 包含 |
| 代码仓库 | Git 仓库数据 | ✅ 包含 |
| 上传文件 | 头像、附件 | ✅ 包含 |
| CI/CD 产物 | 构建产物 | ✅ 包含 |
| LFS 对象 | Git LFS 文件 | ✅ 包含 |
| 容器镜像 | Registry 镜像 | ✅ 包含 |
| 配置文件 | gitlab.rb | ❌ 不包含 |
| 密钥文件 | gitlab-secrets.json | ❌ 不包含 |
| 日志文件 | 系统日志 | ❌ 不包含 |

⚠️ **重要警告**：
```
gitlab.rb 和 gitlab-secrets.json 不会包含在备份中！
必须手动备份这些文件，否则无法恢复！
```

---

### 6.4 备份配置文件与密钥

#### 创建备份脚本

```bash
#!/bin/bash
# /usr/local/bin/gitlab-backup-config.sh

set -e

BACKUP_DIR="/backup/gitlab"
DATE=$(date +%Y%m%d_%H%M%S)
GITLAB_CONFIG="/etc/gitlab"

# 创建备份目录
mkdir -p ${BACKUP_DIR}/${DATE}

# 备份配置文件
echo "备份配置文件..."
cp -r ${GITLAB_CONFIG}/* ${BACKUP_DIR}/${DATE}/

# 创建压缩包
echo "创建压缩包..."
cd ${BACKUP_DIR}
tar -czf gitlab-config-${DATE}.tar.gz ${DATE}/

# 删除临时目录
rm -rf ${DATE}/

# 清理旧备份（保留 30 天）
find ${BACKUP_DIR} -name "gitlab-config-*.tar.gz" -mtime +30 -delete

echo "配置备份完成：${BACKUP_DIR}/gitlab-config-${DATE}.tar.gz"
```

#### 执行配置备份

```bash
# 设置权限
sudo chmod +x /usr/local/bin/gitlab-backup-config.sh

# 执行备份
sudo /usr/local/bin/gitlab-backup-config.sh

# 验证备份
ls -lh /backup/gitlab/

# 查看压缩包内容
tar -tzf /backup/gitlab/gitlab-config-20260321_100000.tar.gz | head -20
```

---

### 6.5 异地备份（rsync/S3）

#### 方案 A：rsync 同步到备份服务器

```bash
#!/bin/bash
# /usr/local/bin/gitlab-sync-remote.sh

REMOTE_HOST="backup.company.com"
REMOTE_USER="gitlab"
REMOTE_PATH="/backup/gitlab"
LOCAL_PATH="/var/opt/gitlab/backups"

# 同步备份文件
rsync -avz --delete \
  ${LOCAL_PATH}/ \
  ${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_PATH}/

# 验证同步
echo "同步完成，验证文件..."
ssh ${REMOTE_USER}@${REMOTE_HOST} "ls -lh ${REMOTE_PATH} | tail -5"
```

#### 方案 B：上传到 S3 对象存储

```bash
# 安装 AWS CLI
sudo yum install -y awscli

# 配置凭证
aws configure
# AWS Access Key ID: [输入]
# AWS Secret Access Key: [输入]
# Default region name: cn-north-1
# Default output format: json

# 创建上传脚本
cat > /usr/local/bin/gitlab-upload-s3.sh << 'EOF'
#!/bin/bash
BACKUP_PATH="/var/opt/gitlab/backups"
S3_BUCKET="gitlab-backups"

# 上传最新备份
LATEST_BACKUP=$(ls -t ${BACKUP_PATH}/*.tar | head -1)
aws s3 cp ${LATEST_BACKUP} s3://${S3_BUCKET}/$(basename ${LATEST_BACKUP})

# 清理 S3 旧备份（保留 30 天）
aws s3 ls s3://${S3_BUCKET}/ | \
  awk '{if(NR>30) print $4}' | \
  xargs -I {} aws s3 rm s3://${S3_BUCKET}/{}
EOF

chmod +x /usr/local/bin/gitlab-upload-s3.sh
```

---

### 6.6 备份完整性校验

#### 校验备份文件

```bash
#!/bin/bash
# /usr/local/bin/gitlab-verify-backup.sh

BACKUP_FILE=$1

if [ -z "${BACKUP_FILE}" ]; then
  echo "用法：$0 <备份文件>"
  exit 1
fi

echo "验证备份文件：${BACKUP_FILE}"

# 检查文件是否存在
if [ ! -f "${BACKUP_FILE}" ]; then
  echo "❌ 文件不存在"
  exit 1
fi

# 检查文件大小（应大于 100MB）
FILE_SIZE=$(stat -c%s "${BACKUP_FILE}")
if [ ${FILE_SIZE} -lt 104857600 ]; then
  echo "⚠️ 警告：备份文件过小 (${FILE_SIZE} bytes)"
fi

# 测试解压（不实际解压）
echo "测试压缩包完整性..."
tar -tf "${BACKUP_FILE}" > /dev/null 2>&1
if [ $? -eq 0 ]; then
  echo "✅ 压缩包完整性检查通过"
else
  echo "❌ 压缩包损坏"
  exit 1
fi

# 列出备份内容
echo ""
echo "备份内容："
tar -tf "${BACKUP_FILE}" | head -20

echo ""
echo "✅ 备份验证完成"
```

#### 定期恢复测试

```bash
# 建议每月进行一次恢复测试
# 在测试环境执行

# 1. 下载最新备份
scp gitlab.example.com:/var/opt/gitlab/backups/1711000811_*.tar /backup/test/

# 2. 在测试环境恢复
gitlab-rake gitlab:backup:restore BACKUP=1711000811_2026_03_21_16.8.3

# 3. 验证数据完整性
# - 检查项目数量
# - 检查用户登录
# - 检查代码克隆
# - 检查 CI/CD 流水线

# 4. 记录测试结果
echo "恢复测试完成 - $(date)" >> /var/log/gitlab-restore-test.log
```

---

### 6.7 数据恢复流程

#### 恢复场景

| 场景 | 恢复方式 | 预计时间 |
|:---|:---|:---:|
| 误删项目 | 从备份恢复单个项目 | 30 分钟 |
| 数据库损坏 | 完整恢复数据库 | 1-2 小时 |
| 服务器故障 | 新服务器完整恢复 | 2-4 小时 |
| 灾难恢复 | 异地备份恢复 | 4-8 小时 |

#### 步骤 1：停止服务

```bash
# 停止 GitLab 服务（防止数据写入）
sudo gitlab-ctl stop

# 验证服务已停止
sudo gitlab-ctl status
```

#### 步骤 2：恢复配置文件

```bash
# 恢复密钥文件（必须！）
sudo cp /backup/gitlab/gitlab-secrets.json /etc/gitlab/

# 恢复配置文件
sudo cp /backup/gitlab/gitlab.rb /etc/gitlab/

# 设置权限
sudo chown root:root /etc/gitlab/gitlab-secrets.json
sudo chown root:root /etc/gitlab/gitlab.rb
sudo chmod 600 /etc/gitlab/gitlab-secrets.json
```

#### 步骤 3：恢复备份数据

```bash
# 复制备份文件到备份目录
sudo cp /backup/gitlab/1711000811_2026_03_21_16.8.3_gitlab_backup.tar \
  /var/opt/gitlab/backups/

# 设置权限
sudo chown git:git /var/opt/gitlab/backups/*.tar

# 执行恢复
sudo gitlab-rake gitlab:backup:restore BACKUP=1711000811_2026_03_21_16.8.3

# 输出示例：
# Unpacking backup tar file ... done
# Restoring database ...
# Restoring PostgreSQL database gitlabhq_production ... done
# Restoring repositories ...
# done
# Restoring uploads ...
# done
```

#### 步骤 4：重新配置并启动

```bash
# 重新配置 GitLab
sudo gitlab-ctl reconfigure

# 启动服务
sudo gitlab-ctl start

# 检查服务状态
sudo gitlab-ctl status

# 验证恢复
# 1. 访问 Web 界面
# 2. 检查项目是否存在
# 3. 测试用户登录
# 4. 验证代码克隆
```

---

### 6.8 定时备份配置

#### 配置系统定时任务

```bash
# 编辑 crontab
sudo crontab -e

# 添加备份任务（每 4 小时备份一次）
0 */4 * * * /opt/gitlab/bin/gitlab-rake gitlab:backup:create CRON=1 >> /var/log/gitlab/backup.log 2>&1

# 每天凌晨 2 点备份配置文件
0 2 * * * /usr/local/bin/gitlab-backup-config.sh >> /var/log/gitlab/config-backup.log 2>&1

# 每天凌晨 3 点同步到异地
0 3 * * * /usr/local/bin/gitlab-sync-remote.sh >> /var/log/gitlab/sync.log 2>&1

# 每周日凌晨 4 点上传到 S3
0 4 * * 0 /usr/local/bin/gitlab-upload-s3.sh >> /var/log/gitlab/s3-upload.log 2>&1
```

#### 监控备份状态

```bash
#!/bin/bash
# /usr/local/bin/gitlab-check-backup.sh

BACKUP_DIR="/var/opt/gitlab/backups"
MAX_AGE=14400  # 4 小时（秒）

# 查找最新备份
LATEST_BACKUP=$(ls -t ${BACKUP_DIR}/*.tar | head -1)

if [ -z "${LATEST_BACKUP}" ]; then
  echo "❌ 未找到备份文件"
  exit 1
fi

# 检查备份时间
BACKUP_TIME=$(stat -c %Y "${LATEST_BACKUP}")
CURRENT_TIME=$(date +%s)
AGE=$((CURRENT_TIME - BACKUP_TIME))

if [ ${AGE} -gt ${MAX_AGE} ]; then
  echo "❌ 警告：备份超过 4 小时未更新"
  echo "最新备份：${LATEST_BACKUP}"
  echo "备份时间：$(date -d @${BACKUP_TIME})"
  exit 1
else
  echo "✅ 备份正常"
  echo "最新备份：${LATEST_BACKUP}"
  echo "备份时间：$(date -d @${BACKUP_TIME})"
  echo "距今：$((AGE / 3600)) 小时"
fi
```

---

## 第 7 章 高可用架构与监控

### 7.1 高可用集群架构设计

#### 架构图

```
                          ┌─────────────────┐
                          │   负载均衡器     │
                          │  (HAProxy +     │
                          │   Keepalived)   │
                          │   10.0.0.100    │
                          │   VIP: 10.0.0.10│
                          └────────┬────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
      ┌───────┴────────┐  ┌───────┴────────┐  ┌───────┴────────┐
      │  GitLab 节点 1  │  │  GitLab 节点 2  │  │  GitLab 节点 3  │
      │  10.0.0.201    │  │  10.0.0.202    │  │  10.0.0.203    │
      │  (Active)      │  │  (Standby)     │  │  (Standby)     │
      │  16GB RAM      │  │  16GB RAM      │  │  16GB RAM      │
      │  8 CPU         │  │  8 CPU         │  │  8 CPU         │
      └───────┬────────┘  └───────┬────────┘  └───────┬────────┘
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   │
                          ┌────────┴────────┐
                          │   PostgreSQL    │
                          │   (主从复制)     │
                          │  10.0.0.210/211 │
                          └────────┬────────┘
                                   │
                          ┌────────┴────────┐
                          │      Redis      │
                          │   (Sentinel)    │
                          │  10.0.0.220/221 │
                          └─────────────────┘
```

#### 组件说明

| 组件 | 数量 | 配置 | 作用 |
|:---|:---:|:---:|:---|
| **负载均衡器** | 2 | 4GB/4CPU | 流量分发、故障转移 |
| **GitLab 节点** | 3 | 16GB/8CPU | 应用服务、无状态 |
| **PostgreSQL** | 2 | 32GB/8CPU | 数据库主从复制 |
| **Redis** | 2 | 8GB/4CPU | 缓存、Sentinel 高可用 |
| **NFS 存储** | 1 | 1TB SSD | 共享文件存储 |

---

### 7.2 主从复制配置

#### PostgreSQL 主从配置

```ruby
# 主节点配置 (gitlab.rb)
postgresql['listen_address'] = '*'
postgresql['max_wal_senders'] = 5
postgresql['wal_keep_segments'] = 100
postgresql['replication_timeout'] = '60s'
postgresql['synchronous_commit'] = 'on'
postgresql['synchronous_standby_names'] = 'gitlab2'

# 启用 SSL 加密复制
postgresql['hostssl'] = [
  {
    'database' => 'all',
    'user' => 'gitlab_replicator',
    'address' => '10.0.0.211/32',
    'method' => 'md5'
  }
]
```

#### 配置从节点

```bash
# 在从节点执行
sudo -u gitlab-psql /opt/gitlab/embedded/bin/pg_basebackup \
  -h 10.0.0.210 \
  -U gitlab_replicator \
  -D /var/opt/gitlab/postgresql/data \
  -Fp -Xs -P -R

# 创建 standby.signal
touch /var/opt/gitlab/postgresql/data/standby.signal

# 配置从节点
cat >> /var/opt/gitlab/postgresql/data/postgresql.auto.conf << EOF
primary_conninfo = 'host=10.0.0.210 user=gitlab_replicator password=replica_password'
EOF
```

---

### 7.3 负载均衡配置

#### HAProxy 配置

```bash
# /etc/haproxy/haproxy.cfg

global
    log         127.0.0.1 local2
    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    maxconn     4000
    user        haproxy
    group       haproxy
    daemon

defaults
    mode                    http
    log                     global
    option                  httplog
    option                  dontlognull
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout http-keep-alive 10s
    timeout check           10s

frontend gitlab_frontend
    bind *:80
    bind *:443 ssl crt /etc/haproxy/certs/gitlab.pem
    default_backend gitlab_backend

backend gitlab_backend
    balance roundrobin
    option httpchk GET /-/health
    http-check expect status 200
    server gitlab1 10.0.0.201:80 check inter 5s fall 3 rise 2
    server gitlab2 10.0.0.202:80 check inter 5s fall 3 rise 2
    server gitlab3 10.0.0.203:80 check inter 5s fall 3 rise 2
```

---

### 7.4 Prometheus 监控对接

#### 启用 GitLab 内置监控

```ruby
# /etc/gitlab/gitlab.rb

# 启用 Prometheus
prometheus['enable'] = true
prometheus['listen_address'] = 'localhost:9090'

# 启用 Node Exporter
node_exporter['enable'] = true

# 启用 GitLab Exporter
gitlab_exporter['enable'] = true
gitlab_exporter['listen_address'] = 'localhost:9122'

# 配置告警
alertmanager['enable'] = true
alertmanager['listen_address'] = 'localhost:9093'
```

#### 配置监控面板

```
访问路径：
http://gitlab.example.com/-/monitoring/dashboard

内置面板：
- System Overview（系统概览）
- API 性能
- 数据库性能
- Redis 性能
- CI/CD 流水线
- 存储使用
```

#### 配置告警规则

```yaml
# /etc/gitlab/prometheus/rules/gitlab-alerts.yml

groups:
  - name: gitlab
    rules:
      - alert: GitLabDown
        expr: probe_success{job="gitlab-health"} == 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "GitLab 服务不可用"
          description: "GitLab 实例 {{ $labels.instance }} 无法访问"

      - alert: HighMemoryUsage
        expr: node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes < 0.1
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "内存使用率过高"
          description: "可用内存低于 10%"

      - alert: DiskSpaceLow
        expr: node_filesystem_avail_bytes / node_filesystem_size_bytes < 0.15
        for: 30m
        labels:
          severity: warning
        annotations:
          summary: "磁盘空间不足"
          description: "可用磁盘空间低于 15%"
```

---

### 7.5 高频故障排查手册

#### 故障 1：502 GitLab is not responding

**症状**：
```
浏览器访问显示 502 错误
GitLab is not responding
```

**排查步骤**：

```bash
# 1. 检查服务状态
sudo gitlab-ctl status

# 2. 检查内存使用
free -h
top -bn1 | grep -E "unicorn|sidekiq"

# 3. 检查 Unicorn 日志
sudo gitlab-ctl tail unicorn

# 4. 查看系统日志
dmesg | grep -i "killed\|oom"

# 5. 检查磁盘空间
df -h
```

**解决方案**：

```bash
# 方案 A：增加内存（推荐）
# 最低 4GB，推荐 8GB+

# 方案 B：减少 Unicorn worker 数量
# 编辑 gitlab.rb
puma['worker_processes'] = 2  # 默认 3

# 方案 C：增加 Swap
sudo fallocate -l 4G /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# 方案 D：重启服务
sudo gitlab-ctl restart
```

#### 故障 2：仓库损坏无法克隆

**症状**：
```bash
git clone git@gitlab.example.com:group/project.git
fatal: Could not read from remote repository.
```

**排查步骤**：

```bash
# 1. 检查仓库完整性
sudo -u gitlab-psql /opt/gitlab/embedded/bin/gitlab-rake \
  gitlab:git:fsck

# 2. 检查 Gitaly 日志
sudo gitlab-ctl tail gitaly

# 3. 检查磁盘空间
df -h /var/opt/gitlab/git-data
```

**解决方案**：

```bash
# 方案 A：修复仓库
sudo -u gitlab-psql /opt/gitlab/embedded/bin/gitlab-rake \
  gitlab:git:fsck REPAIR=true

# 方案 B：从备份恢复
# 参考 6.7 数据恢复流程

# 方案 C：重新克隆
# 从其他备份仓库重新推送
```

#### 故障 3：CI/CD 流水线卡住

**症状**：
```
Pipeline 状态一直为 "Running"
Job 状态为 "Stuck" 或 "Pending"
```

**排查步骤**：

```bash
# 1. 检查 Runner 状态
sudo gitlab-runner list

# 2. 检查 Runner 日志
sudo journalctl -u gitlab-runner -f

# 3. 检查 Docker 服务
docker ps
docker logs <container_id>

# 4. 检查并发限制
# Settings → CI/CD → Runners
```

**解决方案**：

```bash
# 方案 A：重启 Runner
sudo gitlab-runner restart

# 方案 B：清理卡住的 Job
# Web 界面：CI/CD → Jobs → Cancel

# 方案 C：增加 Runner 并发数
# 编辑 config.toml
concurrent = 8  # 增加并发数

# 方案 D：检查 Docker 资源
docker system prune -a  # 清理未使用资源
```

#### 故障 4：数据库连接失败

**症状**：
```
Error connecting to database
PG::ConnectionBad: could not connect to server
```

**排查步骤**：

```bash
# 1. 检查 PostgreSQL 状态
sudo gitlab-ctl status postgresql

# 2. 检查数据库日志
sudo gitlab-ctl tail postgresql

# 3. 测试本地连接
sudo -u gitlab-psql /opt/gitlab/embedded/bin/psql \
  -h /var/opt/gitlab/postgresql \
  -U gitlab

# 4. 检查连接数
sudo -u gitlab-psql /opt/gitlab/embedded/bin/psql \
  -c "SELECT count(*) FROM pg_stat_activity;"
```

**解决方案**：

```bash
# 方案 A：重启 PostgreSQL
sudo gitlab-ctl restart postgresql

# 方案 B：增加最大连接数
# 编辑 gitlab.rb
postgresql['max_connections'] = 1000  # 默认 800

# 方案 C：清理空闲连接
sudo -u gitlab-psql /opt/gitlab/embedded/bin/psql \
  -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state = 'idle';"
```

#### 故障 5：SSH 克隆失败

**症状**：
```bash
ssh: connect to host gitlab.example.com port 22: Connection refused
fatal: Could not read from remote repository.
```

**排查步骤**：

```bash
# 1. 测试 SSH 连接
ssh -v -T -p 22 git@gitlab.example.com

# 2. 检查 SSH 服务
sudo gitlab-ctl status gitlab-shell

# 3. 检查 SSH 密钥
ssh-add -l

# 4. 检查防火墙
sudo firewall-cmd --list-all
```

**解决方案**：

```bash
# 方案 A：重启 gitlab-shell
sudo gitlab-ctl restart gitlab-shell

# 方案 B：重新添加 SSH 密钥
# Settings → SSH Keys → Add key

# 方案 C：检查 SSH 配置
# 编辑 /etc/ssh/sshd_config
# 确保 Port 22 未被注释

# 方案 D：放行防火墙
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

---

## 🎯 实战练习

### 练习 1：部署 GitLab 生产环境

```bash
目标：在 CentOS 8 服务器部署 GitLab 16.x LTS

步骤：
1. 系统优化（Swap、内核参数）
2. 配置官方 YUM 源（GPG 校验）
3. 安装 GitLab 16.8.3
4. 配置 HTTPS（Let's Encrypt）
5. 启用双因素认证
6. 配置备份策略
```

### 练习 2：配置企业级权限

```bash
目标：实现完整的权限管理体系

步骤：
1. 创建组结构（公司→部门→团队）
2. 创建用户并启用 2FA
3. 配置 SSH 密钥（ed25519）
4. 设置分支保护规则
5. 配置合并请求审批
6. 配置代码提交门禁
```

### 练习 3：搭建 CI/CD 流水线

```bash
目标：实现自动化构建→测试→部署

步骤：
1. 部署 GitLab Runner
2. 配置 .gitlab-ci.yml
3. 配置环境变量和密钥
4. 配置质量门禁
5. 配置通知告警
6. 测试完整流水线
```

### 练习 4：备份与恢复演练

```bash
目标：掌握完整备份恢复流程

步骤：
1. 配置本地备份路径
2. 配置异地备份（rsync/S3）
3. 执行完整备份
4. 备份完整性校验
5. 模拟数据恢复
6. 验证恢复结果
```

---

## 📚 相关文档

- **Git 基础回顾** - [01-Git 基础回顾.md](./01-Git 基础回顾.md)
- **Jenkins 持续集成** - [03-Jenkins 持续集成.md](./03-Jenkins 持续集成.md)
- **SonarQube 代码质量** - [04-SonarQube 代码质量.md](./04-SonarQube 代码质量.md)
- **GitLab 官方文档** - https://docs.gitlab.com/
- **GitLab 版本计划** - https://about.gitlab.com/releases/categories/releases/

---

## 🔒 安全检查清单

部署前请确认：

- [ ] 系统已更新最新安全补丁
- [ ] 防火墙已正确配置
- [ ] HTTPS 证书已配置
- [ ] 管理员启用 2FA
- [ ] SSH 密钥使用 ed25519
- [ ] 分支保护规则已配置
- [ ] 合并请求审批已启用
- [ ] 备份策略已实施
- [ ] 监控告警已配置
- [ ] 审计日志已启用

---

**文档版本**: v2.0  
**GitLab 版本**: 16.8.3 LTS  
**更新时间**: 2026-03-21  
**作者**: hjs2015 <1656126280@qq.com>  
**仓库地址**: https://github.com/hjs2015/git-tutorial  
**许可证**: CC BY-SA 4.0

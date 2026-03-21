# GitLab 企业级代码管理实战教程

> 📘 **CI/CD 实战版教程第二部分**  
> 📌 包含：安装部署、权限管理、CI/CD 配置、备份恢复、高可用架构、工具链集成  
> 🚀 **版本**: GitLab 16.x LTS | **系统**: CentOS 8/9, RHEL 8/9, Ubuntu 20.04+  
> 🔒 **安全**: GPG 校验、HTTPS、2FA、审计日志、分支保护、LDAP 集成

---

## 📑 快速索引

### 部署方案选型
- [3.1 部署方案选型指南](#31-部署方案选型指南) - 快速选择适合的部署方式
  - [三种部署方案对比](#三种部署方案对比) - 详细对比表
  - [方案 A：原生安装](#方案-a 原生安装推荐生产环境) - 适用场景/优缺点/典型案例
  - [方案 B：Docker 部署](#方案-b-docker 部署推荐测试小团队) - 适用场景/优缺点/典型案例
  - [方案 C：Kubernetes 部署](#方案-c-kubernetes 部署推荐大型企业) - 适用场景/优缺点/典型案例
  - [选型决策树](#选型决策树) - 快速决策流程
  - [快速选型表](#快速选型表) - 按企业特征推荐
- [3.2 环境准备与硬件要求](#32-环境准备与硬件要求)
- [3.3 系统优化与依赖安装](#33-系统优化与依赖安装)

### 安装部署
- [3.4 配置官方 YUM 源（含 GPG 校验）](#34-配置官方 yum 源含 gpg 校验)
- [3.5 安装 GitLab LTS 版本](#35-安装-gitlab-lts-版本)
- [3.6 配置 external_url 与 HTTPS](#36-配置-external_url-与-https)
- [3.7 初始化配置与访问](#37-初始化配置与访问)
- [3.8 Docker 容器化部署方案](#38-docker 容器化部署方案)
- [3.9 Kubernetes 集群部署方案](#39-kubernetes 集群部署方案)
- [3.10 常用命令与故障排查](#310-常用命令与故障排查)

### 权限管理
- [第 4 章 GitLab 权限管理](#第 4 章-gitlab 权限管理)
- [4.11 权限矩阵最佳实践](#411-权限矩阵最佳实践)
  - [企业权限矩阵示例](#企业权限矩阵示例) - 角色权限对照表
  - [基于部门的权限配置](#基于部门的权限配置) - 研发/运维/安全部门
  - [基于项目的权限配置](#基于项目的权限配置) - 核心项目/公共库
  - [基于分支的精细化权限](#基于分支的精细化权限) - 保护分支配置
- [4.12 审计日志与操作追溯](#412-审计日志与操作追溯)
  - [审计日志查看](#审计日志查看) - 事件类型/筛选/导出
  - [操作追溯示例](#操作追溯示例) - 权限变更/代码删除/密钥泄露
- [4.13 企业安全增强配置](#413-企业安全增强配置)
  - [敏感信息检测](#敏感信息检测) - 密钥扫描/模式识别
  - [IP 白名单配置](#ip 白名单配置) - GitLab 配置/防火墙规则
  - [双因素认证强制启用](#双因素认证 2fa 强制启用) - 策略配置/用户指南
  - [会话管理](#会话管理) - 超时配置/活跃会话查看

### CI/CD 实战
- [第 5 章 GitLab CI/CD 实战](#第 5 章-gitlab-cicd 实战)
- [5.4 多技术栈 CI/CD 模板](#54-多技术栈-cicd 模板)
  - [模板 1：Java/Maven](#模板-1java-maven 项目) - Spring Boot 示例
  - [模板 2：Node.js/前端](#模板-2-nodejs 前端项目) - React/Vue 示例
  - [模板 3：Python 项目](#模板-3python 项目) - Django/Flask 示例
  - [模板 4：Go 项目](#模板-4-go-项目) - Go 微服务示例
  - [模板 5：PHP 项目](#模板-5php 项目 laravel) - Laravel 示例
  - [模板 6：.NET Core 项目](#模板-6-net-core 项目) - ASP.NET Core 示例
  - [模板 7：多项目 Monorepo](#模板-7 多项目-monorepo) - 前后端分离示例
- [5.5 流水线高级配置](#55-流水线高级配置)
  - [缓存配置优化](#缓存配置优化) - 各技术栈缓存最佳实践
  - [Artifacts 产物管理](#artifacts 产物管理) - 报告类型/配置示例
  - [定时任务配置](#定时任务配置) - Cron 表达式/配置步骤
  - [触发规则详解](#触发规则详解) - 触发源/分支条件/手动触发
  - [流水线常见问题排查](#流水线常见问题排查) - 5 大高频问题
- [5.6 环境变量与密钥管理](#56-环境变量与密钥管理)

### 工具链集成
- [第 8 章 工具链生态集成](#第 8 章-工具链生态集成)
- [8.1 工具链集成概览](#81-工具链集成概览) - 工具对比表
- [8.2 SonarQube 代码质量集成](#82-sonarqube 代码质量集成)
- [8.3 Nexus 制品库集成](#83-nexus 制品库集成)
- [8.4 钉钉/企业微信通知](#84-钉钉企业微信通知)
- [8.5 LDAP 统一认证集成](#85-ldap 统一认证集成)

### 运维监控
- [第 7 章 高可用架构与监控](#第 7 章-高可用架构与监控)
- [7.4 Prometheus 监控对接](#74-prometheus 监控对接)
- [7.5 高频故障排查手册](#75-高频故障排查手册)
- [7.6 GitLab 性能调优](#76-gitlab 性能调优)
  - [Unicorn/Puma 配置优化](#unicorn-puma 配置优化) - Worker 数量计算
  - [数据库优化](#数据库优化) - PostgreSQL 配置/维护
  - [Redis 优化](#redis 优化) - 配置/监控
  - [大仓库处理方案](#大仓库处理方案) - Git LFS/清理历史
  - [Gitaly 优化](#gitaly 优化) - 并发配置
  - [Nginx 优化](#nginx 优化) - Worker/HTTP2/Gzip
  - [Sidekiq 优化](#sidekiq 优化) - 并发/队列监控
  - [性能监控指标](#性能监控指标) - 关键指标/健康值
- [7.7 日常维护与巡检](#77-日常维护与巡检)
  - [服务状态巡检脚本](#服务状态巡检脚本)
  - [Grafana 监控面板](#grafana 监控面板) - 推荐面板/导入方法
  - [告警规则配置](#告警规则配置) - Prometheus 规则
  - [日常维护周期建议](#日常维护周期建议) - 每天/每周/每月/每季度

### 备份容灾
- [第 6 章 GitLab 备份与容灾](#第 6 章-gitlab 备份与容灾)
- [6.9 备份自动清理策略](#69-备份自动清理策略)
  - [本地备份清理](#本地备份清理) - 基础脚本/增强脚本
  - [备份保留策略建议](#备份保留策略建议) - 各环境保留时间
  - [S3 备份生命周期策略](#s3 备份生命周期策略) - 自动归档
- [6.10 跨区域容灾方案](#610-跨区域容灾方案)
  - [容灾架构设计](#容灾架构设计) - 主从热备/双活集群/冷备份
  - [跨区域同步方案](#跨区域同步方案) - 完整同步脚本
  - [故障切换流程](#故障切换流程) - 检查清单/DNS 切换
  - [备份恢复演练](#备份恢复演练) - 演练计划/测试脚本
  - [容灾演练报告模板](#容灾演练报告模板)

### 快速参考
- [附录 A：快速参考卡片](#附录 a 快速参考卡片)
- [附录 B：常见问题 FAQ](#附录 b 常见问题-faq)

---

## 第 3 章 GitLab 安装部署

### 3.1 部署方案选型指南

> 💡 **如何选择部署方案？**
> 
> 根据企业规模、团队人数、运维能力选择最适合的部署方式，避免过度设计或资源不足。
> 
> **快速决策指南**：
> - 👤 **个人/小团队（<10 人）** → Docker 部署（10 分钟快速搭建）
> - 🏢 **中型企业（10-200 人）** → 原生安装（性能最优，稳定可靠）
> - 🏭 **大型企业（200 人+）** → Kubernetes 集群（高可用，弹性伸缩）

#### 三种部署方案对比

| 对比维度 | 原生安装 | Docker 部署 | Kubernetes |
|:---|:---|:---|:---|
| **部署难度** | ⭐⭐ 中等 | ⭐ 简单 | ⭐⭐⭐⭐ 复杂 |
| **运维成本** | ⭐⭐⭐ 中等 | ⭐⭐ 较低 | ⭐⭐⭐⭐⭐ 高 |
| **扩展性** | ⭐⭐ 有限 | ⭐⭐⭐ 较好 | ⭐⭐⭐⭐⭐ 优秀 |
| **资源利用** | ⭐⭐⭐ 固定 | ⭐⭐⭐ 可限制 | ⭐⭐⭐⭐⭐ 动态 |
| **升级难度** | ⭐⭐⭐ 较复杂 | ⭐⭐ 简单 | ⭐⭐⭐⭐ 复杂 |
| **适合团队** | 50-200 人 | 10-100 人 | 200 人 + |
| **内存需求** | 8GB+ | 4GB+ | 16GB+ (集群) |
| **部署时间** | 30-60 分钟 | 10-20 分钟 | 2-4 小时 |
| **高可用** | 需手动配置 | 需手动配置 | ✅ 自动故障转移 |
| **备份恢复** | 手动脚本 | 卷挂载 | 快照 + 卷 |
| **网络配置** | 简单 | 端口映射 | Service/Ingress |
| **存储方案** | 本地磁盘 | Docker Volume | PV/PVC/StorageClass |
| **监控集成** | 手动配置 | 手动配置 | ✅ Prometheus Operator |
| **日志收集** | 本地文件 | 需配置驱动 | ✅ EFK/ELK Stack |
| **成本估算** | ¥500-2000/月 | ¥300-1000/月 | ¥2000-10000/月 |

> ⚠️ **成本说明**：以上为云服务器估算成本（阿里云/腾讯云），包含计算、存储、网络费用。

#### 方案 A：原生安装（推荐生产环境）

**适用场景**：
- ✅ 企业生产环境（50-200 人团队）
- ✅ 有专职运维人员（至少 1 名）
- ✅ 需要长期稳定运行（99.9% 可用性）
- ✅ 服务器资源充足（8GB+ 内存）
- ✅ 需要完整功能支持
- ✅ 代码仓库数量 >100 个
- ✅ 日均 CI/CD 流水线 >50 次

**优点**：
- 🚀 性能最优（无容器开销，直接访问硬件）
- 📚 官方原生支持（文档齐全，社区活跃）
- 🔍 故障排查简单（日志清晰，工具完善）
- 📖 社区文档丰富（问题容易找到解决方案）
- 🔧 系统级调优（可优化内核参数、文件系统）
- 💰 成本可控（无额外容器管理开销）

**缺点**：
- ⏱️ 部署时间较长（30-60 分钟）
- 📦 系统依赖较多（需安装多个系统包）
- 🛑 升级需要停机（需维护窗口）
- 🔒 系统耦合度高（可能影响其他服务）

**典型企业案例**：
```
某金融科技公司（150 人研发团队）
- 服务器配置：16GB 内存，8 核 CPU，500GB SSD
- 仓库数量：300+
- 日均流水线：200+
- 可用性：99.95%
- 运维团队：2 名专职运维
```

#### 方案 B：Docker 部署（推荐测试/小团队）

**适用场景**：
- ✅ 测试/开发环境
- ✅ 小团队（10-100 人）
- ✅ 快速搭建演示环境
- ✅ 资源有限（4GB 内存）
- ✅ 需要频繁升级
- ✅ 代码仓库数量 <50 个
- ✅ 日均 CI/CD 流水线 <20 次
- ✅ 无专职运维，开发人员兼任

**优点**：
- ⚡ 部署快速（10 分钟完成）
- 📦 环境隔离好（不影响宿主机）
- 🔄 升级简单（换镜像即可）
- 🎯 资源可限制（CPU/内存限制）
- 🗑️ 清理方便（删除容器即可）
- 📋 配置可移植（docker-compose 文件）

**缺点**：
- 🐌 性能略有损耗（~5% 容器开销）
- 🐳 Docker 依赖（需安装 Docker）
- 🌐 网络配置复杂（端口映射、桥接）
- 💾 数据持久化需注意（卷挂载）
- 🔍 故障排查较复杂（需懂 Docker 命令）

**典型企业案例**：
```
某创业公司（30 人研发团队）
- 服务器配置：8GB 内存，4 核 CPU，200GB SSD
- 仓库数量：25
- 日均流水线：15
- 可用性：99.5%
- 运维：开发人员轮值
```

#### 方案 C：Kubernetes 部署（推荐大型企业）

**适用场景**：
- ✅ 大型企业（200 人+）
- ✅ 高可用要求（99.9% SLA）
- ✅ 已有 K8s 集群
- ✅ 需要弹性伸缩
- ✅ 多租户隔离
- ✅ 代码仓库数量 >500 个
- ✅ 日均 CI/CD 流水线 >200 次
- ✅ 全球化团队（多地域访问）

**优点**：
- 🛡️ 高可用自动故障转移（Pod 自动重启）
- 📈 弹性伸缩（HPA 自动扩缩容）
- 💎 资源利用率高（多服务共享集群）
- 🏢 多租户隔离（Namespace 隔离）
- 🔄 滚动更新无停机（Rolling Update）
- 📊 原生监控集成（Prometheus Operator）
- 🌍 多集群管理（Federation）

**缺点**：
- 🎓 部署复杂度高（需配置 Helm Chart）
- 👨‍💻 需要 K8s 专业知识（学习曲线陡峭）
- 💸 运维成本高（需专职 K8s 团队）
- 🐛 故障排查困难（多层抽象）
- 📦 资源开销大（K8s 自身占用资源）

**典型企业案例**：
```
某互联网上市公司（800 人研发团队）
- K8s 集群：3 Master + 10 Worker
- 仓库数量：1200+
- 日均流水线：800+
- 可用性：99.99%
- 运维团队：5 名专职 SRE
- 地域：北京、上海、深圳三地域部署
```

#### 选型决策树

```
开始
  │
  ├─ 团队人数 < 50 人？
  │   ├─ 是 → Docker 部署（快速简单）
  │   └─ 否 → 继续判断
  │
  ├─ 有 K8s 集群且运维成熟？
  │   ├─ 是 → Kubernetes 部署（高可用）
  │   └─ 否 → 继续判断
  │
  ├─ 生产环境且有专职运维？
  │   ├─ 是 → 原生安装（性能最优）
  │   └─ 否 → Docker 部署
  │
  ├─ 高可用要求（99.9% SLA）？
  │   ├─ 是 → Kubernetes 或 原生集群
  │   └─ 否 → 继续判断
  │
  ├─ 仓库数量 > 500 或 日均流水线 > 200？
  │   ├─ 是 → Kubernetes（弹性伸缩）
  │   └─ 否 → 原生安装
  │
  └─ 预算有限（<¥1000/月）？
      ├─ 是 → Docker 部署（单服务器）
      └─ 否 → 原生安装（生产推荐）
```

#### 快速选型表

| 企业特征 | 推荐方案 | 理由 |
|:---|:---|:---|
| 个人开发者 | Docker | 快速搭建，零成本 |
| 创业团队（<30 人） | Docker | 成本低，部署快 |
| 成长型企业（30-100 人） | 原生安装 | 性能稳定，易维护 |
| 中型企业（100-300 人） | 原生安装 + HA | 高可用，性能优 |
| 大型企业（300 人+） | Kubernetes | 弹性伸缩，多租户 |
| 金融/政企 | 原生安装 | 安全合规，审计完善 |
| 互联网公司 | Kubernetes | 快速迭代，DevOps |
| 外包/多项目 | Kubernetes | 多租户隔离 |
| 测试/开发环境 | Docker | 快速重建，成本低 |
| 演示/POC | Docker | 10 分钟部署 |

---

### 3.2 环境准备与硬件要求

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

---

### 3.3 系统优化与依赖安装

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
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload

# Ubuntu (ufw)
sudo ufw allow http
sudo ufw allow https
sudo ufw allow ssh
sudo ufw enable

# 验证防火墙规则
sudo firewall-cmd --list-all
# 或
sudo ufw status
```

⚠️ **注意**：生产环境建议仅开放必要端口，可通过负载均衡器统一入口。

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

### 3.4 配置官方 YUM 源（含 GPG 校验）

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

---

### 3.5 安装 GitLab LTS 版本

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

### 3.6 配置 external_url 与 HTTPS

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

### 3.7 初始化配置与访问

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

### 3.8 Docker 容器化部署方案

#### 方案优势对比

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

#### 步骤 4：Docker Compose 部署（推荐）

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

### 3.9 Kubernetes 集群部署方案

> 💡 **适用场景**：大型企业（200 人+）、高可用要求、已有 K8s 集群

#### 步骤 1：添加 Helm Chart

```bash
# 添加 GitLab Helm Chart 仓库
helm repo add gitlab https://charts.gitlab.io/
helm repo update

# 查看可用版本
helm search repo gitlab
```

#### 步骤 2：创建命名空间

```bash
kubectl create namespace gitlab-system
```

#### 步骤 3：配置 values.yaml

```yaml
# gitlab-values.yaml

global:
  hosts:
    domain: gitlab.example.com
    https: true
  
  ingress:
    configureCertmanager: false
    class: nginx
    tls:
      enabled: true
      secretName: gitlab-tls
  
  gitlab:
    email:
      from: gitlab@example.com
      reply_to: noreply@example.com
  
gitlab-runner:
  install: true
  runners:
    config: |
      [[runners]]
        executor = "kubernetes"
        [runners.kubernetes]
          namespace = "gitlab-runners"
          privileged = true

registry:
  enabled: true

certmanager:
  install: false

nginx-ingress:
  enabled: true

gitlab:
  webservice:
    replicas: 3
    resources:
      requests:
        cpu: 500m
        memory: 2Gi
      limits:
        cpu: 2000m
        memory: 4Gi
  
  sidekiq:
    replicas: 3
    resources:
      requests:
        cpu: 500m
        memory: 2Gi
  
  postgresql:
    replicas: 1
    persistence:
      size: 50Gi
  
  redis:
    replicas: 1
    persistence:
      size: 10Gi
```

#### 步骤 4：安装 GitLab

```bash
# 安装 GitLab（耗时 10-20 分钟）
helm install gitlab gitlab/gitlab \
  --namespace gitlab-system \
  -f gitlab-values.yaml \
  --timeout 600s

# 查看安装状态
helm status gitlab -n gitlab-system

# 查看 Pod 状态
kubectl get pods -n gitlab-system
```

#### 步骤 5：配置 Ingress

```yaml
# gitlab-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: gitlab-ingress
  namespace: gitlab-system
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/proxy-body-size: "0"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "600"
spec:
  tls:
  - hosts:
    - gitlab.example.com
    secretName: gitlab-tls
  rules:
  - host: gitlab.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: webservice
            port:
              number: 8181
```

```bash
# 应用 Ingress
kubectl apply -f gitlab-ingress.yaml
```

---

### 3.10 常用命令与故障排查

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

### 4.11 权限矩阵最佳实践

#### 企业权限矩阵示例

| 角色 | 组级别 | 项目级别 | 分支权限 | MR 审批 | 部署权限 | CI/CD 变量 | 审计日志 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **CTO** | Owner | Owner | 所有分支 | ✅ | ✅ | ✅ | ✅ |
| **技术经理** | Maintainer | Maintainer | 保护分支 | ✅ | ✅ | ✅ | ✅ |
| **高级开发** | Developer | Developer | 功能分支 | ✅ | 测试环境 | ❌ | ❌ |
| **初级开发** | Developer | Developer | 功能分支 | ❌ | ❌ | ❌ | ❌ |
| **测试人员** | Reporter | Reporter | 只读 | ❌ | ❌ | ❌ | ❌ |
| **运维人员** | Developer | Maintainer | 保护分支 | ✅ | 生产环境 | ✅ | ✅ |
| **产品经理** | Reporter | Reporter | 只读 | ✅ | ❌ | ❌ | ❌ |
| **外部顾问** | Guest | Guest | 只读 | ❌ | ❌ | ❌ | ❌ |
| **安全审计** | Reporter | Reporter | 只读 | ❌ | ❌ | ❌ | ✅ |

> 💡 **权限设计原则**：
> - **最小权限原则**：只授予完成工作所需的最小权限
> - **职责分离原则**：开发、测试、部署权限分离
> - **审计可追溯**：关键操作必须记录审计日志
> - **定期审查**：每季度审查权限分配

#### 基于部门的权限配置

**研发部（rd）**：
```
rd-group (研发组)
├── 组长：Owner
│   ├── 创建/删除项目
│   ├── 管理组成员
│   └── 查看所有审计日志
├── 高级开发：Maintainer
│   ├── 管理保护分支
│   ├── 审批 MR
│   └── 管理 CI/CD 变量
├── 开发：Developer
│   ├── 创建分支
│   ├── 创建 MR
│   └── 查看 CI/CD 流水线
├── 测试：Reporter
│   ├── 查看代码
│   ├── 创建 Issue
│   └── 查看流水线结果
└── 产品：Reporter
    ├── 查看代码
    ├── 管理 Issue
    └── 管理 Milestone
```

**运维部（ops）**：
```
ops-group (运维组)
├── 经理：Owner
│   ├── 管理所有环境
│   └── 查看审计日志
├── 运维：Maintainer（所有项目）
│   ├── 生产环境部署
│   ├── 管理环境变量
│   └── 查看监控告警
└── DBA: Maintainer（数据库项目）
    ├── 数据库变更
    └── 备份恢复
```

**安全部（security）**：
```
security-group (安全组)
├── 经理：Owner
│   └── 管理安全策略
├── 审计：Reporter（所有项目，只读）
│   ├── 查看审计日志
│   ├── 查看安全报告
│   └── 查看合规性
└── 渗透测试：Developer（仅测试项目）
    ├── 安全测试
    └── 漏洞扫描
```

#### 基于项目的权限配置

**核心项目（backend-api）**：
```yaml
项目名称：backend-api
访问级别：Private
成员权限:
  - tech-lead: Maintainer
  - senior-dev: Developer
  - junior-dev: Developer (仅功能分支)
  - tester: Reporter
分支保护:
  - main:
    - 允许推送：Maintainer  only
    - 允许合并：Maintainer only
    - 需要审批：2 人
    - 需要 CI 通过：是
  - develop:
    - 允许推送：Developer+
    - 允许合并：Maintainer only
    - 需要审批：1 人
    - 需要 CI 通过：是
  - feature/*:
    - 允许推送：创建者
    - 允许合并：Developer+
    - 需要审批：1 人
    - 需要 CI 通过：是
部署权限:
  - 测试环境：Developer+
  - 预发布环境：Maintainer+
  - 生产环境：运维人员 only
CI/CD 变量:
  - 生产密钥：Protected + Masked (仅 Maintainer)
  - 测试密钥：Unprotected (Developer 可用)
```

**公共库（frontend-components）**：
```yaml
项目名称：frontend-components
访问级别：Internal (公司内部可见)
成员权限:
  - 组件团队：Maintainer
  - 其他开发：Developer
分支保护:
  - main:
    - 允许推送：Maintainer only
    - 需要审批：2 人
    - 需要 CI 通过：是
特殊规则:
  - 允许外部贡献：是（通过 MR）
  - 需要签署 CLA: 是
```

#### 基于分支的精细化权限

**保护分支配置**：
```
1. 项目 → Settings → Repository
2. 展开 "Protected branches"
3. 配置分支规则：

Branch: main
- Allowed to merge: Maintainers
- Allowed to push: No one
- Allowed to force push: No
- Enable commit signature requirement: Yes (可选)

Branch: develop
- Allowed to merge: Maintainers + Developers
- Allowed to push: Maintainers
- Allowed to force push: No

Branch: release/*
- Allowed to merge: Maintainers
- Allowed to push: Maintainers
- Allow force push: No
```

**分支保护级别对比**：

| 保护级别 | 推送权限 | 合并权限 | 强制推送 | 删除分支 | 适用场景 |
|:---|:---|:---|:---|:---|:---|
| **No one** | ❌ 禁止 | Maintainer | ❌ | ❌ | main 分支 |
| **Developers** | Developer+ | Developer+ | ❌ | ❌ | develop 分支 |
| **Developers + Maintainers** | Developer+ | Maintainer | ❌ | ❌ | release 分支 |
| **Maintainers** | Maintainer only | Maintainer only | ❌ | ❌ | 热修复分支 |

---

### 4.12 审计日志与操作追溯

#### 审计日志查看

**访问审计日志**：
```
1. Admin Area（管理员区域）→ Monitoring → Audit Log
2. 或使用项目级别：Project → Settings → Audit Log
```

**审计日志内容**：
```yaml
审计事件类型:
  - project_create: 项目创建
  - project_destroy: 项目删除
  - project_transfer: 项目转移
  - user_add_to_group: 用户添加到组
  - user_remove_from_group: 用户从组移除
  - user_add_to_project: 用户添加到项目
  - user_remove_from_project: 用户从项目移除
  - project_access_token_created: 项目 Token 创建
  - project_access_token_revoked: 项目 Token 撤销
  - branch_protect_rule_created: 分支保护创建
  - branch_protect_rule_destroyed: 分支保护删除
  - approval_rule_created: 审批规则创建
  - approval_rule_updated: 审批规则更新
  - ci_variable_created: CI 变量创建
  - ci_variable_updated: CI 变量更新
  - ci_variable_destroyed: CI 变量删除
  - webhook_created: Webhook 创建
  - webhook_destroyed: Webhook 删除
```

**审计日志筛选**：
```bash
# 按时间筛选
2026-03-20 - 2026-03-21

# 按事件类型筛选
- 仅显示权限变更
- 仅显示项目操作
- 仅显示 CI/CD 操作

# 按用户筛选
- 特定用户的所有操作

# 按项目筛选
- 特定项目的所有操作
```

**导出审计日志**：
```bash
# API 导出
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/audit_events"

# 按时间范围导出
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/audit_events?created_after=2026-03-01&created_before=2026-03-31"

# 导出为 JSON
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/audit_events" | jq .
```

#### 操作追溯示例

**追溯权限变更**：
```
场景：发现某用户获得了不应有的权限

追溯步骤：
1. Admin Area → Audit Log
2. 筛选条件：
   - Event type: user_add_to_group, user_add_to_project
   - User: 目标用户
   - Date range: 最近 30 天
3. 查看：
   - 谁授予的权限
   - 授予时间
   - 授予的权限级别
4. 如有异常，立即撤销权限并调查
```

**追溯代码删除**：
```
场景：重要代码被删除

追溯步骤：
1. 项目 → Repository → Branches
2. 查看已删除分支（需要审计日志）
3. Audit Log 筛选：
   - Event type: branch_destroyed
   - Date range: 删除时间范围
4. 查看：
   - 谁删除的分支
   - 删除时间
   - 分支最后提交
5. 从备份恢复（如有必要）
```

**追溯密钥泄露**：
```
场景：CI/CD 密钥可能泄露

追溯步骤：
1. 项目 → Settings → CI/CD → Variables
2. 查看变量审计日志
3. Audit Log 筛选：
   - Event type: ci_variable_created, ci_variable_updated
   - Variable name: 敏感变量名
4. 查看：
   - 谁创建/修改了变量
   - 创建/修改时间
   - 变量值变更历史
5. 立即轮换密钥（撤销旧密钥，创建新密钥）
```

---

### 4.13 企业安全增强配置

#### 敏感信息检测

**启用密钥扫描**：
```
1. Admin Area → Settings → General
2. 展开 "Secret detection"
3. 启用：
   - ✅ Enable secret detection in CI/CD pipelines
   - ✅ Block pipelines with detected secrets
```

**常见敏感信息模式**：
```yaml
AWS 密钥:
  - AKIA[0-9A-Z]{16}  # Access Key ID
  - [A-Za-z0-9/+=]{40}  # Secret Access Key

GitHub Token:
  - ghp_[A-Za-z0-9]{36}  # Personal Access Token
  - gho_[A-Za-z0-9]{36}  # OAuth Token
  - ghu_[A-Za-z0-9]{36}  # User-to-Server Token
  - ghs_[A-Za-z0-9]{36}  # Server-to-Server Token
  - ghr_[A-Za-z0-9]{36}  # Refresh Token

私钥:
  - -----BEGIN RSA PRIVATE KEY-----
  - -----BEGIN OPENSSH PRIVATE KEY-----

数据库连接字符串:
  - mysql://user:password@host:port/db
  - postgresql://user:password@host:port/db
  - mongodb://user:password@host:port/db

API 密钥:
  - [A-Za-z0-9]{32}  # 通用 API Key
  - sk-[A-Za-z0-9]{48}  # OpenAI API Key
```

**手动扫描代码库**：
```bash
# 使用 truffleHog 扫描
docker run --rm -it -v "$(pwd)":/code trufflesecurity/trufflehog \
  git file:///code --only-verified

# 使用 GitLeaks 扫描
docker run --rm -it -v "$(pwd)":/code zricethezav/gitleaks \
  detect -v /code

# 查看扫描结果
# 发现密钥立即撤销并轮换
```

#### IP 白名单配置

**配置 IP 白名单**：
```ruby
# /etc/gitlab/gitlab.rb

# 限制 GitLab Web 访问
nginx['allowlist'] = [
  '10.0.0.0/8',      # 内网
  '192.168.1.0/24',  # 办公网
  '203.0.113.50'     # 特定 IP
]

# 限制 Git SSH 访问
gitlab_rails['gitlab_shell_allowlist'] = [
  '10.0.0.0/8',
  '192.168.1.0/24'
]

# 应用配置
sudo gitlab-ctl reconfigure
```

**防火墙规则**：
```bash
# CentOS/RHEL (firewalld)
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.0.0.0/8" port port="443" protocol="tcp" accept'
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" port port="443" protocol="tcp" accept'
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="443" protocol="tcp" reject'
sudo firewall-cmd --reload

# Ubuntu (ufw)
sudo ufw allow from 10.0.0.0/8 to any port 443 proto tcp
sudo ufw allow from 192.168.1.0/24 to any port 443 proto tcp
sudo ufw deny 443/tcp
sudo ufw enable
```

#### 双因素认证（2FA）强制启用

**强制 2FA 策略**：
```
1. Admin Area → Settings → General
2. 展开 "Account and limit"
3. 启用：
   - ✅ Enforce two-factor authentication for all users
   - ✅ Allow users to request two-factor authentication enforcement
4. 设置宽限期：7 天（给用户时间配置）
```

**2FA 配置指南（发给用户）**：
```
各位同事：

为提高账户安全性，公司要求所有 GitLab 用户启用双因素认证（2FA）。

配置步骤：
1. 下载安装认证 App：
   - Google Authenticator (iOS/Android)
   - Authy (iOS/Android/桌面)
   - Microsoft Authenticator (iOS/Android)

2. GitLab 配置：
   - 登录 GitLab
   - 点击头像 → Settings
   - 点击 "Account"
   - 点击 "Enable two-factor authentication"
   - 使用 App 扫描二维码
   - 输入验证码确认
   - 保存恢复码（重要！）

3. 恢复码保存：
   - 打印保存
   - 或存入密码管理器
   - 丢失后无法恢复账户！

截止日期：2026-04-01
逾期未配置将暂停账户访问权限。

IT 部门
```

#### 会话管理

**会话超时配置**：
```ruby
# /etc/gitlab/gitlab.rb

# 会话超时时间（秒）
gitlab_rails['session_expire_delay'] = 7200  # 2 小时

# 强制登出闲置用户
gitlab_rails['logout_timeout'] = 86400  # 24 小时

# 应用配置
sudo gitlab-ctl reconfigure
```

**查看活跃会话**：
```
1. 用户设置 → Account
2. 查看 "Active sessions"
3. 可撤销可疑会话
```

**会话审计**：
```bash
# API 查看用户会话
curl --header "PRIVATE-TOKEN: <admin_token>" \
  "https://gitlab.example.com/api/v4/users/:id/sessions"
```

---

# 普通项目（internal-tools）
- 访问级别：Internal
- 分支保护：main（仅 Maintainer 推送）
- MR 审批：至少 1 人
- 部署权限：开发人员（测试环境）

# 开源项目（open-source）
- 访问级别：Public
- 分支保护：main（仅 Maintainer 推送）
- MR 审批：至少 1 人
- 部署权限：自动
```

---

## 第 5 章 GitLab CI/CD 实战

### 5.1 CI/CD 核心概念

#### 什么是 CI/CD？

**CI/CD** 是 **持续集成（Continuous Integration）**、**持续交付（Continuous Delivery）** 和 **持续部署（Continuous Deployment）** 的统称，是现代软件开发的自动化实践。

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   代码提交   │ →  │  持续集成   │ →  │  持续交付   │ →  │  持续部署   │
│  Commit     │    │     CI      │    │     CD      │    │     CD      │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                        ↓                  ↓                  ↓
                   自动构建测试         自动发布到         自动部署到
                   自动代码检查         预发布环境         生产环境
```

#### CI/CD 三阶段详解

| 阶段 | 英文 | 含义 | 自动化程度 | 人工干预 |
|:---|:---|:---|:---:|:---:|
| **持续集成** | CI | 频繁集成代码，自动构建测试 | ✅ 全自动 | ❌ 无需 |
| **持续交付** | CD | 自动发布到预发布环境 | ✅ 全自动 | ⚠️ 手动确认部署 |
| **持续部署** | CD | 自动部署到生产环境 | ✅ 全自动 | ❌ 无需 |

#### 1. 持续集成（Continuous Integration）

**核心理念**：
- 开发人员频繁提交代码（每天多次）
- 每次提交自动触发构建和测试
- 快速发现并修复集成错误

**CI 流程**：
```
1. 开发人员推送代码到 GitLab
        ↓
2. GitLab 检测到代码变更
        ↓
3. 自动触发 Pipeline
        ↓
4. 执行构建（编译、打包）
        ↓
5. 运行自动化测试（单元测试、集成测试）
        ↓
6. 代码质量检查（SonarQube）
        ↓
7. 生成测试报告和覆盖率报告
        ↓
8. 成功/失败通知
```

**CI 最佳实践**：
- ✅ 每天至少提交一次代码
- ✅ 每次提交都运行完整测试套件
- ✅ 构建失败立即修复
- ✅ 保持快速反馈（<10 分钟）
- ✅ 测试覆盖率 > 80%

#### 2. 持续交付（Continuous Delivery）

**核心理念**：
- 在 CI 基础上，自动发布到预发布环境
- 随时可以手动部署到生产
- 保证代码始终处于可发布状态

**CD 流程**：
```
CI 流程完成
        ↓
自动部署到 Staging 环境
        ↓
运行自动化验收测试
        ↓
性能测试
        ↓
安全扫描
        ↓
✅ 准备就绪，等待手动部署到生产
```

**CD 最佳实践**：
- ✅ 自动化部署脚本
- ✅ 环境配置版本化
- ✅ 一键回滚能力
- ✅ 部署审批流程
- ✅ 部署通知

#### 3. 持续部署（Continuous Deployment）

**核心理念**：
- 在持续交付基础上，自动部署到生产
- 无需人工干预
- 需要完善的监控和告警

**CD 流程**：
```
CD 流程完成
        ↓
自动部署到 Production
        ↓
健康检查
        ↓
监控告警
        ↓
✅ 用户立即可用
```

**CD 最佳实践**：
- ✅ 完善的监控体系
- ✅ 自动化回滚机制
- ✅ 灰度发布/蓝绿部署
- ✅ 功能开关（Feature Flag）
- ✅ A/B 测试能力

#### GitLab CI/CD 核心术语

| 术语 | 英文 | 含义 | 示例 |
|:---|:---|:---|:---|
| **流水线** | Pipeline | CI/CD 流程的完整执行 | 一次代码提交触发一次流水线 |
| **阶段** | Stage | 流水线的逻辑分组 | build、test、deploy |
| **任务** | Job | 具体执行的工作单元 | 编译、测试、部署 |
| **Runner** | Runner | 执行 Job 的代理程序 | Shell Runner、Docker Runner |
| **Artifacts** | Artifacts | Job 生成的文件 | 编译产物、测试报告 |
| **缓存** | Cache | 跨 Job 共享的文件 | 依赖包、编译中间文件 |
| **环境变量** | Variables | 配置参数 | CI_COMMIT_SHA、DEPLOY_ENV |

#### Pipeline 执行流程示例

```yaml
stages:
  - build    # 第 1 阶段：构建
  - test     # 第 2 阶段：测试
  - deploy   # 第 3 阶段：部署

build_job:
  stage: build
  script:
    - echo "构建项目..."
    - ./build.sh

test_job_1:
  stage: test
  script:
    - echo "运行单元测试..."
    - ./test.sh

test_job_2:
  stage: test
  script:
    - echo "运行集成测试..."
    - ./integration-test.sh

deploy_job:
  stage: deploy
  script:
    - echo "部署到生产..."
    - ./deploy.sh
  only:
    - main
```

**执行顺序**：
```
         build_job
         (阶段 1)
              ↓
    ┌─────────┴─────────┐
    ↓                   ↓
test_job_1         test_job_2
(阶段 2，并行执行)
    ↓                   ↓
    └─────────┬─────────┘
              ↓
         deploy_job
         (阶段 3)
```

**执行规则**：
- ✅ 同一阶段的 Job **并行执行**
- ✅ 不同阶段的 Job **顺序执行**
- ✅ 前一阶段全部成功，才执行下一阶段
- ✅ 任一 Job 失败，后续阶段不执行

#### CI/CD 成熟度模型

```
Level 1: 手动部署
└─ 开发手动构建、手动部署
   ⭐ 成熟度：低
   ⏱️ 部署时间：小时级
   😰 风险：高

Level 2: 部分自动化
└─ 自动构建、手动部署
   ⭐ 成熟度：中低
   ⏱️ 部署时间：30 分钟
   😰 风险：中高

Level 3: 持续集成
└─ 自动构建、自动测试、手动部署
   ⭐ 成熟度：中
   ⏱️ 部署时间：10 分钟
   😰 风险：中

Level 4: 持续交付
└─ 自动构建、自动测试、自动部署到预发布、手动确认生产部署
   ⭐ 成熟度：高
   ⏱️ 部署时间：5 分钟
   😰 风险：低

Level 5: 持续部署
└─ 全自动部署到生产
   ⭐ 成熟度：最高
   ⏱️ 部署时间：1 分钟
   😰 风险：最低（有完善监控）
```

---

### 5.2 GitLab Runner 部署

#### Runner 类型介绍

GitLab Runner 是执行 CI/CD Job 的代理程序，有三种类型：

| 类型 | 英文 | 作用范围 | 适用场景 | 配置位置 |
|:---|:---|:---|:---|:---|
| **共享 Runner** | Shared Runner | 整个 GitLab 实例 | 公共项目、通用任务 | Admin Area → Runners |
| **组 Runner** | Group Runner | 组内所有项目 | 团队项目、部门项目 | Group → Settings → CI/CD |
| **项目 Runner** | Project Runner | 单个项目 | 专用环境、特殊需求 | Project → Settings → CI/CD |

#### Runner 架构图

```
┌─────────────────┐
│   GitLab Server │
│   (10.0.0.10)   │
└────────┬────────┘
         │
         │ HTTP/HTTPS
         │
    ┌────┴────┐
    │         │
    ↓         ↓
┌─────────┐ ┌─────────┐
│ Runner 1│ │ Runner 2│
│(共享)   │ │(项目)   │
│10.0.0.20│ │10.0.0.21│
└─────────┘ └─────────┘
    │             │
    ↓             ↓
┌─────────┐ ┌─────────┐
│  Job 1  │ │  Job 2  │
│ 构建    │ │ 测试    │
└─────────┘ └─────────┘
```

#### Runner 执行器（Executor）

| 执行器 | 特点 | 适用场景 | 隔离性 |
|:---|:---|:---|:---:|
| **Docker** | 每个 Job 独立容器 | 推荐，环境隔离好 | ⭐⭐⭐⭐⭐ |
| **Shell** | 直接在宿主机执行 | 简单场景、高性能 | ⭐⭐ |
| **Kubernetes** | 在 K8s Pod 中执行 | 大规模、弹性伸缩 | ⭐⭐⭐⭐⭐ |
| **VirtualBox** | 在虚拟机中执行 | 特殊需求 | ⭐⭐⭐⭐ |
| **SSH** | 通过 SSH 远程执行 | 远程服务器部署 | ⭐⭐⭐ |

#### 部署方式 1：Docker 部署（推荐）

**步骤 1：安装 Docker**

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
docker --version
```

**步骤 2：运行 GitLab Runner 容器**

```bash
docker run -d --name gitlab-runner \
  --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest
```

**步骤 3：注册 Runner**

```bash
# 进入容器
docker exec -it gitlab-runner gitlab-runner register

# 按提示输入：
# GitLab URL: https://gitlab.company.com
# Registration token: <从 GitLab 获取>
# Description: docker-runner-01
# Tags: docker,build,test
# Executor: docker
# Default Docker image: docker:24.0
```

**步骤 4：验证注册**

```bash
# 查看 Runner 状态
docker exec -it gitlab-runner gitlab-runner list

# 或在 GitLab Web 界面查看
# Admin Area → Monitoring → Runners
```

#### 部署方式 2：二进制部署

**步骤 1：下载 Runner**

```bash
# 下载最新版本
curl -L --output /usr/local/bin/gitlab-runner \
  "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64"

# 添加执行权限
chmod +x /usr/local/bin/gitlab-runner

# 验证版本
gitlab-runner --version
```

**步骤 2：创建系统用户**

```bash
sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash
```

**步骤 3：安装为系统服务**

```bash
sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
sudo gitlab-runner start
sudo systemctl enable gitlab-runner
sudo systemctl status gitlab-runner
```

**步骤 4：注册 Runner**

```bash
sudo gitlab-runner register

# 按提示输入：
# GitLab URL: https://gitlab.company.com
# Registration token: <从 GitLab 获取>
# Description: shell-runner-01
# Tags: shell,deploy
# Executor: shell
```

#### 部署方式 3：Kubernetes 部署

**步骤 1：添加 Helm Chart 仓库**

```bash
helm repo add gitlab https://charts.gitlab.io
helm repo update
```

**步骤 2：创建命名空间**

```bash
kubectl create namespace gitlab-runner
```

**步骤 3：配置 values.yaml**

```yaml
# values.yaml

gitlabUrl: https://gitlab.company.com
runnerRegistrationToken: "<从 GitLab 获取>"

runners:
  config: |
    [[runners]]
      [runners.kubernetes]
        namespace = "gitlab-runner"
        image = "ubuntu:20.04"
        privileged = true
        service_account = "gitlab-runner"
        
  tags: "kubernetes,docker"
  parallel: 10  # 并发数
```

**步骤 4：安装 Runner**

```bash
helm install --namespace gitlab-runner gitlab-runner gitlab/gitlab-runner \
  -f values.yaml
```

**步骤 5：验证安装**

```bash
kubectl get pods -n gitlab-runner
kubectl get configmap -n gitlab-runner gitlab-runner-config -o yaml
```

#### Runner 配置详解

**配置文件位置**：
```bash
# Docker 部署
/srv/gitlab-runner/config/config.toml

# 二进制部署
/etc/gitlab-runner/config.toml

# Kubernetes 部署
kubectl get configmap -n gitlab-runner gitlab-runner-config
```

**config.toml 示例**：
```toml
concurrent = 10  # 全局并发数
check_interval = 0  # 检查间隔（秒）

[session_server]
  session_timeout = 1800  # 会话超时（秒）

[[runners]]
  name = "docker-runner-01"
  url = "https://gitlab.company.com/"
  token = "xxxxx"
  executor = "docker"
  limit = 5  # 该 Runner 最大并发
  
  [runners.docker]
    tls_verify = false
    image = "docker:24.0"
    privileged = true
    disable_entrypoint = false
    disable_cache = false
    volumes = ["/cache", "/var/run/docker.sock:/var/run/docker.sock"]
    shm_size = 0
    network_mode = "host"
    pull_policy = "if-not-present"  # 镜像拉取策略
    
  [runners.cache]
    Type = "s3"  # 缓存类型
    Shared = true
    [runners.cache.s3]
      ServerAddress = "s3.amazonaws.com"
      AccessKey = "xxx"
      SecretKey = "xxx"
      BucketName = "gitlab-runner-cache"
      Insecure = true
```

#### Runner 标签（Tags）管理

**标签作用**：
- 将 Job 路由到特定 Runner
- 实现环境隔离（dev/test/prod）
- 实现资源隔离（普通/高性能）

**标签配置示例**：
```toml
[[runners]]
  name = "dev-runner"
  tags = ["docker", "dev", "small"]
  executor = "docker"

[[runners]]
  name = "prod-runner"
  tags = ["docker", "prod", "large"]
  executor = "docker"
```

**Job 中使用标签**：
```yaml
deploy_dev:
  script: ./deploy.sh dev
  tags:
    - dev

deploy_prod:
  script: ./deploy.sh prod
  tags:
    - prod
```

#### Runner 监控与维护

**查看 Runner 状态**：
```bash
# 列出所有 Runner
gitlab-runner list

# 查看 Runner 详情
gitlab-runner verify

# 重启 Runner
sudo systemctl restart gitlab-runner

# 查看 Runner 日志
journalctl -u gitlab-runner -f
```

**Runner 健康检查**：
```bash
#!/bin/bash
# /usr/local/bin/runner-health-check.sh

echo "=== Runner 健康检查 ==="
echo "时间：$(date)"
echo ""

# 1. 检查服务状态
echo "【1】服务状态"
systemctl is-active gitlab-runner
echo ""

# 2. 检查 Runner 列表
echo "【2】Runner 列表"
gitlab-runner list
echo ""

# 3. 检查系统资源
echo "【3】系统资源"
echo "CPU: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}')%"
echo "内存：$(free -h | awk 'NR==2 {print $3"/"$2}')"
echo "磁盘：$(df -h / | awk 'NR==2 {print $5}')"
echo ""

# 4. 检查 Docker（如使用）
echo "【4】Docker 状态"
docker info | grep -E "Containers|Images"
echo ""

echo "=== 检查完成 ==="
```

#### Runner 常见问题排查

**问题 1：Runner 离线**

```bash
# 检查服务状态
sudo systemctl status gitlab-runner

# 检查网络连接
curl -I https://gitlab.company.com

# 检查 Token 是否有效
# Admin Area → Runners → 查看 Runner 状态

# 解决方案：
# 1. 重启 Runner 服务
# 2. 重新注册 Runner
# 3. 检查防火墙规则
```

**问题 2：Job 一直 Pending**

```bash
# 检查 Runner 并发数
# config.toml 中的 concurrent 和 limit

# 检查标签匹配
# Job 的 tags 是否与 Runner 的 tags 匹配

# 解决方案：
# 1. 增加 Runner 数量
# 2. 提高并发数
# 3. 检查标签配置
```

**问题 3：Docker 权限不足**

```bash
# 错误信息：permission denied while trying to connect to Docker daemon socket

# 解决方案：
# 1. 将 gitlab-runner 用户加入 docker 组
sudo usermod -aG docker gitlab-runner

# 2. 或使用 privileged 模式
[runners.docker]
  privileged = true
```

---

### 5.3 .gitlab-ci.yml 基础配置

#### YAML 语法基础

**基本规则**：
```yaml
# 键值对用冒号分隔
key: value

# 列表用短横线
list:
  - item1
  - item2
  - item3

# 缩进使用空格（不能用 Tab）
parent:
  child:
    - item1
    - item2

# 字符串可以用引号包裹（可选）
string: "hello world"
string2: 'hello world'

# 注释用 # 开头
# 这是注释
```

**多行字符串**：
```yaml
# 保留换行符（|）
description: |
  这是第一行
  这是第二行
  这是第三行

# 折叠换行符（>）
description: >
  这是第一行
  这是第二行
  这是第三行
# 实际值：这是第一行 这是第二行 这是第三行
```

#### .gitlab-ci.yml 基本结构

**最简示例**：
```yaml
# 定义阶段
stages:
  - build
  - test
  - deploy

# 定义 Job
build_job:
  stage: build
  script:
    - echo "构建项目..."
    - ./build.sh

test_job:
  stage: test
  script:
    - echo "运行测试..."
    - ./test.sh

deploy_job:
  stage: deploy
  script:
    - echo "部署项目..."
    - ./deploy.sh
  only:
    - main  # 仅 main 分支触发
```

#### 核心关键字详解

**1. stages（阶段）**

```yaml
# 定义流水线的执行阶段
stages:
  - build      # 第 1 阶段：构建
  - test       # 第 2 阶段：测试
  - deploy     # 第 3 阶段：部署
  - cleanup    # 第 4 阶段：清理

# 执行顺序：从左到右
# 同一阶段的 Job 并行执行
```

**2. image（镜像）**

```yaml
# 全局镜像（所有 Job 默认使用）
image: docker:24.0

# Job 级别镜像
build:
  image: maven:3.9-openjdk-17
  script:
    - mvn package

test:
  image: python:3.11
  script:
    - pytest
```

**3. variables（变量）**

```yaml
# 全局变量
variables:
  APP_NAME: "my-app"
  DOCKER_REGISTRY: "registry.company.com"
  DEPLOY_ENV: "production"

# Job 级别变量
deploy:
  variables:
    DEPLOY_ENV: "staging"  # 覆盖全局变量
  script:
    - echo "部署到 ${DEPLOY_ENV}"
```

**4. before_script / after_script**

```yaml
# 全局 before_script（所有 Job 执行前运行）
before_script:
  - echo "准备环境..."
  - apt-get update

# 全局 after_script（所有 Job 执行后运行）
after_script:
  - echo "清理环境..."

# Job 级别 before_script
build:
  before_script:
    - echo "构建前准备..."
  script:
    - ./build.sh

# Job 级别 after_script
test:
  after_script:
    - echo "测试后清理..."
  script:
    - ./test.sh
```

**5. script（执行脚本）**

```yaml
job:
  script:
    - echo "单行命令"
    - |
      # 多行命令
      echo "第一行"
      echo "第二行"
    - bash script.sh
    - |
      if [ -f file.txt ]; then
        echo "文件存在"
      else
        echo "文件不存在"
      fi
```

**6. tags（标签）**

```yaml
# 指定 Runner 标签
deploy_dev:
  script: ./deploy.sh dev
  tags:
    - docker
    - dev

deploy_prod:
  script: ./deploy.sh prod
  tags:
    - docker
    - prod
    - large
```

**7. artifacts（产物）**

```yaml
# 基础配置
build:
  script:
    - ./build.sh
  artifacts:
    paths:
      - dist/
      - build/
    expire_in: 1 week  # 保留时间

# 报告类型
test:
  script:
    - ./test.sh
  artifacts:
    reports:
      junit: test-results.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml
```

**8. cache（缓存）**

```yaml
# 全局缓存
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/

# Job 级别缓存
build:
  cache:
    key: ${CI_COMMIT_REF_NAME}
    paths:
      - dependencies/
    policy: pull-push  # pull, push, pull-push
```

**9. only / except（触发条件）**

```yaml
# 仅 main 分支
deploy:
  script: ./deploy.sh
  only:
    - main

# 仅标签
release:
  script: ./release.sh
  only:
    - tags

# 排除特定分支
test:
  script: ./test.sh
  except:
    - main

# 多种条件
job:
  script: ./run.sh
  only:
    - main
    - develop
    - tags
    - schedules  # 定时任务
    - web  # 手动触发
```

**10. rules（高级触发规则）**

```yaml
# 基础规则
job:
  script: ./run.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      when: on_success

# 多条件
deploy:
  script: ./deploy.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "main" && $CI_PIPELINE_SOURCE == "push"
      when: manual
    - if: $CI_COMMIT_TAG
      when: on_success
    - when: never  # 默认不执行
```

**11. dependencies（依赖）**

```yaml
# 指定依赖的 Job
deploy:
  stage: deploy
  dependencies:
    - build
    - test
  script:
    - ./deploy.sh

# 不依赖任何 Job
independent:
  stage: test
  dependencies: []
  script:
    - ./independent-test.sh
```

**12. needs（并行流水线）**

```yaml
# 传统方式（顺序执行）
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script: ./build.sh

test:
  stage: test
  script: ./test.sh
  needs: [build]  # 等待 build 完成

deploy:
  stage: deploy
  script: ./deploy.sh
  needs: [test]  # 等待 test 完成

# 使用 needs 实现 DAG（有向无环图）
build_frontend:
  stage: build
  script: ./build-frontend.sh

build_backend:
  stage: build
  script: ./build-backend.sh

test_frontend:
  stage: test
  script: ./test-frontend.sh
  needs: [build_frontend]  # 只依赖 frontend build

test_backend:
  stage: test
  script: ./test-backend.sh
  needs: [build_backend]  # 只依赖 backend build

deploy:
  stage: deploy
  script: ./deploy.sh
  needs: [test_frontend, test_backend]  # 等待两个测试完成
```

#### 完整示例：前端项目

```yaml
# .gitlab-ci.yml - 前端项目完整示例

image: node:20

stages:
  - lint
  - test
  - build
  - deploy

# 全局变量
variables:
  NPM_CONFIG_CACHE: "${CI_PROJECT_DIR}/.npm"
  APP_NAME: "frontend-app"

# 全局缓存
cache:
  key: ${CI_COMMIT_REF_SLUG}-npm
  paths:
    - node_modules/
    - .npm/

# 全局 before_script
before_script:
  - echo "Node 版本：$(node -v)"
  - echo "NPM 版本：$(npm -v)"

# Lint 检查
lint:
  stage: lint
  script:
    - npm ci --cache ${NPM_CONFIG_CACHE} --prefer-offline
    - npm run lint
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# 单元测试
unit_test:
  stage: test
  script:
    - npm ci --cache ${NPM_CONFIG_CACHE} --prefer-offline
    - npm run test:coverage
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
  coverage: '/Lines\s*:\s*(\d+.\d+)%/'
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# E2E 测试
e2e_test:
  stage: test
  image: cypress/included:latest
  script:
    - npm run e2e
  artifacts:
    paths:
      - cypress/videos/
      - cypress/screenshots/
    when: on_failure
  rules:
    - if: $CI_COMMIT_BRANCH == "develop"

# 构建
build:
  stage: build
  script:
    - npm ci --cache ${NPM_CONFIG_CACHE} --prefer-offline
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 week
  rules:
    - if: $CI_COMMIT_BRANCH == "main" || $CI_COMMIT_BRANCH == "develop"

# 部署到测试环境
deploy_test:
  stage: deploy
  script:
    - echo "部署到测试环境..."
    - ./deploy.sh test
  environment:
    name: test
    url: https://test.example.com
  tags:
    - shell
    - test
  rules:
    - if: $CI_COMMIT_BRANCH == "develop"

# 部署到生产环境
deploy_prod:
  stage: deploy
  script:
    - echo "部署到生产环境..."
    - ./deploy.sh prod
  environment:
    name: production
    url: https://www.example.com
  tags:
    - shell
    - prod
  when: manual  # 手动触发
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

#### 配置验证

**语法检查**：
```bash
# 使用 GitLab CI Lint
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --request POST \
  --form "content=@.gitlab-ci.yml" \
  "https://gitlab.example.com/api/v4/ci/lint"

# 或在 GitLab Web 界面
# Project → CI/CD → CI/CD Editor
# 粘贴 .gitlab-ci.yml 内容，点击 "Validate"
```

**本地验证工具**：
```bash
# 安装 gitlab-ci-lint
npm install -g @gitlab/lint

# 验证配置
gitlab-ci-lint .gitlab-ci.yml
```

#### 最佳实践

**1. 保持配置简洁**
```yaml
# ❌ 避免过度复杂
job:
  script:
    - echo "Step 1"
    - echo "Step 2"
    - echo "Step 3"
    - echo "Step 4"
    - echo "Step 5"
    - echo "Step 6"
    - echo "Step 7"
    - echo "Step 8"

# ✅ 使用脚本文件
job:
  script:
    - ./ci-scripts/job-script.sh
```

**2. 使用模板和 extends**
```yaml
# 定义模板
.test_template:
  script:
    - npm test
  artifacts:
    reports:
      junit: test-results.xml

# 复用模板
unit_test:
  extends: .test_template
  script:
    - npm run test:unit

integration_test:
  extends: .test_template
  script:
    - npm run test:integration
```

**3. 合理设置超时**
```yaml
job:
  timeout: 30 minutes  # 默认 60 分钟
```

**4. 允许失败（非关键 Job）**
```yaml
notify:
  script: ./notify.sh
  allow_failure: true
  when: always
```

**5. 使用锚点减少重复**
```yaml
# 定义锚点
.variables_common: &variables_common
  NODE_ENV: production
  LOG_LEVEL: info

# 使用锚点
job1:
  variables:
    <<: *variables_common
    APP_NAME: app1

job2:
  variables:
    <<: *variables_common
    APP_NAME: app2
```

---

### 5.4 多技术栈 CI/CD 模板

#### 模板 1：Java/Maven 项目

```yaml
# .gitlab-ci.yml - Java/Maven 项目

stages:
  - build
  - test
  - package
  - deploy

variables:
  MAVEN_OPTS: "-Dmaven.repo.local=./.m2/repository"
  MAVEN_CLI_OPTS: "-B -DskipTests"
  APP_NAME: "backend-service"
  DOCKER_REGISTRY: "registry.company.com"

cache:
  key: ${CI_COMMIT_REF_SLUG}-maven
  paths:
    - .m2/repository/
    - target/

build:
  stage: build
  image: maven:3.9-openjdk-17
  script:
    - echo "编译 Java 项目..."
    - mvn compile $MAVEN_CLI_OPTS
  tags:
    - maven
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

test:
  stage: test
  image: maven:3.9-openjdk-17
  script:
    - echo "运行单元测试..."
    - mvn test
  artifacts:
    reports:
      junit: target/surefire-reports/TEST-*.xml
    coverage: '/Total coverage: \d+\.\d+%/'
  tags:
    - maven
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

package:
  stage: package
  image: maven:3.9-openjdk-17
  script:
    - echo "打包应用..."
    - mvn package -DskipTests $MAVEN_CLI_OPTS
    - echo "构建 Docker 镜像..."
    - docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA} .
    - docker push ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
  dependencies:
    - test
  tags:
    - maven
    - docker
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

deploy_staging:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context staging
    - kubectl set image deployment/${APP_NAME} \
        ${APP_NAME}=${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
    - kubectl rollout status deployment/${APP_NAME}
  environment:
    name: staging
    url: https://staging-app.company.com
  tags:
    - k8s
  rules:
    - if: $CI_COMMIT_BRANCH == "develop"

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
    url: https://app.company.com
  when: manual
  tags:
    - k8s
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

#### 模板 2：Node.js/前端项目

```yaml
# .gitlab-ci.yml - Node.js/前端项目

stages:
  - lint
  - test
  - build
  - deploy

variables:
  NODE_VERSION: "18"
  NPM_CONFIG_CACHE: "${CI_PROJECT_DIR}/.npm"
  APP_NAME: "frontend-web"

cache:
  key: ${CI_COMMIT_REF_SLUG}-npm
  paths:
    - node_modules/
    - .npm/

lint:
  stage: lint
  image: node:${NODE_VERSION}
  script:
    - npm ci --cache .npm --prefer-offline
    - npm run lint
  tags:
    - node
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

test:
  stage: test
  image: node:${NODE_VERSION}
  script:
    - npm ci --cache .npm --prefer-offline
    - npm run test:unit -- --coverage
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
    paths:
      - coverage/
    expire_in: 1 week
  tags:
    - node
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

build:
  stage: build
  image: node:${NODE_VERSION}
  script:
    - npm ci --cache .npm --prefer-offline
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 week
  tags:
    - node
  rules:
    - if: $CI_COMMIT_BRANCH == "main" || $CI_COMMIT_BRANCH == "develop"

deploy_staging:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache curl
  script:
    - echo "部署到 staging 环境..."
    - curl -X POST ${DEPLOY_WEBHOOK_STAGING} \
        -H "Authorization: Bearer ${DEPLOY_TOKEN}" \
        -d "commit=${CI_COMMIT_SHA}"
  environment:
    name: staging
    url: https://staging.company.com
  tags:
    - shell
  rules:
    - if: $CI_COMMIT_BRANCH == "develop"

deploy_production:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache curl
  script:
    - echo "部署到生产环境..."
    - curl -X POST ${DEPLOY_WEBHOOK_PRODUCTION} \
        -H "Authorization: Bearer ${DEPLOY_TOKEN}" \
        -d "commit=${CI_COMMIT_SHA}"
  environment:
    name: production
    url: https://www.company.com
  when: manual
  tags:
    - shell
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

#### 模板 3：Python 项目

```yaml
# .gitlab-ci.yml - Python 项目

stages:
  - lint
  - test
  - build
  - deploy

variables:
  PYTHON_VERSION: "3.11"
  PIP_CACHE_DIR: "${CI_PROJECT_DIR}/.cache/pip"
  APP_NAME: "python-service"
  DOCKER_REGISTRY: "registry.company.com"

cache:
  key: ${CI_COMMIT_REF_SLUG}-pip
  paths:
    - .cache/pip/
    - venv/

lint:
  stage: lint
  image: python:${PYTHON_VERSION}
  before_script:
    - pip install flake8 black mypy
  script:
    - flake8 . --exclude=venv/
    - black --check .
    - mypy .
  tags:
    - python
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

test:
  stage: test
  image: python:${PYTHON_VERSION}
  before_script:
    - pip install -r requirements.txt
    - pip install pytest pytest-cov
  script:
    - pytest --cov=. --cov-report=xml
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml
  tags:
    - python
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

build:
  stage: build
  image: docker:24.0
  services:
    - docker:24.0-dind
  script:
    - docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA} .
    - docker push ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
  tags:
    - docker
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

deploy:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context production
    - kubectl set image deployment/${APP_NAME} \
        ${APP_NAME}=${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
    - kubectl rollout status deployment/${APP_NAME}
  environment:
    name: production
  when: manual
  tags:
    - k8s
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

#### 模板 4：Go 项目

```yaml
# .gitlab-ci.yml - Go 项目

stages:
  - lint
  - test
  - build
  - deploy

variables:
  GO_VERSION: "1.21"
  APP_NAME: "go-service"
  DOCKER_REGISTRY: "registry.company.com"
  CGO_ENABLED: "0"
  GOOS: "linux"
  GOARCH: "amd64"

cache:
  key: ${CI_COMMIT_REF_SLUG}-go
  paths:
    - .cache/go-build/
    - ~/go/pkg/mod/

lint:
  stage: lint
  image: golang:${GO_VERSION}
  before_script:
    - go install golang.org/x/lint/golint@latest
    - go install honnef.co/go/tools/cmd/staticcheck@latest
  script:
    - golint ./...
    - staticcheck ./...
  tags:
    - go
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

test:
  stage: test
  image: golang:${GO_VERSION}
  script:
    - go test -race -coverprofile=coverage.txt -covermode=atomic ./...
  artifacts:
    reports:
      coverage_report:
        coverage_format: go
        path: coverage.txt
  tags:
    - go
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

build:
  stage: build
  image: golang:${GO_VERSION}
  script:
    - go build -o ${APP_NAME} -ldflags="-s -w" .
    - docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA} .
    - docker push ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
  artifacts:
    paths:
      - ${APP_NAME}
    expire_in: 1 week
  tags:
    - go
    - docker
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

deploy:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context production
    - kubectl set image deployment/${APP_NAME} \
        ${APP_NAME}=${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
  environment:
    name: production
  when: manual
  tags:
    - k8s
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

#### 模板 5：PHP 项目（Laravel）

```yaml
# .gitlab-ci.yml - PHP/Laravel 项目

stages:
  - lint
  - test
  - build
  - deploy

variables:
  PHP_VERSION: "8.2"
  APP_NAME: "laravel-app"
  DOCKER_REGISTRY: "registry.company.com"

cache:
  key: ${CI_COMMIT_REF_SLUG}-php
  paths:
    - vendor/
    - node_modules/

lint:
  stage: lint
  image: php:${PHP_VERSION}-cli
  before_script:
    - docker-php-ext-install pdo_mysql
    - curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
  script:
    - composer install --no-interaction
    - ./vendor/bin/phpcs --standard=PSR12 app/
    - ./vendor/bin/phpstan analyse
  tags:
    - php
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

test:
  stage: test
  image: php:${PHP_VERSION}-cli
  before_script:
    - docker-php-ext-install pdo_mysql
    - curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
    - composer install --no-interaction --dev
  script:
    - cp .env.testing .env
    - php artisan key:generate
    - php artisan test --coverage-clover=coverage.xml
  artifacts:
    reports:
      coverage_report:
        coverage_format: clover
        path: coverage.xml
  tags:
    - php
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

build:
  stage: build
  image: docker:24.0
  services:
    - docker:24.0-dind
  script:
    - docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA} .
    - docker push ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
  tags:
    - docker
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

deploy:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache curl openssh-client
  script:
    - echo "部署到生产服务器..."
    - ssh ${DEPLOY_USER}@${DEPLOY_SERVER} "cd /var/www/${APP_NAME} && docker-compose pull && docker-compose up -d"
  environment:
    name: production
  when: manual
  tags:
    - shell
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

#### 模板 6：.NET Core 项目

```yaml
# .gitlab-ci.yml - .NET Core 项目

stages:
  - restore
  - build
  - test
  - publish
  - deploy

variables:
  DOTNET_VERSION: "8.0"
  APP_NAME: "dotnet-service"
  DOCKER_REGISTRY: "registry.company.com"

cache:
  key: ${CI_COMMIT_REF_SLUG}-dotnet
  paths:
    - .nuget/packages/

restore:
  stage: restore
  image: mcr.microsoft.com/dotnet/sdk:${DOTNET_VERSION}
  script:
    - dotnet restore
  tags:
    - dotnet
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

build:
  stage: build
  image: mcr.microsoft.com/dotnet/sdk:${DOTNET_VERSION}
  script:
    - dotnet build --configuration Release --no-restore
  tags:
    - dotnet
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

test:
  stage: test
  image: mcr.microsoft.com/dotnet/sdk:${DOTNET_VERSION}
  script:
    - dotnet test --configuration Release --no-build --collect:"XPlat Code Coverage"
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: "**/coverage.cobertura.xml"
  tags:
    - dotnet
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

publish:
  stage: publish
  image: mcr.microsoft.com/dotnet/sdk:${DOTNET_VERSION}
  script:
    - dotnet publish --configuration Release --no-build -o ./publish
    - docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA} .
    - docker push ${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
  artifacts:
    paths:
      - publish/
    expire_in: 1 week
  tags:
    - dotnet
    - docker
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

deploy:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context production
    - kubectl set image deployment/${APP_NAME} \
        ${APP_NAME}=${DOCKER_REGISTRY}/${APP_NAME}:${CI_COMMIT_SHA}
    - kubectl rollout status deployment/${APP_NAME}
  environment:
    name: production
  when: manual
  tags:
    - k8s
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

#### 模板 7：多项目 Monorepo

```yaml
# .gitlab-ci.yml - Monorepo 多项目管理

stages:
  - lint
  - test
  - build
  - deploy

# 检测变更的文件路径
variables:
  FRONTEND_CHANGED: "false"
  BACKEND_CHANGED: "false"

# 前置 Job 检测变更
check_changes:
  stage: .pre
  image: alpine:latest
  script:
    - apk add --no-cache git
    - git diff --name-only CI_MERGE_REQUEST_DIFF_BASE_SHA $CI_COMMIT_SHA > changes.txt
    - |
      if grep -q "^frontend/" changes.txt; then
        echo "FRONTEND_CHANGED=true" >> build.env
      fi
    - |
      if grep -q "^backend/" changes.txt; then
        echo "BACKEND_CHANGED=true" >> build.env
      fi
  artifacts:
    reports:
      dotenv: build.env
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# 前端项目
frontend_lint:
  stage: lint
  image: node:20
  script:
    - cd frontend
    - npm ci
    - npm run lint
  rules:
    - if: $FRONTEND_CHANGED == "true"

frontend_test:
  stage: test
  image: node:20
  script:
    - cd frontend
    - npm ci
    - npm run test:coverage
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: frontend/coverage/cobertura-coverage.xml
  rules:
    - if: $FRONTEND_CHANGED == "true"

frontend_build:
  stage: build
  image: node:20
  script:
    - cd frontend
    - npm ci
    - npm run build
  artifacts:
    paths:
      - frontend/dist/
    expire_in: 1 week
  rules:
    - if: $FRONTEND_CHANGED == "true"
      when: on_success

# 后端项目
backend_test:
  stage: test
  image: python:3.11
  script:
    - cd backend
    - pip install -r requirements.txt
    - pytest --cov=. --cov-report=xml
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: backend/coverage.xml
  rules:
    - if: $BACKEND_CHANGED == "true"

backend_build:
  stage: build
  image: docker:24.0
  services:
    - docker:24.0-dind
  script:
    - cd backend
    - docker build -t ${DOCKER_REGISTRY}/backend:${CI_COMMIT_SHA} .
    - docker push ${DOCKER_REGISTRY}/backend:${CI_COMMIT_SHA}
  rules:
    - if: $BACKEND_CHANGED == "true"
```

---

### 5.5 流水线高级配置

#### 缓存配置优化

**基础缓存配置**：
```yaml
# 全局缓存配置
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/
  policy: pull-push  # pull, push, pull-push

# 按分支使用不同缓存
cache:
  key: ${CI_COMMIT_REF_NAME}
  paths:
    - dependencies/
  policy: pull  # 仅拉取，不推送

# 多缓存配置
cache:
  - key: common-cache
    paths:
      - .common/
  - key: ${CI_JOB_NAME}-cache
    paths:
      - ${CI_JOB_NAME}/
```

**缓存最佳实践**：

| 技术栈 | 缓存路径 | 缓存 Key 建议 |
|:---|:---|:---|
| **Node.js** | `node_modules/`, `.npm/` | `${CI_COMMIT_REF_SLUG}-npm` |
| **Python** | `.cache/pip/`, `venv/` | `${CI_COMMIT_REF_SLUG}-pip` |
| **Go** | `.cache/go-build/`, `~/go/pkg/mod/` | `${CI_COMMIT_REF_SLUG}-go` |
| **Maven** | `~/.m2/repository/` | `${CI_COMMIT_REF_SLUG}-maven` |
| **Gradle** | `~/.gradle/caches/` | `${CI_COMMIT_REF_SLUG}-gradle` |
| **NuGet** | `.nuget/packages/` | `${CI_COMMIT_REF_SLUG}-nuget` |

> ⚠️ **缓存注意事项**：
> - 缓存不是永久的，会被自动清理（通常 30 天未使用）
> - 缓存大小有限制（GitLab.com 10GB，自建实例可配置）
> - 敏感数据不要放入缓存（如密钥、证书）
> - 缓存 key 变更会导致缓存失效

#### Artifacts 产物管理

**基础配置**：
```yaml
# 基础配置
artifacts:
  paths:
    - dist/
    - build/
  expire_in: 1 week  # 保留时间（1 week, 30 days, 1 year, permanent）

# 按环境保留不同时间
artifacts:
  paths:
    - dist/
  expire_in: 30 days
  reports:
    junit: test-results.xml
    coverage_report:
      coverage_format: cobertura
      path: coverage.xml

# 仅特定分支保留
deploy:
  stage: deploy
  script:
    - ./build.sh
  artifacts:
    paths:
      - dist/
    expire_in: 1 week
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

**Artifacts 报告类型**：
```yaml
# JUnit 测试报告
artifacts:
  reports:
    junit: test-results.xml

# 代码覆盖率
artifacts:
  reports:
    coverage_report:
      coverage_format: cobertura
      path: coverage.xml

# 代码质量（Code Climate）
artifacts:
  reports:
    codequality: codeclimate.json

# 容器扫描
artifacts:
  reports:
    container_scanning: container-scanning-report.json

# 依赖扫描
artifacts:
  reports:
    dependency_scanning: dependency-scanning-report.json

# 安全扫描
artifacts:
  reports:
    sast: sast-report.json
    secret_detection: secret-detection-report.json

# 性能测试
artifacts:
  reports:
    performance_testing: performance-report.json

# 测试报告汇总
artifacts:
  reports:
    junit:
      - test-results/backend.xml
      - test-results/frontend.xml
    coverage_report:
      coverage_format: cobertura
      path: coverage.xml
```

> 💡 **Artifacts vs Cache**：
> - **Artifacts**：构建产物，传递给后续 Job，可下载，有版本
> - **Cache**：依赖缓存，加速构建，不传递，无版本
> - **建议**：构建产物用 artifacts，依赖包用 cache

#### 定时任务配置

**Cron 表达式语法**：
```
分 时 日 月 周
│  │  │  │  │
│  │  │  │  └─ 星期 (0-6, 0=周日)
│  │  │  └──── 月份 (1-12)
│  │  └─────── 日期 (1-31)
│  └────────── 小时 (0-23)
└───────────── 分钟 (0-59)

常用表达式：
0 2 * * *     # 每天凌晨 2 点
0 2 * * 1-5   # 工作日凌晨 2 点
0 */4 * * *   # 每 4 小时
0 2 1 * *     # 每月 1 号凌晨 2 点
```

**配置示例**：
```yaml
# 每天凌晨 2 点执行
nightly_build:
  stage: build
  script:
    - ./nightly-build.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"

# 每周一凌晨 3 点执行
weekly_report:
  stage: report
  script:
    - ./generate-weekly-report.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
      when: on_success

# 每小时执行健康检查
hourly_health_check:
  stage: monitor
  script:
    - ./health-check.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
```

**配置定时任务步骤**：
```
1. 项目页面 → CI/CD → Schedules
2. 点击 "New schedule"
3. 配置：
   - Description: 描述（如"每日构建"）
   - Target branch: main
   - Cron pattern: 0 2 * * *
   - Cron timezone: Asia/Shanghai
   - Variables: （可选，如 DEPLOY_ENV=production）
4. 点击 "Create schedule"
```

#### 触发规则详解

**Pipeline 触发源**：
```yaml
# 推送触发
push:
  script: ./build.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "push"

# 合并请求触发
merge_request:
  script: ./test.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# 定时任务触发
schedule:
  script: ./nightly.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"

# 标签触发
tag:
  script: ./release.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "tag"

# Web 触发（手动）
web:
  script: ./manual.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "web"

# API 触发
api:
  script: ./api-triggered.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "pipeline"

# 父流水线触发
child:
  script: ./child.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "parent_pipeline"
```

**分支/标签条件**：
```yaml
# 仅 main 分支
main_only:
  script: ./deploy.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

# 仅 develop 分支
develop_only:
  script: ./deploy-dev.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "develop"

# 仅标签
tag_only:
  script: ./release.sh
  rules:
    - if: $CI_COMMIT_TAG

# 特定标签模式
release_tag:
  script: ./release.sh
  rules:
    - if: $CI_COMMIT_TAG =~ /^v\d+\.\d+\.\d+$/

# 排除特定分支
not_main:
  script: ./test.sh
  rules:
    - if: $CI_COMMIT_BRANCH != "main"
```

**手动触发**：
```yaml
# 手动部署到生产
deploy_prod:
  stage: deploy
  script: ./deploy-prod.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      when: manual

# 手动触发带确认
manual_approval:
  stage: deploy
  script: ./deploy.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      when: manual
      allow_failure: false
```

**变量条件**：
```yaml
# 根据环境变量
deploy_staging:
  script: ./deploy.sh
  rules:
    - if: $DEPLOY_ENV == "staging"

deploy_production:
  script: ./deploy.sh
  rules:
    - if: $DEPLOY_ENV == "production"
      when: manual

# 多条件组合
complex_condition:
  script: ./deploy.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "main" && $DEPLOY_ENV == "production"
      when: manual
```

**允许失败**：
```yaml
# 可选测试（失败不影响流水线）
optional_test:
  script: ./experimental-test.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
  allow_failure: true

# 通知 Job（失败不影响）
notify:
  script: ./send-notification.sh
  stage: .post
  rules:
    - if: $CI_PIPELINE_SOURCE == "push"
  allow_failure: true
```

#### 流水线常见问题排查

**问题 1：Job 一直 Pending**

```bash
# 检查 Runner 状态
gitlab-runner list

# 查看 Runner 日志
journalctl -u gitlab-runner -f

# 检查 Runner 是否在线
# Admin Area → Monitoring → Runners

# 检查并发限制
# Settings → CI/CD → Runners → Concurrent jobs

# 解决方案：
# 1. 增加 Runner 数量
# 2. 提高并发数（默认 10）
# 3. 检查 Runner 标签匹配
# 4. 检查 Runner 是否被暂停
```

**问题 2：缓存不生效**

```bash
# 检查缓存 key 是否一致
# 所有 Job 必须使用相同的 cache key

# 查看缓存文件：
# Settings → CI/CD → Cache

# 清除缓存：
# Settings → CI/CD → Clear runner caches

# 解决方案：
# 1. 使用相同的 cache key
# 2. 确保 paths 正确（相对路径）
# 3. 清除旧缓存重新构建
# 4. 检查 cache policy（pull-push）
```

**问题 3：Artifacts 找不到**

```bash
# 检查 artifacts 路径是否正确
# 查看过期时间设置（expire_in）

# 解决方案：
# 1. 确认 paths 配置正确（相对路径）
# 2. 检查 expire_in 设置（默认 30 天）
# 3. 使用 dependencies 明确依赖
# 4. 检查 artifacts 大小限制（默认 100MB）
```

**问题 4：流水线慢**

```bash
# 优化建议：
# 1. 使用缓存减少依赖下载
# 2. 并行执行独立任务
# 3. 使用 Docker 层缓存
# 4. 增加 Runner 并发数
# 5. 优化测试用例（并行测试）
# 6. 使用 needs 替代 dependencies
# 7. 减少不必要的 artifacts
```

**问题 5：变量不生效**

```bash
# 检查变量作用域：
# - Instance 级别：所有项目
# - Group 级别：组内所有项目
# - Project 级别：单个项目
# - Environment 级别：特定环境

# 检查变量类型：
# - Variable: 普通变量
# - File: 文件变量（内容为文件路径）
# - Masked: 隐藏变量（日志中不显示）
# - Protected: 仅保护分支可用

# 解决方案：
# 1. 确认变量作用域正确
# 2. 检查变量名是否正确（大小写敏感）
# 3. 保护分支需要 Protected 变量
# 4. 敏感变量使用 Masked
```

---

### 5.6 环境变量与密钥管理

（保持原有内容）

---

## 第 8 章 工具链生态集成

### 8.1 工具链集成概览

| 工具 | 用途 | 集成难度 | 推荐度 |
|:---|:---|:---:|:---:|
| **SonarQube** | 代码质量检查 | ⭐⭐ 简单 | ✅ 强烈推荐 |
| **Nexus** | 制品库管理 | ⭐⭐ 简单 | ✅ 推荐 |
| **钉钉** | 通知告警 | ⭐ 简单 | ✅ 推荐 |
| **企业微信** | 通知告警 | ⭐ 简单 | ✅ 推荐 |
| **LDAP** | 统一认证 | ⭐⭐⭐ 中等 | ✅ 企业必备 |
| **Jenkins** | CI/CD 补充 | ⭐⭐⭐ 中等 | ⚠️ 可选 |
| **Harbor** | 镜像仓库 | ⭐⭐ 简单 | ✅ 推荐 |

---

### 8.2 SonarQube 代码质量集成

#### 步骤 1：部署 SonarQube

```bash
# Docker 部署 SonarQube
docker run -d --name sonarqube \
  -p 9000:9000 \
  -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true \
  -v sonarqube_data:/opt/sonarqube/data \
  -v sonarqube_extensions:/opt/sonarqube/extensions \
  -v sonarqube_logs:/opt/sonarqube/logs \
  sonarqube:10.3-community
```

#### 步骤 2：配置 SonarQube

```
1. 访问 http://sonarqube:9000
2. 登录（默认 admin/admin）
3. 创建项目
4. 生成 Token：
   - User → My Account → Security
   - Create Token → 复制 Token
```

#### 步骤 3：GitLab CI 集成

```yaml
# .gitlab-ci.yml 添加 SonarQube 检查

sonarqube_check:
  stage: test
  image: sonarsource/sonar-scanner-cli:latest
  variables:
    SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"
    GIT_DEPTH: "0"
  script:
    - sonar-scanner
      -Dsonar.qualitygate.wait=true
      -Dsonar.qualitygate.timeout=300
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
```

#### 步骤 4：配置 sonar-project.properties

```properties
# sonar-project.properties

sonar.projectKey=my-project
sonar.projectName=My Project
sonar.projectVersion=1.0

sonar.sources=src/
sonar.tests=test/
sonar.language=java

sonar.sourceEncoding=UTF-8
sonar.qualitygate.wait=true

# Java 特定配置
sonar.java.binaries=target/classes
sonar.java.coverageReportPaths=target/site/jacoco/jacoco.xml
```

#### 步骤 5：配置质量门禁

```
1. SonarQube → Quality Gates
2. 创建新门禁或编辑默认
3. 配置条件：
   - Bugs: 0
   - Vulnerabilities: 0
   - Code Coverage: > 80%
   - Duplication: < 3%
4. 保存并设为默认
```

⚠️ **注意**：
```
- 质量门禁不通过会导致流水线失败
- 可在 GitLab MR 中显示质量报告
- 建议逐步提高门禁标准
```

---

### 8.3 Nexus 制品库集成

#### 步骤 1：部署 Nexus

```bash
# Docker 部署 Nexus
docker run -d --name nexus \
  -p 8081:8081 \
  -v nexus_data:/nexus-data \
  -e INSTALL4J_ADD_VM_PARAMS="-Xms2g -Xmx2g" \
  sonatype/nexus3:3.65.0
```

#### 步骤 2：配置 Nexus 仓库

```
1. 访问 http://nexus:8081
2. 登录（默认 admin/admin123）
3. 创建仓库：
   - Maven: maven-releases, maven-snapshots
   - Docker: docker-hosted, docker-group
   - npm: npm-hosted, npm-group
```

#### 步骤 3：Maven 集成示例

```yaml
# .gitlab-ci.yml

deploy_to_nexus:
  stage: deploy
  image: maven:3.9-openjdk-17
  script:
    - mvn deploy -DskipTests \
        -DaltDeploymentRepository=nexus::default::${NEXUS_URL}/repository/maven-releases/
  variables:
    NEXUS_URL: "http://nexus:8081"
  rules:
    - if: $CI_COMMIT_TAG
```

```xml
<!-- pom.xml 配置 -->
<distributionManagement>
  <repository>
    <id>nexus</id>
    <name>Releases</name>
    <url>${NEXUS_URL}/repository/maven-releases/</url>
  </repository>
  <snapshotRepository>
    <id>nexus</id>
    <name>Snapshots</name>
    <url>${NEXUS_URL}/repository/maven-snapshots/</url>
  </snapshotRepository>
</distributionManagement>
```

#### 步骤 4：Docker 镜像推送

```bash
# 配置 Docker 登录 Nexus
docker login nexus:8081 -u admin -p admin123

# 推送镜像
docker tag myapp:latest nexus:8081/docker-repo/myapp:latest
docker push nexus:8081/docker-repo/myapp:latest
```

```yaml
# GitLab CI 配置
deploy_docker:
  stage: deploy
  image: docker:24.0
  services:
    - docker:24.0-dind
  script:
    - docker login ${NEXUS_URL} -u ${NEXUS_USER} -p ${NEXUS_PASSWORD}
    - docker tag ${APP_NAME}:${CI_COMMIT_SHA} ${NEXUS_URL}/docker-repo/${APP_NAME}:${CI_COMMIT_SHA}
    - docker push ${NEXUS_URL}/docker-repo/${APP_NAME}:${CI_COMMIT_SHA}
  variables:
    NEXUS_URL: "nexus:8081"
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

---

### 8.4 钉钉/企业微信通知

#### 钉钉机器人配置

```yaml
# .gitlab-ci.yml

notify_dingtalk:
  stage: .post
  image: curlimages/curl:latest
  script:
    - |
      if [ "$CI_JOB_STATUS" == "failed" ]; then
        curl -X POST "${DINGTALK_WEBHOOK}" \
          -H "Content-Type: application/json" \
          -d "{
            \"msgtype\": \"markdown\",
            \"markdown\": {
              \"title\": \"流水线失败通知\",
              \"text\": \"## 🚨 流水线失败\n\n- **项目**: ${CI_PROJECT_NAME}\n- **分支**: ${CI_COMMIT_REF_NAME}\n- **提交**: ${CI_COMMIT_SHORT_SHA}\n- **用户**: ${GITLAB_USER_NAME}\n- **详情**: ${CI_PIPELINE_URL}\n\"
            }
          }"
      fi
  rules:
    - if: $CI_PIPELINE_SOURCE == "push"
      when: on_failure
```

**获取钉钉 Webhook**：
```
1. 钉钉群 → 群设置 → 智能群助手
2. 添加机器人 → 自定义
3. 复制 Webhook 地址
4. 添加到 GitLab CI/CD Variables：DINGTALK_WEBHOOK
```

#### 企业微信机器人配置

```yaml
# .gitlab-ci.yml

notify_wechat:
  stage: .post
  image: curlimages/curl:latest
  script:
    - |
      if [ "$CI_JOB_STATUS" == "failed" ]; then
        curl -X POST "${WECHAT_WEBHOOK}" \
          -H "Content-Type: application/json" \
          -d "{
            \"msgtype\": \"markdown\",
            \"markdown\": {
              \"content\": \"## 🚨 流水线失败通知\n\n- **项目**: ${CI_PROJECT_NAME}\n- **分支**: ${CI_COMMIT_REF_NAME}\n- **提交**: ${CI_COMMIT_SHORT_SHA}\n- **用户**: ${GITLAB_USER_NAME}\n- [查看详情](${CI_PIPELINE_URL})\"
            }
          }"
      fi
  rules:
    - if: $CI_PIPELINE_SOURCE == "push"
      when: on_failure
```

**获取企业微信 Webhook**：
```
1. 企业微信群 → 群设置 → 群机器人
2. 添加机器人
3. 复制 Webhook 地址
4. 添加到 GitLab CI/CD Variables：WECHAT_WEBHOOK
```

---

### 8.5 LDAP 统一认证集成

#### 步骤 1：编辑 GitLab 配置

```bash
sudo vim /etc/gitlab/gitlab.rb
```

#### 步骤 2：配置 LDAP 参数

```ruby
# LDAP 配置
gitlab_rails['ldap_enabled'] = true
gitlab_rails['ldap_servers'] = {
  'main' => {
    'label' => 'LDAP',
    'host' => 'ldap.company.com',
    'port' => 389,
    'uid' => 'sAMAccountName',
    'bind_dn' => 'CN=gitlab,CN=Users,DC=company,DC=com',
    'password' => 'ldap_password',
    'encryption' => 'plain',
    'active_directory' => true,
    'allow_username_or_email_login' => true,
    'block_auto_created_users' => false,
    'base' => 'DC=company,DC=com',
    'user_filter' => '(|(objectClass=user))',
    'group_base' => 'OU=Groups,DC=company,DC=com',
  }
}

# LDAP 超时配置
gitlab_rails['ldap_timeout'] = 10
gitlab_rails['ldap_active_timeout'] = 10
```

#### 步骤 3：应用配置

```bash
# 重新配置
sudo gitlab-ctl reconfigure

# 测试 LDAP 连接
sudo gitlab-rake gitlab:ldap:check

# 输出示例：
# Server: main
# ...
# Checking users ...
# 用户同步成功
```

#### 步骤 4：配置 LDAP 组映射

```ruby
# LDAP 组映射到 GitLab 组
gitlab_rails['ldap_group_sync'] = true
gitlab_rails['ldap_group_sync_base'] = 'OU=GitLab,DC=company,DC=com'

# 组映射规则
gitlab_rails['ldap_group_mappings'] = {
  'CN=GitLab-Admin,OU=Groups,DC=company,DC=com' => 40,  # Owner
  'CN=GitLab-Dev,OU=Groups,DC=company,DC=com' => 30,    # Maintainer
  'CN=GitLab-Ops,OU=Groups,DC=company,DC=com' => 30,    # Maintainer
  'CN=GitLab-Test,OU=Groups,DC=company,DC=com' => 20,   # Developer
}
```

#### 步骤 5：同步 LDAP 组

```bash
# 同步 LDAP 组
sudo gitlab-rake gitlab:ldap:group_sync

# 查看同步日志
sudo gitlab-ctl tail gitlab-rails
```

⚠️ **注意事项**：
```
1. 确保 LDAP 服务器防火墙允许 GitLab 访问
2. bind_dn 账户需要读取权限
3. 首次同步可能需要较长时间
4. 建议配置定时同步（每天凌晨）
```

---

## 第 7 章 高可用架构与监控

### 7.4 Prometheus 监控对接

（保持原有内容）

### 7.5 高频故障排查手册

（保持原有内容）

### 7.6 GitLab 性能调优

#### Unicorn/Puma 配置优化

**基础配置**：
```ruby
# /etc/gitlab/gitlab.rb

# Puma worker 数量（推荐：CPU 核心数 * 2 + 1）
# 4 核 CPU: 4 * 2 + 1 = 9
# 8 核 CPU: 8 * 2 + 1 = 17
puma['worker_processes'] = 4

# 每个 worker 线程数
puma['min_threads'] = 1
puma['max_threads'] = 16

# Worker 超时时间（秒）
puma['worker_timeout'] = 60

# 内存限制（每个 worker，MB）
puma['max_memory'] = 1024  # MB

# 启用 HTTP/2
puma['http2'] = true
```

**Worker 数量计算**：
```
公式：worker_processes = (CPU 核心数 * 2) + 1

示例：
- 2 核 CPU → 5 workers
- 4 核 CPU → 9 workers
- 8 核 CPU → 17 workers
- 16 核 CPU → 33 workers

内存估算：
每个 worker 约 200-400MB
总内存 = worker_processes * 300MB + 2GB (基础)

4 workers: 4 * 300MB + 2GB = 3.2GB
8 workers: 8 * 300MB + 2GB = 4.4GB
16 workers: 16 * 300MB + 2GB = 6.8GB
```

> ⚠️ **注意**：
> - Worker 过多会导致内存不足
> - Worker 过少会导致请求排队
> - 根据实际监控调整

#### 数据库优化

**PostgreSQL 配置**：
```ruby
# /etc/gitlab/gitlab.rb

# 共享缓冲区（推荐：系统内存的 25%）
postgresql['shared_buffers'] = '256MB'  # 4GB 系统
postgresql['shared_buffers'] = '512MB'  # 8GB 系统
postgresql['shared_buffers'] = '1GB'    # 16GB 系统
postgresql['shared_buffers'] = '2GB'    # 32GB 系统

# 工作内存（每个连接）
postgresql['work_mem'] = '16MB'

# 维护工作内存（VACUUM、CREATE INDEX）
postgresql['maintenance_work_mem'] = '256MB'

# 有效缓存大小（推荐：系统内存的 50-75%）
postgresql['effective_cache_size'] = '2GB'  # 4GB 系统
postgresql['effective_cache_size'] = '4GB'  # 8GB 系统
postgresql['effective_cache_size'] = '8GB'  # 16GB 系统

# 最大连接数
postgresql['max_connections'] = 800

# 检查点配置
postgresql['checkpoint_timeout'] = '15min'
postgresql['checkpoint_completion_target'] = 0.9

# WAL 配置
postgresql['wal_buffers'] = '16MB'
postgresql['min_wal_size'] = '1GB'
postgresql['max_wal_size'] = '4GB'

# 慢查询日志（毫秒）
postgresql['log_min_duration_statement'] = 1000  # 1 秒

# 连接池
postgresql['statement_timeout'] = 60000  # 60 秒
```

**数据库维护**：
```bash
# 分析表统计信息
sudo -u gitlab-psql /opt/gitlab/embedded/bin/vacuumdb --all --analyze

# 清理死锁
sudo -u gitlab-psql /opt/gitlab/embedded/bin/vacuumdb --all --verbose

# 重建索引
sudo -u gitlab-psql /opt/gitlab/embedded/bin/reindexdb --all

# 查看慢查询
sudo -u gitlab-psql /opt/gitlab/embedded/bin/psql -h /var/opt/gitlab/postgresql -U gitlab \
  -c "SELECT query, calls, total_time, mean_time FROM pg_stat_statements ORDER BY mean_time DESC LIMIT 10;"
```

#### Redis 优化

**Redis 配置**：
```ruby
# /etc/gitlab/gitlab.rb

# 最大内存（推荐：系统内存的 10-20%）
redis['maxmemory'] = '512mb'  # 4GB 系统
redis['maxmemory'] = '1gb'    # 8GB 系统
redis['maxmemory'] = '2gb'    # 16GB 系统

# 内存淘汰策略
# allkeys-lru: 淘汰最近最少使用的键
# volatile-lru: 仅淘汰有过期时间的键
# allkeys-random: 随机淘汰
redis['maxmemory_policy'] = 'allkeys-lru'

# 超时时间（0 = 永不超时）
redis['timeout'] = 0

# TCP keepalive（秒）
redis['tcp_keepalive'] = 300

# 持久化
redis['appendonly'] = 'yes'  # 启用 AOF
redis['appendfsync'] = 'everysec'  # 每秒同步
```

**Redis 监控**：
```bash
# 查看 Redis 信息
/opt/gitlab/embedded/bin/redis-cli -s /var/opt/gitlab/redis/redis.socket INFO

# 查看内存使用
/opt/gitlab/embedded/bin/redis-cli -s /var/opt/gitlab/redis/redis.socket INFO memory

# 查看慢查询
/opt/gitlab/embedded/bin/redis-cli -s /var/opt/gitlab/redis/redis.socket SLOWLOG GET 10

# 查看连接数
/opt/gitlab/embedded/bin/redis-cli -s /var/opt/gitlab/redis/redis.socket CLIENT LIST | wc -l
```

#### 大仓库处理方案

**Git LFS 配置**：
```ruby
# /etc/gitlab/gitlab.rb

# 启用 Git LFS
gitlab_rails['lfs_enabled'] = true

# LFS 存储路径
gitlab_rails['lfs_storage_path'] = "/var/opt/gitlab/gitlab-rails/lfs-objects"

# 最大文件大小（字节）
gitlab_rails['max_attachment_size'] = 104857600  # 100MB
gitlab_rails['max_import_size'] = 104857600  # 100MB
```

**使用 Git LFS**：
```bash
# 安装 Git LFS
git lfs install

# 跟踪大文件
git lfs track "*.psd"
git lfs track "*.zip"
git lfs track "*.tar.gz"
git lfs track "datasets/*.csv"

# 提交 .gitattributes
git add .gitattributes
git commit -m "Configure Git LFS"

# 推送 LFS 对象
git push origin main
```

**清理大文件历史**：
```bash
# 1. 查找大文件
git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail 5 | awk '{print$1}')"

# 2. 使用 BFG Repo-Cleaner（推荐）
java -jar bfg.jar --strip-blobs-bigger-than 50M .

# 3. 或使用 git-filter-branch
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/large-file' \
  --prune-empty --tag-name-filter cat -- --all

# 4. 清理引用
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 5. 强制推送（⚠️ 危险！）
git push origin --force --all
```

> ⚠️ **警告**：
> - 清理历史会改变提交哈希
> - 需要所有协作者重新克隆
> - 先在备份上测试

#### Gitaly 优化

**Gitaly 配置**：
```ruby
# /etc/gitlab/gitlab.rb

# Ruby 最大内存（字节）
gitaly['ruby_max_rss'] = 300000000  # 300MB

# gRPC 最大消息大小（字节）
gitaly['grpc_max_call_recv_msg_size'] = 209715200  # 200MB

# Gitaly 并发限制
gitaly['concurrency'] = [
  { 'rpc' => '/gitaly.SmartHTTPService/PostReceivePack', 'max_per_repo' => 20 },
  { 'rpc' => '/gitaly.SSHService/SSHUploadPack', 'max_per_repo' => 5 },
  { 'rpc' => '/gitaly.CommitService/GetCommit', 'max_per_repo' => 50 },
  { 'rpc' => '/gitaly.DiffService/GetDiff', 'max_per_repo' => 10 }
]

# Gitaly 存储路径
gitaly['storage'] = [
  { 'path' => '/var/opt/gitlab/git-data/repositories' }
]
```

#### Nginx 优化

**Nginx 配置**：
```ruby
# /etc/gitlab/gitlab.rb

# Worker 进程数
nginx['worker_processes'] = 4

# Worker 连接数
nginx['worker_connections'] = 10240

# 启用 HTTP/2
nginx['http2'] = true

# 客户端最大请求体大小
nginx['client_max_body_size'] = '100m'

# 保持连接超时
nginx['keepalive_timeout'] = 65

# 启用 Gzip 压缩
nginx['gzip_enabled'] = true
nginx['gzip_comp_level'] = 6
nginx['gzip_min_length'] = 1000
nginx['gzip_types'] = ['text/plain', 'text/css', 'application/json', 'application/javascript']

# SSL 会话缓存
nginx['ssl_session_cache'] = 'shared:SSL:10m'
nginx['ssl_session_timeout'] = '10m'
```

#### Sidekiq 优化

**Sidekiq 配置**：
```ruby
# /etc/gitlab/gitlab.rb

# Sidekiq 并发数
sidekiq['max_concurrency'] = 25

# Sidekiq 队列限制
sidekiq['job_timeout'] = 60

# 内存限制
sidekiq['shutdown_timeout'] = 30
```

**Sidekiq 队列监控**：
```bash
# 查看队列状态
sudo gitlab-rake gitlab:sidekiq:queue:status

# 查看积压任务
sudo gitlab-rake gitlab:sidekiq:jobs:status

# 重启 Sidekiq
sudo gitlab-ctl restart sidekiq
```

#### 性能监控指标

**关键性能指标**：

| 指标 | 健康值 | 警告值 | 危险值 |
|:---|:---|:---|:---|
| **Puma 响应时间** | <200ms | 200-500ms | >500ms |
| **数据库查询时间** | <50ms | 50-200ms | >200ms |
| **Redis 响应时间** | <10ms | 10-50ms | >50ms |
| **内存使用率** | <70% | 70-85% | >85% |
| **CPU 使用率** | <60% | 60-80% | >80% |
| **磁盘使用率** | <70% | 70-85% | >85% |
| **Sidekiq 队列积压** | <100 | 100-500 | >500 |
| **5xx 错误率** | <0.1% | 0.1-1% | >1% |

**性能分析工具**：
```bash
# GitLab 内置性能面板
# Admin Area → Monitoring → Performance

# 查看慢请求
sudo gitlab-ctl tail nginx | grep -E "[1-5]s$"

# 查看数据库慢查询
sudo gitlab-ctl tail postgresql | grep "duration:"

# 使用 pg_stat_statements
sudo -u gitlab-psql /opt/gitlab/embedded/bin/psql -h /var/opt/gitlab/postgresql -U gitlab \
  -c "SELECT * FROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT 10;"
```

---

### 7.7 日常维护与巡检

#### 服务状态巡检脚本

```bash
#!/bin/bash
# /usr/local/bin/gitlab-health-check.sh

GITLAB_URL="https://gitlab.company.com"
TOKEN="glpat-xxxxxxxxxxxx"

echo "=== GitLab 健康检查 ==="
echo "时间：$(date)"
echo ""

# 1. 检查服务状态
echo "【1】服务状态检查"
sudo gitlab-ctl status | grep -E "run|down"
echo ""

# 2. 检查磁盘空间
echo "【2】磁盘空间检查"
df -h /var/opt/gitlab | awk 'NR==2 {print "使用率:", $5}'
echo ""

# 3. 检查内存使用
echo "【3】内存使用检查"
free -h | awk 'NR==2 {print "使用率:", $3"/"$2, "("$3/$2*100"%)"}'
echo ""

# 4. 检查备份
echo "【4】备份检查"
LATEST_BACKUP=$(ls -t /var/opt/gitlab/backups/*.tar 2>/dev/null | head -1)
if [ -n "$LATEST_BACKUP" ]; then
  BACKUP_TIME=$(stat -c %Y "$LATEST_BACKUP")
  CURRENT_TIME=$(date +%s)
  AGE=$((CURRENT_TIME - BACKUP_TIME))
  HOURS=$((AGE / 3600))
  echo "最新备份：$(basename $LATEST_BACKUP)"
  echo "备份时间：${HOURS}小时前"
else
  echo "❌ 未找到备份文件"
fi
echo ""

# 5. 检查 GitLab API
echo "【5】API 健康检查"
curl -s -o /dev/null -w "HTTP 状态码：%{http_code}\n" \
  -H "PRIVATE-TOKEN: $TOKEN" \
  "${GITLAB_URL}/api/v4/version"
echo ""

# 6. 检查 Runner 状态
echo "【6】Runner 状态检查"
sudo gitlab-runner list 2>/dev/null | grep -E "active|paused"
echo ""

echo "=== 检查完成 ==="
```

#### Grafana 监控面板

```
推荐导入的 Grafana 面板：

1. GitLab 官方面板
   - ID: 16006
   - 包含：系统概览、API 性能、数据库性能

2. GitLab CI/CD 面板
   - ID: 10566
   - 包含：流水线状态、构建时间、成功率

3. Node Exporter 面板
   - ID: 1860
   - 包含：CPU、内存、磁盘、网络

导入方法：
1. Grafana → Dashboards → Import
2. 输入面板 ID
3. 选择数据源（Prometheus）
4. 点击 Import
```

#### 告警规则配置

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

      - alert: HighErrorRate
        expr: rate(gitlab_rails_requests_total{status="5xx"}[5m]) > 0.1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "GitLab 错误率过高"
          description: "5xx 错误率超过 10%"

      - alert: PipelineFailureRate
        expr: rate(gitlab_ci_pipelines_failed_total[1h]) > 0.2
        for: 30m
        labels:
          severity: warning
        annotations:
          summary: "流水线失败率过高"
          description: "流水线失败率超过 20%"
```

#### 日常维护周期建议

| 周期 | 任务 | 说明 |
|:---|:---|:---|
| **每天** | 检查服务状态 | 确认所有服务正常运行 |
| **每天** | 检查备份 | 确认备份成功完成 |
| **每天** | 检查磁盘空间 | 确保磁盘使用率<80% |
| **每周** | 检查日志 | 查看错误日志和警告 |
| **每周** | 检查 Runner | 确认 Runner 在线且正常 |
| **每月** | 性能分析 | 查看慢查询和性能瓶颈 |
| **每月** | 清理旧数据 | 清理旧日志、旧备份、旧 artifacts |
| **每月** | 安全更新 | 应用系统安全补丁 |
| **每季度** | 恢复演练 | 测试备份恢复流程 |
| **每季度** | 容量规划 | 评估资源使用情况，规划扩容 |
| **每年** | 版本升级 | 升级到最新 LTS 版本 |

---

## 第 6 章 GitLab 备份与容灾

### 6.1-6.8 保持原有内容

### 6.9 备份自动清理策略

#### 本地备份清理

**基础清理脚本**：
```bash
#!/bin/bash
# /usr/local/bin/gitlab-cleanup-backups.sh

BACKUP_DIR="/var/opt/gitlab/backups"
RETENTION_DAYS=7

echo "清理 ${RETENTION_DAYS} 天前的备份..."

# 查找并删除旧备份
find ${BACKUP_DIR} -name "*.tar" -mtime +${RETENTION_DAYS} -delete

# 记录清理日志
echo "$(date): 清理完成" >> /var/log/gitlab/backup-cleanup.log

# 显示剩余备份
echo "当前备份文件："
ls -lh ${BACKUP_DIR}/*.tar 2>/dev/null
```

**增强清理脚本（带通知）**：
```bash
#!/bin/bash
# /usr/local/bin/gitlab-cleanup-backups-enhanced.sh

set -e

BACKUP_DIR="/var/opt/gitlab/backups"
RETENTION_DAYS=7
LOG_FILE="/var/log/gitlab/backup-cleanup.log"
WEBHOOK_URL="${DINGTALK_WEBHOOK:-}"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a ${LOG_FILE}
}

# 清理前统计
log "=== 备份清理开始 ==="
BEFORE_COUNT=$(ls -1 ${BACKUP_DIR}/*.tar 2>/dev/null | wc -l)
BEFORE_SIZE=$(du -sh ${BACKUP_DIR} 2>/dev/null | cut -f1)
log "清理前：${BEFORE_COUNT} 个文件，${BEFORE_SIZE}"

# 清理旧备份
DELETED_COUNT=0
for file in ${BACKUP_DIR}/*.tar; do
  if [ -f "$file" ]; then
    FILE_AGE=$(( ($(date +%s) - $(stat -c %Y "$file")) / 86400 ))
    if [ ${FILE_AGE} -gt ${RETENTION_DAYS} ]; then
      rm -f "$file"
      DELETED_COUNT=$((DELETED_COUNT + 1))
      log "删除：$(basename $file) (${FILE_AGE}天)"
    fi
  fi
done

# 清理后统计
AFTER_COUNT=$(ls -1 ${BACKUP_DIR}/*.tar 2>/dev/null | wc -l)
AFTER_SIZE=$(du -sh ${BACKUP_DIR} 2>/dev/null | cut -f1)
log "清理后：${AFTER_COUNT} 个文件，${AFTER_SIZE}"
log "删除：${DELETED_COUNT} 个文件"
log "=== 备份清理完成 ==="

# 发送通知
if [ -n "${WEBHOOK_URL}" ] && [ ${DELETED_COUNT} -gt 0 ]; then
  curl -X POST "${WEBHOOK_URL}" \
    -H "Content-Type: application/json" \
    -d "{
      \"msgtype\": \"text\",
      \"text\": {
        \"content\": \"GitLab 备份清理完成\\n删除：${DELETED_COUNT} 个文件\\n剩余：${AFTER_COUNT} 个文件\\n占用：${AFTER_SIZE}\"
      }
    }"
fi
```

#### 配置定时清理

```bash
# 编辑 crontab
sudo crontab -e

# 每天凌晨 5 点清理（备份后 1 小时）
0 5 * * * /usr/local/bin/gitlab-cleanup-backups.sh >> /var/log/gitlab/backup-cleanup.log 2>&1

# 或使用增强版（带通知）
0 5 * * * /usr/local/bin/gitlab-cleanup-backups-enhanced.sh
```

#### 备份保留策略建议

| 环境 | 本地保留 | 远程保留 | 归档保留 |
|:---|:---|:---|:---|
| **开发** | 3 天 | 7 天 | 无 |
| **测试** | 7 天 | 30 天 | 无 |
| **预发布** | 7 天 | 30 天 | 90 天 |
| **生产** | 7 天 | 30 天 | 1 年 |

#### S3 备份生命周期策略

```json
{
  "Rules": [
    {
      "ID": "BackupRetention",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "gitlab-backups/"
      },
      "Expiration": {
        "Days": 30
      },
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 7
      }
    },
    {
      "ID": "ArchiveOldBackups",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "gitlab-backups/"
      },
      "Transitions": [
        {
          "Days": 90,
          "StorageClass": "GLACIER"
        }
      ]
    }
  ]
}
```

```bash
# 应用生命周期策略
aws s3api put-bucket-lifecycle-configuration \
  --bucket gitlab-backups \
  --lifecycle-configuration file://lifecycle-policy.json

# 验证策略
aws s3api get-bucket-lifecycle-configuration --bucket gitlab-backups
```

---

### 6.10 跨区域容灾方案

#### 容灾架构设计

**方案 A：主从热备**：
```
主数据中心（北京）
┌─────────────────┐
│  GitLab 集群    │
│  10.0.0.0/24    │
│  实时备份       │
│  (每 4 小时)    │
└────────┬────────┘
         │
         │ 异步复制
         │ (rsync + cron)
         ▼
┌─────────────────┐
│  备份数据中心   │
│  (上海)         │
│  172.16.0.0/24  │
│  热备状态       │
│  (可快速切换)   │
└─────────────────┘

RTO: < 4 小时
RPO: < 4 小时
成本：中等
```

**方案 B：双活集群**：
```
数据中心 A（北京）          数据中心 B（上海）
┌─────────────────┐        ┌─────────────────┐
│  GitLab 节点 1  │◄──────►│  GitLab 节点 2  │
│  10.0.0.10      │  同步  │  172.16.0.10    │
│  活跃           │        │  活跃           │
└────────┬────────┘        └────────┬────────┘
         │                          │
         └──────────┬───────────────┘
                    │
              ┌─────▼─────┐
              │  全局负载均衡  │
              │  (DNS/GSLB)  │
              └─────┬─────┘
                    │
              ┌─────▼─────┐
              │   用户访问   │
              └───────────┘

RTO: < 5 分钟
RPO: ~0
成本：高
```

**方案 C：冷备份**：
```
生产环境
┌─────────────────┐
│  GitLab 生产    │
│  10.0.0.200     │
└────────┬────────┘
         │
         │ 定时备份
         │ (每天凌晨)
         ▼
┌─────────────────┐
│  备份存储       │
│  (S3/NAS/磁带)  │
│  离线保存       │
└─────────────────┘

RTO: < 24 小时
RPO: < 24 小时
成本：低
```

#### 跨区域同步方案

**完整同步脚本**：
```bash
#!/bin/bash
# /usr/local/bin/gitlab-sync-dr.sh

set -e

# 配置
PRIMARY_HOST="gitlab-primary.company.com"
DR_HOST="gitlab-dr.company.com"
BACKUP_DIR="/var/opt/gitlab/backups"
DR_BACKUP_DIR="/backup/dr"
CONFIG_DIR="/etc/gitlab"
LOG_FILE="/var/log/gitlab/dr-sync.log"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a ${LOG_FILE}
}

# 1. 在主节点执行备份
log "【1/5】在主节点执行备份..."
ssh ${PRIMARY_HOST} "sudo gitlab-rake gitlab:backup:create"

# 2. 同步备份文件到灾备中心
log "【2/5】同步备份文件到灾备中心..."
rsync -avz --progress \
  ${PRIMARY_HOST}:${BACKUP_DIR}/ \
  ${DR_BACKUP_DIR}/ \
  --delete

# 3. 同步配置文件
log "【3/5】同步配置文件..."
rsync -avz \
  ${PRIMARY_HOST}:${CONFIG_DIR}/gitlab.rb \
  ${DR_BACKUP_DIR}/config/
rsync -avz \
  ${PRIMARY_HOST}:${CONFIG_DIR}/gitlab-secrets.json \
  ${DR_BACKUP_DIR}/config/

# 4. 同步 SSH 密钥（可选）
log "【4/5】同步 SSH 密钥..."
rsync -avz \
  ${PRIMARY_HOST}:/var/opt/gitlab/.ssh/ \
  ${DR_BACKUP_DIR}/ssh/

# 5. 验证同步
log "【5/5】验证同步..."
ssh ${DR_HOST} "ls -lh ${DR_BACKUP_DIR} | tail -5"

# 检查最新备份时间
LATEST_BACKUP=$(ssh ${DR_HOST} "ls -t ${DR_BACKUP_DIR}/*.tar | head -1")
if [ -n "$LATEST_BACKUP" ]; then
  BACKUP_TIME=$(ssh ${DR_HOST} "stat -c %Y $LATEST_BACKUP")
  CURRENT_TIME=$(date +%s)
  AGE=$((CURRENT_TIME - BACKUP_TIME))
  HOURS=$((AGE / 3600))
  log "最新备份：${HOURS}小时前"
  
  if [ ${HOURS} -gt 24 ]; then
    log "⚠️ 警告：备份超过 24 小时未更新！"
    # 发送告警通知
  fi
else
  log "❌ 错误：未找到备份文件！"
  exit 1
fi

log "=== 灾备同步完成 ==="
```

**配置定时同步**：
```bash
# 编辑 crontab
sudo crontab -e

# 每 4 小时同步一次
0 */4 * * * /usr/local/bin/gitlab-sync-dr.sh

# 或每天凌晨 3 点同步
0 3 * * * /usr/local/bin/gitlab-sync-dr.sh
```

#### 故障切换流程

**切换检查清单**：

```
□ 1. 确认主站点故障
   □ Ping 测试失败
   □ HTTP 请求超时
   □ 监控告警确认
   □ 联系主站点运维确认

□ 2. 评估故障影响
   □ 预计恢复时间
   □ 影响用户数量
   □ 关键业务影响

□ 3. 决策是否切换
   □ RTO 要求（<4 小时）
   □ 数据一致性风险
   □ 切换成本评估

□ 4. 执行切换（如决策切换）
   □ 通知相关人员
   □ 停止主站点写入（如可能）
   □ 恢复灾备站点备份
   □ 更新 DNS 解析
   □ 验证灾备站点功能

□ 5. 通知用户
   □ 发送故障通知
   □ 提供临时访问地址
   □ 预估恢复时间
   □ 定期更新进展

□ 6. 主站点恢复后
   □ 数据反向同步
   □ 验证数据一致性
   □ 切换回主站点
   □ 恢复灾备状态
   □ 编写事故报告
```

**DNS 故障切换**：

```bash
# 使用 AWS Route53 健康检查 + 故障转移

# 主记录（带健康检查）
gitlab.company.com. 300 IN A 10.0.0.200
; 健康检查 ID: hc-12345678
; 检查间隔：30 秒
; 失败阈值：3 次

# 灾备记录（故障转移）
gitlab.company.com. 300 IN A 172.16.0.200
; 故障转移记录
; 关联健康检查：hc-12345678
; 仅当主记录不可用时生效
```

**手动 DNS 切换**：
```bash
# 修改 DNS 记录（阿里云示例）
aliyun alidns UpdateDomainRecord \
  --RecordId "123456789" \
  --RR "gitlab" \
  --Type "A" \
  --Value "172.16.0.200" \
  --TTL "60"

# 验证 DNS 传播
dig gitlab.company.com +short
# 应返回 172.16.0.200
```

#### 备份恢复演练

**演练计划**：

```
演练频率：每季度一次
演练时间：周六凌晨 2:00-6:00
参与人员：运维团队、开发代表
演练环境：隔离的测试环境

演练场景：
1. 完整恢复（从备份恢复整个 GitLab）
2. 项目恢复（恢复单个项目）
3. 数据库恢复（恢复特定数据库表）
4. 跨区域切换（切换到灾备站点）

演练步骤：
1. 准备测试环境
2. 执行备份恢复
3. 验证功能正常
4. 记录恢复时间
5. 编写演练报告
6. 优化恢复流程
```

**恢复测试脚本**：
```bash
#!/bin/bash
# /usr/local/bin/gitlab-restore-test.sh

set -e

BACKUP_FILE="$1"
TEST_SERVER="gitlab-test.company.com"

if [ -z "$BACKUP_FILE" ]; then
  echo "用法：$0 <备份文件>"
  exit 1
fi

echo "=== GitLab 恢复测试 ==="
echo "备份文件：$BACKUP_FILE"
echo "测试服务器：$TEST_SERVER"
echo ""

# 1. 上传备份到测试服务器
echo "【1/5】上传备份文件..."
scp $BACKUP_FILE ${TEST_SERVER}:/var/opt/gitlab/backups/

# 2. 停止 GitLab 服务
echo "【2/5】停止测试服务器 GitLab 服务..."
ssh ${TEST_SERVER} "sudo gitlab-ctl stop"

# 3. 恢复备份
echo "【3/5】恢复备份..."
BACKUP_NAME=$(basename $BACKUP_FILE _gitlab_backup.tar)
ssh ${TEST_SERVER} "sudo gitlab-rake gitlab:backup:restore BACKUP=${BACKUP_NAME} FORCE=true"

# 4. 启动 GitLab 服务
echo "【4/5】启动 GitLab 服务..."
ssh ${TEST_SERVER} "sudo gitlab-ctl start"

# 5. 验证恢复
echo "【5/5】验证恢复..."
sleep 60  # 等待服务启动

# 检查服务状态
ssh ${TEST_SERVER} "sudo gitlab-ctl status"

# 检查 Web 访问
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" https://${TEST_SERVER})
if [ "$HTTP_CODE" = "200" ]; then
  echo "✅ Web 访问正常"
else
  echo "❌ Web 访问失败 (HTTP $HTTP_CODE)"
  exit 1
fi

echo ""
echo "=== 恢复测试完成 ==="
echo "请在浏览器访问：https://${TEST_SERVER}"
echo "验证项目、用户、流水线等功能"
```

#### 容灾演练报告模板

```markdown
# GitLab 容灾演练报告

## 演练信息
- 演练日期：2026-03-21
- 演练时间：02:00-06:00
- 参与人员：张三、李四、王五
- 演练场景：主站点故障，切换到灾备站点

## 演练目标
- [x] 验证灾备站点可正常接管
- [x] 验证数据完整性
- [x] 测试 RTO/RPO 达标
- [x] 验证切换流程文档

## 关键指标
- RTO（恢复时间目标）：2 小时 30 分（目标：<4 小时）✅
- RPO（恢复点目标）：3 小时 45 分（目标：<4 小时）✅
- 数据完整性：100% ✅
- 服务可用性：100% ✅

## 演练步骤
1. 02:00 - 开始演练
2. 02:10 - 模拟主站点故障
3. 02:15 - 启动切换流程
4. 03:30 - 灾备站点接管完成
5. 04:00 - 功能验证完成
6. 04:30 - 通知用户切换
7. 06:00 - 演练结束

## 发现问题
1. DNS 传播时间较长（~30 分钟）
2. 部分用户会话丢失
3. 监控告警延迟

## 改进措施
1. 降低 DNS TTL 到 60 秒
2. 优化会话持久化配置
3. 调整监控告警阈值

## 结论
演练成功，灾备方案可行。建议每半年进行一次完整演练。

报告人：张三
日期：2026-03-21
```

---
rsync -avz --progress \
  ${PRIMARY_HOST}:${BACKUP_DIR}/ \
  ${DR_BACKUP_DIR}/

# 3. 同步配置文件
echo "同步配置文件..."
rsync -avz \
  ${PRIMARY_HOST}:/etc/gitlab/gitlab.rb \
  ${DR_BACKUP_DIR}/config/
rsync -avz \
  ${PRIMARY_HOST}:/etc/gitlab/gitlab-secrets.json \
  ${DR_BACKUP_DIR}/config/

# 4. 验证同步
echo "验证同步..."
ssh ${DR_HOST} "ls -lh ${DR_BACKUP_DIR} | tail -5"

echo "灾备同步完成"
```

#### 故障切换流程

```
1. 确认主站点故障
   - 检查网络连通性
   - 检查服务状态
   - 确认无法快速恢复

2. 启用灾备站点
   - 登录灾备 GitLab
   - 恢复最新备份
   - 更新 DNS 解析

3. 通知用户
   - 发送故障通知
   - 提供临时访问地址
   - 预估恢复时间

4. 主站点恢复后
   - 数据反向同步
   - 切换回主站点
   - 恢复灾备状态
```

#### DNS 故障切换

```bash
# 使用 Route53 健康检查 + 故障转移

# 主记录
gitlab.company.com. 300 IN A 10.0.0.200
; 健康检查：每 30 秒
; 故障转移：3 次失败后切换

# 灾备记录
gitlab.company.com. 300 IN A 172.16.0.200
; 故障转移记录
; 仅当主记录不可用时生效
```

---

## 附录 A：快速参考卡片

### 常用命令速查

```bash
# 服务管理
gitlab-ctl status          # 查看服务状态
gitlab-ctl restart         # 重启所有服务
gitlab-ctl reconfigure     # 重新配置

# 备份恢复
gitlab-rake gitlab:backup:create      # 创建备份
gitlab-rake gitlab:backup:restore     # 恢复备份

# 健康检查
gitlab-rake gitlab:check              # 系统检查
gitlab-rake gitlab:ldap:check         # LDAP 检查

# 日志查看
gitlab-ctl tail                       # 查看所有日志
gitlab-ctl tail nginx                 # 查看 Nginx 日志

# Runner 管理
gitlab-runner list                    # 列出 Runner
gitlab-runner restart                 # 重启 Runner
```

### 端口速查

| 端口 | 服务 | 说明 |
|:---:|:---|:---|
| 80 | HTTP | Web 访问（重定向到 HTTPS） |
| 443 | HTTPS | Web 访问（加密） |
| 22 | SSH | Git SSH 克隆 |
| 2222 | SSH | Git SSH 克隆（Docker） |
| 8080 | Prometheus | 监控指标 |
| 9090 | Prometheus | Web 界面 |
| 3000 | Grafana | 监控面板 |
| 9000 | SonarQube | 代码质量 |
| 8081 | Nexus | 制品库 |

### 配置文件位置

| 文件 | 路径 | 说明 |
|:---|:---|:---|
| 主配置 | /etc/gitlab/gitlab.rb | GitLab 主配置 |
| 密钥 | /etc/gitlab/gitlab-secrets.json | 密钥文件 |
| 数据 | /var/opt/gitlab | 数据目录 |
| 备份 | /var/opt/gitlab/backups | 备份目录 |
| 日志 | /var/log/gitlab | 日志目录 |
| Runner | /etc/gitlab-runner/config.toml | Runner 配置 |

---

## 附录 B：常见问题 FAQ

### Q1: 内存不足怎么办？

**A**: 
1. 增加 Swap 分区（至少 4GB）
2. 减少 Puma worker 数量
3. 升级服务器内存
4. 使用 Docker 限制资源

### Q2: 如何升级 GitLab？

**A**:
```bash
# 1. 备份
gitlab-rake gitlab:backup:create

# 2. 升级
yum update gitlab-ce

# 3. 重新配置
gitlab-ctl reconfigure

# 4. 运行数据库迁移
gitlab-rake gitlab:migrate

# 5. 验证
gitlab-rake gitlab:check
```

### Q3: 如何重置 root 密码？

**A**:
```bash
sudo gitlab-rake "gitlab:password:reset[root]"
# 按提示输入新密码
```

### Q4: 如何迁移 GitLab 到新服务器？

**A**:
1. 旧服务器执行完整备份
2. 复制备份文件到新服务器
3. 复制配置文件（gitlab.rb、gitlab-secrets.json）
4. 新服务器恢复备份
5. 更新 DNS 解析

### Q5: CI/CD 流水线慢怎么办？

**A**:
1. 使用缓存减少依赖下载
2. 并行执行独立任务
3. 使用 Docker 层缓存
4. 增加 Runner 并发数
5. 优化测试用例

---

**文档版本**: v3.0  
**GitLab 版本**: 16.8.3 LTS  
**更新时间**: 2026-03-21  
**作者**: hjs2015 <1656126280@qq.com>  
**仓库地址**: https://github.com/hjs2015/git-tutorial  
**许可证**: CC BY-SA 4.0

# SonarQube 代码质量管理

> 📘 **CI/CD 实战版教程第四部分**  
> 📌 包含：MySQL 安装、SonarQube 部署、Jenkins 集成

---

## 目录

- [第 9 章 SonarQube 部署](#第 9 章-sonarqube 部署)
- [第 10 章 SonarQube 与 Jenkins 集成](#第 10 章-sonarqube 与-jenkins 集成)

---

## 第 9 章 SonarQube 部署

### 9.1 安装 MySQL（SonarQube 数据库）

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

### 9.2 安装 SonarQube

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

### 9.3 解决启动报错

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

### 9.4 初始化 SonarQube

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

## 第 10 章 SonarQube 与 Jenkins 集成

### 10.1 安装 Sonar 客户端

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

### 10.2 推送代码到 SonarQube

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

### 10.3 Jenkins 集成 SonarQube

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

### 10.4 项目配置 Sonar 扫描

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

### 10.5 测试完整流程

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

## 🎯 实战练习

### 练习 1：安装 SonarQube
```bash
# 目标：完成 SonarQube 安装和配置

步骤：
1. 安装 MySQL 数据库
2. 创建 sonar 数据库
3. 安装 SonarQube
4. 配置数据库连接
5. 启动并验证服务
```

### 练习 2：代码质量扫描
```bash
# 目标：掌握 SonarQube 基本使用

步骤：
1. 安装 Sonar 客户端
2. 配置项目信息
3. 执行代码扫描
4. 查看扫描结果
```

### 练习 3：Jenkins 集成
```bash
# 目标：实现自动化代码质量检查

步骤：
1. 安装 SonarQube 插件
2. 配置 Sonar 服务器
3. 配置项目扫描
4. 测试完整流程
```

---

## 📊 代码质量指标说明

### Bug（Bug）
```
严重程度：
- Blocker（阻塞）：必须立即修复
- Critical（严重）：需要尽快修复
- Major（主要）：应该修复
- Minor（次要）：可以稍后修复
- Info（提示）：可选修复
```

### Vulnerabilities（漏洞）
```
安全漏洞分类：
- SQL 注入
- XSS 跨站脚本
- 缓冲区溢出
- 敏感信息泄露
- 认证和授权问题
```

### Code Smells（代码异味）
```
常见问题：
- 重复代码
- 过长的方法
- 复杂的条件判断
- 未使用的变量
- 不规范的命名
```

### Coverage（覆盖率）
```
测试覆盖率：
- 行覆盖率：被测试覆盖的代码行比例
- 分支覆盖率：被测试覆盖的分支比例
- 条件覆盖率：被测试覆盖的条件组合比例

建议目标：
- 新项目：≥ 80%
- 老项目：≥ 60%
```

---

## 🔧 常见问题排查

### 问题 1：SonarQube 无法启动

**症状**：
```bash
systemctl status sonar.service
# Active: failed
```

**排查步骤**：
```bash
# 1. 查看日志
tail -f /opt/sonarqube/logs/sonar.log
tail -f /opt/sonarqube/logs/es.log

# 2. 检查数据库连接
mysql -uroot -p123456 -e 'show databases;'

# 3. 检查端口占用
netstat -lntup | grep 9000

# 4. 检查用户权限
ls -la /opt/sonarqube/
```

### 问题 2：扫描失败

**症状**：
```
ERROR: Error during SonarQube Scanner execution
```

**排查步骤**：
```bash
# 1. 检查 Token 是否有效
# 2. 检查网络连接
curl http://10.0.0.203:9000

# 3. 检查项目配置
cat sonar-project.properties

# 4. 查看详细日志
sonar-scanner -X
```

### 问题 3：Jenkins 集成失败

**症状**：
```
SonarQube server is not reachable
```

**排查步骤**：
```bash
# 1. 检查插件是否安装
# 2. 检查服务器配置
# 3. 检查 Token 权限
# 4. 检查网络连通性
```

---

## 📚 相关文档

- **Git 基础回顾** - [01-Git 基础回顾.md](./01-Git 基础回顾.md)
- **GitLab 企业级代码管理** - [02-GitLab 企业级代码管理.md](./02-GitLab 企业级代码管理.md)
- **Jenkins 持续集成** - [03-Jenkins 持续集成.md](./03-Jenkins 持续集成.md)

---

## 🌟 完整 CI/CD 流水线

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

**完整流程**：
1. 开发人员提交代码到 GitLab
2. GitLab Webhook 触发 Jenkins 构建
3. Jenkins 拉取代码并执行 SonarQube 扫描
4. 代码质量检查通过
5. 自动部署到测试环境
6. 自动化测试通过
7. 部署到预发布环境
8. 质量检查（性能、安全）
9. 部署到生产环境

---

**文档版本**: v1.0  
**提取自**: Git 完全指南-CICD 实战版.md  
**更新时间**: 2026-03-21  
**仓库地址**: https://github.com/hjs2015/git-tutorial

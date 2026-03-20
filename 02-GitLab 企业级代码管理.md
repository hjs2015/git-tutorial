# GitLab 企业级代码管理

> 📘 **CI/CD 实战版教程第二部分**  
> 📌 包含：安装部署、权限管理、备份恢复

---

## 目录

- [第 3 章 GitLab 安装部署](#第 3 章-gitlab 安装部署)
- [第 4 章 GitLab 权限管理](#第 4 章-gitlab 权限管理)
- [第 5 章 GitLab 备份与恢复](#第 5 章-gitlab 备份与恢复)

---

## 第 3 章 GitLab 安装部署

### 3.1 环境准备

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

### 3.2 安装 GitLab（方法 1：直接下载 RPM 包）

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

### 3.3 安装 GitLab（方法 2：配置 YUM 源）

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

### 3.4 配置 GitLab

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

### 3.5 Web 页面访问

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

### 3.6 GitLab 常用命令

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

## 第 4 章 GitLab 权限管理

### 4.1 用户 - 项目组 - 项目关系

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

### 4.2 权限实验需求

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

### 4.3 创建组和项目

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

### 4.4 创建用户

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

### 4.5 授权用户到组

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

### 4.6 SSH 公钥配置

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

### 4.7 克隆项目测试

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

### 4.8 创建分支并提交

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

### 4.9 创建合并请求 (Merge Request)

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

### 4.10 合并分支

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

## 第 5 章 GitLab 备份与恢复

### 5.1 为什么需要备份？

> **重要提示**：
> 
> 数据无价！备份是运维的基本职责。
> 
> **需要备份的内容**：
> - ✅ 代码仓库数据
> - ✅ 数据库（用户、项目、Issue 等）
> - ✅ 配置文件（gitlab.rb、gitlab-secrets.json）
> - ✅ 上传的文件（头像、附件等）

### 5.2 配置备份路径

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

### 5.3 执行备份

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

### 5.4 备份配置文件

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

### 5.5 恢复数据

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

### 5.6 定时备份（可选）

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

## 🎯 实战练习

### 练习 1：完整部署 GitLab
```bash
# 目标：在服务器上部署 GitLab 并配置完成

步骤：
1. 下载 GitLab RPM 包
2. 安装并配置 external_url
3. 执行 gitlab-ctl reconfigure
4. Web 界面访问并设置密码
5. 创建测试项目和用户
```

### 练习 2：权限管理实验
```bash
# 目标：掌握 GitLab 权限管理

步骤：
1. 创建 dev 和 ops 两个组
2. 创建 3 个用户（cto、dev、ops）
3. 配置不同的访问权限
4. 测试权限控制
```

### 练习 3：备份与恢复
```bash
# 目标：掌握 GitLab 备份恢复流程

步骤：
1. 配置备份路径
2. 执行完整备份
3. 备份配置文件
4. 模拟恢复流程
```

---

## 📚 相关文档

- **Git 基础回顾** - [01-Git 基础回顾.md](./01-Git 基础回顾.md)
- **Jenkins 持续集成** - [03-Jenkins 持续集成.md](./03-Jenkins 持续集成.md)
- **SonarQube 代码质量** - [04-SonarQube 代码质量.md](./04-SonarQube 代码质量.md)

---

**文档版本**: v1.0  
**提取自**: Git 完全指南-CICD 实战版.md  
**更新时间**: 2026-03-21  
**仓库地址**: https://github.com/hjs2015/git-tutorial

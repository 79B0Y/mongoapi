### MongoAPI Assistant 原始提示词记录整理

#### 🧩 功能扩展请求
- 我需要一个应用来完成这个，包括通过 configuration.yaml 来配置 MongoDB
- database collection 放在 http 请求里
- 我想执行直接输入 mongodb_upsert
- 能否将 MongoDB 的主要能力都用 HTTP request 实现掉
- 提供 zip 下载，然后提供详细的设计文档和操作说明
- 安装后，直接输入 mongoapi 执行
- 文档用 md 方式输出
- 加入 n8n HTTP Request node 的具体使用方法
- 我希望在程序里增加日志，可以在配置文件里打开和关闭日志
- HTTP 请求增加 API 的状态，包含连接数据的地址、状态、数据库列表
- 如何查 API status
- 不是这样的，我需要有单独查 API 状态的接口
- 需要（添加 `/status` 接口）
- 重新整理接口文档，并且整理出最新的文档，包括设计文档、接口文档和安装使用文档
- 更新程序，需要支持在 ubuntu 系统开机自启动
- 合并进打包 ZIP、加入日志轮转支持
- Mongoapi Full Docs 里增加 简介和项目结构、安装与使用、配置文件 configuration.yaml、log 查看方式
- 重新打包一下，包含全部的文件
- Mongoapi Autostart 这个文件放在结构里哪个地方
- 设置一个 py 还是 sh 文件
- 生成完整 ZIP 包
- 增加数据库
- MongoAPI 软件已经完全可用了，将我所有的提示词整理出来

#### 🧪 问题排查
- curl -XPOST 请求 `/create_database` 返回 500 错误
- 我收到 Internal Server Error，怎么排查

#### 📄 输出格式指定
- 文档用 markdown 方式输出
- 我希望输出 JSON 格式
- 提供下载链接

#### 🛠️ 安装部署
- 安装后可以通过 mongoapi 执行
- 如何加入开机自启
- 安装脚本里加入日志轮转
- 安装脚本放在哪个目录下最合理
- 如何设置为 systemd 服务

#### 🧠 设计与建议
- 所有接口是否都应该返回 status？（答：不需要）
- `/status` 接口是否需要 service_name 字段？（答：需要）

###优化后的提示词

### MongoAPI 项目提示词（按阶段整理）

将提示词分为“需求分析 ➝ 功能开发 ➝ 部署配置 ➝ 文档编写 ➝ 问题排查”5 个阶段，以便更清晰表达开发意图。

---

## 🧭 阶段 1：需求分析

- 我需要一个 HTTP 接口应用，封装 MongoDB 的核心功能（insert/find/update/delete...）
- 这个程序需要通过 configuration.yaml 配置 MongoDB 地址、服务端口、日志文件
- 程序要能用命令 `mongoapi` 启动运行
- 我希望在 n8n 或远程设备中通过 HTTP 操作 MongoDB

---

## 🛠️ 阶段 2：功能开发请求

- 请实现 insert、find、update、delete、upsert、aggregate 等接口
- 请新增 `/status` 接口，用于查询连接状态、数据库结构、Mongo URI
- 请添加 `/create_database` 接口，主动创建数据库和集合
- 是否能统一接口响应格式，返回 result + status 信息？（改为只在 `/status` 中返回）
- 程序中增加日志控制开关，可记录连接事件、操作行为、错误信息

---

## 🚀 阶段 3：部署配置需求

- 请提供一份 Ubuntu 系统安装脚本，支持 systemd 开机自启
- 安装脚本应创建虚拟环境、安装依赖、生成服务文件并启动服务
- 日志文件需要加入 logrotate，每周轮转并压缩
- 请打包为 zip 文件，包含全部源代码、配置、install.sh 脚本

---

## 📄 阶段 4：文档生成请求

- 请用 markdown 生成完整文档，包含以下部分：
  - 项目简介
  - 项目结构说明
  - 安装与使用
  - configuration.yaml 字段说明
  - 日志查看方式
  - 所有 HTTP API 接口说明
  - 示例 curl 与 n8n 配置
- 是否能导出为 PDF 或 HTML 文档？

---

## 🧪 阶段 5：运行问题排查

- curl 调用 `/create_database` 报错 500，请帮我添加异常捕获并返回错误信息 JSON
- 如何确认 MongoAPI 服务是否运行？在哪查看日志？
- 如果遇到依赖无法安装，如何使用国内源？

---

> 该结构便于你后续快速调用不同阶段的功能请求，并利于多项目共用类似提示模版

---

> 本列表为用户与 Assistant 交互中提出的重要功能/请求/问题整理，可用于后续产品文档、助手训练或接口优化依据。

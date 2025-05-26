### MongoAPI Assistant 提示词记录整理

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

---

> 本列表为用户与 Assistant 交互中提出的重要功能/请求/问题整理，可用于后续产品文档、助手训练或接口优化依据。

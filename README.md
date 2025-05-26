# MongoDB HTTP API 服务文档（mongoapi CLI 版本）

## 📦 简介

该项目提供一个轻量级的 HTTP API 接口服务，封装了 MongoDB 的核心数据库能力，便于 n8n、前端系统、脚本等通过 HTTP 请求访问 MongoDB。

支持接口包括文档操作、聚合、状态查询、数据库创建等。

---

## 📁 项目结构

```
mongoapi/
├── mongoapi/
│   ├── main.py               # 主服务入口
│   ├── config_loader.py      # 读取配置文件
│   └── handlers/             # 各类 API 操作模块
├── configuration.yaml        # MongoDB 配置与日志配置
├── requirements.txt          # 安装依赖
├── setup.py                  # 安装脚本
```

---

## ⚙️ 安装使用说明

### 1. 解压并安装

```bash
unzip mongoapi_status_plus_db.zip
cd mongoapi_status_final
pip install .
```

### 2. 启动服务

```bash
mongoapi
```

默认监听地址：`http://0.0.0.0:8080`

---

## 🧩 配置文件 configuration.yaml

```yaml
mongodb:
  uri: "mongodb://localhost:27017"

server:
  host: "0.0.0.0"
  port: 8080

logging:
  enabled: true
  file: "mongoapi.log"
```

---

## 🌐 API 接口文档

### 🔹 `POST /insert`

插入单条文档。

```json
{
  "database": "test",
  "collection": "users",
  "document": { "name": "Alice", "age": 30 }
}
```

---

### 🔹 `POST /find`

查询集合中的文档。

```json
{
  "database": "test",
  "collection": "users",
  "query": { "age": { "$gte": 18 } },
  "projection": { "name": 1, "_id": 0 }
}
```

---

### 🔹 `POST /update`

更新文档。

```json
{
  "database": "test",
  "collection": "users",
  "filter": { "name": "Alice" },
  "update": { "age": 31 }
}
```

---

### 🔹 `POST /delete`

删除文档。

```json
{
  "database": "test",
  "collection": "users",
  "filter": { "name": "Alice" }
}
```

---

### 🔹 `POST /upsert`

更新或插入文档。

```json
{
  "database": "test",
  "collection": "users",
  "filter": { "name": "Bob" },
  "update": { "age": 25 }
}
```

---

### 🔹 `POST /aggregate`

执行聚合管道。

```json
{
  "database": "test",
  "collection": "users",
  "pipeline": [
    { "$group": { "_id": null, "avg_age": { "$avg": "$age" } } }
  ]
}
```

---

### 🔹 `POST /create_database`

显式创建数据库（可选建集合）。

```json
{
  "database": "newdb",
  "collection": "init_collection"
}
```

---

### 🔹 `GET /status`

获取 API 服务运行状态。

返回示例：

```json
{
  "service_name": "mongoapi",
  "connected": true,
  "uri": "mongodb://localhost:27017",
  "databases": {
    "test": ["users", "devices"],
    "admin": ["system.version"]
  }
}
```

---

## 🧠 设计说明与扩展建议

### ✅ 模块化架构

每个接口为独立模块，便于扩展和维护。

### ✅ 可配置日志

所有操作可记录日志，路径可配置。

### ✅ 可拓展能力建议

- [ ] 增加 `/count`, `/distinct`, `/create_index` 等接口
- [ ] 增加用户权限认证（Token/API Key）
- [ ] 添加 WebSocket 数据推送或订阅
- [ ] 集成 Swagger 自动文档
- [ ] Docker 镜像 & Systemd 后台守护

---

## 🧪 示例调用工具

- `curl`, `httpie`, `Postman`, `n8n` 中 HTTP Request 节点
- 支持 JSON 动态传参与 n8n 自动流程化调用

---

## 🧾 示例 n8n 请求配置

- URL: `http://localhost:8080/upsert`
- Method: `POST`
- Content-Type: `application/json`

```json
{
  "database": "test",
  "collection": "devices",
  "filter": { "did": "{{ $json.did }}" },
  "update": {
    "name": "{{ $json.name }}",
    "status": "{{ $json.status }}"
  }
}
```
---

## 📘 简介

MongoAPI 是一个轻量级、可移植的 HTTP API 服务，使用 Python + Flask 实现，封装了 MongoDB 的基础功能，包括：
- 插入、查询、更新、删除、聚合、upsert
- 状态查询
- 显式创建数据库
- 支持 n8n 自动化流程调用
- 提供 systemd 启动和日志轮转

适用于边缘设备、内网服务、嵌入式设备、测试系统、小型 SaaS 服务等快速集成场景。

---

## 🧱 项目结构说明

```
mongoapi_status_final/
├── mongoapi/
│   ├── main.py              # 启动入口
│   ├── config_loader.py     # 读取 configuration.yaml
│   └── handlers/            # 各路由接口模块
│       ├── insert.py
│       ├── find.py
│       ├── update.py
│       ├── delete.py
│       ├── upsert.py
│       ├── aggregate.py
│       └── create_database.py
├── configuration.yaml       # MongoDB 连接与服务配置
├── requirements.txt         # Python 依赖
├── setup.py                 # pip 安装定义
├── install.sh               # 一键 systemd 安装脚本
```

---

## ⚙️ 配置文件 configuration.yaml 说明

```yaml
mongodb:
  uri: "mongodb://localhost:27017"

server:
  host: "0.0.0.0"
  port: 8080

logging:
  enabled: true
  file: "mongoapi.log"
```

- `mongodb.uri`: MongoDB 实例地址
- `server`: HTTP 服务监听地址与端口
- `logging`: 是否开启日志记录及输出文件位置

---

## 📝 查看日志方式

系统日志默认写入 `/var/log/mongoapi.log`，你可以使用如下命令查看：

```bash
tail -f /var/log/mongoapi.log
```

系统日志轮转通过 `/etc/logrotate.d/mongoapi` 实现，默认每周保留 4 份压缩日志。

---

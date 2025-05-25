# MongoDB HTTP API 服务文档（mongoapi CLI 版本）

## 📦 简介

本项目提供一个轻量级的 HTTP API 服务，封装了 MongoDB 的常见数据库操作，支持通过命令行工具 `mongoapi` 启动服务，便于集成到 n8n、前端系统、远程设备控制等场景。

---

## 📁 项目结构

```
mongoapi/
├── mongoapi/
│   ├── main.py              # 主服务入口
│   ├── config_loader.py     # 加载 configuration.yaml
│   └── handlers/            # 各类操作模块
├── configuration.yaml       # MongoDB 和服务配置
├── requirements.txt         # Python 依赖
├── setup.py                 # pip 安装定义
```

---

## ⚙️ 安装与使用

### 1. 解压安装

```bash
unzip mongoapi_status.zip
cd mongoapi_status
pip install .
```

### 2. 启动服务

```bash
mongoapi
```

默认监听地址：`http://0.0.0.0:8080`

---

## 📄 配置文件 `configuration.yaml`

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

## 🔌 API 接口文档

所有接口均使用 `application/json` 格式，请求方式为 `POST`（除 `/status`）。

---

### 1. 插入文档 `/insert`

```json
{
  "database": "test",
  "collection": "users",
  "document": { "name": "Alice", "age": 30 }
}
```

---

### 2. 查询文档 `/find`

```json
{
  "database": "test",
  "collection": "users",
  "query": { "age": { "$gte": 18 } },
  "projection": { "name": 1, "_id": 0 }
}
```
示例：字段的区间查询，你可以使用查询运算符如：

操作符	含义
$gt	大于
$gte	大于等于
$lt	小于
$lte	小于等于
---
✅ 示例：查询 age 在 18 到 30 之间的用户
{
  "database": "test",
  "collection": "users",
  "query": {
    "age": {
      "$gte": 18,
      "$lt": 60
    }
  }
}




### 3. 更新文档 `/update`

```json
{
  "database": "test",
  "collection": "users",
  "filter": { "name": "Alice" },
  "update": { "age": 31 }
}
```

---

### 4. 删除文档 `/delete`

```json
{
  "database": "test",
  "collection": "users",
  "filter": { "name": "Alice" }
}
```

---

### 5. Upsert（更新或插入） `/upsert`

```json
{
  "database": "test",
  "collection": "users",
  "filter": { "name": "Bob" },
  "update": { "age": 25 }
}
```

---

### 6. 聚合查询 `/aggregate`

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

### 7. 查询 API 状态 `/status` ✅

- 请求方式：`GET`
- 返回结构：

```json
{
  "connected": true,
  "uri": "mongodb://localhost:27017",
  "databases": {
    "test": ["users", "devices"],
    "admin": ["system.version"]
  }
}
```

---

## 🧾 所有接口统一返回结构

```json
{
  "result": { ...接口具体返回... },
  "status": {
    "connected": true,
    "uri": "mongodb://localhost:27017",
    "databases": {
      "test": ["users", "devices"]
    }
  }
}
```

---

## 📋 日志记录说明

- 控制开关位于 `configuration.yaml` 中：
```yaml
logging:
  enabled: true
  file: "mongoapi.log"
```

- 日志记录内容：
  - 启动时记录 MongoDB 连接与数据库列表
  - 插入后记录数据库状态
  - 所有操作记录执行标识和时间戳

---

## 🌐 在 n8n 中使用 mongoapi 接口

- 节点类型：HTTP Request
- Method：POST
- URL：如 `http://localhost:8080/upsert`
- Headers：Content-Type = application/json

### 示例 Upsert 请求体：

```json
{
  "database": "test",
  "collection": "devices",
  "filter": { "did": "{{ $json.did }}" },
  "update": {
    "name": "{{ $json.name }}",
    "status": "{{ $json.status }}",
    "timestamp": "{{ $json.timestamp }}"
  }
}
```

---

## 🛠️ 可拓展方向

- ✅ API Key 权限控制
- ✅ systemd 后台服务
- ✅ Docker 镜像打包
- ✅ 自动 Swagger 文档生成
- ✅ MongoDB 操作审计与告警

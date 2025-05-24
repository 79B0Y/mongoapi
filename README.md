# MongoDB HTTP API 服务文档（mongoapi CLI 版本）

## 📦 简介

本项目提供一个轻量级的 HTTP API 服务，封装了 MongoDB 的常见数据库操作，支持通过命令行工具 `mongoapi` 启动服务，便于集成到 n8n、前端系统、远程设备控制等场景。

---

## 📁 项目结构

```
mongoapi_cli/
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
unzip mongoapi_cli.zip
cd mongoapi_cli
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
```

---

## 🔌 API 接口文档

所有接口均使用 `application/json` 格式，请求方式为 `POST`。

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

---

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

## 🔐 安全建议

- ✅ 加入 API Key 或 Token 认证
- ✅ 限制允许访问的 database 和 collection
- ✅ 日志审计与速率限制（可拓展）

---

## 🛠️ 未来可拓展功能

- [ ] systemd 后台服务支持
- [ ] Docker 镜像
- [ ] 数据导出/导入接口
- [ ] WebSocket 实时推送
- [ ] 自动化注册 Swagger 文档

---

## 📞 支持

如需功能拓展或部署帮助，请联系作者或项目维护团队。

## 🌐 在 n8n 中使用 mongoapi 接口

你可以通过 n8n 的 `HTTP Request` 节点调用本服务实现 MongoDB 的远程操作。

---

### ✅ 通用设置（所有接口）

- **Method**: `POST`
- **URL**: `http://localhost:8080/<接口路径>`
- **Content-Type**: `application/json`
- **Response Format**: `JSON`

---

### 📥 示例：Upsert 操作

**接口路径**：`/upsert`  
**目标**：更新或插入设备信息

#### 📄 HTTP Request 节点配置：

| 项目           | 值                          |
|----------------|-----------------------------|
| HTTP Method    | `POST`                      |
| URL            | `http://localhost:8088/upsert` |
| Content-Type   | `application/json`          |
| Body Parameters（JSON） |                      |

```json
{
  "database": "test",
  "collection": "devices",
  "filter": {
    "did": "{{ $json.did }}"
  },
  "update": {
    "name": "{{ $json.name }}",
    "status": "{{ $json.status }}",
    "timestamp": "{{ $json.timestamp }}"
  }
}
```

---

### 📥 示例：Find 查询

**接口路径**：`/find`  
**目标**：查询指定条件下的用户信息

#### 📄 HTTP Request 配置：

```json
{
  "database": "test",
  "collection": "users",
  "query": {
    "status": "active"
  },
  "projection": {
    "_id": 0,
    "name": 1,
    "email": 1
  }
}
```

---

### 🧠 小技巧（动态字段）

你可以结合前置节点（如 Set、Function）设置动态 JSON，例如：

```js
{
  "did": "device-123",
  "name": "温湿度传感器",
  "status": "online",
  "timestamp": {{ new Date().getTime() }}
}
```

---

### 🛡️ 安全建议

- 建议添加 API Key Header（可拓展）
- 可将服务部署于内网 + VPN，防止公网滥用

---

如需我生成可导入的 n8n 流程 `.json` 文件，也可以继续告诉我。

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

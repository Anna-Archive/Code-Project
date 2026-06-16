# 🚀 Low-Code Data Dashboard Backend (低代码数据大屏后端系统)

本项目是一套高性能、规范化的后端 RESTful API 系统，专为数据大屏及低代码看板提供数据支撑。

## 🛠️ 技术栈
* **核心框架**：Spring Boot / FastAPI
* **数据库**：MySQL 8.0
* **缓存/限流**：Redis
* **安全鉴权**：JWT (JSON Web Token)
* **文档工具**：Swagger UI / OpenAPI 3.0

## 🏗️ 系统架构图
![系统架构图](./images/architecture.png)

## ✨ 核心亮点
1. **高性能缓存**：针对大屏高频请求指标，采用 Redis 作为旁路缓存，极大减轻 MySQL 压力，QPS 提升明显。
2. **安全防护**：基于 JWT 实现无状态用户鉴权，并在网关/中间件层集成基于 Redis 计数器的 IP 限流机制（429 Too Many Requests）。
3. **工程规范**：严格遵循 RESTful API 设计规范，集成 Swagger 自动生成交互式 API 文档。

## 🏁 快速启动
1. 克隆项目：`git clone ...`
2. 配置 `application.yml` / `.env` 中的 MySQL 和 Redis 连接。
3. 运行主程序，访问 `/docs` 或 `/swagger-ui/index.html` 查看接口并测试。

# 引入新版官方推荐的异步 Redis 客户端
import redis.asyncio as aioredis

# 异步 Redis 客户端连接配置
REDIS_URL = "redis://localhost:6379"

redis_client = aioredis.from_url(REDIS_URL, decode_responses=True)
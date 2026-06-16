from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import auth, screen
from app.core.redis_config import redis_client
import time

app = FastAPI(
    title="Low-Code Data Dashboard API",
    description="这是一个专为数据大屏和低代码看板设计的高性能后端 RESTful API 系统。",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 配置 CORS 跨域（方便前端大屏调用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 全局高并发限流中间件（基于 Redis 计数器）
@app.middleware("http")
async def rate_limiter_middleware(request: Request, call_next):
    client_ip = request.client.host
    redis_key = f"rate_limit:{client_ip}"

    try:
        # 单个IP一分钟请求超过60次，触发429拦截
        current_requests = await redis_client.incr(redis_key)
        if current_requests == 1:
            await redis_client.expire(redis_key, 60)

        if current_requests > 60:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="请求过于频繁，请稍后再试（限流防护：60次/分钟）"
            )
    except Exception:
        # 如果底层 Redis 挂了，降级处理直接放行，确保不影响核心业务运行
        pass

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# 路由分发挂载
app.include_router(auth.router, prefix="/api/v1/auth", tags=["用户认证与鉴权"])
app.include_router(screen.router, prefix="/api/v1/screen", tags=["大屏可视化数据"])
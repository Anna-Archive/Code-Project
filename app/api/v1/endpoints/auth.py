from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.core.security import create_access_token

router = APIRouter()


# 定义前端传过来的 JSON 数据格式（Pydantic 模型，自带参数校验）
class LoginSchema(BaseModel):
    username: str
    password: str


@router.post("/login", summary="用户登录获取JWT Token")
async def login(data: LoginSchema):
    # 模拟数据库用户校验
    # 实际开发中会查 MySQL，这里为了快速落地，我们固定一个初始账号密码
    if data.username == "admin" and data.password == "123456":
        # 校验通过，生成 JWT 令牌
        token = create_access_token(data={"sub": data.username})
        return {
            "access_token": token,
            "token_type": "bearer",
            "message": "登录成功"
        }

    # 校验失败，抛出 401 认证错误
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="用户名或密码错误"
    )
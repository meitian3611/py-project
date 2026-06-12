from fastapi import FastAPI

"""
FastAPI 是一个用于构建 Web 应用的 Python 框架。
"""
# 创建 FastAPI 应用
app = FastAPI()


# 定义一个 GET 请求的接口的路由
@app.get("/")
async def root():
    return {"message": "Hello World"}


# 创建一个接口，返回用户列表
@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]


"""
    运行项目
    uvicorn: python中的轻量级web服务器
"""
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3333)

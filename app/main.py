from fastapi import FastAPI
from router.auth.login import router as login_router

app = FastAPI()

@app.get("/")
async def root():
    return {"hello": "world"}


app.include_router(login_router)
from fastapi import FastAPI, HTTPException, Depends, status
from router.auth.login import router as login_router
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

@app.get("/")
async def root():
    return {"hello": "world"}


app.include_router(login_router)
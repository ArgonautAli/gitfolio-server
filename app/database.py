from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends
import os

load_dotenv()

DB_URL = os.getenv("URL_DATABASE")


URL_DATABASE = DB_URL


engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

db = SessionLocal()

def get_db():
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
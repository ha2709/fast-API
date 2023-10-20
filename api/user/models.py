from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# DATABASE_URL = "sqlite:///./test.db"  # Use your database URL here
# DATABASE_URL = "mysql+mysqlconnector://username:password@host/dbname"

HOST=os.getenv("DATABASE_HOST")
PORT=3306,
USER_NAME=os.environ.get("DATABASE_USERNAME")
PASSWORD=os.environ.get("DATABASE_PASSWORD")
DATABASE=os.environ.get("DATABASE")
DATABASE_URL = "mysql+mysqlconnector://"+USER_NAME+":"+PASSWORD+"@"+HOST+"/"+DATABASE
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class User(BaseModel):
    __tablename__ = "users"
    id: int
    username: str
    email: str

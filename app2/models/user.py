from app2.backend.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app2.backend.db_depends import get_db
from typing import Annotated
from app2.models import *
from app2.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates='user')


from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))

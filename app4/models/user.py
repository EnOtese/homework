from app4.backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app4.models.task import Task


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

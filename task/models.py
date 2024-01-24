from sqlalchemy import  Column, Date, Integer, String, Enum
from enum import Enum as PyEnum
from .database import Base

class TaskStatus(str, PyEnum):
    PENDING = 'pending'
    IN_PROGRESS = 'in progress'
    COMPLETED = 'completed'

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    status = Column(Enum(TaskStatus), nullable=False)
    due_date = Column(Date, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
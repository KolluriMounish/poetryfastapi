from pydantic import BaseModel
from datetime import date
from .models import TaskStatus
from typing import List
# from enum import Enum

# class TaskStatus(str, Enum):
#     PENDING = 'pending'
#     IN_PROGRESS = 'in progress'
#     COMPLETED = 'completed'


class TaskBase(BaseModel):
    title: str
    description: str
    status: TaskStatus
    due_date: date
    # user_id: int

class Task(TaskBase):
    # title: str
    # description: str
    # status: TaskStatus
    # due_date: date
    user_id: int
    # class Config():
    #     from_attributes = True

class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel):
    name : str
    email : str
    tasks : List[TaskBase]

    class Config():
        from_attributes = True


class ShowTask(BaseModel):
    title: str
    description: str
    status: TaskStatus
    due_date: date
    creater: ShowUser
    class Config():
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
# class ShowTask(Task):
#     class Config():
#         orm_model = True

# class ShowTask(BaseModel):
#     title: str
#     description: str
#     status: TaskStatus
#     due_date: date
#     class Config():
#         orm_model = True

# class UpdateTask(BaseModel):
#     id: int
#     title: str
#     description: str
#     status: TaskStatus
#     due_date: date

# class CreateTask(BaseModel):
#     # id: int
#     title: str
#     description: str
#     status: TaskStatus
#     due_date: date
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "id": 1,
    #             "title": "My Task",
    #             "description": "This is my task",
    #             "status": "not_started",
    #             "due_date": "2022-01-01",
    #         }
    #     }
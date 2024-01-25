from typing import List
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def all(db: Session):
    tasks = db.query(models.Task).all()
    return tasks

def get_Task(task_id:int,  db: Session):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"task with id {task_id} is not found")
    return task

def create(request: schemas.Task, db:Session ):
    new_task = models.Task(title=request.title, description=request.description, status=request.status, due_date=request.due_date, user_id=request.user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def destroy(task_id:int,db:Session) :
    task = db.query(models.Task).filter(models.Task.id == task_id)

    if not task.first() :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {task_id} not found")
    task.delete(synchronize_session=False)
    db.commit()
    return "deleted task"

def update(task_id:int, request: schemas.Task, db:Session):
    # task=db.query(models.Task).filter(models.Task.id == task_id).update(request.dict())
    task=db.query(models.Task).filter(models.Task.id == task_id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {task_id} not found")
    task.update({'id':task_id,'title':request.title, 'description':request.description, 'status':request.status, 'due_date':request.due_date})
    db.commit()
    return "updated"
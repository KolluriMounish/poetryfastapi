from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas,models,database, oauth2
from sqlalchemy.orm import Session
from ..repository import task


router = APIRouter(
    prefix="/task",
    tags=['Task']
)
get_db = database.get_db

@router.get('/', response_model=List[schemas.Task])
async def get_all_tasks(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return task.all(db)

@router.get('/{task_id}', status_code=200, response_model=schemas.ShowTask)
async def get_Task(task_id:int,  db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return task.get_Task(task_id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Task, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return task.create(request, db)


@router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_task(task_id:int,db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)) :
    return task.destroy(task_id,db)


@router.put('/{task_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_task(task_id:int, request: schemas.Task, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return task.update(task_id, request, db)
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import models, schemas
from .database import engine, SessionLocal
# from database import engine, SessionLocal
from sqlalchemy.orm import Session
# from passlib.context import CryptContext
# from pydantic import BaseModel
from typing import List, Annotated
from .hashing import Hash

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/')
def index():
    return {"Hello": "Welcome to poetry based fastapi"}

@app.post('/task', status_code=status.HTTP_201_CREATED, tags=['Task'])
def create(request: schemas.Task, db:Session = Depends(get_db)):
    new_task = models.Task(title=request.title, description=request.description, status=request.status, due_date=request.due_date, user_id=request.user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# response_model=List[schemas.ShowTask]
@app.get('/task', response_model=List[schemas.ShowTask], tags=['Task'])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks

# response_model=schemas.ShowTask
@app.get('/task/{task_id}', status_code=200, response_model=schemas.ShowTask, tags=['Task'])
def get_Task(task_id:int,  db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"task with id {task_id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"task with id {task_id} not found"}
    return task


@app.delete('/task/{task_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Task'])
def destroy_task(task_id:int,db:Session = Depends(get_db)) :
    task = db.query(models.Task).filter(models.Task.id == task_id)

    if not task.first() :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {task_id} not found")
    task.delete(synchronize_session=False)
    db.commit()
    return {f"task with id {task_id} is deleted"}


@app.put('/task/{task_id}', status_code=status.HTTP_202_ACCEPTED, tags=['Task'])
def update_task(task_id:int, request: schemas.Task, db:Session = Depends(get_db)):
    # task=db.query(models.Task).filter(models.Task.id == task_id).update(request.dict())
    task=db.query(models.Task).filter(models.Task.id == task_id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {task_id} not found")
    task.update({'id':task_id,'title':request.title, 'description':request.description, 'status':request.status, 'due_date':request.due_date})
    db.commit()
    return "updated"

# @app.post("/task/taskwithbodyperameter")
# def post_data(task:schemas.Task):
#     print(task)
#     return {
#         'title':task.title,
#         'description':task.description, 
#         'status':task.status, 
#         'due_date':task.due_date
#     }

# pwd_cxt =CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post('/user', response_model=schemas.ShowUser, tags=['User'])
def create_user(request: schemas.User, db:Session = Depends(get_db)):
    # hashedPassword = pwd_cxt.hash(request.password)
    new_user =models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['User'])
def get_user(id: int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} is not found")

    return user
# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port="9000")
                

from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas,models,database
from ..hashing import Hash
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['User']
)
get_db = database.get_db

pwd_cxt =CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db:Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db:Session = Depends(get_db)):
    return user.get(id,db)
from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database, users

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)) -> Union[schemas.UserResponse, HTTPException]:
    return users.create_user(db, user)


@router.get("/", response_model=List[schemas.UserResponse])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)) -> Union[List[schemas.UserResponse], HTTPException]:
    return users.list_users(db, skip, limit)


@router.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(database.get_db)) -> Union[schemas.UserResponse, HTTPException]:
    return users.get_user(db, user_id)


@router.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, name: str, email: str, password: str, db: Session = Depends(database.get_db)) -> Union[schemas.UserResponse, HTTPException]:
    return users.update_user(db, user_id, name, email, password)


@router.delete("/users/{user_id}", response_model=schemas.MessageResponse)
def delete_user(user_id: int, db: Session = Depends(database.get_db)) -> Union[schemas.MessageResponse, HTTPException]:
    return users.delete_user(db, user_id)

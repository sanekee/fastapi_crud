from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext
from .utils import get_password_hash


def create_user(db: Session, user: schemas.UserCreate) -> schemas.UserResponse:
    hashed_password = get_password_hash(user.password)
    db_user = models.User(name=user.name, email=user.email,
                          hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def list_users(db: Session, skip: int = 0, limit: int = 10) -> List[schemas.UserResponse]:
    users = db.query(models.User).offset(skip).limit(limit).all()
    return [{"id": u.id, "name": u.name, "email": u.email} for u in users]


def get_user(db: Session, user_id: int) -> schemas.UserResponse:
    user = db.query(models.User).get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")

    return {"id": user.id, "name": user.name, "email": user.email}


def update_user(db: Session, user_id: int, name: str, email: str, password: str) -> schemas.UserResponse:
    user = db.query(models.User).get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")

    user.name = name
    user.email = email
    user.hashed_password = get_password_hash(password)
    db.commit()
    return {"id": user.id, "name": user.name, "email": user.email}


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

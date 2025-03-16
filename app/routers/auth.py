
from typing import Union
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import auth, database, schemas


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/token", response_model=schemas.AuthResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)) -> Union[schemas.AuthResponse, HTTPException]:
    return auth.login(db, form_data)

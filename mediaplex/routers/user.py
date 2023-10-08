from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from mediaplex.database import get_db
from mediaplex.repository import user
from mediaplex.schemas import user_schema
from mediaplex.config.oauth2 import get_current_user

router = APIRouter(tags=['user'])

@router.get('/profile', response_model=user_schema.User)
def get_profile(current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return user.get_profile(current_user, db)

@router.patch('/profile', response_model=user_schema.User)
def update_profile(request: user_schema.UserUpdate, current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return user.update_profile(request, current_user, db)

router.prefix = '/user'

@router.get('', response_model=List[user_schema.User])
def get_all(current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return user.get_all(current_user, db)

@router.get('/{id}', response_model=user_schema.User)
def get(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)

@router.post('')
def register(request: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user.register(request, db)
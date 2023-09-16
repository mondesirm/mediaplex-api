from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from mediaplex.database import get_db
from mediaplex.repository import user
from mediaplex.schemas import user_schema
from mediaplex.config.oauth2 import get_current_user

router = APIRouter(tags=['user'], prefix='/user')

@router.get('/', response_model=user_schema.UserView)
def get_profile(current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return user.get_profile(current_user, db)

@router.get('/{id}', response_model=user_schema.UserView)
def get(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)

@router.post('/')
def create(request: user_schema.User, db: Session = Depends(get_db)):
    return user.create(request, db)
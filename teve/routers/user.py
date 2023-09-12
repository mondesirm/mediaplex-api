from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from teve.database import get_db
from teve.repository import user
from teve.schemas import user_schema
from teve.config.oauth2 import get_current_user

router = APIRouter(tags=['user'], prefix='/user')

@router.post('/')
def create(request: user_schema.User, db: Session = Depends(get_db)):
    return user.create(db, request)

@router.get('/{id}', response_model=user_schema.UserView)
def get(id: int, db: Session = Depends(get_db), current_user: user_schema.User = Depends(get_current_user)):
    return user.get(db, id)
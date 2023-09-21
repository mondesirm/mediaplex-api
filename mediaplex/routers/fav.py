from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from mediaplex.repository import fav
from mediaplex.database import get_db
from mediaplex.config.oauth2 import get_current_user
from mediaplex.schemas import fav_schema, user_schema

router = APIRouter(tags=['favs'], prefix='/fav')

@router.get('', response_model=List[fav_schema.Fav])
def get_all_for(current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return fav.get_all(current_user, db)

@router.post('')
def add_to(request: fav_schema.FavCreate, current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return fav.add_to(current_user, request, db)

@router.delete('/{id}', response_model=fav_schema.Fav)
def delete(id: int, current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return fav.delete(id, current_user, db)
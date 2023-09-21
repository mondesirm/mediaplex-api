from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from mediaplex.database import get_db
from mediaplex.schemas.login_schema import Login
from mediaplex.repository.login import login, token

router = APIRouter(tags=['login'], prefix='/login')

@router.post('')
def login(request: Login, db: Session = Depends(get_db)):
    return login(request, db)

@router.post('/auth')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return token(request, db)
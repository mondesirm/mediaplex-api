from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from teve.database import get_db
from teve.schemas.login_schema import Login
from teve.repository.login import login_user, get_token

router = APIRouter(tags=['login'], prefix='/login')

@router.post('/')
def login(request: Login, db: Session = Depends(get_db)):
    return login_user(db, request)

@router.post('/auth')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return get_token(db, request)
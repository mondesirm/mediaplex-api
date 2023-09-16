from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from mediaplex.models import User
from mediaplex.config.hashing import Hash
from mediaplex.schemas.login_schema import Login
from mediaplex.config.authtoken import create_access_token

def login_user(db: Session, request: Login):
    user = db.query(User).filter(User.email == request.username).first()
    if not user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User doesn\'t exist')
    if not Hash.verify(user.password, request.password): raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect Password')
    access_token = create_access_token(data={'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}

def get_token(db: Session, request):
    user = db.query(User).filter(User.email == request.username).first()
    if not user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User doesn\'t exist')
    if not Hash.verify(user.password, request.password): raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect Password')
    access_token = create_access_token(data={'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}
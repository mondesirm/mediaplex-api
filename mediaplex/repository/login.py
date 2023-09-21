from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from mediaplex.models import User
from mediaplex.config.hashing import Hash
from mediaplex.schemas.login_schema import Login
from mediaplex.config.authtoken import create_access_token

def login(request: Login, db: Session):
    # Check if user exists and password is correct
    user: User = db.query(User).filter(User.email == request.email).first()
    if not user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    if not Hash.verify(user.password, request.password): raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect Password')
    # Return access token
    access_token = create_access_token(data={'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}

def token(request: Login, db: Session):
    # Check if user exists and password is correct
    user: User = db.query(User).filter(User.email == request.email).first()
    if not user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    if not Hash.verify(user.password, request.password): raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect Password')
    # Return access token
    access_token = create_access_token(data={'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}
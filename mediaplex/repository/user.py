from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends

from mediaplex.models import User
from mediaplex.database import get_db
from mediaplex.config.hashing import Hash
from mediaplex.config.authtoken import create_access_token

def get_profile(current_user: str, db: Session):
    if not current_user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User doesn\'t exist')
    user = db.query(User).filter(User.email == current_user).first()
    if not user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {current_user} not found')
    return user

def get(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user: raise HTTPException(status.HTTP_404_NOT_FOUND, f'User {id} not found')
    return user

def create(request: User, db: Session):
    user = User(email=request.email, password=Hash.bcrypt(request.password), username=request.username)
    db.add(user); db.commit(); db.refresh(user)
    access_token = create_access_token({'sub': user.email})
    return { 'access_token': access_token, 'token_type': 'bearer' }
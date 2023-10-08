from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from mediaplex.models import User, Fav
from mediaplex.config.hashing import Hash
from mediaplex.schemas.user_schema import UserUpdate
from mediaplex.config.authtoken import create_access_token

def get_profile(current_user: str, db: Session):
    # Check if current user exists and is authenticated
    if not current_user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Current user not found')
    user: User = db.query(User).filter(User.email == current_user).first()
    if not user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {current_user} not found')
    # Return current user's data
    return user

def update_profile(request: UserUpdate, current_user: str, db: Session):
    # Check if current user exists and is authenticated
    if not current_user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Current user not found')
    user: User = db.query(User).filter(User.email == current_user).first()
    if not user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {current_user} not found')
    # Check if old password is provided and is correct
    if not request.old_password: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Old password not provided')
    if not Hash.verify(user.password, request.old_password): raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Old password is incorrect')
    # Update user_id in favs by new email
    db.query(Fav).filter(Fav.user_id == user.id).update({Fav.user_id: user.id})
    # Update user's data and return it
    user.email = request.email; user.username = request.username
    if request.new_password: user.password = Hash.bcrypt(request.new_password)
    db.commit(); db.refresh(user)
    return user

def get_all(current_user: str, db: Session):
    # Check if current user exists and is authenticated
    if not current_user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Current user not found')
    user: User = db.query(User).filter(User.email == current_user).first()
    if not user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {current_user} not found')
    # Return all users except current user
    users: List[User] = db.query(User).filter(User.email != user.email).all()
    #? if not users: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No users found')
    return users

def get(id: int, db: Session):
    user: User = db.query(User).filter(User.id == id).first()
    if not user: raise HTTPException(status.HTTP_404_NOT_FOUND, f'User {id} not found')
    return user

def register(request: User, db: Session):
    # Check if user already exists
    user = db.query(User).filter(User.email == request.email).first()
    if user: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already taken')
    # Create user otherwise
    user: User = User(email=request.email, password=Hash.bcrypt(request.password), username=request.username)
    db.add(user); db.commit(); db.refresh(user)
    # Return access token
    access_token = create_access_token({'sub': user.email})
    return { 'access_token': access_token, 'token_type': 'bearer' }
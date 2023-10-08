from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from mediaplex.models import User, Fav

def get_all(current_user: str, db: Session):
    # Check if current user exists and is authenticated
    if not current_user: raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Current user not found')
    user: User = db.query(User).filter(User.email == current_user).first()
    if not user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {current_user} not found')
    # Return all associated data for the current user
    favs: List[Fav] = db.query(Fav).filter(Fav.user_id == user.id).all()
    #? if not favs: raise HTTPException(status.HTTP_404_NOT_FOUND, 'No favorites found')
    return favs

def add_to(current_user: str, request: Fav, db: Session):
    # Check if current user exists and is authenticated
    if not current_user: raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Current user not found')
    user: User = db.query(User).filter(User.email == current_user).first()
    if not user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {current_user} not found')
    # Check if data is already in the database
    fav: Fav = db.query(Fav).filter(Fav.user_id == user.id, Fav.url == request.url).first()
    if fav: raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, 'Already in favorites')
    # Add it otherwise and return it
    fav: Fav = Fav(url=request.url, name=request.name, category=request.category, user_id=user.id)
    db.add(fav); db.commit(); db.refresh(fav)
    return fav

def delete(id: int, current_user: str, db: Session):
    # Check if current user exists and is authenticated
    if not current_user: raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Current user not found')
    user: User = db.query(User).filter(User.email == current_user).first()
    if not user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {current_user} not found')
    # Check if data is already in the database
    fav: Fav = db.query(Fav).filter(Fav.user_id == user.id, Fav.id == id).first()
    if not fav: raise HTTPException(status.HTTP_404_NOT_FOUND, 'Favorite not found')
    # Delete it otherwise
    db.delete(fav); db.commit()
    return fav
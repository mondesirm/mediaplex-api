from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends

from mediaplex.database import get_db
from mediaplex.models import User, Fav
from mediaplex.schemas import fav_schema

def get_for(current_user: str, db: Session):
    if not current_user: raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'User doesn\'t exist')
    favs = db.query(Fav).filter(Fav.user_id == current_user).all()
    return favs

def add_to(current_user: str, request: fav_schema.Fav, db: Session):
    if not current_user: raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'User doesn\'t exist')

    try:
        user = db.query(User).filter(User.email == current_user).first()
        user_fav = Fav(stream_link=request.stream_link, category=request.category, channel_name=request.channel_name, user_id=user.email)
        db.add(user_fav); db.commit(); db.refresh(user_fav)
        return user_fav
    except Exception: raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, 'Already in favorites')

def remove_from(current_user: str, request: fav_schema.Fav, db: Session = Depends(get_db)):
    if not current_user: raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'User doesn\'t exist')
    try:
        db.query(Fav).filter(Fav.user_id == current_user, Fav.stream_link == request.stream_link, Fav.category == request.category).delete(synchronize_session=False)
        db.commit()
    except Exception: raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, "Nothing to delete")
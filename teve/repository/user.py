from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from teve.models import User
from teve.config.hashing import Hash
from teve.config.authtoken import create_access_token

def create(db: Session, request: User):
    user = User(email=request.email, password=Hash.bcrypt(request.password), username=request.username)
    db.add(user)
    db.commit()
    db.refresh(user)
    access_token = create_access_token({'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}

def get(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    if not user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {id} not found')
    return user
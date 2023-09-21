from typing import List
from pydantic import BaseModel
from mediaplex.schemas.fav_schema import Fav

class UserBase(BaseModel):
    email: str
    username:  str
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    old_password: str = None
    new_password: str = None

class User(UserBase):
    id: int
    favs: List[Fav]
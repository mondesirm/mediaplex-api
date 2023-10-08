from mediaplex.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    favs = relationship('Fav', back_populates='user')

class Fav(Base):
    __tablename__ = 'fav'
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    name = Column(String)
    category = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='favs')
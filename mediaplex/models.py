from mediaplex.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    favs = relationship('Fav', back_populates='owner')

class Fav(Base):
    __tablename__ = 'fav'
    stream_link = Column(String, primary_key=True)
    category = Column(String)
    channel_name = Column(String)
    user_id = Column(String, ForeignKey('user.email'))
    owner = relationship('User', back_populates='favs')
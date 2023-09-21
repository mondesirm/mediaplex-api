from pydantic import BaseModel

class FavBase(BaseModel):
    url : str
    name: str
    category: str
    class Config:
        orm_mode = True

class FavCreate(FavBase):
    pass

class Fav(FavBase):
    id: int
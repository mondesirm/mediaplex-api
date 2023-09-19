from pydantic import BaseModel


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Fav(OurBaseModel):
    url : str
    name: str
    category: str
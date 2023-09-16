from pydantic import BaseModel

class MyBaseModel(BaseModel):
    class Config:
        orm_mode = True

class User(MyBaseModel):
    email: str
    password: str
    username:  str

class UserView(MyBaseModel):
    email: str
    username:str
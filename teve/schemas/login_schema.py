from pydantic import BaseModel

class MyBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Login(MyBaseModel):
    password: str
    username: str
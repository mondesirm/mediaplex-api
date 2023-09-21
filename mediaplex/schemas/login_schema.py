from pydantic import BaseModel

class MyBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Login(MyBaseModel):
    email: str
    password: str
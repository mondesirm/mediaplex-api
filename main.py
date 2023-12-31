import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from mediaplex import models
from mediaplex.database import engine
from mediaplex.routers import user, login, fav

app = FastAPI()
app.mount('/assets', StaticFiles(directory='assets'), name='assets')

models.Base.metadata.create_all(bind=engine)

origins = ['*']
# origins = [
#     'http://localhost.tiangolo.com',
#     'https://localhost.tiangolo.com',
#     'http://localhost',
#     'http://localhost:8080',
# ]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

# @app.get('/')
# async def main():
#     return {'message': 'Hello World'}

app.include_router(login.router)
app.include_router(user.router)
app.include_router(fav.router)

if __name__ == '__main__': uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
import datetime

from fastapi import FastAPI

from ttdiagnosis.models.user import User
from ttdiagnosis.repositories.user_repository import UserRepository

user_repository = UserRepository()

app = FastAPI()


@app.get('/')
async def dashboard():
    return {'status': 'ok'}


@app.post('/sessions')
async def sessions():
    user = User(name='joao', session_date=datetime.datetime.now())
    user_repository.add(user)

    return {'message': 'registered user session'}


@app.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
    user = user_repository.get_by_id(user_id)

    return user


@app.get('/users')
async def get_all_users():
    users = user_repository.list()

    return users

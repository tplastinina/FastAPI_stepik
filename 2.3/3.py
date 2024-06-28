
from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    username: str
    user_info: str


app = FastAPI()

fake_db = [{"username": "Vasya", "user_info": "gut schlafen"},
           {"username": "Katia", "user_info": "gehen spazieren"}]


@app.get('/users')
async def get_all_users():
    return fake_db


@app.post('/add_user')
async def add_user(user: User):
    fake_db.append({"username": user.username, "user_info": user.user_info})
    return user

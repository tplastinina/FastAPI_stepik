
import random
from typing import Annotated, List
from urllib import response
from fastapi import Cookie, FastAPI, Form, Request, Response

from models import Users


app = FastAPI()

sample_user: dict = {"username": "user123", "password": "password123"}
users: list[Users] = [Users(**sample_user)]

sessions: dict = {}


@app.post("/login")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
async def login(user: Users, response: Response):
    token = str(random.randint(100, 999))
    for u in users:
        if u.username == user.username and (u.password == user.password):
            response.set_cookie(key="session_token",
                                value=token, httponly=True)  # тут установили куки с защищенным флагом httponly - недоступны для вредоносного JS; флаг secure означает, что куки идут только по HTTPS
            return {"message": "Login successful"}
    return {"message": "Invalid login or password"}


@app.get("/user")
async def user(session_token=Cookie()):
    user = sessions.get(session_token)
    if user:
        return user.dict()
    return {"message": "Unauthorized"}

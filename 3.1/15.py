from fastapi import FastAPI
from models import UserCreate


app = FastAPI()
users: list[UserCreate] = []


@app.post("/create_user")
async def create_user(user: UserCreate):
    users.append(user)
    return user


@app.get("/all_users")
async def all_users():
    return {"users": users}

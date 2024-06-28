#  настоятельно рекомендуем вам не ограничиваться полученной в данном курсе информацией, а детально изучить технологии OAuth2 и JWT и
# прочее в разделах "Безопасность" обычного и продвинутого руководства пользователя FastAPI по адресам: https://fastapi.tiangolo.com/tutorial/security/
#  и https://fastapi.tiangolo.com/advanced/security/
# https://fastapi.tiangolo.com/ru/tutorial/


from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from pydantic import BaseModel


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

USER_DATA = [{"username": "admin", "password": "adminpass"}]


class User(BaseModel):
    username: str
    password: str


def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_user_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM
                                                            ])

        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        pass
    except jwt.InvalidTokenError:
        pass


def get_user(username: str):
    for user in USER_DATA:
        if user.get("username") == username:
            return user
    return None


@app.post("/login")
async def login(user_in: User):
    for user in USER_DATA:
        if user.get("username") == user_in.username and user.get("password") == user_in.password:
            return {"access_token": create_jwt_token({"sub": user_in.username}), "token_type": "bearer"}
        return {"error": "Invalid credentials"}


@app.get("/abot_me")
async def about_me(current_user: str = Depends(get_user_from_token)):
    user = get_user(current_user)
    if user:
        return user
    return {"error": "User not found"}

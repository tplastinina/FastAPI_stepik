from typing import Annotated, Optional
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from pydantic import BaseModel

from security import create_jwt_token, get_user, get_user_token


app = FastAPI()


@app.post("/token/")
def login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_data_from_db = get_user(user_data.username)
    if user_data_from_db is None or user_data.password != user_data_from_db.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},)
    # тут мы добавляем полезную нагрузку в токен, и говорим,
    return {"access_token": create_jwt_token({"sub": user_data.username}), "token_type": "bearer"}
# что "sub" содержит значение username


@app.get("/admin/")
def get_admin_info(current_user: str = Depends(get_user_token)):
    user_data = get_user(current_user)
    if user_data.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return {"message": "Welcom Admin"}


@app.get("/user/")
def get_user_info(current_user: str = Depends(get_user_token)):
    user_data = get_user(current_user)
    if user_data.role != "user":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return {"message": "Hello User!"}

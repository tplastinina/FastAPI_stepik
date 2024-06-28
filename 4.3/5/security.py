from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt

from config import ALGORITHM, SECRET_KEY, USER_DATA
from models import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# jwt token


def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

# token -> user


def get_user_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # тут мы идем в полезную нагрузку JWT-токена и возвращаем утверждение о юзере (subject); обычно там еще можно взять "iss" - issuer/эмитент, или "exp" -
        return payload.get("sub")
        # expiration time - время 'сгорания' и другое, что мы сами туда кладем
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# получение пользовательских данных на основе имени пользователя


def get_user(username: str):
    if username in USER_DATA:
        user_data = USER_DATA[username]
        return User(**user_data)
    return None

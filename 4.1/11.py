

import secrets
from typing import Annotated
from wsgiref import headers
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from models import User


app = FastAPI()
security = HTTPBasic()


USER_DATA = [User(**{"username": "user1", "password": "pass1"}),
             User(**{"username": "user2", "password": "pass2"})]


def authentificate_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    # current_username_bytes = credentials.username.encode("utf8")
    # correct_username_bytes = b"stanleyjobson"
    # is_correct_username = secrets.compare_digest(
    #     current_username_bytes, correct_username_bytes)
    # current_password_bytes = credentials.password.encode("utf8")
    # correct_password_bytes = b"swordfish"
    # is_correct_password = secrets.compare_digest(
    #     current_password_bytes, correct_password_bytes)

    for user in USER_DATA:
        is_correct_username = secrets.compare_digest(
            credentials.username, user.username)
        is_correct_password = secrets.compare_digest(
            credentials.password, user.password)
        if is_correct_username and is_correct_password:
            return user

    if not (is_correct_password and is_correct_username):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Basic"},)

    return {"message": "You got my secret, welcome"}


@app.get("/login/")
async def log(username: Annotated[User, Depends(authentificate_user)]):
    return {"username": username}

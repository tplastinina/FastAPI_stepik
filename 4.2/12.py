

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
import jwt
from pydantic import BaseModel


class Users(BaseModel):
    user_name: str
    password: str


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "mykey22"
ALGORITHM = "HS256"

USER_DATA = [{"username": "admin", "password": "adminpass"}]


def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.post("/login")
async def login(user_in: Users):
    for user in USER_DATA:
        if user['username'] == user_in.user_name and user['password'] == user_in.password:
            return {"access_token": create_jwt_token({"sub": user_in.user_name}), "token_type": "bearer"}
        return {"detail": "Invalid credentials"}


@app.get("/protected_resource")
async def auth(payload: dict = Depends(verify_token)):
    return {"message": "This is a protected resource", "user": payload}

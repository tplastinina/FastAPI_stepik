from fastapi import FastAPI

app = FastAPI()

fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}


@app.get('/users/')
async def read_user(limit: int = 10):
    return dict(list(fake_users.items())[:limit])

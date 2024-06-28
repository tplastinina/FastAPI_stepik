# как оно раюотает?

from fastapi import FastAPI, Header


app = FastAPI()


@app.get("/")
def root(user_agent: str = Header()):
    return {"User-agent:": user_agent}

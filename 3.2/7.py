

import datetime
from fastapi import FastAPI, Response


app = FastAPI()


@app.get("/")
def root(response: Response):
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    # метод помогает определить имя файла, значение и доп параметры (домен, путь, срок действия и параметры безопасности)
    response.set_cookie(key="las_visit", value=now)
    return {"message": "куки установлены"}

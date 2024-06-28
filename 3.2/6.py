
from fastapi import Cookie, FastAPI


app = FastAPI()

# last visit- название переменной в обработчике маршрута соответсвует ключу куков!!!


@app.get("/")
def root(last_visit=Cookie()):
    return {"last visit": last_visit}

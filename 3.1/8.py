from typing import Annotated


@app.get("/users/{user_id}")
def read_user(user_id: int, is_admin: bool = False):
    return {"user_id": user_id, "is_admin": is_admin}

# В этом примере маршрут `/users/{user_id}` принимает параметр пути `user_id` и необязательный параметр запроса `is_admin`. Параметр `is_admin` по умолчанию имеет значение `False`, если он не указан в запросе.


# 1. Path
@app.get("/{some_param}")
async
 def func_with_path_param(some_param: <type>):


# oder
@app.get("/{some_param}")
async def func_with_path_param(some_param: Annotated[<type>, Path()]):
   

# Body

@app.post("/")
async def func_with_body_param(user: User):
   
@app.post("/")
async def func_with_body_param(user: Annotated[User, Body()]):
   
# Query

@app.get("/")
async def func_with_query_param(query_param: <type>):

@app.get("/")
async def func_with_query_param(query_param: Annotated[<type>, Query()]):
   


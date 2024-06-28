# это нужно проверить

import re
from typing import Annotated, List, Union
from fastapi import FastAPI, Header, Response


app = FastAPI()


@app.get("/headers")
async def head(user_agent: Annotated[Union[List[str], None], Header(convert_underscores=False)] = None, accept_language: Annotated[Union[str, None], Header(convert_underscores=False)] = None):
    if (user_agent == None and accept_language == None) or (accept_language != re.search(r'\D{2}-\D{2},\D{2};q=\d+\.\d+')):
        return {"Error": "400"}
    else:
        return {"User-Agent": user_agent, "Accept-Language": accept_language}

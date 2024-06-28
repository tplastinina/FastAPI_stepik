from pydantic import BaseModel


class Feedback(BaseModel):
    id: int
    name: str
    message: str

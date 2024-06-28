
from typing import Union
from pydantic import BaseModel, EmailStr, Field, PositiveInt


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt | None = Field(default=None, lt=130)
    is_subscribed: Union[bool, None] = None


class Product(BaseModel):
    product_id: PositiveInt
    name: str
    category: str
    price: float

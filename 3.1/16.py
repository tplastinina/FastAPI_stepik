

from typing import Union
from fastapi import FastAPI

from models import Product


app = FastAPI()
all_product: list[Product] = []


@app.post("/add_product")
async def add_product(prod: Product):
    all_product.append(prod)
    return all_product


@app.get("/product/{product_id}")
async def get_product(product_id: int):
    for product in all_product:
        if all_product.product_id == product_id:
            return product
    return {"message": "Product not found"}


@app.get("/products/search")
async def product_search(keyword: str, category: str = "", limit: int = 10):
    products = []
    for product in all_product:
        if (keyword.lower() in product.name.lower()) and (category.lower() in product.category.lower()):
            products.append(product)
    return products[:limit]

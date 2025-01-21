from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False


# Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Item endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


# Create item endpoint
@app.post("/items/")
def create_item(item: Item):
    return item

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

from middleware import authenticate
from .utils import find_item
import os


fastapi = FastAPI()

# the list of items of inventory
inventoy = [{"id":1, "name": "Treasure", "quantity":3}]

# an item model
class Items(BaseModel):
    name : str
    quantity : int
    
# item update class 
class ItemUpdate(BaseModel):
    name : Optional[str] = Field(None, description="Optional name of the item")
    quantity : Optional[int] = Field(None, description="Optional quantity of the item")
    

# to get items
@fastapi.get("/items")
async def get_items():
    return {"items":inventoy} 

# to get item by id
@fastapi.get("/items/{item_id}")
async def get_item(item_id:int):
    item, idx = find_item(inventoy,lambda x : x["id"] == item_id)
    return {"item":item} 

# to delete item by id
@fastapi.delete("/items/{item_id}")
async def delete_item(item_id:int,authenticated:bool = Depends(authenticate)):
    item, idx = find_item(inventoy,lambda x : x["id"] == item_id)
    if idx == -1:return HTTPException(404,"item not found")
    inventoy.pop(idx)
    return {"item":item} 

@fastapi.post("/items")
async def add_item(data:Items):
    item ={
        "id":len(inventoy) + 1,
        "name":data.name,
        "quantity":data.quantity
    }
    
    inventoy.append(item)
    return item

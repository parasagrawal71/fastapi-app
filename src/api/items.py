from fastapi import APIRouter, Body, Request, Depends
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from bson import ObjectId, json_util
from src.middlewares.items_middleware import items_common_logger, get_items_logger

router = APIRouter(dependencies=[Depends(items_common_logger)]) # middleware to multiple routes in a router


class Item(BaseModel):
    task: str


@router.get("/items")
def getItems(
    request: Request, _=Depends(get_items_logger)
):  # middleware to only one route
    items = list(request.app.database["items"].find({}))
    for item in items:
        item["_id"] = str(item["_id"])
    return items


@router.get("/items/{id}")
def getItem(request: Request, id: str):
    item = request.app.database["items"].find_one({"_id": ObjectId(id)})
    if item is None:
        return "Id not found"
    item["_id"] = str(item["_id"])
    return item


@router.post("/items")
def addItem(request: Request, body: Item):
    body = jsonable_encoder(body)
    new_item = request.app.database["items"].insert_one(body)
    created_item = request.app.database["items"].find_one({"_id": new_item.inserted_id})
    created_item["_id"] = str(created_item["_id"])
    return created_item


@router.put("/items/{id}")
def updateItem(request: Request, id: str, body=Body()):
    update_result = request.app.database["items"].update_one(
        {"_id": ObjectId(id)}, {"$set": body}
    )
    if update_result.matched_count == 0:
        return "Id not found"

    item = request.app.database["items"].find_one({"_id": ObjectId(id)})
    item["_id"] = str(item["_id"])
    return item


@router.delete("/items/{id}")
def deleteItem(request: Request, id: str):
    delete_result = request.app.database["items"].delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return id
    return "Id not found"

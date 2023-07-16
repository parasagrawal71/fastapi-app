from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter()

fakeDatabase = {1: {"task": "Clean bike"}, 2: {"task": "Workout"}, 3: {"task": "Study"}}


class Item(BaseModel):
    task: str


@router.get("/items")
def getItems():
    return fakeDatabase


@router.get("/items/{id}")
def getItem(id: int):
    if id not in fakeDatabase:
        return "Id not found"
    return fakeDatabase[id]


@router.post("/items")
def addItem(body: Item):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = body
    return fakeDatabase[newId]


@router.put("/items/{id}")
def updateItem(id: int, body=Body()):
    if id not in fakeDatabase:
        return "Id not found"
    fakeDatabase[id] = body
    return fakeDatabase[id]


@router.delete("/items/{id}")
def deleteItem(id: int):
    if id not in fakeDatabase:
        return "Id not found"
    del fakeDatabase[id]
    return id


# References:
# https://betterprogramming.pub/my-first-crud-app-with-fast-api-74ac190d2dcc
# https://github.com/KenMwaura1/Fast-Api-example
# DOCS
# https://fastapi.tiangolo.com

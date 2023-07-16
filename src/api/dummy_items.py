from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter()

fakeDatabase = {1: {"task": "Clean bike"}, 2: {"task": "Workout"}, 3: {"task": "Study"}}


class Item(BaseModel):
    task: str


@router.get("/dummy_items")
def getItems():
    return fakeDatabase


@router.get("/dummy_items/{id}")
def getItem(id: int):
    if id not in fakeDatabase:
        return "Id not found"
    return fakeDatabase[id]


@router.post("/dummy_items")
def addItem(body: Item):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = body
    return fakeDatabase[newId]


@router.put("/dummy_items/{id}")
def updateItem(id: int, body=Body()):
    if id not in fakeDatabase:
        return "Id not found"
    fakeDatabase[id] = body
    return fakeDatabase[id]


@router.delete("/dummy_items/{id}")
def deleteItem(id: int):
    if id not in fakeDatabase:
        return "Id not found"
    del fakeDatabase[id]
    return id


# References:
# https://betterprogramming.pub/my-first-crud-app-with-fast-api-74ac190d2dcc
# https://github.com/KenMwaura1/Fast-Api-example - Break down APIs into modules
# DOCS
# https://fastapi.tiangolo.com

from fastapi import APIRouter, Body

router = APIRouter()

fakeDatabase = {1: {"task": "Clean bike"}, 2: {"task": "Workout"}, 3: {"task": "Study"}}


@router.get("/items")
def getItems():
    return fakeDatabase


@router.get("/items/{id}")
def getItem(id: int):
    if id not in fakeDatabase:
        return "Id not found"
    return fakeDatabase[id]


@router.post("/items")
def addItem(body=Body()):
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

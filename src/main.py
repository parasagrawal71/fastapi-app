from fastapi import FastAPI

from src.api import items

app = FastAPI()


@app.get("/")
def healthcheck():
    return "Ok"


app.include_router(items.router)

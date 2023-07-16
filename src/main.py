from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api import items

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)


@app.get("/")
def healthcheck():
    return "Ok"


@app.on_event("startup")
def startup():
    print("Starting fastapi server...")


@app.on_event("shutdown")
def shutdown():
    print("Closing fastapi server...")


app.include_router(items.router)

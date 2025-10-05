from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pymongo import MongoClient


# CUSTOM IMPORTs
from src.api import dummy_items, items
from src.config import config

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT", "HEAD", "PATCH", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/health")
def healthcheck():
    return "Ok"


@app.on_event("startup")
def startup():
    print("Starting {appName}...".format(appName=config.APP_NAME))
    print("Connecting database...")
    app.mongodb_client = MongoClient(config.MONGODB_URI)
    app.database = app.mongodb_client[config.DATABASE_NAME]
    print("Database connected!")


@app.on_event("shutdown")
def shutdown():
    print("Closing fastapi server...")
    print("Disconnecting database...")
    app.mongodb_client.close()
    print("Database disconnected!")


app.include_router(dummy_items.router)
app.include_router(items.router)

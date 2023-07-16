from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# CUSTOM IMPORTs
from src.api import items
from src.config import config

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
    print("Starting {appName}...".format(appName=config.APP_NAME))


@app.on_event("shutdown")
def shutdown():
    print("Closing fastapi server...")


app.include_router(items.router)

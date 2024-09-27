from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.v1 import order_controller

app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.title = "Beers Bar Api"
app.version = "1.0"

app.include_router(order_controller.router, prefix="/api/v1")

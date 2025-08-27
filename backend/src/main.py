from contextlib import asynccontextmanager

from fastapi import FastAPI

from .api.views import router as api_router
from .db.utils import get_mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    mongodb = get_mongodb()
    app.mongodb = mongodb

    yield
    app.mongodb.close()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def read_doc():
    return {"Hello": "World"}

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .connect4.settings import settings

from .api.views import router as api_router
from .db.utils import get_mongodb_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = get_mongodb_client()
    db = client.get_database(settings.MONGO_DB_DB)
    app.mongodb = db

    yield
    client.mongodb.close()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def read_doc():
    return {"Hello": "World"}

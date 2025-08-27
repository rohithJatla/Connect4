from motor.motor_asyncio import AsyncIOMotorClient

from ..connect4.settings import settings


def get_mongodb_client() -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(settings.MONGO_DB_URL)
    return client

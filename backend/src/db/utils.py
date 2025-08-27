from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from ..connect4.settings import settings


def get_mongodb() -> AsyncIOMotorDatabase:
    client = AsyncIOMotorClient(settings.MONGO_DB_URL)
    return client.get_database(settings.MONGO_DB_DB)

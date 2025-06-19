from datetime import datetime
import os
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, init_beanie
from pydantic import Field

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://microlearn:microlearn@mongodb:27017/microlearn?authSource=admin")

async def init_db():
    # Create Motor client
    client = AsyncIOMotorClient(MONGODB_URI)
    await init_beanie(database=client.db_name, document_models=[User, Card, Deck])

class User(Document):
    username: str
    email: str
    password: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime

class Card(Document):
    front: str
    back: str
    user: Optional[User] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime

class Deck(Document):
    title: str
    cards: Optional[list[Card]] = []
    user: Optional[User] = None
    description: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime

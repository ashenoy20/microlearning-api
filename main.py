from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import flash_cards
from app.db.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    yield 

app = FastAPI(lifespan=lifespan)

app.include_router(flash_cards.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

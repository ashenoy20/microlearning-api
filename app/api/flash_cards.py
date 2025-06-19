from datetime import datetime
from fastapi import APIRouter
from app.db.database import Deck
from app.models.flash_cards import DeckCreate

router = APIRouter(prefix="/flashcards", tags=["flashcards"])

@router.get("/", response_model=list[Deck])
async def get_decks():
    decks = await Deck.find().to_list()
    return decks

@router.post("/", response_model=Deck)
async def create_deck(deck: DeckCreate):
    now = datetime.now()
    new_deck = Deck(**deck.model_dump(), created_at=now, updated_at=now)
    await new_deck.save()
    return new_deck
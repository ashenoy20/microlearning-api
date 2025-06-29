from fastapi import APIRouter, Depends

from app.db.database import Deck
from app.models.flash_cards import DeckCreate
from app.services.flash_cards_service import (
    FlashCardsService,
    inject_flash_card_service,
)

router = APIRouter(prefix="/flashcards", tags=["flashcards"])


@router.get("/", response_model=list[Deck])
async def get_decks(
    flash_card_service: FlashCardsService = Depends(inject_flash_card_service),
):
    decks = await flash_card_service.get_decks()
    return decks


@router.post("/", response_model=Deck)
async def create_deck(
    deck: DeckCreate,
    flash_card_service: FlashCardsService = Depends(inject_flash_card_service),
):
    new_deck = flash_card_service.create_deck(deck)
    return new_deck

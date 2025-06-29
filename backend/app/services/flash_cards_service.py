from datetime import datetime
from typing import Optional

from app.db.database import Deck
from app.models.flash_cards import DeckCreate


class DeckNotFoundError(Exception):
    """Raised when a deck is not found"""

    pass


class DeckOperationError(Exception):
    """Raised when a deck operation fails"""

    pass


class FlashCardsService:
    def __init__(self):
        pass

    async def create_deck(self, deck: DeckCreate) -> Deck:
        """Create a new deck.

        Args:
            deck: Deck data to create
        Returns:
            The created deck
        Raises:
            DeckOperationError: If creation fails
        """
        try:
            now = datetime.now()
            new_deck = Deck(**deck.model_dump(), created_at=now, updated_at=now)
            await new_deck.save()
            return new_deck
        except Exception as e:
            raise DeckOperationError(f"Failed to create deck: {str(e)}") from e

    async def get_decks(self) -> list[Deck]:
        """Retrieve all decks.

        Returns:
            List of all decks (empty if none found)
        Raises:
            DeckOperationError: If retrieval fails
        """
        try:
            decks = await Deck.find().to_list()
            return decks
        except Exception as e:
            raise DeckOperationError(f"Failed to retrieve decks: {str(e)}") from e

    async def update_deck(self, deck_id: str, deck_update: DeckCreate) -> Deck:
        """Update an existing deck by ID.

        Args:
            deck_id: ID of the deck to update
            deck_update: Updated deck data
        Returns:
            The updated deck
        Raises:
            DeckNotFoundError: If deck not found
            DeckOperationError: If update fails
        """
        try:
            deck = await self.get_deck_by_id(deck_id)
            if deck is None:
                raise DeckNotFoundError(f"Deck with ID {deck_id} not found")

            deck.title = deck_update.title
            deck.description = deck_update.description
            deck.updated_at = datetime.now()
            await deck.save()

            return deck
        except DeckNotFoundError:
            raise
        except Exception as e:
            raise DeckOperationError(f"Failed to update deck: {str(e)}") from e

    async def delete_deck(self, deck_id: str) -> bool:
        """Delete a deck by ID.

        Args:
            deck_id: ID of the deck to delete
        Returns:
            True if deletion successful
        Raises:
            DeckNotFoundError: If deck not found
            DeckOperationError: If deletion fails
        """
        try:
            deck = await self.get_deck_by_id(deck_id)
            if deck is None:
                raise DeckNotFoundError(f"Deck with ID {deck_id} not found")

            await deck.delete()

            return True
        except DeckNotFoundError:
            raise
        except Exception as e:
            raise DeckOperationError(f"Failed to delete deck: {str(e)}") from e

    async def get_deck_by_id(self, deck_id: str) -> Optional[Deck]:
        """Retrieve a deck by ID.

        Args:
            deck_id: ID of the deck to retrieve
        Returns:
            The deck if found, None otherwise
        """

        deck = await Deck.get(deck_id)
        return deck


def inject_flash_card_service():
    return FlashCardsService()

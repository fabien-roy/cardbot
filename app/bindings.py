from app.cards.factories import DeckFactory, CardFactory
from app.games.factories import GameFactory
from app.sessions.factories import SessionFactory
from app.sessions.services import SessionService

# TODO : Fix injection
card_factory = CardFactory()
deck_factory = DeckFactory(card_factory)
game_factory = GameFactory(deck_factory)
session_factory = SessionFactory(game_factory)
session_service = SessionService(session_factory)

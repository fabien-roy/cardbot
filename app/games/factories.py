from injector import inject

from app.cards.factories import DeckFactory
from app.games.enums import GameType
from app.games.exceptions import InvalidGameTypeException
from app.games.models import FuckYouGame, RideTheBusGame


class GameFactory:
    @inject
    def __init__(self, deck_factory: DeckFactory):
        self.deck_factory = deck_factory

    def create(self, game_type):
        deck = self.deck_factory.create()

        if game_type == GameType.fuck_you.name:
            return FuckYouGame(deck)
        if game_type == GameType.ride_the_bus.name:
            return RideTheBusGame(deck)

        raise InvalidGameTypeException

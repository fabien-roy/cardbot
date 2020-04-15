import inject

from app.cards.factories.deck_factories import DeckFactory
from app.games.enums.game_types import GameType
from app.games.exceptions import InvalidGameTypeException
from app.games.models.fuck_you_game import FuckYouGame
from app.games.models.ride_the_bus_game import RideTheBusGame


class GameFactory:
    deck_factory = inject.attr(DeckFactory)

    def create(self, game_type):
        deck = self.deck_factory.create()

        if game_type == GameType.fuck_you.name:
            return FuckYouGame(deck)
        if game_type == GameType.ride_the_bus.name:
            return RideTheBusGame(deck)

        raise InvalidGameTypeException

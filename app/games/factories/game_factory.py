import inject

from app.cards.factories.deck_factories import DeckFactory
from app.games.configs import GameConfig
from app.games.enums.game_types import GameType
from app.games.exceptions import InvalidGameTypeException
from app.games.models.fuck_you_games import FuckYouGame
from app.games.models.ride_the_bus_games import RideTheBusGame


class GameFactory:
    deck_factory = inject.attr(DeckFactory)
    game_config = inject.attr(GameConfig)

    def create(self, game_type):
        deck = self.deck_factory.create()
        rules = self.game_config.get_rules(game_type)

        if game_type == GameType.fuck_you.name:
            return FuckYouGame(deck, rules)
        if game_type == GameType.ride_the_bus.name:
            return RideTheBusGame(deck, rules)

        raise InvalidGameTypeException

from app.games.enums.game_types import GameType
from app.games.models.fuck_you_game import FuckYouGame
from app.games.models.ride_the_bus_game import RideTheBusGame
from tests.games.models.create_games import create_game_type, create_deck


def a_game():
    return GameBuilder()


class GameBuilder:

    default_deck = create_deck()
    deck = default_deck

    default_game_type = create_game_type()
    game_type = default_game_type

    def with_deck(self, deck):
        self.deck = deck
        return self

    def with_type(self, game_type):
        self.game_type = game_type
        return self

    def build(self):
        if self.game_type == GameType.fuck_you:
            return FuckYouGame(self.deck)
        if self.game_type == GameType.ride_the_bus:
            return RideTheBusGame(self.deck)

from app.games.enums.game_types import GameType
from app.games.entities.fuck_you_games import FuckYouGame
from app.games.entities.ride_the_bus_games import RideTheBusGame
from tests.games.entities.create_games import create_game_type, create_deck


def a_game():
    return GameBuilder()


class GameBuilder:

    def __init__(self):
        self.deck = create_deck()
        self.game_type = create_game_type()

    def with_deck(self, deck):
        self.deck = deck
        return self

    def with_type(self, game_type):
        self.game_type = game_type
        return self

    def build(self):
        if self.game_type == GameType.fuck_you:
            return FuckYouGame(self.deck, {})
        if self.game_type == GameType.ride_the_bus:
            return RideTheBusGame(self.deck, {})

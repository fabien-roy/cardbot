from app.cards.factories import create_random_deck
from app.games.enums import GameType
from app.games.exceptions import InvalidGameTypeException
from app.games.models import FuckYouGame, RideTheBusGame


def create_game(game_type):
    deck = create_random_deck()

    if game_type == GameType.fuck_you.name:
        return FuckYouGame(deck)
    if game_type == GameType.ride_the_bus.name:
        return RideTheBusGame(deck)

    raise InvalidGameTypeException

import unittest

from app.games.enums import GameType
from app.games.exceptions import InvalidGameTypeException
from app.games.factories import create_game
from app.games.models import FuckYouGame, RideTheBusGame


class CardFactoryTest(unittest.TestCase):

    def test_create_game_with_fuck_you_should_create_fuck_you(self):
        game_type = GameType.fuck_you.name

        game = create_game(game_type)

        self.assertTrue(isinstance(game, FuckYouGame))

    def test_create_game_with_ride_the_bus_should_create_ride_the_bus(self):
        game_type = GameType.ride_the_bus.name

        game = create_game(game_type)

        self.assertTrue(isinstance(game, RideTheBusGame))

    def test_create_game_with_invalid_game_type_should_throw_invalid_game_type_exception(self):
        game_type = 'invalid'

        self.assertRaises(InvalidGameTypeException, create_game(game_type))

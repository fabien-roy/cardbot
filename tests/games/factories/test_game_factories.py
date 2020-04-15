from app.games.enums.game_types import GameType
from app.games.exceptions import InvalidGameTypeException
from app.games.factories.game_factory import GameFactory
from app.games.models.fuck_you_game import FuckYouGame
from app.games.models.ride_the_bus_game import RideTheBusGame
from tests.test_basic import BasicTest


class GameFactoryTest(BasicTest):

    def setUp(self):
        self.factory = GameFactory()

    def test_create_with_fuck_you_should_create_fuck_you(self):
        game_type = GameType.fuck_you.name

        game = self.factory.create(game_type)

        self.assertTrue(isinstance(game, FuckYouGame))

    def test_create_with_ride_the_bus_should_create_ride_the_bus(self):
        game_type = GameType.ride_the_bus.name

        game = self.factory.create(game_type)

        self.assertTrue(isinstance(game, RideTheBusGame))

    def test_create_with_invalid_game_type_should_throw_invalid_game_type_exception(self):
        game_type = 'invalid'

        self.assertRaises(InvalidGameTypeException, self.factory.create, game_type)

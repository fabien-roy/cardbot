from unittest.mock import Mock

from app.games.enums.game_types import GameType
from app.games.exceptions import InvalidGameTypeException
from app.games.factories.game_factory import GameFactory
from app.games.models.fuck_you_games import FuckYouGame
from app.games.models.ride_the_bus_games import RideTheBusGame
from tests.cards.factories.mock_deck_factories import mock_deck_factory
from tests.games.mock_configs import mock_game_config
from tests.test_basic import BasicTest


class GameFactoryTest(BasicTest):
    mock_deck = Mock()
    mock_rules = Mock()
    test_game_type = None

    def setUp(self):
        mock_deck_factory.create.return_value = self.mock_deck
        mock_game_config.get_rules.side_effect = self.return_mock_rules_for_game_type
        self.factory = GameFactory()

    def return_mock_rules_for_game_type(self, game_type):
        if game_type == self.test_game_type:
            return self.mock_rules

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

    def test_create_should_create_with_deck(self):
        game_types = [GameType.fuck_you.name, GameType.ride_the_bus.name]
        for game_type in game_types:
            self.assert_create_with_deck(game_type)

    def assert_create_with_deck(self, game_type):
        game = self.factory.create(game_type)

        self.assertEqual(self.mock_deck, game.deck)

    def test_create_should_create_with_rules(self):
        game_types = [GameType.fuck_you.name, GameType.ride_the_bus.name]
        for game_type in game_types:
            self.test_game_type = game_type
            self.assert_create_with_rules(game_type)

    def assert_create_with_rules(self, game_type):
        game = self.factory.create(game_type)

        self.assertEqual(self.mock_rules, game.rules)

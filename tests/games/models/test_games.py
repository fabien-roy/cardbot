from app.cards.models.cards import Card
from app.games.exceptions import PlayerAlreadyAddedException, PlayerNotFoundException
from app.games.models.games import Game
from tests.test_basic import BasicTest


class GameTest(BasicTest):
    deck = [Card(1), Card(2)]
    player = 'Player'
    other_player = 'OtherPlayer'

    def setUp(self):
        self.game = Game(self.deck)
        self.game.add_player(self.player)
        self.game.add_player(self.other_player)

    def test_add_player_should_add_player(self):
        new_player = 'NewPlayer'

        self.game.add_player(new_player)

        self.assertEqual(new_player, self.game.get_player(new_player).name)

    def test_add_player_with_existing_player_should_raise_player_already_added_exception(self):
        self.assertRaises(PlayerAlreadyAddedException, self.game.add_player, self.player)

    def test_get_player_should_get_player(self):
        player = self.game.get_player(self.player)

        self.assertEqual(self.player, player.name)

    def test_add_player_with_non_existing_player_should_raise_player_not_found_exception(self):
        non_existing_player = 'NonExistingPlayer'

        self.assertRaises(PlayerNotFoundException, self.game.get_player, non_existing_player)

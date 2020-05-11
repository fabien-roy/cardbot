from app.sessions.ui.messages import new_game_message, add_player_message, add_players_message, \
    print_players_message, remove_player_message, remove_players_message, draw_message
from tests.games.models.build_players import a_player
from tests.test_basic import BasicTest


class SessionMessagesTest(BasicTest):
    in_game_player = a_player().with_no(1).with_name('player_name').build()
    other_in_game_player = a_player().with_no(2).with_name('other_player_name').build()
    not_in_game_player = a_player().with_no(3).with_name(
        'another_player_name').that_has_quit().build()

    def test_new_game_message_should_format_message_with_game_type(self):
        expected_message = 'Beginning a new game of game_type!'

        message = new_game_message('game_type')

        self.assertEqual(expected_message, message)

    def test_add_player_message_should_format_message_with_player(self):
        expected_message = 'Added player'

        message = add_player_message('player')

        self.assertEqual(expected_message, message)

    def test_add_players_message_should_format_message_with_players(self):
        expected_message = 'Added player, other_player'

        message = add_players_message(['player', 'other_player'])

        self.assertEqual(expected_message, message)

    def test_remove_player_message_should_format_message_with_player(self):
        expected_message = 'Removed player'

        message = remove_player_message('player')

        self.assertEqual(expected_message, message)

    def test_remove_players_message_should_format_message_with_players(self):
        expected_message = 'Removed player, other_player'

        message = remove_players_message(['player', 'other_player'])

        self.assertEqual(expected_message, message)

    def test_print_players_message_should_print_players(self):
        expected_message = ('**Player no #1 : player_name (in game)** \n'
                            '**Player no #2 : other_player_name (in game)** \n')

        message = print_players_message([self.in_game_player, self.other_in_game_player])

        self.assertEqual(expected_message, message)

    def test_print_players_message_with_not_in_game_players_should_print_players(self):
        expected_message = ('**Player no #1 : player_name (in game)** \n'
                            'Player no #3 : another_player_name (has quit) \n')

        message = print_players_message([self.in_game_player, self.not_in_game_player])

        self.assertEqual(expected_message, message)

    def test_print_players_message_without_players_should_return_no_players_message(self):
        expected_message = 'No players!'

        message = print_players_message([])

        self.assertEqual(expected_message, message)

    def test_draw_message_should_format_message_with_name_and_result(self):
        expected_message = 'name has drawn : result'

        message = draw_message('name', 'result')

        self.assertEqual(expected_message, message)

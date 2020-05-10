from unittest.mock import Mock, call

from app.sessions.exceptions import UserAlreadyAddedException
from app.sessions.models.sessions import Session
from tests.sessions.models.build_users import a_user
from tests.test_basic import BasicTest


class SessionTest(BasicTest):
    mock_game = Mock()
    user = a_user().build()
    other_user = a_user().build()

    def setUp(self):
        self.session = Session(self.mock_game)

    def test_add_user_should_add_user(self):
        self.session.add_user(self.user.name)

        self.assertEqual(1, len(self.session.users))
        self.assertEqual(self.user.name, self.session.users[0].name)

    def test_add_user_should_add_player_to_game(self):
        self.session.add_user(self.user.name)

        self.mock_game.add_player.assert_called_with(self.user.name)

    def test_add_user_with_already_added_user_should_raise_user_already_added_exception(self):
        self.session.add_user(self.user.name)

        self.assertRaises(UserAlreadyAddedException, self.session.add_user, self.user.name)

    def test_add_users_should_add_users(self):
        users = [self.user.name, self.other_user.name]

        self.session.add_users(users)

        self.assertEqual(2, len(self.session.users))
        self.assertEqual(self.user.name, self.session.users[0].name)
        self.assertEqual(self.other_user.name, self.session.users[1].name)

    def test_add_users_should_add_players_to_game(self):
        users = [self.user.name, self.other_user.name]

        self.session.add_users(users)

        calls = [call(self.user.name), call(self.other_user.name)]
        self.mock_game.add_player.assert_has_calls(calls)

    def test_add_users_with_already_added_user_should_raise_user_already_added_exception(self):
        users = [self.user.name, self.other_user.name]

        self.session.add_users(users)

        self.assertRaises(UserAlreadyAddedException, self.session.add_users, users)

    def test_remove_user_should_remove_user(self):
        pass

    def test_remove_user_should_remove_player_from_game(self):
        pass

    def test_remove_user_with_nonexistent_user_should_raise_user_not_found_exception(self):
        pass

    def test_remove_users_should_remove_users(self):
        pass

    def test_remove_users_should_remove_players_from_game(self):
        pass

    def test_remove_users_with_nonexistent_user_should_raise_user_not_found_exception(self):
        pass

    def test_get_players_should_get_players_from_game(self):
        pass

    def test_draw_should_draw_from_game(self):
        pass

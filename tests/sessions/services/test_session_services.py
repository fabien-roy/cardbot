from unittest.mock import Mock

from app.sessions.exceptions import SessionNotStartedException
from app.sessions.services.session_services import SessionService
from tests.games.entities.build_games import a_game
from tests.games.entities.create_games import create_game_type
from tests.sessions.factories.mock_session_factories import mock_session_factory
from tests.sessions.entities.build_users import a_user
from tests.test_basic import BasicTest


class SessionServiceTest(BasicTest):
    mock_session = Mock()
    mock_drawn = Mock()
    mock_players = Mock()
    game_type = create_game_type()
    user = a_user().build()
    other_user = a_user().build()

    def setUp(self):
        self.mock_session.game = a_game().with_type(self.game_type).build()
        self.mock_session.draw.return_value = self.mock_drawn
        self.mock_session.get_players.return_value = self.mock_players
        mock_session_factory.create.side_effect = lambda game_type: self.mock_session

        self.service = SessionService()
        self.service.new_game(self.game_type.name)

    def test_new_game_should_return_game_type(self):
        actual_game_type = self.service.new_game(self.game_type.name)

        self.assertEqual(self.game_type.value, actual_game_type)

    def test_add_user_should_add_user_to_session(self):
        self.service.add_user(self.user.name)

        self.mock_session.add_user.assert_called_with(self.user.name)

    def test_add_user_should_return_user_name(self):
        name = self.service.add_user(self.user.name)

        self.assertEqual(self.user.name, name)

    def test_add_users_should_add_users_to_session(self):
        users = [self.user.name, self.other_user.name]

        self.service.add_users(users)

        self.mock_session.add_users.assert_called_with(users)

    def test_add_users_should_return_user_names(self):
        users = [self.user.name, self.other_user.name]

        names = self.service.add_users(users)

        self.assertCountEqual(users, names)

    def test_remove_user_should_remove_user_from_session(self):
        self.service.remove_user(self.user.name)

        self.mock_session.remove_user.assert_called_with(self.user.name)

    def test_remove_user_should_return_user_name(self):
        name = self.service.remove_user(self.user.name)

        self.assertEqual(self.user.name, name)

    def test_remove_users_should_remove_users_from_session(self):
        users = [self.user.name, self.other_user.name]

        self.service.remove_users(users)

        self.mock_session.remove_users.assert_called_with(users)

    def test_remove_users_should_return_user_names(self):
        users = [self.user.name, self.other_user.name]

        names = self.service.remove_users(users)

        self.assertCountEqual(users, names)

    def test_get_players_should_get_players(self):
        players = self.service.get_players()

        self.assertEqual(self.mock_players, players)

    def test_get_players_without_session_should_raise_session_not_started_exception(self):
        self.service = SessionService()

        self.assertRaises(SessionNotStartedException, self.service.get_players)

    def test_draw_should_drawn_from_game(self):
        drawn = self.service.draw()

        self.assertEqual(self.mock_drawn, drawn)

from unittest.mock import Mock

from app.sessions.services.session_services import SessionService
from tests.games.models.build_games import a_game
from tests.games.models.create_games import create_game_type
from tests.sessions.factories.mock_session_factories import mock_session_factory
from tests.sessions.models.build_users import a_user
from tests.test_basic import BasicTest


class SessionServiceTest(BasicTest):
    mock_session = Mock()
    game_type = create_game_type()
    user = a_user().build()

    def setUp(self):
        self.mock_session.game = a_game().with_type(self.game_type).build()
        mock_session_factory.create.side_effect = lambda game_type: self.mock_session

        self.service = SessionService()
        self.service.new_game(self.game_type.name)

    def test_new_game_should_return_game_type(self):
        actual_game_type = self.service.new_game(self.game_type.name)

        self.assertEquals(self.game_type.value, actual_game_type)

    def test_add_user_should_add_user_to_session(self):
        self.service.add_user(self.user.name)

        self.mock_session.add_user.assert_called_with(self.user.name)

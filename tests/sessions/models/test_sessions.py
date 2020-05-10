from app.sessions.models.sessions import Session
from tests.games.models.build_games import a_game
from tests.test_basic import BasicTest


class SessionServiceTest(BasicTest):
    def setUp(self):
        game = a_game().build()

        self.session = Session(game)

    def test_add_user_should_add_user_to_users(self):
        pass

    def test_add_user_should_add_user_to_game(self):
        pass

    def test_add_user_with_already_added_user_should_raise_user_already_added_exception(self):
        pass

    def test_add_users_should_add_users_to_users(self):
        pass

    def test_add_users_should_add_users_to_game(self):
        pass

    def test_add_users_with_already_added_user_should_raise_user_already_added_exception(self):
        pass

    def test_remove_user_should_remove_user_from_users(self):
        pass

    def test_remove_user_should_remove_user_from_game(self):
        pass

    def test_remove_user_with_nonexistent_user_should_raise_user_not_found_exception(self):
        pass

    def test_remove_users_should_remove_users_from_users(self):
        pass

    def test_remove_users_should_remove_users_from_game(self):
        pass

    def test_remove_users_with_nonexistent_user_should_raise_user_not_found_exception(self):
        pass

    def test_get_players_should_get_players_from_game(self):
        pass

    def test_draw_should_draw_from_game(self):
        pass

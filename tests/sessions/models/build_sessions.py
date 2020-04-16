from app.sessions.models.sessions import Session
from tests.sessions.models.create_sessions import create_game


def a_session():
    return SessionBuilder()


class SessionBuilder:

    default_game = create_game()
    game = default_game

    def with_game(self, game):
        self.game = game
        return self

    def build(self):
        return Session(self.game)

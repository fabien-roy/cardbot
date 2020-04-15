import inject

from app.games.factories import GameFactory
from app.sessions.models.sessions import Session


class SessionFactory:
    game_factory = inject.attr(GameFactory)

    def create(self, game_type):
        game = self.game_factory.create(game_type)
        return Session(game)

import inject

from app.games.factories.game_factory import GameFactory
from app.sessions.entities.sessions import Session


class SessionFactory:
    game_factory = inject.attr(GameFactory)

    def create(self, game_type):
        game = self.game_factory.create(game_type)
        return Session(game)

from injector import inject

from app.games.factories import GameFactory
from app.sessions.models import Session


class SessionFactory:
    @inject
    def __init__(self, game_factory: GameFactory):
        self.game_factory = game_factory

    def create(self, game_type):
        game = self.game_factory.create(game_type)
        return Session(game)

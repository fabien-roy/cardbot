import inject

from app.sessions.exceptions import SessionNotStartedException
from app.sessions.factories.session_factories import SessionFactory


class SessionService:
    session = None
    session_factory = inject.attr(SessionFactory)

    def new_game(self, game_type):
        self.session = self.session_factory.create(game_type)
        return self.session.game.type

    def add_user(self, name):
        self.session.add_user(name)
        return name

    def add_users(self, names):
        self.session.add_users(names)
        return names

    def remove_user(self, name):
        self.session.remove_user(name)
        return name

    def remove_users(self, names):
        self.session.remove_users(names)
        return names

    def get_players(self):
        if self.session is None:
            raise SessionNotStartedException

        return self.session.get_players()

    def draw(self):
        return self.session.draw()

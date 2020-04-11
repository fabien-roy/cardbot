from injector import inject

from app.sessions.factories import SessionFactory


class SessionService:
    session = None

    @inject
    def __init__(self, session_factory: SessionFactory):
        self.session_factory = session_factory

    # TODO : Valide user not present
    def new_game(self, game_type):
        self.session = self.session_factory.create(game_type)
        return self.session.game.type

    def add_user(self, name):
        self.session.add_user(name)
        return name

    def draw(self, name):
        user = self.session.get_user(name)
        return self.session.draw(user)

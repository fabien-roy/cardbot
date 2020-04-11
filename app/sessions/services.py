from app.sessions.factories import create_session


class SessionService:
    session = None

    # TODO : Valide user not present
    def new_game(self, game_type):
        self.session = create_session(game_type)
        return self.session.game.type

    def add_user(self, name):
        self.session.add_user(name)
        return name

    def draw(self, name):
        user = self.session.get_user(name)
        return self.session.draw(user)

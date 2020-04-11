from app import create_game, Session


class SessionService:
    session = None

    # TODO : Valide user not present
    def new_game(self, game_type):
        game = create_game(game_type)
        self.session = Session(game)
        return self.session.game.type

    def add_user(self, name):
        self.session.add_user(name)
        return name

    def draw(self, name):
        user = self.session.get_user(name)
        return self.session.draw(user)

class User:
    def __init__(self, name):
        self.name = name


class Session:
    # TODO : Have session.users and game.players
    def __init__(self, game):
        self.game = game

    # TODO : Valide user not present
    def add_user(self, name):
        user = User(name)
        self.game.add_player(user)

class User:
    def __init__(self, name):
        self.name = name


class Session:
    def __init__(self, game):
        self.game = game
        self.users = []

    def get_user(self, name):
        return list(filter(lambda user: user.name == name, self.users))[0]

    # TODO : Valide user not present
    def add_user(self, name):
        user = User(name)
        self.users.append(user)
        self.game.add_player(user.name)

    def draw(self, user):
        player = self.game.get_player(user.name)
        return self.game.draw(player)

from app.sessions.exceptions import UserNotFoundException, UserAlreadyAddedException


class User:
    def __init__(self, name):
        self.name = name


class Session:
    def __init__(self, game):
        self.game = game
        self.users = []

    def add_user(self, name):
        user = self.get_user_if_present(name)

        if user is not None:
            raise UserAlreadyAddedException

        user = User(name)
        self.users.append(user)
        self.game.add_player(user.name)

    def get_user(self, name):
        user = self.get_user_if_present(name)

        if user is None:
            raise UserNotFoundException

        return user

    def get_user_if_present(self, name):
        for user in self.users:
            if user.name == name:
                return user

    def get_players(self):
        return self.game.get_players()

    def draw(self):
        return self.game.draw()

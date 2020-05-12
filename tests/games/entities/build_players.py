from app.games.entities.players import Player
from tests.games.entities.create_players import create_no, create_name


def a_player():
    return PlayerBuilder()


class PlayerBuilder:

    def __init__(self):
        self.no = create_no()
        self.name = create_name()
        self.in_game = True

    def with_no(self, no):
        self.no = no
        return self

    def with_name(self, name):
        self.name = name
        return self

    def that_has_quit(self):
        self.in_game = False
        return self

    def build(self):
        player = Player(self.no, self.name)
        player.in_game = self.in_game
        return player

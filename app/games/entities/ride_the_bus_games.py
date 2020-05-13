from app.games.enums.game_types import GameType
from app.games.entities.games import Game


class RideTheBusGame(Game):
    type = GameType.ride_the_bus.value

    def __init__(self, deck, rules):
        super().__init__(deck, rules)
        self.dealer = None
        self.player = None

    def set_dealer(self, name):
        self.dealer = super().add_player(name)
        self.players.append(self.dealer)

    def add_player(self, name):
        self.player = super().add_player(name)
        self.players.append(self.player)

    def draw(self):
        pass

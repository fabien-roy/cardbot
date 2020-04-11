class Player:
    def __init__(self, name):
        self.name = name


class Game:
    def __init__(self, deck):
        self.deck = deck

    def add_player(self, player):
        pass


class FuckYouGame(Game):
    def __init__(self, deck):
        super().__init__(deck)
        self.players = []

    # TODO : Valide player not present
    def add_player(self, player):
        self.players.append(player)


class RideTheBusGame(Game):
    def __init__(self, deck):
        super().__init__(deck)
        self.dealer = None
        self.player = None

    # TODO : Valide dealer
    def set_dealer(self, dealer):
        self.dealer = dealer

    # TODO : Valide add player
    def add_player(self, player):
        self.player = player

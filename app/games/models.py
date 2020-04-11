class Player:
    def __init__(self, name):
        self.name = name


class Game:
    def __init__(self, deck):
        self.deck = deck

    def add_player(self, name):
        pass

    def get_player(self, name):
        pass

    def draw(self, player):
        pass


class FuckYouGame(Game):
    type = 'Fuck you'

    def __init__(self, deck):
        super().__init__(deck)
        self.players = []

    # TODO : Valide player not present
    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def get_player(self, name):
        return list(filter(lambda player: player.name == name, self.players))[0]

    def draw(self, player):
        card = self.deck.draw()
        return player.name, card.value


class RideTheBusGame(Game):
    type = 'Ride the bus'

    def __init__(self, deck):
        super().__init__(deck)
        self.dealer = None
        self.player = None

    # TODO : Valide dealer
    def set_dealer(self, name):
        self.dealer = Player(name)

    # TODO : Valide add player
    def add_player(self, name):
        self.player = Player(name)

    # TODO : Throw exception if wrong name
    def get_player(self, name):
        if name == self.player.name:
            return self.player

        return None

    # TODO
    def draw(self, player):
        pass

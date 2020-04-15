from app.games.exceptions import PlayerNotFoundException, PlayerAlreadyAddedException


class Player:
    def __init__(self, no, name):
        self.no = no
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.no == other.no and self.name == other.name
        return False


# TODO : Separate Game from CardGame
class Game:
    def __init__(self, deck):
        self.deck = deck
        self.players = []

    def add_player(self, name):
        player = self.get_player_if_present(name)

        if player is not None:
            raise PlayerAlreadyAddedException

        player = Player(self.next_player_no(), name)
        self.players.append(player)
        return player

    def get_player(self, name):
        player = self.get_player_if_present(name)

        if player is None:
            raise PlayerNotFoundException

        return player

    def get_player_if_present(self, name):
        for player in self.players:
            if player.name == name:
                return player

        return None

    def get_players(self):
        return self.players

    def draw(self, player):
        pass

    def next_player_no(self):
        return len(self.players) + 1


class FuckYouGame(Game):
    type = 'Fuck you'

    def __init__(self, deck):
        super().__init__(deck)

    def draw(self, player):
        card = self.deck.draw()
        result = '{} of {}'.format(card.house_value.name, card.house_suit.name)
        return player.name, result


class RideTheBusGame(Game):
    type = 'Ride the bus'

    def __init__(self, deck):
        super().__init__(deck)
        self.dealer = None
        self.player = None

    # TODO : Valide dealer
    def set_dealer(self, name):
        self.dealer = super().add_player(name)
        self.players.append(self.dealer)

    # TODO : Valide add player
    def add_player(self, name):
        self.player = super().add_player(name)
        self.players.append(self.player)

    # TODO
    def draw(self, player):
        pass

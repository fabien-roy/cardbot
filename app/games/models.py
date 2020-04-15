from app.games.exceptions import PlayerNotFoundException, PlayerAlreadyAddedException


class Player:
    def __init__(self, no, name):
        self.no = no
        self.name = name
        self.in_game = True

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.no == other.no and self.name == other.name
        return False


# TODO : Separate Game from CardGame
class Game:
    def __init__(self, deck):
        self.deck = deck
        self.current_players = []
        self.players = []

    def add_player(self, name):
        player = self.get_player_if_present(name)

        if player is not None:
            raise PlayerAlreadyAddedException

        player = Player(self.next_player_no(), name)
        self.players.append(player)
        self.current_players.append(player)
        return player

    # TODO : Unused
    def remove_player(self, name):
        player = self.get_player_if_present(name)
        player.in_game = False
        self.current_players.remove(player)
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

    def draw(self):
        pass

    def next_player_no(self):
        return len(self.players) + 1


class OrderedGame(Game):
    def __init__(self, deck):
        super().__init__(deck)
        self.current_no = 0

    def add_player(self, name):
        super().add_player(name)
        self.increment_current_order_no()

    def remove_player(self, name):
        super().remove_player(name)
        self.decrement_current_order_no()

    def draw(self):
        card = self.deck.draw()
        player = self.current_players[self.current_no]
        self.increment_current_order_no()
        return player, card

    def decrement_current_order_no(self):
        self.current_no = self.current_no - 1 if self.current_no > 1 else len(self.current_players)

    def increment_current_order_no(self):
        self.current_no = self.current_no + 1 if self.current_no + 1 < len(self.current_players) \
            else 0


class FuckYouGame(OrderedGame):
    type = 'Fuck you'

    def draw(self):
        player, card = super().draw()
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
    def draw(self):
        pass

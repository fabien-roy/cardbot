from app.games.exceptions import PlayerNotFoundException, PlayerAlreadyAddedException


from app.games.entities.players import Player


class Game:
    def __init__(self, deck, rules):
        self.deck = deck
        self.rules = rules
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

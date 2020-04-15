from app.games.models.game import Game


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

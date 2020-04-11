class Deck:
    def __init__(self, cards):
        self.cards = cards

    def draw(self):
        return self.cards.pop()


class Card:
    pass

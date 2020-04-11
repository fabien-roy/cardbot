from app.cards.exceptions import EmptyDeckException


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def draw(self):
        if len(self.cards) == 0:
            raise EmptyDeckException

        return self.cards.pop()


class Card:
    def __init__(self, value):
        self.value = value

from app.cards.exceptions import EmptyDeckException


class Card:
    def __init__(self, value, house_suite, house_value):
        self.value = value
        self.house_suite = house_suite
        self.house_value = house_value


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def draw(self):
        if len(self.cards) == 0:
            raise EmptyDeckException

        return self.cards.pop()

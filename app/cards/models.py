from math import floor

from app.cards.enums import HouseSuit, HouseValue
from app.cards.exceptions import EmptyDeckException


NORMAL_HOUSE_LENGTH = 13
NORMAL_DECK_LENGTH = 52


class Card:
    def __init__(self, value):
        self.value = value
        self.house_suit = self.create_house_suit(value)
        self.house_value = self.create_house_value(value)

    @staticmethod
    def create_house_suit(value):
        house_suit = floor(value / NORMAL_HOUSE_LENGTH)

        if value == NORMAL_DECK_LENGTH:
            return HouseSuit(house_suit)

        return HouseSuit(house_suit + 1)

    @staticmethod
    def create_house_value(value):
        house_value = value

        while house_value > NORMAL_HOUSE_LENGTH:
            house_value = house_value - NORMAL_HOUSE_LENGTH

        return HouseValue(house_value)


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def draw(self):
        if len(self.cards) == 0:
            raise EmptyDeckException

        return self.cards.pop()

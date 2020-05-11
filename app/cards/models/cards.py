from math import floor

from app.cards.enums.suit_house import SuitHouse
from app.cards.enums.suit_values import SuitValue

NORMAL_HOUSE_LENGTH = 13
NORMAL_DECK_LENGTH = 52


class Card:
    def __init__(self, value):
        self.value = value
        self.suit_house = self.create_suit_house(value)
        self.suit_value = self.create_suit_value(value)

    @staticmethod
    def create_suit_house(value):
        house_suit = floor(value / NORMAL_HOUSE_LENGTH)

        if value == NORMAL_DECK_LENGTH:
            return SuitHouse(house_suit)

        return SuitHouse(house_suit + 1)

    @staticmethod
    def create_suit_value(value):
        house_value = value

        while house_value > NORMAL_HOUSE_LENGTH:
            house_value = house_value - NORMAL_HOUSE_LENGTH

        return SuitValue(house_value)

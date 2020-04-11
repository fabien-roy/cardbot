from math import floor
from random import sample

from injector import inject

from app.cards.enums import HouseValue, HouseSuit
from app.cards.models import Card, Deck

NORMAL_HOUSE_LENGTH = 13
NORMAL_DECK_LENGTH = 52


class CardFactory:
    def create(self, value):
        return Card(value, self.create_house_suite(value), self.create_house_value(value))

    @staticmethod
    def create_house_suite(value):
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


class DeckFactory:
    @inject
    def __init__(self, card_factory: CardFactory):
        self.card_factory = card_factory

    def create(self):
        cards = []
        values = sample(range(1, NORMAL_DECK_LENGTH + 1), NORMAL_DECK_LENGTH)

        for value in values:
            card = self.card_factory.create(value)
            cards.append(card)

        return Deck(cards)

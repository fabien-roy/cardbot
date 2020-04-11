from random import sample

from injector import inject

from app.cards.models import Card, Deck

NORMAL_DECK_LENGTH = 52


class CardFactory:
    @staticmethod
    def create(value):
        return Card(value)


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

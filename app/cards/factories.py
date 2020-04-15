from random import sample

import inject

from app.cards.models import Card, Deck, NORMAL_DECK_LENGTH


class CardFactory:
    def create(self, value):
        return Card(value)


class DeckFactory:
    card_factory = inject.attr(CardFactory)

    def create(self):
        cards = []
        values = sample(range(1, NORMAL_DECK_LENGTH + 1), NORMAL_DECK_LENGTH)

        for value in values:
            card = self.card_factory.create(value)
            cards.append(card)

        return Deck(cards)

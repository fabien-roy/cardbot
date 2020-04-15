from random import sample

import inject

from app.cards.factories.card_factories import CardFactory
from app.cards.models.cards import NORMAL_DECK_LENGTH
from app.cards.models.decks import Deck


class DeckFactory:
    card_factory = inject.attr(CardFactory)

    def create(self):
        cards = []
        values = sample(range(1, NORMAL_DECK_LENGTH + 1), NORMAL_DECK_LENGTH)

        for value in values:
            card = self.card_factory.create(value)
            cards.append(card)

        return Deck(cards)

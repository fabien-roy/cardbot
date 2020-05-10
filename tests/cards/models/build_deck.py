from app.cards.models.decks import Deck
from tests.cards.models.create_decks import create_cards


def a_deck():
    return DeckBuilder()


class DeckBuilder:
    def __init__(self):
        self.cards = create_cards()

    def with_cards(self, cards):
        self.cards = cards
        return self

    def build(self):
        return Deck(self.cards)

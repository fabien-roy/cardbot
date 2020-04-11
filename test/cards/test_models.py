import unittest

from app.cards.exceptions import EmptyDeckException
from app.cards.models import Card, Deck


class CardModelTest(unittest.TestCase):

    card = Card(1)
    other_card = Card(2)

    def test_draw_should_pop_last_card(self):
        deck = Deck([self.card, self.other_card])

        drawn_card = deck.draw()

        self.assertEqual(drawn_card, self.other_card)

    def test_draw_without_cards_should_raise_empty_deck_exception(self):
        deck = Deck([])

        self.assertRaises(EmptyDeckException, deck.draw)

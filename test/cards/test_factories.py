import unittest
from unittest import mock

from app.cards.factories import NORMAL_DECK_LENGTH, DeckFactory
from app.cards.models import Card


class DeckFactoryTest(unittest.TestCase):

    def setUp(self):
        card_factory = mock.Mock()
        card_factory.create.side_effect = lambda value: Card(value)
        self.factory = DeckFactory(card_factory)

    def test_create_should_create_without_duplicate(self):
        deck = self.factory.create()

        hasDuplicates = len(deck.cards) != len(set(deck.cards))

        self.assertFalse(hasDuplicates)

    def test_create_should_have_normal_deck_length(self):
        deck = self.factory.create()

        length = len(deck.cards)

        self.assertEqual(NORMAL_DECK_LENGTH, length)

import unittest

from app.cards.factories import NORMAL_DECK_LENGTH, DeckFactory


class DeckFactoryTest(unittest.TestCase):

    def setUp(self):
        self.factory = DeckFactory()

    def test_create_should_create_without_duplicate(self):
        deck = self.factory.create()

        hasDuplicates = len(deck.cards) != len(set(deck.cards))

        self.assertFalse(hasDuplicates)

    def test_create_should_have_normal_deck_length(self):
        deck = self.factory.create()

        length = len(deck.cards)

        self.assertEquals(NORMAL_DECK_LENGTH, length)

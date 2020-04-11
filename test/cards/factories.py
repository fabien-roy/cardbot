import unittest

from app.cards.factories import create_random_deck, NORMAL_DECK_LENGTH


class CardFactoryTest(unittest.TestCase):

    def test_create_random_deck_should_create_without_duplicate(self):
        deck = create_random_deck()

        hasDuplicates = len(deck.cards) != len(set(deck.cards))

        self.assertFalse(hasDuplicates)

    def test_create_random_deck_should_have_normal_deck_length(self):
        deck = create_random_deck()

        length = len(deck.cards)

        self.assertEquals(NORMAL_DECK_LENGTH, length)

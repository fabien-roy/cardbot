from app.cards.factories.deck_factories import DeckFactory
from app.cards.models.cards import NORMAL_DECK_LENGTH
from tests.test_basic import BasicTest


class DeckFactoryTest(BasicTest):

    def setUp(self):
        self.factory = DeckFactory()

    def test_create_should_create_without_duplicate(self):
        deck = self.factory.create()

        has_duplicates = len(deck.cards) != len(set(deck.cards))

        self.assertFalse(has_duplicates)

    def test_create_should_have_normal_deck_length(self):
        deck = self.factory.create()

        length = len(deck.cards)

        self.assertEqual(NORMAL_DECK_LENGTH, length)

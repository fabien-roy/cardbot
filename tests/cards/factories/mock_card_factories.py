from unittest import mock

from app.cards.models.cards import Card

mock_card_factory = mock.Mock()
mock_card_factory.create.side_effect = lambda value: Card(value)

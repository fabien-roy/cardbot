from app.cards.factories.card_factories import CardFactory
from app.cards.factories.deck_factories import DeckFactory
from app.sessions.services.session_services import SessionService
from tests.cards.factories.mock_card_factories import mock_card_factory
from tests.cards.factories.mock_deck_factories import mock_deck_factory
from tests.sessions.services.mock_session_services import mock_session_service


def test_config(binder):
    binder.bind(CardFactory, mock_card_factory)
    binder.bind(DeckFactory, mock_deck_factory)

    binder.bind(SessionService, mock_session_service)

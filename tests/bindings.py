from app.cards.factories.card_factories import CardFactory
from app.cards.factories.deck_factories import DeckFactory
from app.games.configs import GameConfig
from app.sessions.factories.session_factories import SessionFactory
from app.sessions.services.session_services import SessionService
from tests.cards.factories.mock_card_factories import mock_card_factory
from tests.cards.factories.mock_deck_factories import mock_deck_factory
from tests.games.mock_configs import mock_game_config
from tests.sessions.factories.mock_session_factories import mock_session_factory
from tests.sessions.services.mock_session_services import mock_session_service


def test_config(binder):
    binder.bind(GameConfig, mock_game_config)

    binder.bind(CardFactory, mock_card_factory)
    binder.bind(DeckFactory, mock_deck_factory)
    binder.bind(SessionFactory, mock_session_factory)

    binder.bind(SessionService, mock_session_service)

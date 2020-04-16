from unittest.mock import Mock


def mock_session(game_type):
    session = Mock()
    session.game.return_value = mock_game()
    return session

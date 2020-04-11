from app import create_game
from app.sessions.models import Session


def create_session(game_type):
    game = create_game(game_type)
    return Session(game)

from app.games.enums.game_types import GameType
from tests.cards.models.build_deck import a_deck
from tests.create_basic import random_enum


def create_deck():
    return a_deck().build()


def create_game_type():
    return random_enum(GameType)

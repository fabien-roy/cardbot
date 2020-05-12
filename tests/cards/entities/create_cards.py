from random import randint

from app.cards.entities.cards import NORMAL_DECK_LENGTH


def create_value():
    return randint(1, NORMAL_DECK_LENGTH)

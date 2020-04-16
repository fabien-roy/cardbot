from random import randint

from app.cards.models.cards import NORMAL_DECK_LENGTH
from tests.cards.models.build_card import a_card


def create_cards():
    cards = []

    for i in range(0, randint(0, NORMAL_DECK_LENGTH)):
        cards.append(a_card().build())

    return cards

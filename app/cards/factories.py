from random import sample

from app.cards.models import Card, Deck

NORMAL_DECK_LENGTH = 52


def create_card(value):
    return Card(value)


def create_random_deck():
    cards = []
    values = sample(range(1, NORMAL_DECK_LENGTH + 1), NORMAL_DECK_LENGTH)

    for value in values:
        cards.append(create_card(value))

    return Deck(cards)

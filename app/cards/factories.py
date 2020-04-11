from random import sample

from app.cards.models import Card, Deck


def create_card(value):
    return Card(value)


def create_random_deck():
    cards = []
    values = sample(range(1, 53), 52)

    for value in values:
        cards.append(create_card(value))

    return Deck(cards)

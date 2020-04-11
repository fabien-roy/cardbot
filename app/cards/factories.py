from app.cards.models import Card, Deck


def create_random_deck():
    cards = []

    for i in range(0, 51):
        cards.append(Card())

    return Deck(cards)

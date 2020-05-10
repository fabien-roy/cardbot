from app.cards.models.cards import Card
from tests.cards.models.create_cards import create_value


def a_card():
    return CardBuilder()


class CardBuilder:
    def __init__(self):
        self.value = create_value()

    def with_value(self, value):
        self.value = value
        return self

    def build(self):
        return Card(self.value)

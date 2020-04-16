from app.cards.models.cards import Card
from tests.cards.models.create_cards import create_value


def a_card():
    return CardBuilder()


class CardBuilder:

    default_value = create_value()
    value = default_value

    def with_value(self, value):
        self.value = value
        return self

    def build(self):
        return Card(self.value)

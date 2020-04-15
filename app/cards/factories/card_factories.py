from app.cards.models.cards import Card


class CardFactory:
    def create(self, value):
        return Card(value)

from app.cards.entities.cards import Card


class CardFactory:
    def create(self, value):
        return Card(value)

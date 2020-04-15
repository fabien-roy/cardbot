from app.games.models.ordered_games import OrderedGame


class FuckYouGame(OrderedGame):
    type = 'Fuck you'

    def draw(self):
        player, card = super().draw()
        result = '{} of {}'.format(card.house_value.name, card.house_suit.name)
        return player.name, result

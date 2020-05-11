from app.games.models.ordered_games import OrderedGame


class FuckYouGame(OrderedGame):
    type = 'Fuck you'

    def __init__(self, deck, rules):
        super().__init__(deck, rules)

    # TODO : Test FuckYouGame.draw
    def draw(self):
        player, card = super().draw()
        result = f'{card.house_value.name} of {card.house_suit.name} \n'
        result += f'Which stands for : {self.rules.get(card.house_value)} \n'
        return player.name, result

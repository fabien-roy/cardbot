from app.games.models.ordered_games import OrderedGame


class FuckYouGame(OrderedGame):
    type = 'Fuck you'

    # TODO : Test FuckYouGame.draw
    def draw(self):
        player, card = super().draw()
        rule, description = self.rules.get(card.suit_value)
        result = f'{card.suit_value.name} of {card.suit_house.name} \n'
        result += f'Which stands for : {rule} ({description}) \n'
        return player.name, result

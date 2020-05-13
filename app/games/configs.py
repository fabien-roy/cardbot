from app.games.defaults import default_fuck_you_rules
from app.games.enums.game_types import GameType


class GameConfig:
    rules_per_game_type = {
        GameType.fuck_you.name: default_fuck_you_rules,
        GameType.ride_the_bus.name: {}
    }

    def get_rules(self, game_type):
        return self.rules_per_game_type.get(game_type)

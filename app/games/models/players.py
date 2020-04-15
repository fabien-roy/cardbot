class Player:
    def __init__(self, no, name):
        self.no = no
        self.name = name
        self.in_game = True

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.no == other.no and self.name == other.name
        return False

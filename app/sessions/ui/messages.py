def new_game_message(game_type):
    return 'Beginning a new game of {}!'.format(game_type)


def list_players_message(names):
    listed_names = ''

    for i, name in enumerate(names):
        listed_names += '{}, '.format(name) if i + 1 < len(names) else name

    return listed_names


def add_player_message(name):
    return 'Added {}'.format(name)


def add_players_message(names):
    return add_player_message(list_players_message(names))


def remove_player_message(name):
    return 'Removed {}'.format(name)


def remove_players_message(names):
    return remove_player_message(list_players_message(names))


def print_players_message(players):
    if len(players) == 0:
        return 'No players!'

    message = ''

    for player in players:
        in_game = 'in game' if player.in_game else 'has quit'
        line = 'Player no #{} : {} ({})'.format(player.no, player.name, in_game)
        line = '**{}**'.format(line) if player.in_game else line
        line = '{} \n'.format(line)
        message += line

    return message


def draw_message(name, result):
    return '{} drawed : {}'.format(name, result)

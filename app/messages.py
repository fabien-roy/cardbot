def print_players_message(players):
    if len(players) == 0:
        return 'No players!'

    message = ''

    for player in players:
        in_game = 'in game' if player.in_game else 'has quit'
        message += 'Player no #{} : @{} ({})'.format(player.no, player.name, in_game)

    return message


def draw_message(name, result):
    return '{} drawed : {}'.format(name, result)

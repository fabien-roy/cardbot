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

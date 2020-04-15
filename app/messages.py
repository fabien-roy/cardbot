def print_players_message(players):
    if len(players) == 0:
        return 'No players!'

    message = ''

    for player in players:
        message += 'Player no #{} : @{}'.format(player.no, player.name)

    return message

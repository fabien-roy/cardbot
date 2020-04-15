from discord.ext import commands

from app.bindings import session_service
from app.error_handler import register_error_handler
from app.messages import print_players_message, draw_message

bot = commands.Bot(command_prefix='$')
register_error_handler(bot)


@bot.event
async def on_ready():
    print(f'Cardbot has connected to Discord!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def new_game(ctx, game_type, *names):
    game_type = session_service.new_game(game_type)
    await ctx.send('Beginning a new game of {}!'.format(game_type))

    if len(names) > 0:
        await add_players(ctx, names)


@bot.command()
async def add_me(ctx):
    added_name = session_service.add_user(ctx.message.author.name)
    await ctx.send('Added {}'.format(added_name))


@bot.command()
async def add_player(ctx, name):
    added_name = session_service.add_user(name)
    await ctx.send('Added {}'.format(added_name))


@bot.command()
async def add_players(ctx, *names):
    names = names[0]
    added_names = ''

    for i in range(0, len(names)):
        name = session_service.add_user(names[i])
        added_names += '{}, '.format(name) if i + 1 < len(names) else name

    await ctx.send('Added {}'.format(added_names))


@bot.command()
async def remove_me(ctx):
    removed_name = session_service.remove_user(ctx.message.author.name)
    await ctx.send('Removed {}'.format(removed_name))


@bot.command()
async def remove_player(ctx, name):
    removed_name = session_service.remove_user(name)
    await ctx.send('Removed {}'.format(removed_name))


@bot.command()
async def remove_players(ctx, *names):
    names = names[0]
    removed_names = ''

    for i in range(0, len(names)):
        name = session_service.remove_user(names[i])
        removed_names += '{}, '.format(name) if i + 1 < len(names) else name

    await ctx.send('Removed {}'.format(removed_names))


@bot.command()
async def print_players(ctx):
    players = session_service.get_players()
    await ctx.send(print_players_message(players))


@bot.command()
async def draw(ctx):
    name, result = session_service.draw()
    await ctx.send(draw_message(name, result))

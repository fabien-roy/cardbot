from discord.ext import commands

from app.bindings import session_service

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print(f'Cardbot has connected to Discord!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def new_game(ctx, arg):
    game_type = session_service.new_game(arg)
    await ctx.send('Beginning a new game of {}!'.format(game_type))


@bot.command()
async def add_me(ctx):
    name = session_service.add_user(ctx.message.author.name)
    await ctx.send('Added {}'.format(name))


@bot.command()
async def draw(ctx):
    name, value = session_service.draw(ctx.message.author.name)
    await ctx.send('{} drawed value {}'.format(name, value))

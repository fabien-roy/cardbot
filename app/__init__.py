from discord.ext import commands

from app.games.factories import create_game
from app.sessions.factories import create_session
from app.sessions.models import Session

bot = commands.Bot(command_prefix='$')
session = None


@bot.event
async def on_ready():
    print(f'Cardbot has connected to Discord!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def new_game(ctx, arg):
    global session
    session = Session(arg)
    await ctx.send('Beginning a new game!')


@bot.command()
async def add_me(ctx):
    session.add_user(ctx.message.author.name)
    await ctx.send('Added {}'.format(ctx.message.author.name))


@bot.command()
async def draw(ctx):
    await ctx.send('Drawing for {}'.format(ctx.message.author.name))

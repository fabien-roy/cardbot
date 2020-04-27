import inject
from discord.ext import commands

from app.bindings import config

bot = commands.Bot(command_prefix='$')

inject.configure(config)

# TODO : Fix injector
from app.ui.commands import register_commands
from app.ui.error_handler import register_error_handlers

register_commands(bot)
register_error_handlers(bot)


@bot.event
async def on_ready():
    print('Cardbot has connected to Discord!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

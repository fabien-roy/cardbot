from discord.ext import commands

from app.bindings import session_service
from app.error_handler import register_error_handler
from app.messages import print_players_message, draw_message
from app.sessions.ui.commands import register_sessions_commands

bot = commands.Bot(command_prefix='$')
register_error_handler(bot)

register_sessions_commands(bot)

@bot.event
async def on_ready():
    print(f'Cardbot has connected to Discord!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

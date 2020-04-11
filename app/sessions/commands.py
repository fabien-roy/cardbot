from injector import inject

from app import bot
from app.sessions.services import SessionService


@bot.command()
async def new_game(session_service: SessionService, ctx, arg):
    game_type = session_service.new_game(arg)
    await ctx.send('Beginning a new game of {}!'.format(game_type))


@bot.command()
async def add_me(session_service: SessionService, ctx):
    name = session_service.add_user(ctx.message.author.name)
    await ctx.send('Added {}'.format(name))


@bot.command()
async def draw(session_service: SessionService, ctx):
    name, value = session_service.draw(ctx.message.author.name)
    await ctx.send('{} drawed value {}'.format(name, value))


class SessionCommand:
    @inject
    def __init__(self, session_service: SessionService):
        self.session_service = session_service

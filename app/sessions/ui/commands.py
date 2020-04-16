import inject

from app.sessions.services.session_services import SessionService
from app.sessions.ui.messages import print_players_message, draw_message, add_player_message, \
    add_players_message, remove_player_message, remove_players_message, new_game_message


session_service = inject.instance(SessionService)


def register_sessions_commands(bot):
    @bot.command()
    async def new_game(ctx, game_type, *names):
        game_type = session_service.new_game(game_type)
        await ctx.send(new_game_message(game_type))

        if len(names[0]) > 0:
            await add_players(ctx, names)

    @bot.command()
    async def add_me(ctx):
        added_name = session_service.add_user(ctx.message.author.name)
        await ctx.send(add_player_message(added_name))

    @bot.command()
    async def add_player(ctx, name):
        added_name = session_service.add_user(name)
        await ctx.send(add_player_message(added_name))

    @bot.command()
    async def add_players(ctx, *names):
        added_names = session_service.add_users(names[0])
        await ctx.send(add_players_message(added_names))

    @bot.command()
    async def remove_me(ctx):
        removed_name = session_service.remove_user(ctx.message.author.name)
        await ctx.send(remove_player_message(removed_name))

    @bot.command()
    async def remove_player(ctx, name):
        removed_name = session_service.remove_user(name)
        await ctx.send(remove_player_message(removed_name))

    @bot.command()
    async def remove_players(ctx, *names):
        removed_names = session_service.remove_users(names[0])
        await ctx.send(remove_players_message(removed_names))

    @bot.command()
    async def print_players(ctx):
        players = session_service.get_players()
        await ctx.send(print_players_message(players))

    @bot.command()
    async def draw(ctx):
        name, result = session_service.draw()
        await ctx.send(draw_message(name, result))

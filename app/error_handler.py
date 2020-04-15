import traceback
import sys
from discord.ext import commands


# Props to : https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612

from app.sessions.exceptions import SessionNotStartedException, UserNotFoundException


# TODO : One error handler per package
class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if ctx.command.qualified_name == 'new_game':
            if isinstance(error, commands.MissingRequiredArgument):
                # TODO : Missing required argument error handling can be generalized
                # TODO : Have missing game type argument be its own handling
                return await ctx.send('Missing requirement argument : game type (fuck_you)')

        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        if isinstance(error, UserNotFoundException):
            return await ctx.send('User not found!')

        if isinstance(error, SessionNotStartedException):
            return await ctx.send('Session must be started! Try $new_game')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def register_error_handler(bot):
    bot.add_cog(CommandErrorHandler(bot))

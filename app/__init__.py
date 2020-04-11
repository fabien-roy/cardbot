from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print(f'Cardbot has connected to Discord!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

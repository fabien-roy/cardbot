import os


from app import bot

if __name__ == "__main__":
    bot.run(os.environ.get('BOT_TOKEN'))

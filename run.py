import os


from app import bot

if __name__ == "__main__":
    print(f'Starting bot...')

    bot.run(os.environ.get('BOT_TOKEN'))

    print(f'...bot started!')

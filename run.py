import os

from app import bot

if __name__ == "__main__":
    os.environ['BOT_TOKEN'] = 'Njk4MzU2NzM5NjU3MDM5OTY4.XpZp4w.DKyAhsy8h_pH6ifiI-g0k-0PDFs'

    bot.run(os.environ.get('BOT_TOKEN'))

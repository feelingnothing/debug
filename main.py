from _types import Bot
from settings import COGS_DIR, BOT_TOKEN
import os

if __name__ == "__main__":
    bot = Bot()

    for file in list(os.walk(COGS_DIR))[0][-1]:
        if file.endswith('.py'):
            bot.load_extension('cogs.' + file.removesuffix('.py'))

    bot.run(BOT_TOKEN)

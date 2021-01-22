from discord.ext import commands
from datetime import datetime
from _types import Bot


class DebugCog(commands.Cog, name='debug'):
    LOAD_DATE = datetime.now()

    def __init__(self, bot):
        self.bot: Bot = bot


def setup(bot: Bot):
    bot.add_cog(DebugCog(bot))

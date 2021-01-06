from discord.ext import commands
from _types import Bot


class DebugCog(commands.Cog, name='debug'):
    def __init__(self, bot):
        self.bot: Bot = bot
        self.loaddate = self.bot.datetime.now()


def setup(bot: Bot):
    bot.add_cog(DebugCog(bot))

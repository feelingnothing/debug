from settings import BOT_DEFAULT_PREFIXES
from discord.ext import commands
import discord


class Bot(commands.Bot):
    def __init__(self, **options):
        super().__init__(command_prefix=self._get_prefix, **options)

    @staticmethod
    def _get_prefix(bot: 'Bot', message: discord.Message) -> iter:
        """Returns predefined prefixes
        :param bot:
        :param message:"""
        return BOT_DEFAULT_PREFIXES

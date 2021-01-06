from settings import BOT_DEFAULT_PREFIXES
from discord.ext import commands
from datetime import datetime
import discord


class Bot(commands.Bot):
    def __init__(self, **options):
        super().__init__(command_prefix=self._get_prefix, **options)

    @property
    def datetime(self):
        return datetime

    @staticmethod
    def _get_prefix(bot: 'Bot', message: discord.Message):
        return BOT_DEFAULT_PREFIXES

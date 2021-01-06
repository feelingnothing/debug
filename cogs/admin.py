from discord.ext import commands
from _types import Bot
from datetime import datetime
import discord


class AdminCog(commands.Cog, name='admin'):
    def __init__(self, bot):
        self.bot: Bot = bot
        self.loaddate: datetime = self.bot.datetime.now()

    @commands.group('cogs', invoke_without_command=True)
    async def _cogs(self, ctx: commands.Context):
        await self._cogs_list(ctx)

    @_cogs.command('list')
    async def _cogs_list(self, ctx: commands.Context):
        embed = discord.Embed(title='Cogs List', color=0x2F3136)
        for cog in map(lambda x: self.bot.get_cog(x), self.bot.cogs):
            data = cog.loaddate.date(), cog.loaddate.time(), self.bot.datetime.now() - cog.loaddate
            embed.add_field(name="{}".format(cog.__class__.__name__),
                            value="Load Date: {}\nLoad Time: {}\nLoaded For: {}".format(*data))
        await ctx.send(embed=embed)

    @_cogs.group('reload', invoke_without_command=True)
    async def _cogs_reload(self, ctx: commands.Context, name: str):
        try:
            self.bot.reload_extension('cogs.' + name)
            await ctx.send('Extension successfully reloaded.')
        except commands.ExtensionFailed:
            await ctx.send('Extension failed to reload.')
        except commands.ExtensionNotFound:
            await ctx.send('Extension not found.')
        except commands.ExtensionNotLoaded:
            message = await ctx.send('Extension not loaded, loading...')
            try:
                self.bot.load_extension('cogs.' + name)
                await message.edit(content='Extension successfully loaded.')
            except commands.ExtensionFailed:
                await message.edit(content='Extension failed to load.')

    @_cogs_reload.command('all')
    async def _cog_reload_all(self, ctx: commands.Context):
        async def empty(_):
            pass

        ctx.send = empty
        for cog_name in self.bot.cogs.copy():
            await self._cogs_reload(ctx, self.bot.get_cog(cog_name).qualified_name)


def setup(bot: Bot):
    bot.add_cog(AdminCog(bot))

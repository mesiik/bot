from .base import MetaBase
from ...objects.commands import Feature
from discord.utils import format_dt
from psutil import Process
from os import getpid
from pkg_resources import get_distribution
from platform import python_version

class About(MetaBase):
    
    @Feature(name = 'about', aliases = ['botinfo', 'stats', 'botstats'])
    async def _about(self, ctx):
        """
        flex
        """
        embed = ctx.bot.Embed()

        uptime = format_dt(ctx.bot.uptime, "R")
        users = sum(g.member_count for g in self.bot.guilds)
        commands = len(list(ctx.bot.walk_commands()))
        p = Process(getpid())
        memory = p.memory_full_info().rss / 1024 ** 2
        memory = p.memory_full_info().uss / 1024 ** 2
        pythonv = python_version()
        dpy = get_distribution('discord.py').version
        fmt = f"Currently in `{len(ctx.bot.guilds)}` guilds with `{users:,}` users."

        embed.add_field(
            name = '\u200b',
            value = f"**Uptime:** {uptime}\n**RAM:** {memory:.2f}MB\n**Commands:** {commands}\n**Python:** {pythonv}\n**Discord.py:** {dpy}",
            inline=False
        )
        embed.description = f"{fmt}"
        embed.from_context(ctx)

        await ctx.reply( embed=embed )
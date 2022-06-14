from .ping import Ping
from .about import About
from ...objects.bot import CommandClient as CC


class Meta(Ping, About):
    pass


async def setup(bot : CC):
    await bot.add_cog(Meta(bot))
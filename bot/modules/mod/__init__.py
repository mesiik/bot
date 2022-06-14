from ...objects.bot import CommandClient
from .kick import Kick
from .prefix import Prefix


class Moderator(Kick, Prefix):
    pass


async def setup(bot: CommandClient):
    await bot.add_cog(Moderator(bot))
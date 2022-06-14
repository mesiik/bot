from .eval import EvalCommand
from .do import DoCommand
from ...objects.bot import CommandClient as CC

class Admin(DoCommand, EvalCommand):
    pass


async def setup(bot : CC):
    await bot.add_cog(Admin(bot))
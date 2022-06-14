from .base import OwnerBase
from ...objects.commands import Feature
from discord.ext.commands import is_owner
from copy import copy

class DoCommand(OwnerBase):

    
    @is_owner()
    @Feature(name = 'do', aliases = ['repeat'])
    async def _do(self, ctx, times: int, *, command):
        '''
        Repeat command `x` times.
        '''
        try:
            message = copy(ctx.message)
            message.content = ctx.prefix + command

            new_ctx = await self.bot.get_context(message, cls=type(ctx))
            for _ in range(times):
                await new_ctx.reinvoke()
        except:
            return

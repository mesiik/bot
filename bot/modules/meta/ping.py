from .base import MetaBase
from ...objects.commands import Feature
from ...objects.context import Context


class Ping(MetaBase):

    @Feature(name = 'ping')
    async def _ping(self, ctx : Context):
        '''
        pong
        '''
        message_to_edit = await ctx.say("Pinging...")
        time_took = (message_to_edit.created_at-ctx.message.created_at).total_seconds() * 1000
        latency = ctx.bot.latency*1000
        format = f'🏓 **Pong!** WS: `{latency:.2f}ms` REST: `{time_took/2:.2f}ms`'

        return await message_to_edit.edit(content=format)
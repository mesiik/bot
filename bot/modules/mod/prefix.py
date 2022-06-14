from ...objects.commands import Feature
from .base import ModeratorBase
from discord.ext.commands import has_permissions
from typing import Optional

class Prefix(ModeratorBase):

    @Feature(name = 'prefix')
    @has_permissions(manage_guild = True)
    async def _prefix(self, ctx, prefix : Optional[str]):
        current_prefix = await ctx.get_prefixes()
        if not prefix:
            
            return await ctx.say(f'current prefix for {ctx.guild.name} is {current_prefix}.')

        if prefix == current_prefix:
            return await ctx.say('I already have this prefix registered.')
            
        req = await ctx.update_prefixes(prefix)
        if req == 200:
            return await ctx.say(f'changed prefix to {prefix}.')
        else:
            return await ctx.say('well, dev skill issue.')

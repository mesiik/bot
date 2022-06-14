from .base import ModeratorBase
from discord.ext.commands import has_permissions, bot_has_permissions
from discord import Member, HTTPException
from typing import Optional
from ...objects.commands import Feature


class Kick(ModeratorBase):

    @Feature(name = 'kick')
    @has_permissions( kick_members = True )
    @bot_has_permissions( kick_members = True )
    async def _kick(self, ctx, member: Member, *, reason : Optional[str]):
        if not reason:
            reason = f'not provided ~ {ctx.author.name}.'
        
        if await self.check(ctx, member):
            return
        
        try:
            await member.kick(reason=reason)
        except (HTTPException) as error:
            return await ctx.say(str(error))


    async def check(self, ctx, member : Member):
        
        if member == ctx.author:
            return await ctx.say(f"You can't {ctx.command.name} yourself.")


        if member.id == ctx.bot.user.id:
            return await ctx.say("one question, why?")


        if ctx.author.id == ctx.guild.owner.id:
            return False


        if member.id == ctx.guild.owner.id:
            return await ctx.say("You can't manage server owner.")


        if ctx.author.top_role == member.top_role:
            return await ctx.say(f"This member has the same role as you.")


        if ctx.author.top_role < member.top_role:
            return await ctx.say("This member has higher role than you.")


        if member.top_role > ctx.me.top_role or member.top_role == ctx.me.top_role:
            return await ctx.say('I can\'t manage this member.')
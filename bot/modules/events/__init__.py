from ...objects.commands import Module
from ...objects.context import Context
from discord import HTTPException, NotFound
from discord.ext.commands import CommandNotFound, NotOwner, CheckFailure, MissingPermissions, MissingRequiredArgument, BadArgument, UserInputError, BotMissingPermissions, CommandOnCooldown, DisabledCommand


class Events(Module):
    def __init__(self, bot):
        self.bot = bot


    @Module.listener('on_command_error')
    async def handler(self, ctx:Context, error:Exception):
        ignored = (CommandNotFound, NotOwner, CheckFailure)
        send_help_errors = (MissingRequiredArgument, BadArgument, UserInputError)

        if isinstance(error, ignored):
            return

        elif isinstance(error, send_help_errors):
            helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(ctx.command)
            try:
                await ctx.message.add_reaction("❔")
            except (HTTPException, NotFound):
                pass
            return await ctx.send_help(helper)

        elif isinstance(error, MissingPermissions):
            return await ctx.send(f"You don't have {', '.join('`'+str(error.missing_permissions)+'`').replace('_', '.')} permission(s)")

        elif isinstance(error, BotMissingPermissions):
            return await  ctx.send(f"I'am missing permissions.")

        elif isinstance(error, CommandOnCooldown):
            return await ctx.send(f'try after `{error.retry_after:.2f}` second(s)')

        elif isinstance(error, DisabledCommand):
            return await  ctx.send(f"This command is disabled")

        else:
            await ctx.send(error)

    @Module.listener('on_command_completion')
    async def when_command_is_completed(self, ctx):
        try:
            await ctx.message.add_reaction('✅')
        except HTTPException:
            pass

async def setup(bot):
    await bot.add_cog(Events(bot))
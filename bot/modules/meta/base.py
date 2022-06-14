from ...objects.commands import Module
from discord.ext.commands import DefaultHelpCommand


class Help(DefaultHelpCommand):
    async def send_bot_help(self, mapping):
        ctx = self.context
        cogs = [c for c in ctx.bot.cogs.keys()]
        cog_objects = [ctx.bot.get_cog(c) for c in cogs]
        embed = ctx.bot.Embed()
        for cog in cog_objects:
            if cog.qualified_name == "Jishaku":
                continue
            if hasattr(cog, 'hidden'):
                if cog.hidden:
                    continue
            commands = cog.get_commands()
            if not commands == list():

                if hasattr(cog, 'icon'):
                    name = f"{cog.icon} {cog.qualified_name}"
                else:
                    name = f"{cog.qualified_name}"

                embed.add_field(
                    name = name,
                    value = ", ".join(map(lambda command_name: f"`{command_name}`", commands)),
                    inline = False
                )
        

        embed.color = 0x181818
        embed.from_context(ctx)
        return await ctx.say( embed = embed )


class MetaBase(Module):
    def __init__(self, bot):
        self.bot = bot
        bot.help_command = Help()
        bot.help_command.cog = self
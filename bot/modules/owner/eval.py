from ...objects.commands import Feature
from .base import OwnerBase
from jishaku.codeblocks import codeblock_converter

class EvalCommand(OwnerBase):
    @Feature(name = 'eval')
    async def _eval(self, ctx, *, code: codeblock_converter):
        '''
        Shortcut for `jishaku python`.
        '''
        jishaku = ctx.bot.get_command('jishaku python')
        await ctx.invoke(jishaku, argument=code)

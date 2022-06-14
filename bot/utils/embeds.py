from discord import Embed


class BotEmbed(Embed):
    '''
    WIP
    '''
    def from_context(self, ctx, set_author : bool = True):
        if set_author:
            self.set_author(name = ctx.author.display_name, icon_url = ctx.author.display_avatar)
        return self

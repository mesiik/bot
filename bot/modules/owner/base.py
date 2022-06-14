from ...objects.commands import Module


class OwnerBase(Module):
    def __init__(self, bot):
        self.bot = bot
        self.hidden = True
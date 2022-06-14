from ...objects.commands import Module
from ...objects.bot import CommandClient

class ModeratorBase(Module):
    def __init__(self, bot: CommandClient):
        self.bot = bot


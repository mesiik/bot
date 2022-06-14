from __future__ import annotations
import logging
from typing import Optional, Union
import discord
from discord.ext.commands import Context as DisContext
log = logging.getLogger(__name__)
from ..utils import AsyncDatabase


class Context(DisContext):
    message: discord.Message
    guild: Optional[discord.Guild]
    author: Union[discord.Member, discord.User]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = self.bot.db
        self.bot.say = self.send
        self.bot.whisper = self.author.send

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:{self.bot}>"


    def get(*args):
        return discord.utils.get(args)


    async def update_prefixes(self, prefix : str):
        await self.db.run('UPDATE prefixes SET prefix = ? WHERE guild_id = ?', (prefix, self.guild.id,))
        return 200

    async def get_prefixes(self):
        data = await self.db.fetchrow('SELECT prefix FROM prefixes WHERE guild_id = ?', (self.guild.id,))
        prefix = data.get('prefix')
        return str(prefix)


    async def say(
        self, *args, channel: discord.abc.Messageable = None, no_reply: bool = False, **kwargs
    ) -> discord.Message:
        if not channel:
            channel = self.channel

        if "reference" not in kwargs and not no_reply:
            kwargs["reference"] = self.message.to_reference(fail_if_not_exists=False)

        return await channel.send(*args, **kwargs)
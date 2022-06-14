import os
import aiohttp
from datetime import datetime
from datetime import timedelta
from .context import Context
from discord.ext.commands import AutoShardedBot as AB, DefaultHelpCommand
from discord import Intents, AllowedMentions, Message, MemberCacheFlags, Embed
from ..data import config
import logging
import jishaku
from ..utils import setup_logging, BotEmbed, AsyncDatabase, get_prefixes

setup_logging()
log = logging.getLogger(__name__)
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"
os.environ["JISHAKU_RETAIN"] = "True"

 
class CommandClient(AB):
    def __init__(self, *args, **kwargs):
        super().__init__(
            description='a discord bot',
            command_prefix=get_prefixes,
            case_insensitive=True,
            strip_after_prefix = True,
            allowed_mentions=AllowedMentions.none(),
            intents=Intents.all(),
            member_cache_flags=MemberCacheFlags(
                joined=True, 
                voice=True
                ),
                owner_ids=config.get('owners'),
                enable_debug_events=True,
                *args, **kwargs
        )
        self.db = AsyncDatabase('bot/data/data.db')
        self.Embed = BotEmbed
        self.uptime = datetime.utcnow()
        self.session = aiohttp.ClientSession()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


    async def get_context(self, message, *, cls=Context):
        return await super().get_context(message, cls=cls)

    async def load_extensions(self, *extensions):
        for extension in extensions:
            await self.load_extension(extension)


    async def on_message_edit(self, before: Message, after: Message):
        if before.content == after.content:
            return

        if not after.edited_at:
            return

        if after.edited_at - after.created_at > timedelta(minutes=1):
            return

        await self.process_commands(after)


    @property
    def sudo(self):
        return self.get_user(563718132863074324)


    @staticmethod
    async def on_connect():
        log.info(f"Starting Client in directory: {os.path.dirname(os.path.abspath(__file__))}")
        log.info("Attempting to start")


    async def on_ready(self):
        log.info(f"Connected to discord API")


    async def on_shard_ready(self, shard_id):
        log.info(f"Created shard #{shard_id}")


    async def load(self):
        for fil in os.listdir("./bot/modules"):
            if not fil.startswith("__"):
                try:
                    await self.load_extension(f"bot.modules.{fil}")
                    log.info(f"Loaded plugin {fil}")
                except Exception as e:
                    log.info(f"Unable to load: {fil}... {e}")

    async def bot_logout(self):
        await super().logout()
        await self.session.close()


    async def run_async(self):
        await self.login(config.get("token"))
        await self.load_extension('jishaku')
        await self.load()
        await self.connect()


    def get_message(self, message_id: int) -> Message:
        return self._connection._get_message(message_id)

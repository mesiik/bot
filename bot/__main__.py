import asyncio
from .objects.bot import CommandClient

async def __run__():
    async with CommandClient() as bot:
        await bot.run_async()

if __name__ == '__main__':
    asyncio.run(__run__())
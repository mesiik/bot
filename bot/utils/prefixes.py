from .database import AsyncDatabase
from ..data import config

db = AsyncDatabase('bot/data/data.db')

async def get_prefixes(bot, message):
    base = [f'<@!{bot.user.id}>', f'<@{bot.user.id}>']
    
    if not message.guild:
        return base
    
    data = await db.fetchrow('SELECT prefix FROM prefixes WHERE guild_id = ?', (message.guild.id,))
    if data is None:
        await db.run('INSERT INTO prefixes (guild_id, prefix) VALUES (?, ?)', (message.guild.id, str(config.get('prefix')),))
        
        return base
    
    base.append(data.get('prefix'))
    return base
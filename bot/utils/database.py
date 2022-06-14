# W           W    I    PPPPPP
# W           W    I    P     P
# W     W     W    I    P     P
#  W   W W   W     I    PPPPPP
#   W W   W W      I    P
#    W     W       I    P

import aiosqlite
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for index, col in enumerate(cursor.description):
        d[col[0]] = row[index]
    return d

class AsyncDatabase:
    def __init__(self, path = 'bot/data/data.db'):
        self.path = path

    async def run(self, sql: str, prepared: tuple = ()):
        async with aiosqlite.connect(self.path, isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES) as db:
            db.row_factory = dict_factory
            async with db.execute(sql, prepared) as data:
                status_word = sql.split(' ')[0].upper()
                status_code = data.rowcount if data.rowcount > 0 else 0
                if status_word == "SELECT":
                    status_code = len(await data.fetchall())
                return f"{status_word} {status_code}"


    async def fetch(self, sql: str, prepared: tuple = ()):
        async with aiosqlite.connect(self.path, isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES) as db:
            db.row_factory = dict_factory
            async with db.execute(sql, prepared) as data:
                return await data.fetchall()


    async def fetchrow(self, sql: str, prepared: tuple = ()):
        async with aiosqlite.connect(self.path, isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES) as db:
            db.row_factory = dict_factory
            async with db.execute(sql, prepared) as data:
                return await data.fetchone()
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.handlers import router
#from app.database.models import async_main
from config import TOKEN

from aiogram.client.default import DefaultBotProperties
import sys
import sqlite3
from aiogram import Bot, Dispatcher


bot = Bot(token=TOKEN)
dp = Dispatcher()
#conn = sqlite3.connect('example2.db')
#cursor = conn.cursor()

#cursor.execute('''CREATE TABLE IF NOT EXISTS users (    id INTEGER PRIMARY KEY,    tg_id INTEGER,    username "TEXT NOT NULL",    login "TEXT NOT NULL",    password "TEXT NOT NULL")''')



async def main():
    #await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
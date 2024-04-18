import os
import asyncio
from aiogram import Bot,Dispatcher,types
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from icecream import ic
from bot.Handlers.handlers import list_handlers
from bot.SQL.sql_func import create_first_db

load_dotenv(".env")
stor=MemoryStorage()
bot=Bot(os.getenv("api_token"))
dp=Dispatcher(bot=bot,storage=MemoryStorage())






  
  
  
  
async def register_handlers(dp: Dispatcher):
    for part in list_handlers:
       await part(dp)
    
async def main():
    await register_handlers(dp)
    
    try:
      await dp.start_polling()
      await create_first_db()
    except Exception as _ex:
        ic("{:>8}, this is error!!".format(_ex))
    


if __name__=="__main__":
    asyncio.run(main())
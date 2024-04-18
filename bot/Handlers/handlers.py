from aiogram import Dispatcher,types
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher.filters import Text


check_interest=lambda message:(message.text).lower()=="парни" or (message.text).lower()=="девушки" or (message.text).lower()=="всё равно"


async def register_handler_greeting(dp:Dispatcher)->None:
    from bot.Functions.functions import greeting
    dp.register_message_handler(greeting,commands=["start"])

async def register_handler_load_name(dp:Dispatcher)->None:
    from bot.Functions.functions import Profile,load_name
    dp.register_message_handler(load_name,state=Profile.name)
    
async def register_handler_load_age(dp:Dispatcher)->None:
    from bot.Functions.functions import Profile,load_age
    dp.register_message_handler(load_age,state=Profile.age)

async def register_hanlder_load_photo(dp:Dispatcher)->None:
    from bot.Functions.functions import Profile,load_photo
    dp.register_message_handler(load_photo,content_types=["photo"],state=Profile.photo)

async def register_handler_check_photo(dp:Dispatcher)->None:
    from bot.Functions.functions import Profile,check_photo
    dp.register_message_handler(check_photo,lambda message:not (message.photo),state=Profile.photo)
    
    

async def register_handler_load_sex(dp:Dispatcher)->None:
    from bot.Functions.functions import Profile,load_sex
    dp.register_message_handler(load_sex,lambda message:((message.text)=="Я девушка" or (message.text)=="Я парень"),state=Profile.sex)

async def register_handler_check_load_sex(dp:Dispatcher)->None:
    from bot.Functions.functions import Profile,check_load_sex
    dp.register_message_handler(check_load_sex,state=Profile.sex)     


async def register_handler_load_interest(dp:Dispatcher)->None:
    from bot.Functions.functions import Profile,load_interest
    dp.register_message_handler(load_interest,check_interest,state=Profile.interest)

async def register_handler_check_load_interest(dp:Dispatcher)->None:
    from bot.Functions.functions import Profile,check_load_interest
    dp.register_message_handler(check_load_interest,state=Profile.interest)


    
async def register_handler_load_city(dp:Dispatcher)->None:
    from bot.Functions.functions import Profile,load_geolocation
    dp.register_message_handler(load_geolocation,state=Profile.city)
    
async def register_handler_load_describe(dp:Dispatcher)->None:
    from bot.Functions.functions import Profile,load_describe
    dp.register_message_handler(load_describe,state=Profile.describe)


    

    
    








list_handlers=[register_handler_greeting,
               register_handler_load_name,
               register_handler_load_age,
               register_hanlder_load_photo,
               register_handler_load_sex,
               register_handler_load_city,
               register_handler_load_interest,
               register_handler_check_load_sex,
               register_handler_check_load_interest,
               register_handler_check_photo,
               register_handler_load_describe,]



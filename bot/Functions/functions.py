from main import bot
from aiogram import Dispatcher,types
from aiogram.dispatcher.filters.state import State,StatesGroup
from bot.Keyboard.keyboards import *
from aiogram.dispatcher import FSMContext
from bot.Keyboard.keyboards import *



#The create button of start
class Profile(StatesGroup):
    name=State()
    age=State()
    photo=State() #with a button "current photo"
    sex=State() #with a button to choose "i am man or girl"
    interest=State()# with a button to choose interesting between girl,men or anyway
    city=State()
    describe=State()
    
    

#Bot for acquintated!!!


async def greeting(message:types.Message)->None:
    await message.answer("Привет, добро пожаловать в Филиал бота Леонардо-Дайвинчик. Начнем знакомство с тобой!\nКак тебя зовут?")
    await Profile.name.set()
   
    
async def load_name(message:types.Message,state:FSMContext)->None:
    await state.update_data(name_text=message.text.lower())
    await message.answer("Сколько тебе лет?")
    await Profile.next()

async def load_age(message:types.Message,state:FSMContext)->None:
    if not (message.text).isnumeric() or float(message.text)>99 or float(message.text)<0:
        await message.reply("Укажите правильный возраст, только цифры")
        return
    await state.update_data(age_text=message.text.lower())
    await message.answer("Пришлите Вашу фотографию!")
    await Profile.next()

async def load_photo(message:types.Message,state:FSMContext)->None:
    
    await state.update_data(photo_text=message.photo[0].file_id)
    await message.answer("Теперь определимся с полом.",reply_markup=keyboard_sex())
    await Profile.next()
    

async def check_photo(message:types.Message,state:FSMContext)->None:
    await message.reply("Пришлите реальную фотографию!!")

async def load_sex(message:types.Message,state:FSMContext)->None:
    
    await state.update_data(sex_text=message.text.lower())
    await message.answer("Кто тебе интересен?",reply_markup=keyboard_interest())
    await Profile.next()
    
# async def check_load_sex(message:types.Message,state:FSMContext)->None:
#     await message.reply("Пользуйтесь встроеннными кнопками!")

async def check_load_sex(message:types.Message,state:FSMContext)->None:
    await message.reply("Пользуйтесь встроенными кнопками!!!",reply_markup=keyboard_sex())
        


async def check_load_interest(message:types.Message,state:FSMContext)->None:
    await message.reply("Пользуйтесь встроенными кнопками!!",reply_markup=keyboard_interest())    


async def load_interest(message:types.Message,state:FSMContext)->None:
    await state.update_data(interes_text=message.text.lower())
    await message.answer("Из какого Вы города?",reply_markup=keyboard_location())
    await Profile.next()


async def load_geolocation(message:types.Message,state:FSMContext)->None:
    await state.update_data(location_text=message.text)
    await message.answer("Расскажите немного о себе")
    await Profile.next()

async def load_describe(message:types.Message,state:FSMContext)->None:
        
        await state.update_data(descr_text=message.text.lower())
        user_data=await state.get_data() #{"..":"..",..."..":".."}
        formated_text=[]
        [
            formated_text.append(f"{key}:{item}")
            for key,item in user_data.items()
        ]    

        
        
        
        await bot.send_photo(chat_id=message.from_user.id,
                               photo=user_data["photo_text"],
                               caption="\n".join(formated_text))
        
        
        await message.answer("Поздравляю, Ваша анкета заполнена!!")
        
        await state.finish()
        
        


    

    





    



        
    



    
    




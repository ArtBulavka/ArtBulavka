import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InputFile

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '2007008934:AAGvBj5PK78pX5OCDCnIwrjAkYSqB6-bLMI'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
button_hi = KeyboardButton('Привет! 👋')
keyboard = types.InlineKeyboardMarkup(row_width=1)
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)
studyboi = InlineKeyboardButton('text')
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(studyboi)


@dp.message_handler(content_types="text")
async def process_hello(message: types.Message):
    photo = InputFile("C:/Users/a.bulavchenkov/Desktop/Pict/CAMEL02.jpg")
    await bot.send_photo(message.from_user.id,photo,caption="Привет!Как картинка?", reply_markup=keyboard)




if __name__== '__main__':
    executor.start_polling(dp, skip_updates=True)

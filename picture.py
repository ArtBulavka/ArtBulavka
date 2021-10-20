import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InputFile

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '2007008934:AAGvBj5PK78pX5OCDCnIwrjAkYSqB6-bLMI'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)





@dp.message_handler(content_types="text")
async def process_hello(message: types.Message):
    
    buttons = [
        types.InlineKeyboardButton(text='hi',callback_data="n"),
        types.InlineKeyboardButton(text='hi2',callback_data="m")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    photo = InputFile("C:/Users/a.bulavchenkov/Desktop/Pict/CAMEL02.jpg")
    await bot.send_photo(message.from_user.id,photo,caption="Привет!Как картинка?", reply_markup=keyboard)


@dp.callback_query_handler(text_contains = "n")
async def callback_data(message: types.CallbackQuery):
        await bot.send_message(message.from_user.id, "❤️")


@dp.callback_query_handler(text_contains = "m")
async def callback_data(message: types.CallbackQuery):
        await bot.send_message(message.from_user.id, "🖤")

if __name__== '__main__':
    executor.start_polling(dp, skip_updates=True)

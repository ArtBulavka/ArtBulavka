import logging


import time
 
from os import waitpid

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from attr import get_run_validators

API_TOKEN = '2007008934:AAGvBj5PK78pX5OCDCnIwrjAkYSqB6-bLMI'

logging.basicConfig(level=logging.INFO) 

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
photo1=("https://moneymakerfactory.ru/Pics/nodecrp/753_1img_n.png")
photo21=("https://back.rapido.ru/storage/uploads/images/nXuWyqzGj5VvArJ53M0xQ0xkA_big.jpg")
photo22=("https://back.rapido.ru/storage/uploads/images/MYfkfDASXKzuiValTMKz49LOP_big.jpg")
photo23=("https://back.rapido.ru/storage/uploads/images/gvzeXPoygfKquSLT4TQrLR5nd_big.jpg")

keyboard = types.InlineKeyboardMarkup(row_width=2)
score=0




@dp.message_handler(content_types="text")
async def process_hello(message: types.Message):
    
    buttons = [
        types.InlineKeyboardButton(text='Да',callback_data="d"),
        types.InlineKeyboardButton(text='Нет',callback_data="n"),
        
    ]
    
    keyboard.add(*buttons)
    
    await bot.send_photo(message.from_user.id,photo1,caption="🍕Хотите сделать заказ?🍕", reply_markup=keyboard)


@dp.callback_query_handler(text_contains = "d")
async def callback_data(message: types. CallbackQuery):
    buttons2 = [
        types.InlineKeyboardButton(text='Классическая',callback_data="a"),
        types.InlineKeyboardButton(text='Неаполитанская',callback_data="b"),
        types.InlineKeyboardButton(text='Пан-пицца',callback_data="c"),
        types.InlineKeyboardButton(text='В чём разница?',callback_data="z"),
        types.InlineKeyboardButton(text='Назад',callback_data="j")
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=1)
    keyboard2.add(*buttons2)
    await bot.send_message(message.from_user.id, "🍕Выберите вид пиццы🍕",reply_markup=keyboard2)

@dp.callback_query_handler(text_contains = "j")
async def callback_data(message: types.CallbackQuery):
    await bot.send_photo(message.from_user.id,photo1,caption="🍕Хотите сделать заказ?🍕", reply_markup=keyboard)

@dp.callback_query_handler(text_contains = "z")
async def callback_data(message: types.CallbackQuery):
    buttons3 = [
        types.InlineKeyboardButton(text='Назад',callback_data="d")
    ]
    keyboard3 = types.InlineKeyboardMarkup(row_width=1)
    keyboard3.add(*buttons3)
    await bot.send_message(message.from_user.id, "Классическая пицца делается на тонком тесте. Неаполитанская меньшая по диаметру и обычно с более высокими бортами. Пан-пицца - это пицца на противне, приготовленная по хлебной технологии, ее отличает высокое тесто и мелкопористый мякиш.",reply_markup=keyboard3)

@dp.callback_query_handler(text_contains = "n")
async def callback_data(message: types.CallbackQuery):
    buttons4 = [
        types.InlineKeyboardButton(text='Я передумал(а)',callback_data="j")
    ]
    keyboard4 = types.InlineKeyboardMarkup(row_width=1)
    keyboard4.add(*buttons4)
    await bot.send_message(message.from_user.id, "Ну и катись отсюда",reply_markup=keyboard4)

@dp.callback_query_handler(text_contains = "a")
async def callback_data(message: types.CallbackQuery):
    
    buttons21 = [
        types.InlineKeyboardButton(text='Маргарита',callback_data="m")
    ]
    keyboard21 = types.InlineKeyboardMarkup(row_width=1)
    keyboard21.add(*buttons21)
    await bot.send_photo(message.from_user.id,photo21,reply_markup=keyboard21)
    buttons22 = [
        types.InlineKeyboardButton(text='Грибная с ветчиной',callback_data="gv")
    ]
    keyboard22 = types.InlineKeyboardMarkup(row_width=1)
    keyboard22.add(*buttons22)
    await bot.send_photo(message.from_user.id,photo22,reply_markup=keyboard22)
    buttons23 = [
        types.InlineKeyboardButton(text='C ветчиной',callback_data="v"),
        types.InlineKeyboardButton(text='Назад',callback_data="d")
    
    ]
    keyboard23 = types.InlineKeyboardMarkup(row_width=1)
    keyboard23.add(*buttons23)
    await bot.send_photo(message.from_user.id,photo23,reply_markup=keyboard23)

@dp.callback_query_handler(text_contains = "m")
async def callback_data(message: types.CallbackQuery):
    buttons221 =[
        types.InlineKeyboardButton(text='В корзину (625 руб)',callback_data="mb"),
        types.InlineKeyboardButton(text='Состав',callback_data="sostav11"),
        types.InlineKeyboardButton(text='Назад',callback_data="a")
    ]
    keyboard221 = types.InlineKeyboardMarkup(row_width=2)
    keyboard221.add(*buttons221)
    await bot.send_photo(message.from_user.id,photo21,caption="Маргарита",reply_markup=keyboard221)

@dp.callback_query_handler(text_contains = "gv")
async def callback_data(message: types.CallbackQuery):
    buttons222 =[
        types.InlineKeyboardButton(text='В корзину (815 руб)',callback_data="gvb"),
        types.InlineKeyboardButton(text='Состав',callback_data="sostav12"),
        types.InlineKeyboardButton(text='Назад',callback_data="a")
    ]
    keyboard222 = types.InlineKeyboardMarkup(row_width=2)
    keyboard222.add(*buttons222)
    await bot.send_photo(message.from_user.id,photo22,caption="Грибная с ветчиной",reply_markup=keyboard222)

@dp.callback_query_handler(text_contains = "v")
async def callback_data(message: types.CallbackQuery):
    buttons223 =[
        types.InlineKeyboardButton(text='В корзину (775 руб)',callback_data="vb"),
        types.InlineKeyboardButton(text='Состав',callback_data="sostav13"),
        types.InlineKeyboardButton(text='Назад',callback_data="a")
    ]
    keyboard223 = types.InlineKeyboardMarkup(row_width=2)
    keyboard223.add(*buttons223)
    await bot.send_photo(message.from_user.id,photo23,caption="С ветчиной",reply_markup=keyboard223)

@dp.callback_query_handler(text_contains = "mb")
async def callback_data(message: types.CallbackQuery):
    await bot.send_message(message.from_user.id,"Хорошо, скоро мы вам её доставим")

@dp.callback_query_handler(text_contains = "gvb")
async def callback_data(message: types.CallbackQuery):
    await bot.send_message(message.from_user.id,"Хорошо, скоро мы вам её доставим")

@dp.callback_query_handler(text_contains = "vb")
async def callback_data(message: types.Message):
    await bot.send_message(message.from_user.id,"Хорошо, скоро мы вам её доставим")

if __name__== '__main__':
    executor.start_polling(dp, skip_updates=True)
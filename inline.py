from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton # импортируем кнопку и клавиатуру

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=1) # инициализируем класс клавиатуры, прописываем ширину ряда, по одной кнопке в ряд
# создаем под каждую кнопку отдельную переменную
# инициализируем класс кнопки, пишем название, которое будет написано на кнопке и ссылку, куда приведет эта кнопка
urlButton = InlineKeyboardButton(text='Ссылка', url='https:/youtube.com') 
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https:/google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https:/google.com'), InlineKeyboardButton(text='Ссылка4', url='https:/google.com'),\
    InlineKeyboardButton(text='Ссылка5', url='https:/google.com')]
urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка6', url='https:/google.com')) # методы такие же, как в обычных кнопках. Добавляем кнопки. Передаем список x, распаковывая его

# Callback-кнопки
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Нажми меня', callback_data='www'))


@dp.message_handler(commands='/ссылки') # пишем хэндлер, чтобы вызвать клавиатуру
async def url_command(message : types.Message):
    await message.answer('Ссылочки:', reply_markup = urlkb) # отвечаем на команду ссылки отправкой клавиатуры


executor.start_polling(dp, skip_updates=True)
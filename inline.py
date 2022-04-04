from subprocess import call
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton # импортируем кнопку и клавиатуру

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

answ = dict()

#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=1) # инициализируем класс клавиатуры, прописываем ширину ряда, по одной кнопке в ряд
# создаем под каждую кнопку отдельную переменную
# инициализируем класс кнопки, пишем название, которое будет написано на кнопке и ссылку, куда приведет эта кнопка
urlButton = InlineKeyboardButton(text='Ссылка', url='https:/youtube.com') 
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https:/google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https:/google.com'), InlineKeyboardButton(text='Ссылка4', url='https:/google.com'),\
    InlineKeyboardButton(text='Ссылка5', url='https:/google.com')]
urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка6', url='https:/google.com')) # методы такие же, как в обычных кнопках. Добавляем кнопки. Передаем список x, распаковывая его

@dp.message_handler(commands='ссылки') # пишем хэндлер, чтобы вызвать клавиатуру
async def url_command(message : types.Message):
    await message.answer('Ссылочки:', reply_markup = urlkb) # отвечаем на команду ссылки отправкой клавиатуры

# Callback-кнопки
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                            InlineKeyboardButton(text='Unlike', callback_data='like_-1'))

@dp.message_handler(commands='test') # пишем хэндлер, чтобы вызвать клавиатуру
async def test_commands(message : types.Message):
    await message.answer('За видео про деплой бота', reply_markup = inkb) # отвечаем на команду ссылки отправкой клавиатуры

@dp.callback_query_handler(Text(startswith='like_')) # один хэндлер может обрабатывать несколько инлайн-кнопок
async def www_call(callback : types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res # по ключу id записываем результат
     # await callback.answer('Нажата онлайн кнопка') # текст отобразится в виде всплывающего окна
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)
# Если бот будет перезапущен, данные из этого словаря не сохранятся

    await callback.message.answer('Нажата онлайн кнопка') # бот отправляет сообщение в чат
    await callback.answer('Нажата онлайн кнопка',show_alert=True) #отправляется сообщение, которое необходимо подтвердить

executor.start_polling(dp, skip_updates=True)
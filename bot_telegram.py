from aiogram import Bot, types # импортируем класс бота, типы данных
from aiogram.dispatcher import Dispatcher # импортируем класс, который улавливает события в чате
from aiogram.utils import executor # для запуска бота, чтобы он вышел в онлайн

import os # для того, чтобы мы смогли прочитать токен из среды окружения


bot = Bot(token=os.getenv('TOKEN')) # инициализируем бота
dp = Dispatcher(bot) # инициализируем Dispatcher

async def on_startup(_): # пишем функцию, которая запускается при выходе бота в онлайн(без декоратора) 
    print('Бот вышел в онлайн') # далее, ниже передаем эту функцию в executor, функция выводит сообщение в консоль
#********************************************КЛИЕНТСКАЯ ЧАСТЬ********************************************#
@dp.message_handler(commands = ['start', 'help']) # указываем декоратор и в аргументах указываем команды, на которые будет реагировать нащ бот
# сработает, когда пользователь напишет команду /start либо команду /help. Handler сработает как только пользователь добавится к нашему боту
async def echo_send(message : types.Message):
    try: # обрабатываеи ошибку (если не получится отправить сообщение пользователю - если он не добавил бота)
        await bot.send_message(message.from_user.id, 'Приятного аппетита') # записываем код, который сработает после команды /start либо команды /help.
        await message.delete() # будем удалять сообщение, если оно не доставлено
    except: # не будем указывать конкретную ошибку
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_arumarov_bot') # данное условие выполнится, если пользователь еще не добавлялся к боту
# добавляем далее все необходимые нам обработчики команд
@dp.message_handler(commands = ['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

@dp.message_handler(commands = ['Расположение'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15')


# @dp.message_handler(commands = ['Меню'])
# async def pizza_menu_command(message : types.Message):
#     for ret in cur.execute('SELECT * FROM menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

# отправляем пользователю в личку сообщение и клавиатуру


#********************************************АДМИНСКАЯ ЧАСТЬ********************************************#

#********************************************ОБЩАЯ ЧАСТЬ********************************************#

@dp.message_handler()# записываем первую функцию сюда будет попадать пустой декоратор, когда в наш чат кто-то что-то пишет
async def echo_send(message : types.Message): # указываем асинхронную функцию, в которую будут попадать любые текстовые сообщения для бота
    

    
    
    
    # Пример с 1-го урока:
    # if message.text == 'Привет':
    #     await message.answer('И тебе привет')
    # await message.answer(message.text) # отправляем сообщение ботом, await - ждет, чтобы появилось свободное место для выполнения команды. В скобках передаем то, что хотим отправить обратно
    # await message.reply(message.text) # также ответ пользователю от бота
    # await bot.send_message(message.from_user.id, message.text) # третий вариант, позволяет отправить сообщение в личку пользователю, сработает только если пользователь уже когда-либо писал боту, или первый добавился к нему в контакты, указываем ID пользователя


executor.start_polling(dp, skip_updates = True, on_startup = on_startup) # записываем команду запуска бота
# skip_updates = True - команда, чтобы бот не отвечал на сообщения, которые приходят, пока бот офлайн


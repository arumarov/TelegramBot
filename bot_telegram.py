from aiogram import Bot, types # импортируем класс бота, типы данных
from aiogram.dispatcher import Dispatcher # импортируем класс, который улавливает события в чате
from aiogram.utils import executor # для запуска бота, чтобы он вышел в онлайн

import os # для того, чтобы мы смогли прочитать токен из среды окружения


bot = Bot(token=os.getenv('TOKEN')) # инициализируем бота
dp = Dispatcher(bot) # инициализируем Dispatcher

@dp.message_handler()# записываем первую функцию сюда будет попадать пустой декоратор, когда в наш чат кто-то что-то пишет
async def echo_send(message : types.Message): # указываем асинхронную функцию, в которую будут попадать любые текстовые сообщения для бота
    await message.answer(message.text) # отправляем сообщение ботом, await - ждет, чтобы появилось свободное место для выполнения команды. В скобках передаем то, что хотим отправить обратно

executor.start_polling(dp, skip_updates = True) # записываем команду запуска бота
# skip_updates = True - команда, чтобы бот не отвечал на сообщения, которые приходят, пока бот офлайн
from aiogram.utils import executor # для запуска бота, чтобы он вышел в онлайн
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_): # пишем функцию, которая запускается при выходе бота в онлайн(без декоратора) 
    print('Бот вышел в онлайн')  # далее, ниже передаем эту функцию в executor, функция выводит сообщение в консоль
    sqlite_db.sql_start() # при старте бота запускаем функцию подключения/ создания базы данных

from handlers import client, admin, other # импортируем файлы

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates = True, on_startup = on_startup) # записываем команду запуска бота
# skip_updates = True - команда, чтобы бот не отвечал на сообщения, которые приходят, пока бот офлайн
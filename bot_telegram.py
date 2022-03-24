from aiogram.utils import executor # для запуска бота, чтобы он вышел в онлайн
from create_bot import dp

async def on_startup(_): # пишем функцию, которая запускается при выходе бота в онлайн(без декоратора) 
    print('Бот вышел в онлайн') # далее, ниже передаем эту функцию в executor, функция выводит сообщение в консоль

executor.start_polling(dp, skip_updates = True, on_startup = on_startup) # записываем команду запуска бота
# skip_updates = True - команда, чтобы бот не отвечал на сообщения, которые приходят, пока бот офлайн
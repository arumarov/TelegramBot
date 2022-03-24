from aiogram import Bot # импортируем класс бота, типы данных
from aiogram.dispatcher import Dispatcher # импортируем класс, который улавливает события в чате
import os # os -для того, чтобы мы смогли прочитать токен из среды окружения, 

bot = Bot(token=os.getenv('TOKEN')) # инициализируем бота
dp = Dispatcher(bot) # инициализируем Dispatcher
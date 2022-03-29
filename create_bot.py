from aiogram import Bot # импортируем класс бота, типы данных
from aiogram.dispatcher import Dispatcher # импортируем класс, который улавливает события в чате
import os # os -для того, чтобы мы смогли прочитать токен из среды окружения, 
from aiogram.contrib.fsm_storage.memory import MemoryStorage # указываем хранилище, в котором бот будет хранить данные, указанные админом (в оперативной памяти)
# Если нужно запоминать действия пользователя с очень важной инфой (например какая либо покупка либо банковские данные), то
# необходимо использовать какое либо из файловых хранилищ (radis или mongo), так при выходе бота в офлайн данные не потеряются

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN')) # инициализируем бота
dp = Dispatcher(bot, storage=storage) # инициализируем Dispatcher
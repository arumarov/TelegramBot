from aiogram import Bot, types # импортируем класс бота, типы данных
from aiogram.dispatcher import Dispatcher # импортируем класс, который улавливает события в чате
from aiogram.utils import executor # для запуска бота, чтобы он вышел в онлайн

import os # для того, чтобы мы смогли прочитать токен из среды окружения
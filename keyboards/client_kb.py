from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы') # создание каждой отдельной кнопки
b2 = KeyboardButton('/Расположение') # данные кнопки отправляют четко то, что в них написано
b3 = KeyboardButton('/Меню')
# кнопки исключения (отправляют не то, что в них написано)
# b4 = KeyboardButton('Поделиться номером', request_contact=True)# текст можно написать любой, отправляет номер телефона
# b5 = KeyboardButton('Отправить где я', request_location=True)# отправляет свое расположение

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) # этот класс замещает обычную клавиатуру на ту, которую мы создаем
# kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) one_time_keyboard удаляет клавиатуру после нажатия
# с помощью resize_keyboard изменяем размер кнопок
# с помощью one_time_keyboard убираем клавиатуру с экрана после нажатия кнопки

kb_client.add(b1).add(b2).add(b3) # добавляем наши кнопки
# kb_client.add(b1).add(b2).add(b3) метод add добавляет каждую кнопку с новой строки
# kb_client.add(b1).add(b2).insert(b3) метод insert добавляет кнопку на той же строке, если позволит место
# kb_client.row(b1, b2, b3) метод row добавляет все кнопки в строку
# все методы можно компоновать как удобно
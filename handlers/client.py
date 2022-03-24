from aiogram import types # импортируем типы данных


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
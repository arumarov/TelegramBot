from aiogram import types # импортируем типы данных

@dp.message_handler()# записываем первую функцию сюда будет попадать пустой декоратор, когда в наш чат кто-то что-то пишет
async def echo_send(message : types.Message): # указываем асинхронную функцию, в которую будут попадать любые текстовые сообщения для бота
    # так как сюда попадают все сообщения, необходимо выполнить проверку, указываем генератор множеств (множества работают быстро)
    # указываем цикл - берем сообщение, отправленное пользователем, берем из него текст, разбиваем его по разделителю
    # переводим все в нижний регистр, используем метод translate, в который передаем макет для замены символов в строке
    # первый аргумент - что менять(''), второй аргумент - на что менять(''), третий аргумент - указывает, какие символы из строки нужно убрать, перечислять не будем, возьмем из модуля string, там есть готовый перечень всех знаков пунктуации
    # итого - получаем сообщение, разбиваем его по разделителю, получаем список слов, проходимся циклом и обрабатываем каждое слово, приводим к нижнему регистру, убираем маскирующие символы и получаем множество из чистых слов (всех отправленных пользователем в нашу группу)
    # реализуем проверку - есть ли в сообщении, отправленном пользователем слова, перечисленные в cenz.json
    # intersection позволяет быстро сравнить, есть совпадения или нет - формируем новое множество, читая данные из json файла
    # load позволяет прочитать данные из файла, в него передаем объект чтения
    # если в результате проверки нет мата, она возвращает пересечение множеств
    # если множество не пустое, значит в сообщении был мат
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены') # отвечаем матерщиннику
        await message.delete() # удаляем сообщение с матом
         
    
    # Пример с 1-го урока:
    # if message.text == 'Привет':
    #     await message.answer('И тебе привет')
    # await message.answer(message.text) # отправляем сообщение ботом, await - ждет, чтобы появилось свободное место для выполнения команды. В скобках передаем то, что хотим отправить обратно
    # await message.reply(message.text) # также ответ пользователю от бота
    # await bot.send_message(message.from_user.id, message.text) # третий вариант, позволяет отправить сообщение в личку пользователю, сработает только если пользователь уже когда-либо писал боту, или первый добавился к нему в контакты, указываем ID пользователя



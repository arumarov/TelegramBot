import sqlite3 as sq # импортируем модуль базы данных
from create_bot import bot

def sql_start(): # описываем функцию по созданию базы данных, или подключение, если она уже создана
    global base, cur
    base = sq.connect('pizza_cool.db') # подключение к файлу базы данных, если файла нет, он создастся
    cur = base.cursor() # часть базы данных, которая осуществляет поиск и выборку данных из базы
    if base:
        print('Data base connected OK!') # вывод сообщения при подключении к базе данных
        # далее создаем таблицу, в которую будем вносить данные, если ее еще нет
        # в таблице - 4 столбца - картинка, название, описание, цена
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)') 
    base.commit() # сохранение изменений

async def sql_add_command(state):
    async with state.proxy() as data: # открываем словарь
        # далее в таблицу вставляются значения
        # переводим данные в кортеж (особенность sqlite)
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit() # сохраняем изменения

# Отправление пользователю информации о товаре
async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()

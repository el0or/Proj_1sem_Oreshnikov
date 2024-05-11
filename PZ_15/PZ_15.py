# Приложение БЮРО ПО ТРУДОУСТРОЙСТВУ для некоторой организации. БД
# должна содержать таблицу Работник со следующей структурой записи: фамилия, имя,
# отчество, возраст, пол, профессия, стаж работы

import sqlite3 as sq

with sq.connect('Employment bureau.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS workers (
    id_work INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name VARCHAR,
    first_name VARCHAR,
    middle_name VARCHAR,
    age INTEGER,
    gender VARCHAR,
    profession VARCHAR,
    experience INTEGER
    )""")

def add_worker(last_name, first_name, middle_name, age, gender, profession, experience):
    cur.execute("INSERT INTO workers(last_name, first_name, middle_name, age, gender, profession, experience) VALUES(?,?,?,?,?,?,?)",
    (last_name, first_name, middle_name, age, gender, profession, experience))
    con.commit()
    print("Новый работник добавлен")

def get_worker():
    cur.execute("SELECT * FROM workers")
    result = cur.fetchall()
    print(result)


# add_worker('Иванов','Иван','Иванович','25','М','Программист','3')
# add_worker('Матвеев','Алексей','Олегович','29','М','Тим-лид','9')
# add_worker('Хмельной','Александр','Виссарионович','27','М','Луа разработчик','7')
# add_worker('Буранов', 'Андрей', 'Олегович', '23', 'М', 'Web разработчик', '2')
# add_worker('Иванова', 'Ольга','Викторовна','35','Ж','Врач-терапевт','10')
# add_worker('Петров','Александр','Сергеевич','45','М','Инженер','20')
# add_worker('Сидорова','Елена','Иванова','28','Ж','Секретарь','5')
# add_worker('Козлов','Дмитрий','Александрович','50','М','Бухгалтер','25')
# add_worker('Новикова','Анна','Павловна','40','Ж','Уборщица','3')
# add_worker('Григорьев','Игорь','Дмитриевич','30','М','Программист','8')


# with sq.connect('Employment bureau.db') as con:
#     cur = con.cursor()
#     cur.execute('SELECT * FROM workers WHERE age > 26')
#     result = cur.fetchall()
#     print(result)

# with sq.connect('Employment bureau.db') as con:
#     cur = con.cursor()
#     cur.execute('SELECT * FROM workers WHERE profession LIKE "Программист"')
#     result = cur.fetchall()
#     print(result)

# with sq.connect('Employment bureau.db') as con:
#     cur = con.cursor()
#     cur.execute('SELECT * FROM workers WHERE experience > 7 and experience < 20')
#     result = cur.fetchall()
#     print(result)

# with sq.connect('Employment bureau.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM workers WHERE age > 27 and age < 45')
#     result = cur.fetchall()
#     print(result)

# with sq.connect('Employment bureau.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM workers WHERE experience < 5')
#     result = cur.fetchall()
#     print(result)

# with sq.connect('Employment bureau.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM workers WHERE first_name LIKE "Александр"')
#     result = cur.fetchall()
#     print(result)

# with sq.connect('Employment bureau.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE workers SET last_name="Петрова" WHERE last_name="Иванова"')
#     result = cur.fetchall()
#     print(result)

# with sq.connect('Employment bureau.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE workers SET age="31" WHERE last_name="Григорьев"')
#     result = cur.fetchall()
#     print(result)

# with sq.connect('Employment bureau.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE workers SET profession="Главный-инженер" WHERE last_name="Петров"')
#     result = cur.fetchall()
#     print(result)

con.close()

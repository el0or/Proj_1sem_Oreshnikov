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
    experience VARCHAR
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


# add_worker('Иванов','Иван','Иванович','25','М','Программист','3 года')
# add_worker('Матвеев','Алексей','Олегович','29','М','Тим-лид','9 лет')

add_worker('Хмельной','Александр','Виссарионович','27','М','Луа разработчик','7 лет')

get_worker()
con.close()

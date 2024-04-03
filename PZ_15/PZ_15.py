# Приложение БЮРО ПО ТРУДОУСТРОЙСТВУ для некоторой организации. БД
# должна содержать таблицу Работник со следующей структурой записи: фамилия, имя,
# отчество, возраст, пол, профессия, стаж работы

import sqlite3 as sq

with sq.connect('Employment bureau') as con:
    cur = con.cursor()
    cur.execute(""""CREATE TABLE IF NOT EXISTS worker
    
    
    
    
    
    
    """)
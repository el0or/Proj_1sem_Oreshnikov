#Дан словарь на 6 персон, найти и вывести их средний возраст.

persons = {
    "Андрей": 32,
    "Виктор": 29,
    "Максим": 18,
    "Елена": 25,
    "Ольга": 30,
    "Иван": 27
}

average_age = sum(persons.values()) / len(persons)

print("Средний возраст:", average_age)

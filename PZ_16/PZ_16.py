"""
Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
Добавьте методы для вычисления среднего балла и определения, является ли студент
отличником.
"""
import pickle
import math
class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_excellent_student(self):
        if len(self.grades) == 0:
            return False
        return all(grade >= 4 for grade in self.grades)


student1 = Student("Иван", "Иванов", [5, 4, 5, 4, 5])
student2 = Student("Петр", "Петров", [3, 4, 2, 3, 3])

#Блок 2
"""
Создание базового класса "Фигура" и его наследование для создания классов 
"Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие 
методы, такие как вычисление площади и периметра, а классы-наследники 
будут иметь специфичные методы и свойства. 
"""
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

square = Square(5)
print(f"Площадь квадрата: {square.area()}")
print(f"Периметр квадрата: {square.perimeter()}")

rectangle = Rectangle(3, 4)
print(f"Площадь прямоугольника: {rectangle.area()}")
print(f"Периметр прямоугольника: {rectangle.perimeter()}")

circle = Circle(2)
print(f"Площадь круга: {circle.area()}")
print(f"Длина окружности круга: {circle.perimeter()}")


#Блок 3
"""
Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате.
"""
def save_def(students, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(students, file)

def load_def(file_name):
    with open(file_name, 'rb') as file:
        return pickle.load(file)

save_def([student1, student2], 'students.pickle')

loaded_students = load_def('students.pickle')

for student in loaded_students:
    print(f"Имя: {student.name}, Фамилия: {student.surname}")
    print(f"Средний балл: {student.calculate_average_grade()}")
    print(f"Студент отличник?: {student.is_excellent_student()}")
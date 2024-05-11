# class Note:
#     def __init__(self, text):
#         self.text = text
#         self.count = 0
#
#     def upcount(self):
#         self.count += 1
#
#
# note1 = Note('Задача 1')
# note2 = Note('Задача 2')

# class NoteTwo:
#     def __init__(self, text, iscompleted):
#         self.text = text
#         self.count = 0
#         self.iscompleted = iscompleted
#
#     def UpCount(self, num):
#         self.count += num
#
#     def ResetCount(self):
#         self.count = 0
#
# note1 = NoteTwo('Текст', True)
#
# print(note1.__dict__)
# note1.UpCount(5)
# print(note1.__dict__)

# class Image:
#     def __init__(self, resolution, extension, title):
#         self.resolution = resolution
#         self.title = title
#         self.extension = extension
#
#     def Resize(self, new_resolution):
#         self.resolution = new_resolution
#
#
#     def TitleUpper(self):
#         self.title = self.title.upper()
#
#
# image3 = Image(2, 'docx', 'Presi')
# image2 = Image(821, 'exe', 'Lowo')
# image1 = Image(500, 'txt', 'Photo')
# # print(image1.__dict__)
# image1.Resize(658)
# image3.Resize(618)
# image2.Resize(258)
#
# class Person:
#     ab = 0
#     def __init__(self, count):
#         self.count = count
#         Person.ab += 1
#
#     @staticmethod
#     def TotalPeople():
#         print(f'Кол-во людей: {Person.ab}')
#
# person1 = Person(17)
# person2 = Person(19)
# person3 = Person(16)
# person2.TotalPeople()

file = open("out.dat", "wb")
import pickle

actor1 = ['alex', '26', 35000]
actor2 = ['Gitler', '66', 135000]
actor3 = ['Kevin', '22', 25000]
actor4 = ['Martin', '19', 95000]

try:
    file = open("out.dat", "wb")
    try:
        pickle.dump(actor1, file)
        pickle.dump(actor1, file)
        pickle.dump(actor1, file)
        pickle.dump(actor1, file)

    finally:
        file.close()

except FileNotFoundError:
    print("Невозможно открыть файл")
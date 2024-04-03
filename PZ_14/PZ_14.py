#Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать
#количество полученных элементов.
import re
with open('experience.txt', 'r') as file:
    data = file.read()

experiencelist = re.findall(r"\d+ (?:год|года|лет) \d+ (?:месяц|месяцев|месяца)", data)

print(f"Стаж работы: {experiencelist}")

print("Количество элементов: ",len(experiencelist))
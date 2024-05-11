#Из предложенного текстового файла (text18-17.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно поставив последнюю строку между первой и второй.

# Чтение файла и вывод его содержимого
with open('text18-17.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print(text)

# Подсчет количества знаков препинания
punctuation_count = sum([1 for char in text if char in '.,:;!?'])
print(f'Количество знаков препинания: {punctuation_count}')

with open('text18-17.txt', 'r') as file:
    text = file.read()

# Формирование нового файла с текстом в стихотворной форме
lines = text.split('\n')
stih = '\n'.join([lines[0], lines[-1], *lines[1:-1]])

with open('stih.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(stih)

print('Файл stih.txt успешно создан с текстом в стихотворной форме.')
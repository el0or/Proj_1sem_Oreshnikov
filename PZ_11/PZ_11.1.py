#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Произведение элементов:
#Количество пар, для которых произведение элементов делится на 3 (элементы пары в
#последовательности являются соседними):
def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read().split()

        # Преобразуем строки в файле в список целых чисел
        numbers = [int(num) for num in data]

        num_elements = len(numbers)
        product = 1
        numbers_of_pair = 0
        for i in range(num_elements):
            product *= numbers[i]
            if i < num_elements - 1 and (numbers[i] * numbers[i+1]) % 3 == 0:
                numbers_of_pair += 1

        # Записываем результаты в новый файл
        with open(output_file, 'w') as new_file:
            new_file.write(f"Исходные данные: {numbers}\n")
            new_file.write(f"Количество элементов: {num_elements}\n")
            new_file.write(f"Произведение элементов: {product}\n")
            new_file.write(f"Количество пар, для которых произведение элементов делится на 3: {numbers_of_pair}\n")

l = ['-99 6 12 -36 20 45 100 -15']
f3 = open('input.txt', 'w')
f3.writelines(l)
f3.close()
input_filename = "input.txt"
output_filename = "output.txt"
process_file(input_filename, output_filename)


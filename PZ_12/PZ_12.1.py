#.В последовательности на n целых чисел умножить все элементы на последний
#минимальный элемент.
n = int(input("Введите количество элементов в последовательности: "))
sequence = []

for i in range(n):
    num = int(input(f"Введите {i+1}-й элемент: "))
    sequence.append(num)

min_element = min(sequence)

new_sequence = [x * min_element for x in sequence]

print("Новая последовательность:")
print(new_sequence)
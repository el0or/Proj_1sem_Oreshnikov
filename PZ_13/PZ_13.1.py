#В матрице найти максимальный положительный элемент, кратный 4
from functools import reduce
import random

# Создание матрицы (например 3x3) со случайными элементами
n = 3
matrix = [[random.randint(-10, 20) for _ in range(n)] for _ in range(n)]
print("Матрица:")
for row in matrix:
    print(row)

# Поиск максимального положительного элемента, кратного 4
max_positive_multiple_of_4 = reduce(lambda x, y: max(x, y) if y % 4 == 0 and y > 0 else x, [0] + [elem for row in matrix for elem in row])
print(f"Максимальный положительный элемент, кратный 4: {max_positive_multiple_of_4}")

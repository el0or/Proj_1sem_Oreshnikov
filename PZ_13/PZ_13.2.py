#В матрице найти сумму элементов первых двух строк.
from functools import reduce
import random

# Создание матрицы
n = 3
matrix = [[random.randint(1, 20) for _ in range(n)] for _ in range(n)]

# Нахождение суммы элементов первых двух строк матрицы
sum_first_two_rows = reduce(lambda acc, row: acc + sum(row), matrix[:2], 0)
print(f"Сумма элементов первых двух строк матрицы: {sum_first_two_rows}")


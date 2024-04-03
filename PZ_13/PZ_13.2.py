#В матрице найти сумму элементов первых двух строк.
from functools import reduce

# Создание матрицы
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Нахождение суммы элементов первых двух строк матрицы
sum_first_two_rows = reduce(lambda acc, row: acc + sum(row), matrix[:2], 0)
print(f"Сумма элементов первых двух строк матрицы: {sum_first_two_rows}")


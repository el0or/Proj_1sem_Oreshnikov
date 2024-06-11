##Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее
#арифметическое элементов список с номерами от K до L включительно.


def average_of_sublist(A, K, L):
    sublist = A[K-1:L]  # Получаем подсписок с элементами от K до L
    average = sum(sublist) / len(sublist)  # Считаем среднее значение подсписка
    return average

A = [3, 1, 2, 2, 7, 5]
K = 1
L = 3

result = average_of_sublist(A, K, L)
print(result)
def find_element(A):
    for AK in A:
        if AK < A[-1]:
            return AK
    return 0

# Пример использования функции
A = [5, 8, 10, 3, 7, 12, 6, 9, 2, 4]
result = find_element(A)
print(result)

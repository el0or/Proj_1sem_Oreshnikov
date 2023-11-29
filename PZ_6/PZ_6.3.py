def cyclic_shift(A, K):
    N = len(A)
    K %= N  # Предотвращаем выход K за пределы длины списка

    # Создаем вспомогательный список B из 4 элементов
    B = A[N-K:] + A[:N-K]

    # Копируем элементы из списка B в список A
    for i in range(N):
        A[i] = B[i]

    return A

# Пример использования функции
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K = 2
result = cyclic_shift(A, K)
print(result)

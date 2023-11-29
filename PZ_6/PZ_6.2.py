def find_closest_elements(A):
    min_diff = abs(A[1] - A[0])
    closest_indexes = [0, 1]
    
    for i in range(1, len(A)-1):
        diff = abs(A[i+1] - A[i])
        if diff < min_diff:
            min_diff = diff
            closest_indexes = [i, i+1]
    
    return sorted(closest_indexes)

# Пример использования функции
A = [5, 8, 10, 3, 7, 12, 6, 9, 2, 4]
result = find_closest_elements(A)
print(result)

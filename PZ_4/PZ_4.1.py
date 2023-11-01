def calculate_e_approximation(N):
    factorial = 1
    e_approximation = 1.0

    for i in range(1, N + 1):
        factorial *= i
        e_approximation += 1.0 / factorial

    return e_approximation

# Введите значение N
N = int(input("Введите целое число N (>0): "))
if N > 0:
    result = calculate_e_approximation(N)
    print(f"Приближенное значение e при N = {N} равно {result}")
else:
    print("N должно быть больше 0.")
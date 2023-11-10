try:
    def calculate_exp(N):
        factorial = 1
        exp = 1.0

        for i in range(1, N + 1):
            factorial *= i
            exp += 1.0 / factorial
        return exp

    # Введите значение N
    N = int(input("Введите целое число N (>0): "))
    if N > 0:
        result = calculate_exp(N)
        print(f"Приближенное значение e при N = {N} равно {result}")
except ValueError:
    print("Введите число больше нуля!!")

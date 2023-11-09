def length(A, B):
    if A <= B:
        return 0  # Если A не больше B, то незанятой части нет

    remaining_length = A
    while remaining_length >= B:
        remaining_length -= B

    return remaining_length

# Введите значения A и B
try:
    A = int(input("Введите положительное число A: "))
    B = int(input("Введите положительное число B (меньше A): "))
except ValueError:
    print("Введите положительное число!")

if A > 0 and B > 0 and A > B:
    result = length(A, B)
    print(f"Длина незанятой части отрезка A равна {result}")
else:
    print("Пожалуйста, введите положительные числа, где A > B.")

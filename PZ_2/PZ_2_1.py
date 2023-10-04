# Вариант 27. С начала прошло N секунд (n- целое). Найти колличество секунд, прошедших с начала последнего часа
while True:
    try:
        n = int(input("Введите колличество секунд: "))
    except ValueError:
        print("Что-то пошло не так")
        continue
    break

lastHour = 3600 // n
print(f"Колличество секунд: {lastHour}")



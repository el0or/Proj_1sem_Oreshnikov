while True:
    try:
        a = float(input("Введите вещественное число: "))
        b = float(input("Введите вещественное число: "))
        c = float(input("Введите вещественное число: "))
    except ValueError:
        print("Введите вещественное число!")
        continue
    break
if a < b < c:
    a *= 2
    b *= 2
    c *= 2
else:
    a = -a
    b = -b
    c = -c

print(f"Новые значения перменных а={a}, b ={b}, c={c}")

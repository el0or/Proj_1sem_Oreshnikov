while True:
    try:
        a = int(input("Введите целое число"))
    except ValueError:
        print("Введите ЦЕЛОЕ число")
        continue
    break

if a > 9 and a<100 or a <-9 and a>-100:
    print("Оно двузначное и положительное :)")
else:
    print("Оно не двузначное или не положительное :(")
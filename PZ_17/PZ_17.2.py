# дано целое положительное число проверить истинность высказывания: "Данное число является четным двузначным"
import tkinter as tk

def check_number():
    try:
        number = int(entry.get())
        if 10 <= number <= 99 and number % 2 == 0:
            result_label.config(text="Число является четным двузначным")
        else:
            result_label.config(text="Число не является четным двузначным")
    except ValueError:
        result_label.config(text="Введите целое число")

# Создаем окно
root = tk.Tk()
root.title("Проверка числа")

# Создаем виджеты
entry_label = tk.Label(root, text="Введите целое число:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Проверить", command=check_number)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Запускаем цикл обработки событий
root.mainloop()

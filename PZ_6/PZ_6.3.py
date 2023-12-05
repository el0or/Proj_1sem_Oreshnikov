#Дан список размера N, все элементы которого, кроме первого, упорядочены по
#возрастанию. Сделать список упорядоченным, переместив первый элемент на новую
#позицию.
def order_list(lst):
    # Проверка наличия элементов в списке
    if len(lst) > 1:
        # Перемещение первого элемента на новую позицию
        first_element = lst.pop(0)
        lst.insert(1, first_element)
        # Сортировка списка
        lst.sort()
    return lst

# Пример использования функции
N = int(input("Введите размер списка N: "))
my_list = []

for i in range(N):
    element = int(input(f"Введите элемент {i + 1}: "))
    my_list.append(element)

result = order_list(my_list)
print("Упорядоченный список:", result)

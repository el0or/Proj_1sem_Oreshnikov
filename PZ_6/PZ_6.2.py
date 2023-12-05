#Дан целочисленный список размера N, содержащий ровно два одинаковых элемента.
#Найти номера одинаковых элементов и вывести эти номера в порядке возрастания.

def find_duplicate_indices(nums):
    dd = {}
    for i, num in enumerate(nums):
        if num in dd:
            return (dd[num], i)
        else:
            dd[num] = i

my_list = [3, 1, 5, 2, 7, 5]
result = find_duplicate_indices(my_list)
print(result)

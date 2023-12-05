#Дана строка, состоящая из русских слов, разделенных пробелами (одним или
#несколькими). Найти длину самого длинного слова.

def find_lenght(stroka):
    words = stroka.split() # Разделение строки на слова по пробелам
    length_words = [len(word) for word in words] # Создание списка длин слов
    longest_word = max(length_words) # Нахождение самой большой длины
    return longest_word

# Пример использования
stroka = "Дана строка, состоящая из русских слов"
print(find_lenght(stroka))
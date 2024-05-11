#Составить генератор (yield), который переведет символы строки из верхнего
#регистра в нижний.
def upper_to_lower(string):
    for char in string:
        if char.isupper():
            yield char.lower()
        else:
            yield char

input_string = "HeLLo, WoRLd!"
result = ''.join(upper_to_lower(input_string))

print(result)
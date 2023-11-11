'''
Ревью кода 2 😠
Требовалось реализовать функцию swapcase_vowels(), которая принимает в качестве 
аргумента строку, заменяет в ней все гласные латинские буквы на заглавные 
и возвращает полученную новую строку. Программист торопился и реализовал функцию неправильно.

Найдите и исправьте все ошибки, допущенные в реализации этой функции (их ровно 3).

Примечание. Известно, что каждая ошибка затрагивает только одну строку и может 
быть исправлена без изменения других строк.

def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char == vowels:
            char.upper()
        swapped_string += char

    return print(swapped_string)
'''
def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char in vowels: # 2
            char = char.upper() # 3
        swapped_string += char

    return swapped_string # 1
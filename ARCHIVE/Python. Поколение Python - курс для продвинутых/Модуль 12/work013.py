'''
Random name and surname
Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 33 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере.

Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:

Aaron
Abdul
Abe
Abel
Abraham
Albert

и

Abramson
Adamson
Adderiy
Addington
Adrian
Albertson
Einstein

то результатом могло быть:

Abdul Albertson
Abel Adamson
Albert Einstein

Примечание 2. Указанные файлы можно скачать по ссылкам (имена, фамилии). 
'''
# Решение
import random as r
with open('first_names.txt', 'rt', encoding='utf-8') as first_name,\
    open('last_names.txt', 'rt', encoding='utf-8') as last_name:
        name_dict = dict(
            zip(
                r.choices(list(map(str.rstrip, first_name)), k=3), 
                r.choices(list(map(str.rstrip, last_name)), k=3)
            )
        )
        print(*[f'{k} {v}' for k, v in name_dict.items()], sep='\n')
'''
The Zen of Python

Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...

Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте. 
Буквы и их количество должны выводиться в лексикографическом порядке, каждая на отдельной строке, 
в следующем формате:

<буква>: <количество>

Примечание 1. Начальная часть ответа выглядит так:

a: 53
b: 21
...

Примечание 2. Программа не должна учитывать регистр, то есть, например, 
буквы a и A считаются одинаковыми.

Примечание 3. Программа должна игнорировать все небуквенные символы.

Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/590120/pythonzen.txt
https://stepik.org/media/attachments/lesson/590120/clue_zen.txt

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''
from collections import Counter

with open(file='021-pythonzen.txt', mode='rt', encoding='utf-8', newline='') as file_opener:
    [print(f'{k}: {v}') for k, v in sorted(Counter(filter(str.isalpha, file_opener.read().lower())).items())]
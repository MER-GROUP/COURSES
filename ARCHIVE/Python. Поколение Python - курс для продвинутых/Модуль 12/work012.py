'''
Статистика по файлу
Вам доступен текстовый файл file.txt, набранный латиницей. 
Напишите программу, которая выводит количество букв 
латинского алфавита, слов и строк. Выведите три 
найденных числа в формате, приведенном в примере.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести три найденных числа в формате, 
приведенном в примере.

Примечание 1. Если бы файл file.txt содержал строки:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

то результатом было бы:
Input file contains:
108 letters 
20 words 
4 lines 

Примечание 2. Словом называется последовательность 
из непробельных символов. Например, строка

abc a21 67pop    qwert bo7ok 83456
содержит 66 слов: abc, a21, 67pop, qwert, bo7ok, 83456.

Примечание 3. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/530408/file.txt
'''
# Решение
import string
with open('file.txt', 'rt', encoding='utf=8') as file:
    letters, words, lines = (0 for i in range(3))
    for line in file:
        letters += sum(
            map(
                lambda x: 1 if x in string.ascii_letters else 0,
                line
            )
        )
        words += len(line.split())
        lines +=1
    print(f'Input file contains:\n{letters} letters\n{words} words\n{lines} lines')
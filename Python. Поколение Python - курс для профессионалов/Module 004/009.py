'''
Гуру прогрессий
Дана последовательность целых чисел. Напишите программу, которая определяет, 
является ли данная последовательность прогрессией, и если да, то определяет её вид.

Формат входных данных
На вход программе подается произвольное количество строк (не менее трёх), 
в каждой строке записано натуральное число — очередной член последовательности.

Формат выходных данных
Программа должна вывести текст:

Арифметическая прогрессия, если введенная последовательность 
чисел является арифметической прогрессией
Геометрическая прогрессия, если введенная последовательность 
чисел является геометрической прогрессией
Не прогрессия, если введенная последовательность 
чисел не является прогрессией

Примечание 1. Гарантируется, что вид прогрессии определяется однозначно.

Примечание 2. Подробнее об арифметической и геометрической 
прогрессиях тут и тут соответственно.
https://ru.wikipedia.org/wiki/Прогрессия
https://ru.wikipedia.org/wiki/Арифметическая_прогрессия
https://lfirmal.com/arifmeticheskaya-progressiya/
https://ru.wikipedia.org/wiki/Геометрическая_прогрессия
https://mathus.ru/math/geometric-progression.pdf

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/520159/tests_30662099.zip

Sample Input 1:
1
2
3
4
5
Sample Output 1:
Арифметическая прогрессия

Sample Input 2:
2
4
8
16
Sample Output 2:
Геометрическая прогрессия

Sample Input 3:
1
9
1
1
4
5
Sample Output 3:
Не прогрессия
'''
import sys

def arif_prog(tup):
    d = abs(tup[0] - tup[1])
    for i in range(1, len(tup)-1):
        if not d == abs(tup[i] - tup[i+1]):
            return False
    else:
        return True

def geom_prog(tup):
    if tup[0]:
        q = tup[1]//tup[0]
        for i in range(1, len(tup)-1):
            if not tup[i] * q == tup[i+1]:
                return False
        else:
            return True
    else:
        return False

# sys.stdin=open('test.txt', 'rt', encoding='utf-8') # tests
tup = tuple(map(int, sys.stdin))
# print(tup)

if arif_prog(tup):
    print('Арифметическая прогрессия')
elif geom_prog(tup):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
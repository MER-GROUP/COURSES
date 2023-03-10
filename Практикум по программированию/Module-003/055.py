'''
Встречалось ли число раньше
Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), 
если это число ранее встречалось в последовательности или NO, 
если не встречалось.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 2 3 2 3 4
Sample Output:
NO
NO
NO
YES
YES
NO
'''
import sys

# sys.stdin = open(file='055.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(*arr, sep='\n') # test

_set = set()
for i in map(int, arr[0].split()):
    if i not in _set:
        print('NO')
        _set.add(i)
    else:
        print('YES')
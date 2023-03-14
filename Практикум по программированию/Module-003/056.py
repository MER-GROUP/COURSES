'''
a + b = c

Даны три действительных числа: a, b, c. Проверьте, выполняется 
ли равенство a + b = c . Если равенство выполняется, выведите YES, 
если не выполняется, выведите NO.

Входные данные
Числа a, b, c –  действительные, положительные, не превосходят 10 
и заданы не более, чем с 7 знаками после точки.

Выходные данные
Выведите результат сравнения.

Sample Input 1:
2
3
7
Sample Output 1:
NO

Sample Input 2:
0.1
0.2
0.3
Sample Output 2:
YES
'''
import sys
import decimal as d

# sys.stdin = open(file='056.csv', mode='rt', encoding='utf-8', newline='')
_tuple = tuple(map(lambda x: d.Decimal(x), map(str.strip, sys.stdin.read().splitlines())))
# print(_tuple) # test

print(('NO', 'YES')[sum(_tuple[:2]) == _tuple[2]])
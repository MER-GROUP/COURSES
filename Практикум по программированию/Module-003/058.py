'''
Утренняя пробежка - 2
В первый день спортсмен пробежал x километров, а затем он каждый день 
увеличивал пробег на 70% от предыдущего значения. По данному числу y определите 
номер дня, на который суммарный пробег спортсмена составит не менее y километров.

Входные данные
На вход программа получает два действительных числа x и y. Числа положительные, 
действительные, не превосходят 1000, заданы с точностью до шести знаков после запятой.

Выходные данные
Программа должна вывести единственное целое число.

Sample Input:
1 20
Sample Output:
6
'''
import sys
import decimal as d

# sys.stdin = open(file='058.csv', mode='rt', encoding='utf-8', newline='')
_x, _y = tuple(map(d.Decimal, str(*map(str.strip, sys.stdin.read().splitlines())).split()))
# print(_x, _y) # test

_count = 1
_sum = d.Decimal(_x)
while _sum < _y:
    _decimal = d.Decimal(_x)
    for i in range(_count):
        _decimal *= d.Decimal('1.7')
    _sum += _decimal
    _count += 1
print(_count)
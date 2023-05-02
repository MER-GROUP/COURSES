'''
Ревизия
В связи с визитом Императора Палпатина было решено обновить состав 
дроидов в ангаре 32. Из-за кризиса было решено новых дроидов не закупать, 
но выкинуть пару старых. Как известно, Палпатин не переносит 
дроидов с маленькими серийными номерами, так что все, 
что требуется - найти среди них двух, у которых серийные номера наименьшие.

Входные данные
Первая строка входного файла содержит целое число N – количество 
дроидов. (2 ≤ N ≤ 1000), вторая строка – N целых чисел, 
по модулю не превышающих 2*10^9 – номера дроидов

Выходные данные
Выведите два числа: первым – последний по величине из номеров 
дроидов (такого следует утилизировать в первую очередь), 
а вторым – предпоследний.

Sample Input:
5
10 2 3 1 5
Sample Output:
1 2
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='007.csv', mode='rt', encoding='utf-8', newline='')
nm, tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(nm)
print(tup)
arr = array('i', map(int, tup.split()))
print(arr)

pass
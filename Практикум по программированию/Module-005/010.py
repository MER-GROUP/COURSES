'''
Серебряная медаль
Спортсмен Василий участвовал в соревнованиях по хоккейболу 
и получил в личном зачете серебряную медаль. Известно, 
что участники, получившие одинаковое количество очков, 
награждаются одинаковыми наградами. Известно, что были 
разыграны золотые серебряные и бронзовые медали. В задаче 
не спрашиваются правила хоккейбола. Необходимо только определить 
сколько очков набрал Василий.

Для решения данной задачи массив лучше не использовать.

PS: Задача сводится к поиску среди введенных значений 
числа второго по величине

Входные данные
На первой строке дано число N (2 ≤ N ≤ 1000) количество спортсменов, 
участвовавших в соревнованиях, на второй N целых чисел – результаты через пробел.

Выходные данные
Требуется вывести одно число – результат Василия

Sample Input1:
5
4 3 3 1 2
Sample Output 1:
3

Sample Input 2:
8
1 2 5 3 5 6 6 5
Sample Output 2:
5
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='010.csv', mode='rt', encoding='utf-8', newline='')
nm, tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(nm)
# print(tup)
# n, m = map(int, nm.split())
# print(n)
# print(m)
# arr = array('i', map(int, tup.split()))
# print(arr)

# 1
print(sorted(set(map(int, tup.split())), reverse=True)[1])

# 2
_arr = tuple(map(int, tup.split()))
_max1, _max2 = max(_arr[:2]), min(_arr[:2])
for el in _arr[2:]:
    if _max1 < el:
        _max1 = el
    elif _max2 < el < _max1:
        _max2 = el
print(_max2)

# 3
_, mx, nxt = tup, 0, 0
for e in map(int, _.split()):
    if e > mx:        
        nxt, mx = mx, e
    elif mx != e > nxt:
        nxt = e
print(nxt)  
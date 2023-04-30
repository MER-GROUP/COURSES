'''
Количество дней от начала эры
Требуется посчитать количество дней от начала эры до данного дня включительно. 
Началом эры считается первое января первого года.

Входные данные
В единственной строке входного файла находится дата в формате ДДММГГГГ.

Выходные данные
Выведите искомое количество дней.

Sample Input:
02010001
Sample Output:
2
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='058.csv', mode='rt', encoding='utf-8', newline='')
nm, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(nm)
# print(tup)
# arr = array('i', list(map(int, arr.split())))
# n, *m = map(int, nm.split())
# print(n)
# # arr = [list(map(int, tup[i].split())) for i in range(n)]
# arr = [[0]*n for _ in range(n)]
# [print(*i, sep='') for i in arr]

# 1
from datetime import datetime
day, month, year = int(nm[0:2]), int(nm[2:4]), int(nm[4:])
print(f'day = {day}, month = {month}, year = {year}')
_date = datetime(year=year, month=month,day=day)
print(_date)
print(_date.toordinal())
print('----------')

# 2
def is_leap(year: int) -> bool:
    return not bool(year % 4) and bool(year % 100) or not bool(year % 400)

day, month, year = int(nm[0:2]), int(nm[2:4]), int(nm[4:])

_day_total = 0
_check = True
for n_year in range(year, 0, -1):
    # print(f'n_year = {n_year}') # test
    _months = {
        1: 31, 2: (28, 29)[is_leap(n_year)], 3: 31, 4: 30, 5: 31, 
        6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    for n_month in range(month, 0, -1):
        # print(f'n_month = {n_month}') # test
        if _check:
            _day_total += day
            _check = False
        else:
            _day_total += _months[n_month]
    month = 12
print(_day_total)
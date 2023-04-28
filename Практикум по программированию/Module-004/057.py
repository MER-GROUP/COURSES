'''
Послезавтра
По заданной дате требуется определить, какое число будет послезавтра.

Напомним, что год является високосным, если его номер кратен 4, 
но не кратен 100, а также если он кратен 400.

Входные данные
Дано число, месяц и год (год  – число в промежутке от 1 до 10000).

Выходные данные
Требуется вывести, какое число будет послезавтра, в формате входных данных.

Sample Input:
1 8 2009
Sample Output:
3 8 2009
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='057.csv', mode='rt', encoding='utf-8', newline='')
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
from datetime import datetime, timedelta
_date = datetime.strptime(nm, '%d %m %Y') + timedelta(days=2)
print(_date.strftime('%d %m %Y')) # for all
print(_date.strftime('%-d %-m %Y')) # for linux
print(_date.strftime('%#d %#m %Y')) # for windows
print(_date.day, _date.month, _date.year) # for this
print('----------')

# 2
from calendar import isleap
day, month, year = map(int, nm.split())
day_z, month_z, year_z = [None] * 3
print(f'day = {day}, month = {month}, year = {year}') # test
print(f'isleap = {isleap(year)}') # test

def is_leap(year: int) -> bool:
    return not bool(year % 4) and bool(year % 100) and bool(year % 400)
print(f'is_leap = {is_leap(year)}') # test

_months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} \
        if is_leap(year) else \
        {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
day_new = sum((_months[i+1] for i in range(month)), start=2)
print(day_new) # test

_days = 366 if is_leap(year) else 365

year_z = year + 1 if day_new > _days else year ################################ error semantic

month_z = month
month_z = month_z + 1 if _months[month] < day + 2 else month_z
month_z = 1 if day_new > _days else month

day_z = day + 2 if _months[month] >= day + 2 else day + 2 - _months[month]

print(day_z, month_z, year_z)
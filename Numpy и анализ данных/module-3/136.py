'''
Фильтрация данных интернет магазина

На вход поступает массив с данными о продажах товаров в интернет-магазине, 
в котором каждый элемент представляет собой сумму продаж за определенный день. 
Найдите все дни, когда было продано товаров на сумму более 1000 рублей и выведите 
соответствующую информацию о продажах за эти дни. Если в какой-нибудь день продаж 
было меньше, замените соответствующее значение на NaN. Выведите итоговый массив на экран.

Sample Input:
2395 701 6319 2959 7591 725 5036 6413 1709 5042 8436 733 5009 6986 8094 3384 6040 4388 2180 4696 7802 660 5396 7195 5534 2875 196 2136 1010 6471

Sample Output:
2395.0 nan 6319.0 2959.0 7591.0 nan 5036.0 6413.0 1709.0 5042.0 8436.0 nan 5009.0 6986.0 8094.0 3384.0 6040.0 4388.0 2180.0 4696.0 7802.0 nan 5396.0 7195.0 5534.0 2875.0 nan 2136.0 1010.0 6471.0
'''
import numpy as np
from sys import stdin
stdin = open(file='136.csv', mode='rt', encoding='utf-8', newline='')

if __name__ == '__main__':
#     arr = np.fromstring(
#         string=stdin.read(),
#         # dtype=int,
#         dtype=float,
#         sep = ' '
#     )
#     print(arr) # test #
#     print(type(arr)) # test #

    # arr1, arr2, arr3, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    # print(arr1, arr2, arr3, sep='\n')

    # arr1, arr2, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    arr1, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    print(arr1) # test
    # print(arr2) # test

    pass
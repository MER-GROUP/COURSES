'''
Анализ данных клиентов

На вход поступает массив целых чисел с информацией о клиентах, в котором каждый 
элемент представляет собой среднемесячный доход клиента в рублях. Найдите 
всех клиентов с доходом выше 100000 рублей в месяц и пометьте их соответствующим 
образом в массиве метками 'High', 'Low'. Данный массив меток выведите на экран 
в виде строки через пробел.

Sample Input:
165903 97237 128368 187888 146599 156138 149556 141726 101633 187440 67525 50291 55938 69684 162119 141230 97434 168158 84146 90461 119371 62846 198485 120646 157500 105496 101447 82622 191250 172662 97755 138215 154904 171561 89881 188396 197934 79905 131856 163578 94850 102638 187358 109292 71822 89413 70547 93069 160630 154801 173656 97414 194345 127287 164460 61708 160631 192194 161240 160024 68027 146681 57594 75078

Sample Output:
High Low High High High High High High High High Low Low Low Low High High Low High Low Low High Low High High High High High Low High High Low High High High Low High High Low High High Low High High High Low Low Low Low High High High Low High High High Low High High High High Low High Low Low
'''
import numpy as np
from sys import stdin
stdin = open(file='134.csv', mode='rt', encoding='utf-8', newline='')

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

    arr1, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    print(arr1) # test

    pass
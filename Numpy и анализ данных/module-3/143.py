'''
Стандартное отклонение

Рассчитать стандартное отклонение веса женщин в возрастной категории 18-30 лет 
на основе данных, представленных в виде одномерного массива, поступающего во входной строке.

Вывести результат в формате: "Стандартное отклонение весов женщин 
в возрастной категории 18-30 лет: x.x кг".

Результат округляйте до одного знака после запятой, кавычки не используйте.

Sample Input:
64.2 63.4 61.3 76.9 78.2 53.6 74.8 56.3 49.4 51.1 81.9 64.5 66.2 51.6 62.2 58.5 48.9 68.8 83.6 45.8 66.1 81.1 50.9 81.6 69.0

Sample Output:
Стандартное отклонение весов женщин в возрастной категории 18-30 лет: 11.5 кг
'''
import numpy as np
from sys import stdin
stdin = open(file='143.csv', mode='rt', encoding='utf-8', newline='')

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

    # arr1, arr2, *_ = (np.array(object=i.split(), dtype=str) for i in stdin)
    # arr1, arr2, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    # arr1, arr2, *_ = (np.array(i.split(), dtype=int) for i in stdin)
    arr1, *_ = (np.fromstring(string=i, dtype=float, sep=' ') for i in stdin)
    print(arr1) # test
    # print(arr2) # test

    pass
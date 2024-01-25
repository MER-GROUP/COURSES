'''
Рассчитать дисперсию

Рассчитать дисперсию оценок учеников в классе на основе данных, представленных 
в виде одномерного массива, поступающего во входной строке. Ответ вывести в формате: 
"Дисперсия оценок учеников в классе равна: x.x"

Результат округляйте до одного знака после запятой, кавычки не используйте.

Sample Input:
5 4 3 3 4 5 3 4 4 3 4 3

Sample Output:
Дисперсия оценок учеников в классе равна: 0.5
'''
import numpy as np
from sys import stdin
stdin = open(file='144.csv', mode='rt', encoding='utf-8', newline='')

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
'''
Cреднее значение

Рассчитать среднее значение роста студентов в группе на основе их ростов, 
представленных в виде одномерного массива, который поступает во входной строке. 
Вывести ответ в формате: "Средний рост студентов в группе: х.х см", где х.х искомые 
значения. Результат округляйте до одного знака после запятой, кавычки не используйте.

Sample Input:
187.0 186.7 220.9 176.0 166.0 171.7 201.7 180.5 133.4 146.3 237.5 141.0 215.3 181.5 166.2 126.2 137.6 189.1 219.5 160.5 217.7 129.1 166.6 159.9 134.2 201.7 153.0

Sample Output:
Средний рост студентов в группе: 174.3 см
'''
import numpy as np
from sys import stdin
stdin = open(file='142.csv', mode='rt', encoding='utf-8', newline='')

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

    print(f'Средний рост студентов в группе: {np.mean(arr1).round(1)} см')
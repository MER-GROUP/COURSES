'''
Анализ результатов бактериологического эксперимента

На вход в первой строке поступает массив с результатами эксперимента, 
в котором каждый элемент представляет собой количество бактерий в петри. 
Во второй строке поступает целое число threshold. Найдите все значения, 
которые превышают значение threshold, и замените их на максимальное значение 
в массиве. Выведите итоговый массив в виде строки чисел через пробел.

Sample Input:
12 21 18 0 9 10 5 2 7 18 3 13 16 4 0 5 11 16 2 17 16 18 21 0
10

Sample Output:
21 21 21 0 9 10 5 2 7 21 3 21 21 4 0 5 21 21 2 21 21 21 21 0
'''
import numpy as np
from sys import stdin
# stdin = open(file='135.csv', mode='rt', encoding='utf-8', newline='')

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

    arr1, arr2, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    # print(arr1) # test
    # print(arr2) # test

    print(*np.where(arr2[0] < arr1, arr1.max(), arr1))
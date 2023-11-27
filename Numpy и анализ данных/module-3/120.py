'''
Экспоненциальный свинг хвоста

Представьте, что вы являетесь собакой и вы хотите вычислить, сколько раз в день 
вы виляете хвостом. Для этого вы записываете свои данные в массив tail_wags_per_hour 
содержащий количество раз, которое вы виляете хвостом за каждый час в течение дня. 
Затем вы применяете функцию

\(e^x - 1\)

к этому массиву и получаете результат, который называется "экспоненциальный свинг хвоста". 
Выведите полученный результат, округленный до двух знаков, на экран.

Sample Input:
5 9 7 6 0 8 0 1 1 3 5 13 6 5 10 13 5 2 6 1 11 7 8 9

Sample Output:
147.41 8102.08 1095.63 402.43 0.0 2979.96 0.0 1.72 1.72 19.09 147.41 442412.39 402.43 147.41 22025.47 442412.39 147.41 6.39 402.43 1.72 59873.14 1095.63 2979.96 8102.08
'''
import numpy as np
from sys import stdin
# stdin = open(file='120.csv', mode='rt', encoding='utf-8', newline='')

if __name__ == '__main__':
    arr = np.fromstring(
        string=stdin.read(),
        # dtype=int,
        dtype=float,
        sep = ' '
    )
    # print(arr) # test #
    # print(type(arr)) # test #

    # arr1, arr2 = (np.fromstring(string=i, dtype=float, sep=' ') for i in stdin)
    # print(arr1, arr2, sep='\n')

    # print(np.round(np.exp(arr)-1, 2))
    # print(np.round(np.expm1(arr), 2))
    res = np.round(np.exp(arr)-1, 2)
  
    for i in res:
        print(i, end=' ')
    print()
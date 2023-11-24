'''
Ограничение значений сигнала в звукозаписи

Представьте, что вы звукоинженер. При записи звука на высоком уровне громкости 
может возникнуть перегрузка, которая проявляется как срыв звука и искажения. 
Для того чтобы избежать этого, можно использовать функцию np.clip(), 
чтобы ограничить значения сигнала в заданном диапазоне.

На вход в первой строке поступает массив действительных чисел, разделенных 
пробелом. Во второй строке действительное число - максимально допустимое 
значение сигнала. Ваша задача вывести данный массив, при этом все значения, 
превышающие допустимый максимум должны быть замененны на этот допустимый максимум.

Sample Input:
3.4 1.3 4.0 1.7 4.4 3.9 2.9 2.3 2.7 1.3 4.9 5.8 1.3 4.5 5.2 3.0 4.1 0.0 5.6 3.6 5.4 4.9 2.8 0.5 4.8 4.1 0.7
4.5

Sample Output:
3.4 1.3 4.0 1.7 4.4 3.9 2.9 2.3 2.7 1.3 4.5 4.5 1.3 4.5 4.5 3.0 4.1 0.0 4.5 3.6 4.5 4.5 2.8 0.5 4.5 4.1 0.7
'''
import numpy as np
from sys import stdin
# stdin = open(file='119.csv', mode='rt', encoding='utf-8', newline='')

if __name__ == '__main__':
    # arr = np.fromstring(
    #     string=stdin.read(),
    #     dtype=float,
    #     sep = ' '
    # )
    # print(arr) # test #
    # print(type(arr)) # test #

    arr1, arr2 = (np.fromstring(string=i, dtype=float, sep=' ') for i in stdin)
    # print(arr1, arr2, sep='\n')

    print(*np.clip(arr1, None, *arr2))
'''
Минимум на отрезке

Рассмотрим последовательность целых чисел длины N. По ней с шагом 1 
двигается “окно” длины K, то есть сначала в “окне” видно первые K чисел, 
на следующем шаге в “окне” уже будут находиться K чисел, начиная со второго, 
и так далее до конца последовательности. Требуется для каждого положения 
“окна” определить минимум в нём.

Входные данные

В первой строке входных данных содержатся два числа 
N и K (1 ≤  N ≤  150000, 1 ≤ K ≤ 10000, K ≤  N) – длины последовательности 
и “окна”, соответственно. На следующей строке находятся 
N чисел – сама последовательность.

Выходные данные

Выходные данные должны содержать N − K + 1 строк – минимумы 
для каждого положения “окна”.

Sample Input:
7 3
1 3 2 4 5 3 1

Sample Output:
1
2
2
3
1
'''
import sys
from array import array
# from copy import copy

if __name__ == '__main__':
    # sys.stdin = open(file='028.csv', mode='rt', encoding='utf-8', newline='')
    n, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
    # print(n)
    # print(tup)
    arr = array('i', map(int, tup[0].split()))
    # print(arr)

    size, otrezok = map(int, n.split())
    for i in range(size):
        if otrezok <= size:
            print(min(arr[i:otrezok]))
        otrezok += 1
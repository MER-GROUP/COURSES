'''
Двойной переворот
Дана последовательность натуральных чисел 1, 2, 3, ..., N (1 ≤ N ≤ 1000). 
Необходимо сначала расположить в обратном порядке часть этой последовательности 
от элемента с номером A до элемента с номером B, а затем от C до D 
(A < B; C < D; 1 ≤ A, B, C, D ≤ N).

Входные данные
Вводятся натуральные числа числа N, A, B, C, D.

Выходные данные
Требуется вывести полученную последовательность. Числа следует выводить через пробел.

Sample Input:
9 2 5 6 9
Sample Output:
1 5 4 3 2 9 8 7 6
'''
import sys
from array import array

# sys.stdin = open(file='013.csv', mode='rt', encoding='utf-8', newline='')
arr= tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

N, A, B, C, D = arr
A -= 1; B -= 1; C -= 1; D -= 1
# print(N, A, B, C, D)

# 1
print(
    *list(range(1, N+1))[:A],
    *list(range(1, N+1))[A:B+1][::-1],
    *list(range(1, N+1))[B+1:C],
    *list(range(1, N+1))[C:D+1][::-1],
    *list(range(1, N+1))[D+1:]
)

# 2
_arr = array('i', range(1, N+1))
# print(_arr) # test
j = B
for i in range(A, B+1):
    if i == j or i > j: break
    _arr[i], _arr[j] = _arr[j], _arr[i]
    j -= 1
# print(_arr) # test
j = D
for i in range(C, D+1):
    if i == j or i > j: break
    _arr[i], _arr[j] = _arr[j], _arr[i]
    j -= 1
# print(_arr) # test
print(*_arr)

# 3
_arr = array('i', range(1, N+1))
# print(_arr) # test
for i, j in zip(range(A, B+1), range(B, A-1, -1)):
    if i == j or i > j: break
    _arr[i], _arr[j] = _arr[j], _arr[i]
# print(_arr) # test
for i, j in zip(range(C, D+1), range(D, C-1, -1)):
    if i == j or i > j: break
    _arr[i], _arr[j] = _arr[j], _arr[i]
# print(_arr) # test
print(*_arr)
'''
Двойной переворот
Дана последовательность натуральных чисел 1, 2, 3, ..., N (1 ≤ N ≤ 1000). 
Необходимо сначала расположить в обратном порядке часть этой последовательности 
от элемента с номером A до элемента с номером B, а затем от C до D (A < B; C < D; 1 ≤ A, B, C, D ≤ N).

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

sys.stdin = open(file='013.csv', mode='rt', encoding='utf-8', newline='')
arr= tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
print(arr) # test

pass
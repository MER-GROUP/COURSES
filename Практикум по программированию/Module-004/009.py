'''
Циклический сдвиг вправо
Напишите программу, которая циклически сдвигает элементы массива вправо 
(например, если элементы нумеруются, начиная с нуля, то 0-й элемент 
становится 1-м, 1-й становится 2-м, ..., последний становится 0-м, 
то есть массив {3, 5, 7, 9} превращается в массив {9, 3, 5, 7}).

Входные данные
Сначала задано число N — количество элементов в массиве (1 ≤ N ≤ 35). 
Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.

Выходные данные
Необходимо вывести массив, полученный после сдвига элементов. 
Числа следует выводить через пробел.

Sample Input:
6
4 5 3 4 2 3
Sample Output:
3 4 5 3 4 2
'''
import sys
from array import array

# sys.stdin = open(file='009.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

# print(arr[-1], *arr[:-1]) # 1

for _i in range(len(arr)-1): # 2
    arr[_i], arr[-1] = arr[-1], arr[_i]
print(*arr)

# tests
# for _i in range(len(arr)-1): 
#     print(arr[_i])
#     print(arr[-1])
#     print(arr[~_i])
#     print(arr[len(arr)-1-_i])
#     print('-----')
# print(*arr)

# n = int(input())
# arr = list(map(int, input().split()[:n]))
# print(arr[-1:])
# print(arr[:n-1])
# shift_arr = arr[-1:] + arr[:n-1]

# print(*shift_arr)

# _ = input()
# l = input().split()
# t = []
# for i in range(len(l)):
#     # t.append(l[i-1 % len(l)]) 
#     t.append(l[i-1]) 
#     print(*t)
#     print('el=', l[i-1 % len(l)])
#     print('i=', i-1 % len(l))
#     print('ost=', 1 % len(l))
#     print('------')
# print(*t)
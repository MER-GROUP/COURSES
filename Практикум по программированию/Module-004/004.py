'''
Количество элементов, больших предыдущего
Дан массив, состоящий из целых чисел. Напишите программу, 
которая подсчитает количество элементов массива, больших предыдущего 
(элемента с предыдущим номером).

Входные данные
Сначала задано число N — количество элементов в массиве (1 ≤ N ≤ 10000). 
Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.

Выходные данные
Необходимо вывести единственное число - количество элементов массива, 
больших предыдущего.

Sample Input:
5
1 2 3 4 5
Sample Output:
4
'''
import sys

# sys.stdin = open(file='004.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = list(map(int, arr[0].split()))
# print(arr) # test

_count = int()
for _i in range(1, len(arr)):
    if arr[_i-1] < arr[_i]:
        _count += 1
print(_count)

print(sum(1 for _i in range(1, len(arr)) if arr[_i-1] < arr[_i]))
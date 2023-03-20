'''
Есть ли два элемента с одинаковыми знаками
Дан массив, состоящий из целых чисел. Напишите программу, которая определяет, 
есть ли в массиве пара соседних элементов с одинаковыми знаками.

Входные данные
Сначала задано число N — количество элементов в массиве (1 ≤ N ≤ 10000). 
Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.

Выходные данные
Необходимо вывести слово YES, если существует пара соседних элементов с одинаковыми знаками. 
В противном случае следует вывести слово NO.

Sample Input:
5
1 -3 4 -2 1
Sample Output:
NO
'''
import sys

def compare(a: int, b: int) -> bool:
    if (a < 0 and b < 0) or (a >= 0 and b >= 0):
        return True
    else:
        return False

# sys.stdin = open(file='005.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = list(map(int, arr[0].split()))
# print(arr) # test

print(('NO', 'YES')[any(compare(arr[_i-1], arr[_i]) for _i in range(1, len(arr)))])
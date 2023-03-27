'''
Больше своих соседей
Дан список чисел. Определите, сколько в этом списке элементов, 
которые больше двух своих соседей и выведите количество таких элементов.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input 1:
1 2 3 4 5
Sample Output 1:
0

Sample Input 2:
1 5 1 5 1
Sample Output 2:
2
'''
import sys
from array import array

# sys.stdin = open(file='021.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

print(sum(arr[i-1] < arr[i] > arr[i+1] for i in range(1, len(arr)-1)))
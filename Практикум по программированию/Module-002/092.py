'''
Количество четных элементов последовательности
Определите количество четных элементов в последовательности, 
завершающейся числом 0.

Само число 0, и все, что следует за ним, учитывать не нужно.

Входные данные
Вводится последовательность целых чисел, оканчивающаяся числом 0 
(само число 0 в последовательность не входит).

Выходные данные
Выведите ответ на задачу.

Sample Input:
2
1
4
0
Sample Output:
2
'''
import sys

sys.stdin = open(file='092.csv', mode='rt', encoding='utf-8', newline='')
tup = tuple(map(int,sys.stdin.readlines()))

# ans = sum(tup[: tup.index(0)]) / len(tup[: tup.index(0)])
# print(int(ans) if ans.is_integer() else ans)
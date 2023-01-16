'''
Среднее значение последовательности
Определите среднее арифметическое элементов последовательности, завершающейся числом 0.

Число 0 в последовательность не входит. Числа, следующие за нулем, считывать не нужно.

Входные данные
Вводится последовательность целых чисел. Ввод завершается, когда будет введено число 0.

Выходные данные
Выведите одно число - среднее арифметическое элементов последовательности. 
Если ответ это целое число - значит нужно выводить целое число. 
Если ответ вещественное число - значит выводить нужно вещественное 
(без округлений, отбрасываний и незначащих нулей).

Sample Input:
1
5
6
0
Sample Output:
4
'''
import sys

# sys.stdin = open(file='091.csv', mode='rt', encoding='utf-8', newline='')
tup = tuple(map(int,sys.stdin.readlines()))

ans = sum(tup[: tup.index(0)]) / len(tup[: tup.index(0)])
print(int(ans) if ans.is_integer() else ans)

# from statistics import mean
# print(mean(tup[: tup.index(0)]))
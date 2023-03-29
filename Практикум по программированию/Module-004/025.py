'''
Шеренга
Петя перешёл в другую школу. На уроке физкультуры 
ему понадобилось определить своё место в строю. 
Помогите ему это сделать.

Входные данные
Программа получает на вход невозрастающую последовательность 
натуральных чисел, означающих рост каждого человека в строю. 
После этого с новой строки вводится число X – рост Пети. 
Все числа во входных данных натуральные и не превышают 200.

Выходные данные
Выведите номер, под которым Петя должен встать в строй. 
Если в строю есть люди с одинаковым ростом, таким же, 
как у Пети, то он должен встать после них.

Sample Input 1:
165 163 160 160 157 157 155 154
162
Sample Output 1:
3

Sample Input 2:
165 163 160 160 157 157 155 154
160
Sample Output 2:
5
'''
import sys
from array import array

# sys.stdin = open(file='025.csv', mode='rt', encoding='utf-8', newline='')
arr, petr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr.split())))
# print(arr) # test
# print(petr) # test

# 1
_count = 1
for _el in arr:
    if _el < int(petr):
        break
    _count += 1
        
print(_count)

# # 2
# arr = array('i', list(arr) + [int(petr)])
# print(len(arr) - sorted(arr).index(int(petr)))
'''
Экспедиция
Месклиниты собрались в экспедицию на край света. У них есть корабль, 
состоящий из N × M плотиков, связанных между собой. У каждого плотика 
есть своя грузоподъемность, а у каждого месклинита – своя масса. 
На каждом плотике может находиться не более одного месклинита. 
Если грузоподъемность выбранного плотика меньше массы месклинита, 
то бедный месклинит утонет при посадке.

Руководитель экспедиции продумывает рассадку по плотикам. Помогите 
ему определить, какому максимальному количеству месклинитов удастся 
отправиться в путь.

Входные данные
В первой строке даны числа N и M (1 ≤ N, M ≤ 40). В каждой из 
последующих N строк содержится по M чисел, обозначающих грузоподъемность 
соответствующего плотика. В (N+2)-ой строке находится 
число K (1 ≤ K ≤ 2000) – количество месклинитов. В (N+3)-ей строке 
содержатся K чисел, i-ое из которых – масса i-ого месклинита. 
Все массы месклинитов и грузоподъемности плотиков – натуральные числа, 
не превышающие 10^9.

Выходные данные
Требуется вывести одно число – максимально возможное количество 
участников экспедиции.

Sample Input:
3 2
5 10
7 5
5 5
6
9 5 3 5 12 10
Sample Output:
4
'''
import sys
from array import array
from copy import copy

# sys.stdin = open(file='022.csv', mode='rt', encoding='utf-8', newline='')
n_m, *tup, mesklinits, mases = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(tup)
# arr1 = array('i', map(int, tup[0].split()))
arr1 = array('i', sorted(map(int, [j for i in tup for j in i.split()])))
# print(arr1)
arr2 = array('i', sorted(map(int, mases.split())))
# print(arr2)

def analis(arr1: list, arr2: list) -> int:
    mesklinits, mases = copy(arr1), copy(arr2)
    _count = 0

    for mas in mases:
        for i, mes in enumerate(mesklinits):
            if mas <= mes:
                _count += 1
                mesklinits.pop(i)
                break

    return _count

print(analis(arr1, arr2))
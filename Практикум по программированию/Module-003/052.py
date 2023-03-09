'''
Структура set
Напишите программу, которая будет выполнять последовательность запросов 
вида ADD num, PRESENT num и COUNT (без параметра). Программу обязательно 
следует писать с использованием шаблонного типа set.

Выполнение каждого запроса вида ADD num должно добавлять элемент num 
во множество (если такой элемент уже есть, добавление ещё одной копии 
не изменяет множество), на экран при этом ничего не выводится.

При выполнении каждого запроса вида PRESENT num должно выдаваться 
сообщение «YES» или «NO» (большими буквами, в отдельной строке), 
соответственно тому, есть ли такой элемент во множестве; значение множества 
при этом не изменяется.

При выполнении каждого запроса вида COUNT должна выдаваться на экран в 
отдельной строке текущее количество различных элементов в множестве; 
значение множества при этом не изменяется.

Входные данные
В первой строке стандартного входного потока задано количество запросов N (1 < N < 100000), 
далее следуют N строк, каждая из которых содержит по одному запросу согласно описанного формата.

Значения чисел не превышают по модулю 100000000.

Выходные данные
Выводите на стандартный выход (экран) в отдельных строках результаты запросов 
PRESENT и COUNT; на запросы ADD ничего выводить не надо.

Sample Input:
7
ADD 5
ADD 7
COUNT
PRESENT 3
PRESENT 5
ADD 3
COUNT
Sample Output:
2
NO
YES
3
'''
import sys
from collections import namedtuple

# sys.stdin = open(file='052.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

request = namedtuple('request', ('req', 'n'))
arr = tuple(
        request(
            req=i.split()[0], 
            n=int(i.split()[-1]) if i.split()[-1].isdigit() else i.split()[-1]
        ) for i in arr
    )
# print(arr) # test

_set = set()
_list = list()
for _request in arr:
    if 'ADD' == _request.req:
        _set.add(_request.n)
    elif 'COUNT' == _request.req:
        _list.append(len(_set))
    elif 'PRESENT' == _request.req:
        _list.append(('NO', 'YES')[_request.n in _set])
print(*_list, sep='\n')
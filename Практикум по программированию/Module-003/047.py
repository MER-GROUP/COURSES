'''
Лучшие учащиеся
Определите учащихся с наилучшей успеваемостью, то есть с максимальным 
средним баллом по трем предметам. Выведите всех учащихся, 
имеющих максимальный средний балл.

Входные данные
Заданы сначала количество учащихся n, затем n строк, каждая 
из которых содержит фамилию, имя и три числа (оценки по трем предметам: 
математике, физике, информатике). Данные в строке разделены одним пробелом. 
Оценки принимают значение от 1 до 5.

Выходные данные
Необходимо вывести пары фамилия-имя по одной на строке, разделяя фамилию 
и имя одним пробелом. Выводить оценки не нужно. Порядок вывода должен 
быть таким же, как в исходных данных.

Sample Input:
2
Markov Valeriy 1 1 1
Petrov Sergey 5 5 5
Sample Output:
Petrov Sergey
'''
import sys
from collections import namedtuple
student = namedtuple('student', ('name', 'marks'))
from statistics import mean

# sys.stdin = open(file='047.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

arr = tuple(
    student(
        name=el.rsplit(' ', maxsplit=3)[0], 
        marks=[*map(int, el.rsplit(' ', maxsplit=3)[1:])]
    ) for el in arr
)
# print(*arr) # test

max_mean = mean(max(arr, key=lambda x: mean(x.marks)).marks)
print(
    *map(
        lambda x: x.name,
        filter(
            lambda x: mean(x.marks) == max_mean,
            arr
        )
    ),
    sep='\n'
)
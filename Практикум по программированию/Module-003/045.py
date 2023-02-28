'''
Средний балл по предметам
Определите средний балл всех учащихся по каждому предмету.

Входные данные
Заданы сначала количество учащихся n, затем n строк, 
каждая из которых содержит фамилию, имя и три числа 
(оценки по трем предметам: математике, физике, информатике). 
Данные в строке разделены одним пробелом. 
Оценки принимают значение от 1 до 5.

Выходные данные
Выведите три действительных числа (до 15  значащих цифр после запятой): 
средний балл всех учащихся по математике, по физике, по информатике.

Sample Input:
2
Markov Valeriy 4 5 2
Kozlov Georgiy 5 1 2
Sample Output:
4.5 3.0 2.0
'''
import sys
from collections import namedtuple
student = namedtuple('student', ('name', 'mathematics', 'physics', 'informatics'))
from statistics import mean

# sys.stdin = open(file='045.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

arr = tuple(student._make(map(str, el.rsplit(' ', maxsplit=3))) for el in arr)
# print(*arr) # test

_, mathematics, physics, informatics = zip(*arr)
print(
    float(mean(map(int, mathematics))),
    float(mean(map(int, physics))),
    float(mean(map(int, informatics)))
)
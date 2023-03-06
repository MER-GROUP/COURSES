'''
Отсортировать по среднему баллу
Выведите фамилии и имена учащихся в порядке убывания их среднего балла.

Входные данные

Заданы сначала количество учащихся n, затем n строк, каждая из которых 
содержит фамилию, имя и три числа (оценки по трем предметам: математике, 
физике, информатике). Данные в строке разделены одним пробелом. 
Оценки принимают значение от 1 до 5.

Общее число учащихся не превосходит 100001.

Выходные данные

Необходимо вывести пары фамилия-имя по одной на строке, 
разделяя фамилию и имя одним пробелом. Выводить оценки не нужно. 
Если несколько учащихся имеют одинаковые средние баллы, 
то их нужно выводить в порядке, заданном во входных данных.

Sample Input:
2
Markov Valeriy 1 1 1
Ivanov Ivan 2 2 2
Sample Output:
Ivanov Ivan
Markov Valeriy
'''
import sys
from collections import namedtuple, defaultdict
student = namedtuple('student', ('name', 'marks'))
from statistics import mean

# sys.stdin = open(file='049.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

arr = tuple(
    student(
        name=el.rsplit(' ', maxsplit=3)[0], 
        marks=[*map(int, el.rsplit(' ', maxsplit=3)[1:])]
    ) for el in arr
)
# print(*arr) # test

[print(k) for k, _ in sorted(arr, key=lambda x: mean(x.marks), reverse=True)]
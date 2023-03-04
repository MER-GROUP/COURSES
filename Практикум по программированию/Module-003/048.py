'''
Трое лучших
Определите трех учащихся с наилучшим средним баллом по трем предметам. 
Выведите фамилии и имена этих учащихся. Если при этом у нескольких учащихся 
средний балл совпадает со средним баллом учащегося, "занявшего 3-е место", 
то необходимо вывести их всех.

Входные данные
Заданы сначала количество учащихся n, затем n строк, каждая из которых 
содержит фамилию, имя и три числа (оценки по трем предметам: математике, 
физике, информатике). Данные в строке разделены одним пробелом. 
Оценки принимают значение от 1 до 5.

Выходные данные
Необходимо вывести пары фамилия-имя по одной на строке, разделяя фамилию 
и имя одним пробелом. Выводить оценки не нужно. Порядок вывода должен быть 
таким же, как в исходных данных.

Sample Input 1:
3
Yakovlev Ivan 5 5 5
Yapryntsev Aleksey 5 5 5
Kozlov Georgiy 5 5 5
Sample Output 1:
Yakovlev Ivan
Yapryntsev Aleksey
Kozlov Georgiy

Sample Input 2:
10
Krasnov Ivan 3 3 3
Shusha Andrey 1 2 4
Ivanov Petr 2 5 3
Markov Valeriy 2 3 5
Petrov Sergey 1 2 1
Garkov Vanya 4 5 1
Radov Stepan 3 2 1
Korod Zenya 1 5 5
Solovey Gavrila 5 5 1
Zubok Anton 3 5 4
Sample Output 2:
Korod Zenya
Solovey Gavrila
Zubok Anton
'''
import sys
from collections import namedtuple, defaultdict
student = namedtuple('student', ('name', 'marks'))
from statistics import mean

sys.stdin = open(file='048.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

arr = tuple(
    student(
        name=el.rsplit(' ', maxsplit=3)[0], 
        marks=[*map(int, el.rsplit(' ', maxsplit=3)[1:])]
    ) for el in arr
)
# print(*arr) # test

dictonary = defaultdict(list)
[dictonary[mean(v)].append(k) for k, v in arr]

mean_1_3 = sorted(dictonary.items(), reverse=True)[:3]
print(mean_1_3) # test
student_count = sum(len(i) for _, i in mean_1_3)
print(student_count) # test
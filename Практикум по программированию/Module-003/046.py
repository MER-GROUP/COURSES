'''
Учащиеся без троек
Выведите фамилии и имена учащихся, не имеющих троек (а также двоек и колов).

Входные данные
Заданы сначала количество учащихся n, затем n строк, 
каждая из которых содержит фамилию, имя и три числа 
(оценки по трем предметам: математике, физике, информатике). 
Данные в строке разделены одним пробелом. Оценки принимают значение от 1 до 5.

Выходные данные
Необходимо вывести пары фамилия-имя по одной на строке, 
разделяя фамилию и имя одним пробелом. Выводить оценки не нужно. 
Порядок вывода должен быть таким же, как в исходных данных.

Sample Input 1:
3
Babat Anna 5 4 3
Belova Galina 4 3 5
Moroz Yaroslav 3 5 4
Sample Output 1:

Sample Input 2:
2
Krasnov Ivan 5 5 5
Shusha Andrey 1 2 4
Sample Output 2:
Krasnov Ivan
'''
import sys
from collections import namedtuple
student = namedtuple('student', ('name', 'marks'))

# sys.stdin = open(file='046.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

arr = tuple(
    student(
        name=el.rsplit(' ', maxsplit=3)[0], 
        marks=[*map(int, el.rsplit(' ', maxsplit=3)[1:])]
    ) for el in arr
)
# print(*arr) # test

print(
    *map(
        lambda x: x.name,
        filter(
            lambda x: 1 not in x.marks and 2 not in x.marks and 3 not in x.marks,
            arr
        )
    ),
    sep='\n'
)
'''
Размах данных
Дана последовательность дат. Напишите программу, 
которая выводит количество дней между максимальной 
и минимальной датами данной последовательности.

Формат входных данных
На вход программе подается произвольное количество строк, 
в каждой строке записана дата в ISO формате (YYYY-MM-DD).

Формат выходных данных
Программа должна вывести единственное число — количество дней 
между максимальной и минимальной датами введенной последовательности.

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/520159/tests_2534822.zip

Sample Input 1:
2022-06-15
2022-06-12
2022-06-16
2022-06-30
Sample Output 1:
18

Sample Input 2:
2077-01-01
2077-01-01
2077-01-01
Sample Output 2:
0
'''
import sys
from datetime import datetime

arr = list(
    map(
        datetime.fromisoformat, 
        map(
            str.strip,
            sys.stdin.readlines()
        )
    )
)
# arr = list(map(datetime.fromisoformat, [input() for i in range(4)]))
print((max(arr) - min(arr)).days)
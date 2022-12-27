'''
Календарь на месяц
Напишите программу, которая выводит календарь на заданные год и месяц.

Формат входных данных
На вход программе подаются год и сокращенное 
название месяца на английском, разделенные пробелом.

Формат выходных данных
Программа должна вывести календарь на введенные год и месяц.

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570049/tests_2580730.zip

Sample Input:
2021 Dec
Sample Output:
   December 2021
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
'''
from datetime import datetime
from calendar import month

pattern = '%Y %b'
d = datetime.strptime(input(), pattern).date()
print(month(d.year, d.month))
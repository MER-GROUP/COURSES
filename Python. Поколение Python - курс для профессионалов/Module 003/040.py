'''
Сотрудники организации 3 😔
Дан список сотрудников организации, в котором указаны их фамилии, 
имена и даты рождения. Напишите программу, которая определяет 
самого молодого сотрудника, празднующего свой день рождения 
в течение ближайших семи дней от текущей даты.

Формат входных данных
На вход программе в первой строке подается текущая дата 
в формате DD.MM.YYYY, в следующей строке вводится натуральное 
число n — количество сотрудников, работающих в организации. 
В последующих n строках вводятся данные о каждом сотруднике: 
имя, фамилия и дата рождения, разделённые пробелом. 
Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна определить самого молодого сотрудника, 
празднующего свой день рождения в течение ближайших семи дней, 
и вывести его имя и фамилию, разделив пробелом. 
Если таких сотрудников нет, программа должна вывести текст:

Дни рождения не планируются

Примечание 1. Гарантируется, что у всех сотрудников даты рождения различны.

Примечание 2. Например, для даты 01.11.2021 ближайшими семью днями являются:

02.11.2021, 03.11.2021, 04.11.2021, 05.11.2021, 06.11.2021, 07.11.2021, 08.11.2021

Примечание 3. Тестовые данные доступны по ссылке. 
https://stepik.org/media/attachments/lesson/571244/tests_2506825.zip

Sample Input 1:
14.11.2021
3
Иван Петров 16.11.1995
Петр Сергеев 14.11.1997
Сергей Романов 17.11.1994
Sample Output 1:
Иван Петров

Sample Input 2:
14.11.2021
3
Иван Петров 25.12.1995
Петр Сергеев 24.11.1997
Сергей Романов 28.12.1994
Sample Output 2:
Дни рождения не планируются

Sample Input 3:
10.11.2021
5
Иван Петров 11.11.1995
Петр Сергеев 12.11.1992
Сергей Романов 13.11.1996
Роман Григорьев 14.11.1994
Григорий Иванов 15.11.1995
Sample Output 3:
Сергей Романов

Sample Input 4:
29.11.2021
5
Иван Петров 01.12.1995
Петр Сергеев 29.11.1992
Сергей Романов 30.11.1993
Роман Григорьев 03.12.1994
Григорий Иванов 16.07.1995
Sample Output 4:
Иван Петров

Sample Input 5:
29.12.2021
4
Иван Петров 30.12.1995
Петр Сергеев 04.01.1997
Сергей Романов 03.01.1994
Маша Иванова 31.12.1996
Sample Output 5:
Петр Сергеев
'''
from datetime import datetime

current_date = datetime.strptime(input(), '%d.%m.%Y').date()
current_date_future = current_date.replace(year=current_date.year + 1)
arr, data_base = [input().rsplit(' ', 1) for i in range(int(input()))], {}
max_year = datetime.min.date()
for i in arr:
    if datetime.strptime(i[1], '%d.%m.%Y').date().month < current_date.month:
        if 1 <= abs(datetime.strptime(i[1], '%d.%m.%Y').date().replace(year=current_date_future.year) - current_date).days <= 7:
            if max_year < datetime.strptime(i[1], '%d.%m.%Y').date():
                max_year = datetime.strptime(i[1], '%d.%m.%Y').date()
            data_base.setdefault(
                datetime.strptime(i[1], '%d.%m.%Y').date(), 
                []
            ).append(*i[:-1])
    else:
        if 1 <= abs(datetime.strptime(i[1], '%d.%m.%Y').date().replace(year=current_date.year) - current_date).days <= 7:
            if max_year < datetime.strptime(i[1], '%d.%m.%Y').date():
                max_year = datetime.strptime(i[1], '%d.%m.%Y').date()
            data_base.setdefault(
                datetime.strptime(i[1], '%d.%m.%Y').date(), 
                []
            ).append(*i[:-1])

data_base_sorted = dict()
for k, v in sorted(data_base.items()):
    if max_year.year == k.year:
        if current_date.month <= k.month:
            data_base_sorted[k.replace(year=current_date.year)] = v
        else:
            data_base_sorted[k.replace(year=current_date_future.year)] = v

for key in data_base_sorted.keys():
    if 1 <= abs(key - current_date).days <= 7:
        print(*data_base_sorted[key])
        break
else:
    print('Дни рождения не планируются')
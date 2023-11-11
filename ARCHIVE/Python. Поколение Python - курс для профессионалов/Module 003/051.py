'''
ТЧМ
Во многих музеях существует один день месяца, 
когда посещение музея для всех лиц или отдельных 
категорий граждан происходит без взимания платы. 
Например, в Эрмитаже это третий четверг месяца.

Напишите программу, которая определяет даты 
бесплатных дней посещения Эрмитажа в заданном году.

Формат входных данных
На вход программе подается натуральное число, представляющее год.

Формат выходных данных
Программа должна определить все даты бесплатных дней 
посещения Эрмитажа в введенном году и вывести их. 
Даты должны быть расположены в порядке возрастания, 
каждая на отдельной строке, в формате DD.MM.YYYY.

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570049/tests_2361914.zip

Sample Input 1:
2021
Sample Output 1:
21.01.2021
18.02.2021
18.03.2021
15.04.2021
20.05.2021
17.06.2021
15.07.2021
19.08.2021
16.09.2021
21.10.2021
18.11.2021
16.12.2021

Sample Input 2:
2020
Sample Output 2:
16.01.2020
20.02.2020
19.03.2020
16.04.2020
21.05.2020
18.06.2020
16.07.2020
20.08.2020
17.09.2020
15.10.2020
19.11.2020
17.12.2020
'''
import calendar
from datetime import date

def get_all_mondays(year):
    thursday = list()
    calendar.setfirstweekday(list(calendar.day_name).index('Thursday'))
    for month in range(1, len(calendar.month_name)):
        arr = list()
        for week in calendar.monthcalendar(year, month):
            thu = week[0]
            if thu:
                arr.append(date(year, month, thu))
        thursday.append(arr[2].strftime('%d.%m.%Y'))
    return thursday

if __name__ == '__main__':
    print(*get_all_mondays(int(input())), sep='\n')
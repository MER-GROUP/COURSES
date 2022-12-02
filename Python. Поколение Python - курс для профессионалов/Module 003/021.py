'''
Ученики онлайн-школы BEEGEEK решили выяснить, 
кто из них быстрее всех решит домашнее задание по математике. 
Для этого каждый ученик зафиксировал время начала 
и окончания решения своей домашней работы.

Вам доступен словарь data, содержащий результаты учеников. 
Ключом в словаре является имя ученика, а значением — кортеж, 
первый элемент которого — время начала решения, 
второй элемент — время окончания решения. 
Дополните приведенный ниже код, чтобы он вывел имя ученика, 
который затратил на решение домашнего задания меньше всего времени.

Примечание 1. Гарантируется, что искомый ученик единственный.

Примечание 2. Дата-времена в кортежах представлены 
в виде строк в формате DD.MM.YYYY HH:MM:SS.
'''
from datetime import datetime

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

for k, v in data.items():
    data[k] = abs(int(
        datetime.strptime(v[0], '%d.%m.%Y %H:%M:%S').timestamp() - \
        datetime.strptime(v[1], '%d.%m.%Y %H:%M:%S').timestamp()
    ))

print(
    min(
        data.items(),
        key=lambda x: x[1]
    )[0]
)
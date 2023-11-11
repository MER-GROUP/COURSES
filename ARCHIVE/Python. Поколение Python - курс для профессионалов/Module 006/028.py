'''
Here we go again
Вам доступен файл name_log.csv, в котором находятся логи изменения 
имени пользователя. В первом столбце записано измененное имя пользователя, 
во втором — адрес электронной почты, в третьем — дата и время изменения. 
При этом email пользователь менять не может, только имя:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...

Напишите программу, которая определяет, сколько раз пользователь менял имя. 
Программа должна вывести адреса электронных почт пользователей, 
указав для каждого соответствующее количество смененных имен. 
Почтовые ящики должны быть расположены в лексикографическом порядке, 
каждый на отдельной строке, в следующем формате:

<адрес электронной почты>: <количество изменений имен>

Примечание 1. Начальная часть ответа выглядит так:

barbaraanderson@bk.ru: 3
barbarabrown@rambler.ru: 3
...

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/635441/name_log.csv
https://stepik.org/media/attachments/lesson/635441/clue_here_we.txt

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
'''
from collections import Counter
import csv

# with open(file='028-name_log.csv', mode='rt', encoding='utf-8', newline='') as file_opener:
with open(file='name_log.csv', mode='rt', encoding='utf-8', newline='') as file_opener:
    csv_opener = csv.DictReader(f=file_opener, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
    _counter = Counter(_dict[csv_opener.fieldnames[1]] for _dict in csv_opener)
[print(f'{_key}: {_counter[_key]}') for _key in sorted(_counter)]
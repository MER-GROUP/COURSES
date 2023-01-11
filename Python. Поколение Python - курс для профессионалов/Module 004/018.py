'''
Лог-файл
Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. 
В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты, 
в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...
Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи 
для каждого пользователя и записывает их в файл new_name_log.csv. В файле new_name_log.csv 
первой строкой должны быть заголовки столбцов такие же, как в файле name_log.csv. 
Логи в итоговом файле должны быть расположены в лексикографическом порядке 
названий электронных ящиков пользователей.

Примечание 1. Для части пользователей в исходном файле запись только одна, и тогда 
в итоговый файл следует записать только ее, для некоторых пользователей 
есть несколько записей с разными именами.

Например, пользователь с электронной почтой c3po@gmail.com несколько раз менял имя:

C=3PO,c3po@gmail.com,16/11/2021 17:10
C3PO,c3po@gmail.com,16/11/2021 17:15
C-3PO,c3po@gmail.com,16/11/2021 17:24

Из этих трех записей в итоговый файл должна быть записана только одна — самая свежая:

C-3PO,c3po@gmail.com,16/11/2021 17:24

Примечание 2. Разделителем в файле name_log.csv является запятая, при этом кавычки не используются.

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/518491/name_log.csv
https://stepik.org/media/attachments/lesson/518491/clue_log.txt

Примечание 4. Начальная часть файла new_name_log.csv выглядит так:

username,email,dtime
angry-barbara2,barbaraanderson@bk.ru,17/11/2021 01:17
dead-barbara6,barbarabrown@rambler.ru,27/11/2021 08:27
busy_barbara7,barbaradavis@aol.com,24/11/2021 08:24
...

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''
import csv
from datetime import datetime

# with open(file='018-name_log.csv', mode='rt', encoding='utf-8', newline='') as file_opener,\
with open(file='name_log.csv', mode='rt', encoding='utf-8', newline='') as file_opener,\
    open(file='new_name_log.csv', mode='wt', encoding='utf-8', newline='') as file_writener:
        csv_opener = csv.reader(file_opener)
        fieldnames = next(csv_opener)
        # print(fieldnames) # test

        dictonary = dict()
        pattern = '%d/%m/%Y %H:%M'
        [dictonary.setdefault(email, []).append(
            (datetime.strptime(dtime, pattern), username)
            ) for username, email, dtime in csv_opener]
        # [print(f'{k} = {v}') for k, v in dictonary.items()] # test

        csv_writener = csv.DictWriter(file_writener, fieldnames=fieldnames)
        csv_writener.writeheader()
        csv_writener.writerows(
            [{fieldnames[0]: max(v, key=lambda x: x[0])[1], \
                fieldnames[1]: k, 
                fieldnames[2]: max(v, key=lambda x: x[0])[0].strftime(pattern)} \
                    for k, v in sorted(dictonary.items(), key=lambda x: x[0])]
        )
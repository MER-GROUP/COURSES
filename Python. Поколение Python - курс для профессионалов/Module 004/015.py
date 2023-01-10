'''
Популярные домены
Вам доступен файл data.csv, который содержит неповторяющиеся данные 
о пользователях некоторого ресурса. В первом столбце записано имя пользователя, 
во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...

Напишите программу, которая создает файл domain_usage.csv, 
имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...

где в первом столбце записано название почтового домена, 
а во втором — количество пользователей, использующих данный домен. 
Домены в файле должны быть расположены в порядке возрастания 
количества их использований, при совпадении количества 
использований — в лексикографическом порядке.

Примечание 1. Разделителем в файле data.csv является запятая, 
при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/518491/data.csv
https://stepik.org/media/attachments/lesson/518491/clue_domains.txt

Примечание 3. Начальная часть файла domain_usage.csv выглядит так:

domain,count
rambler.ru,24
iCloud.com,29
...
Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''
import csv

# with open('015-data.csv', 'rt', encoding='utf-8', newline='') as file_opener:
with open('data.csv', 'rt', encoding='utf-8', newline='') as file_opener:
    csv_opener = csv.DictReader(file_opener)

    db = dict()
    for d in csv_opener:
        key = d[csv_opener.fieldnames[2]].split('@')[1]
        db[key] = db.get(key, 0) + 1

fieldnames = ['domain', 'count']

with open('domain_usage.csv', 'wt', encoding='utf-8', newline='') as file_writener:
    csv_writener = csv.DictWriter(file_writener, fieldnames=fieldnames)
    csv_writener.writeheader()
    csv_writener.writerows(
        [{fieldnames[0]: v1, fieldnames[1]: v2} for v1, v2 in sorted(
            db.items(), key=lambda x: (x[1], x[0])
        )]
    )
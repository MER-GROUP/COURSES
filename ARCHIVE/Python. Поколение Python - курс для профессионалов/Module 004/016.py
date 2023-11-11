'''
Wi-Fi Москвы
Вам доступен файл wifi.csv, который содержит данные о городском Wi-Fi Москвы. 
В первом столбце записано название округа, во втором – название района, 
в третьем — адрес, в четвертом — количество точек доступа по этому адресу:

adm_area;district;location;number_of_access_points
Центральный административный округ;район Якиманка;город Москва, улица Серафимовича, дом 5/16;5
Центральный административный округ;район Якиманка;город Москва, Болотная набережная, дом 11, строение 1;2
...

Напишите программу, которая определяет количество точек доступа в каждом районе Москвы 
и выводит названия всех районов, для каждого указывая соответствующее количество точек доступа, 
каждое на отдельной строке, в следующем формате:

<название района>: <количество точек доступа>
Названия районов должны быть расположены в порядке убывания количества точек доступа, 
при совпадении количества точек доступа — в лексикографическом порядке.

Примечание 1. Разделителем в файле wifi.csv является точка с запятой, 
при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/518491/wifi.csv
https://stepik.org/media/attachments/lesson/518491/clue_wifi.txt

Примечание 3. Начальная часть ответа выглядит так:

Тверской район: 480
район Хамовники: 386
Пресненский район: 349
...

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''
import csv

# with open('016-wifi.csv', 'rt', encoding='utf-8', newline='') as file_opener:
with open('wifi.csv', 'rt', encoding='utf-8', newline='') as file_opener:
    csv_opener = csv.DictReader(f=file_opener, delimiter=';')
    db = dict()
    [db.setdefault(
        d[csv_opener.fieldnames[1]], list()).append(
            int(d[csv_opener.fieldnames[3]])
    ) for d in csv_opener]
    # print(db) # test

arr = sorted(
    map(
        lambda x: (x[0], sum(x[1])),
        db.items()
    ),
    key= lambda x: (x[1], x[0])
)
# print(arr) # test

dictonary = dict()
[dictonary.setdefault(k, []).append(v) for v, k in arr]
for k, v in sorted(dictonary.items(), reverse=True):
    if 1 < len(v):
        for line in v:
            print(f'{line}: {k}')
    else:
        print(f'{v[0]}: {k}')
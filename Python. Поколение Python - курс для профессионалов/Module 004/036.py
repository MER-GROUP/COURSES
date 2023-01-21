'''
Результаты экзамена 🌶️
Вам доступен файл exam_results.csv, который содержит информацию о прошедшем 
экзамене в некотором учебном заведении. В первом столбце записано имя студента, 
во втором — фамилия, в третьем — оценка за экзамен, в четвертом — дата и время 
сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:

name,surname,score,date_and_time,email
Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
...

Каждый студент имеет право пересдать экзамен два раза, поэтому он может 
встречаться в исходном файле до трёх раз с различной оценкой и различными 
датой и временем сдачи.

Напишите программу, которая для каждого студента определяет его максимальную оценку, 
а также дату и время ее получения. Программа должна создать список словарей, 
каждый из которых содержит следующие пары ключ-значение:

name — имя студента
surname — фамилия студента
best_score — максимальная оценка за экзамен
date_and_time — дата и время получения максимальной оценки в исходном формате
email — адрес электронной почты

Полученный список программа должна записать в файл best_scores.json, причем словари 
в списке должны быть расположены в лексикографическом порядке названий электронных почт.

Примечание 1. Если при пересдаче студент получил такую же оценку, что и в прошлый раз, 
то в качестве даты следует указать дату пересдачи.

Примечание 2. В качестве разделителя в файле exam_results.csv используется запятая, 
при этом кавычки не используются.

Примечание 3. Начальная часть файла best_scores.json выглядит так:

[
   {
      "name": "Stephen",
      "surname": "Farley",
      "best_score": 3,
      "date_and_time": "2021-11-12 12:00:00",
      "email": "aardo@mac.com"
   },
   {
      "name": "Kaylen",
      "surname": "Horne",
      "best_score": 4,
      "date_and_time": "2021-11-09 11:00:00",
      "email": "aaribaud@att.net"
   },
   ...
]

Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/exam_results.csv
https://stepik.org/media/attachments/lesson/623073/clue_exam_results.txt

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''
import json, csv
# from operator import itemgetter
from datetime import datetime
pattern = '%Y-%m-%d %H:%M:%S'

# with open(file='036-exam_results.csv', mode='rt', encoding='utf-8', newline='') as file_opener,\
with open(file='exam_results.csv', mode='rt', encoding='utf-8', newline='') as file_opener,\
    open(file='best_scores.json', mode='wt', encoding='utf-8', newline='') as file_writener:
    exam_results_iter_dicts = csv.DictReader(f=file_opener, delimiter=',', quoting=csv.QUOTE_NONE)
    # print(*exam_results_iter_dicts) # test

    scores_dict_dicts = dict()
    for d in exam_results_iter_dicts:
        key = f'{d["name"]} {d["surname"]}'
        if key not in scores_dict_dicts:
            # scores_dict_dicts[key] = d
            d0 = {
                    "name": tuple(d.values())[0],
                    "surname": tuple(d.values())[1],
                    "best_score": int(tuple(d.values())[2]),
                    "date_and_time": tuple(d.values())[3],
                    "email": tuple(d.values())[4],
                }
            scores_dict_dicts[key] = d0
        else:
            # if int(d["score"]) >= int(scores_dict_dicts[key]["score"]):
            # if int(d["score"]) >= int(scores_dict_dicts[key]["best_score"]):
            if int(d["score"]) >= int(scores_dict_dicts[key]["best_score"]) and\
                datetime.strptime(d["date_and_time"], pattern) >= \
                datetime.strptime(scores_dict_dicts[key]["date_and_time"], pattern):
                # scores_dict_dicts[key] = d
                d1 = {
                    "name": tuple(d.values())[0],
                    "surname": tuple(d.values())[1],
                    "best_score": int(tuple(d.values())[2]),
                    "date_and_time": tuple(d.values())[3],
                    "email": tuple(d.values())[4],
                }
                scores_dict_dicts[key] = d1
    # [print(k, v) for k, v in scores_dict_dicts.items()] # test

    json.dump(
        [d for d in sorted(
            scores_dict_dicts.values(), 
            # key=itemgetter('email')
            key=lambda x: x['email']
            )],
        fp=file_writener,indent=3
    )
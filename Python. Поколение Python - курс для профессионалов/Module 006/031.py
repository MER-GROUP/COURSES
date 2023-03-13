'''
Бесплатные курсы берут свое 😢
Для дополнительного заработка Тимур решил заняться продажей овощей. 
У него имеются данные о продажах за год, разделенные на четыре файла 
по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv. 
В каждом файле в первом столбце указывается название продукта, 
а в последующих — количество проданного продукта в килограммах за определенный месяц:

продукт,январь,февраль,март
Картофель,39,61,3
Дайкон,51,96,83
...

Также присутствует файл prices.json, содержащий словарь, 
в котором ключом является название продукта, а значением — цена за килограмм в рублях:

{
   "Картофель": 53,
   "Дайкон": 55,
...
}

Напишите программу, которая выводит единственное число — сумму, 
заработанную Тимуром за год на продаже овощей.

Примечание 1. Ссылки на указанные файлы: quarter1.csv, quarter2.csv, 
quarter3.csv, quarter4.csv, prices.json. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/635441/quarter1.csv
https://stepik.org/media/attachments/lesson/635441/quarter2.csv
https://stepik.org/media/attachments/lesson/635441/quarter3.csv
https://stepik.org/media/attachments/lesson/635441/quarter4.csv
https://stepik.org/media/attachments/lesson/635441/prices.json
https://stepik.org/media/attachments/lesson/635441/clue_free.txt

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
'''
from collections import Counter
import csv, json

# with open(file='031-quarter1.csv', mode='rt', encoding='utf-8', newline='') as _csv_1,\
#     open(file='031-quarter2.csv', mode='rt', encoding='utf-8', newline='') as _csv_2,\
#     open(file='031-quarter3.csv', mode='rt', encoding='utf-8', newline='') as _csv_3,\
#     open(file='031-quarter4.csv', mode='rt', encoding='utf-8', newline='') as _csv_4,\
#     open(file='031-prices.json', mode='rt', encoding='utf-8', newline='') as _json_1:
with open(file='quarter1.csv', mode='rt', encoding='utf-8', newline='') as _csv_1,\
    open(file='quarter2.csv', mode='rt', encoding='utf-8', newline='') as _csv_2,\
    open(file='quarter3.csv', mode='rt', encoding='utf-8', newline='') as _csv_3,\
    open(file='quarter4.csv', mode='rt', encoding='utf-8', newline='') as _csv_4,\
    open(file='prices.json', mode='rt', encoding='utf-8', newline='') as _json_1:
    
    _coounter = Counter()
    for k, *v in tuple(csv.reader(_csv_1, delimiter=','))[1:]:
        _coounter.update({k: sum(map(int, v))})
    for k, *v in tuple(csv.reader(_csv_2, delimiter=','))[1:]:
        _coounter.update({k: sum(map(int, v))})
    for k, *v in tuple(csv.reader(_csv_3, delimiter=','))[1:]:
        _coounter.update({k: sum(map(int, v))})
    for k, *v in tuple(csv.reader(_csv_4, delimiter=','))[1:]:
        _coounter.update({k: sum(map(int, v))})
    # print(_coounter) # test

    _dict = json.load(fp=_json_1)
    _sum = int()
    for k, v in _coounter.most_common():
        _sum += _dict[k] * v
    print(_sum)
'''
Разные типы
Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]

Напишите программу, которая создает список, элементами которого являются объекты из списка, 
содержащегося в файле data.json, измененные по следующим правилам:

если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическое значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
если объект является пустым значением (null), он не добавляется

Полученный список программа должна записать в файл updated_data.json.

Примечание 1. Например, если бы файл data.json имел вид:

["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]

то программа должна была бы создать файл updated_data.json со следующим содержанием:

["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/data.json
https://stepik.org/media/attachments/lesson/623073/clue_different_types.txt

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
'''
import json

# with open(file='029-data.json', mode='rt', encoding='utf-8', newline='') as file_opener,\
with open(file='data.json', mode='rt', encoding='utf-8', newline='') as file_opener,\
    open(file='updated_data.json', mode='wt', encoding='utf-8', newline='') as file_writener:
    json_opener = json.load(file_opener, )

    i = 0
    while i < len(json_opener):
        if isinstance(json_opener[i], str):
            json_opener[i] = f'{json_opener[i]}!'
        elif isinstance(json_opener[i], bool):
            json_opener[i] = not json_opener[i]
        elif isinstance(json_opener[i], int):
            json_opener[i] += 1 
        elif isinstance(json_opener[i], list):
            json_opener[i] = json_opener[i] * 2
        elif isinstance(json_opener[i], dict):
            json_opener[i].update({"newkey": None})
        else:
            del json_opener[i]
            continue
        i += 1

    json.dump(json_opener, file_writener)
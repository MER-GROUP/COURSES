'''
Объединение объектов
Вам доступны два файла data1.json и data2.json, каждый из которых содержит 
по единственному JSON-объекту:

{
   "Holly-Anne": [
      33,
      "failed"
   ],
   "Caty": [
      36,
      "failed"
   ],
   ...
}

Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, 
причем если пары из первого и второго объектов имеют совпадающие ключи, 
то значение следует взять из второго объекта. Полученный JSON-объект программа должна записать 
в файл data_merge.json.

Примечание 1. Например, если бы файлы data1.json и data2.json имели вид:

{
   "Timur": 99,
   "Anri": 97
}
{
   "Dima": 99,
   "Anri": 100
}

то программа должна была бы создать файл data_merge.json со следующим содержанием:

{
   "Anri": 100,
   "Dima": 99,
   "Timur": 99
}

Примечание 2. Элементы в результирующем JSON-объекте могут располагаться в произвольном порядке.

Примечание 3. Указанные файлы доступны по ссылке и ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/data1.json
https://stepik.org/media/attachments/lesson/623073/data2.json
https://stepik.org/media/attachments/lesson/623073/clue_data_merge.txt

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''
import json

# with open(file='030-data1.json', mode='rt', encoding='utf-8', newline='') as file_opener_1,\
#     open(file='030-data2.json', mode='rt', encoding='utf-8', newline='') as file_opener_2,\
with open(file='data1.json', mode='rt', encoding='utf-8', newline='') as file_opener_1,\
    open(file='data2.json', mode='rt', encoding='utf-8', newline='') as file_opener_2,\
    open(file='data_merge.json', mode='wt', encoding='utf-8', newline='') as file_writener:
    dictonary = json.load(file_opener_1)
    dictonary.update(json.load(file_opener_2))
    json.dump(dictonary, file_writener, indent=4)
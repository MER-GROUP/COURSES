'''
Восстановление недостающих ключей
Вам доступен файл people.json, содержащий список JSON-объектов. Причем у различных объектов может быть различное количество ключей:

[
   {
      "age": 33,
      "country": "Lesotho",
      "phone": "(927) 316-2249",
      "family_status": "married",
      "email": "neonatus@outlook.com"
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey",
      "children": "yes",
      "email": "ismail@gmail.com",
      "university": "Khalifa University",
      "family_status": "married"
   },
   ...
]

Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи, присваивая этим ключам значение null. Ключ считается недостающим, если он присутствует в каком-либо другом объекте, но отсутствует в данном. Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json.

Примечание 1. JSON-объекты в создаваемом программой списке должны располагаться в своем исходном порядке. Порядок ключей в JSON-объектах не важен.

Примечание 2. Например, если бы файл people.json имел вид:

[
   {
      "age": 33,
      "country": "Lesotho"
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey"
   }
]

то программа должна была создать файла updated_people.json со следующим содержанием:

[
   {   
      "age": 33,
      "country": "Lesotho"
      "name": null
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey"
   }
]

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/people.json
https://stepik.org/media/attachments/lesson/623073/clue_updated_people.txt

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''
import json

# with open(file='031-people.json', mode='rt', encoding='utf-8', newline='') as file_opener,\
with open(file='people.json', mode='rt', encoding='utf-8', newline='') as file_opener,\
    open(file='updated_people.json', mode='wt', encoding='utf-8', newline='') as file_writener:
    list_dict = json.load(file_opener)
    max_dict = max(list_dict, key=len)
    
    for i, dictonary in enumerate(list_dict):
        for key in max_dict.keys():
            if key not in dictonary.keys():
                list_dict[i].update({key: None})

    json.dump(list_dict, file_writener, indent=4)
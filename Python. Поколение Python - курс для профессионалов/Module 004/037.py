'''
Общественное питание 😥
Вам доступен файл food_services.json, содержащий список JSON-объектов, 
которые представляют данные о заведениях общественного питания:

[
   {
      "Name": "СМЕТАНА",
      "IsNetObject": "нет",
      "OperatingCompany": "",
      "TypeObject": "кафе",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Ярославский район",
      "Address": "город Москва, улица Егора Абакумова, дом 9",
      "SeatsCount": 48
   },
   ...
]

Под «заведением» будем подразумевать один JSON-объект из этого списка. 
У заведения имеются следующие атрибуты:

Name — название 
IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
OperatingCompany — название сети
TypeObject — вид (кафе, столовая, ресторан и т.д.)
AdmArea — административная зона
District — район
Address — полный адрес
SeatsCount — количество мест

Напишите программу, которая:

определяет район Москвы, в котором находится больше всего заведений, 
и выводит название этого района и количество заведений в нем
определяет сеть с самым большим числом заведений и выводит название 
этой сети и количество заведений этой сети
Полученные значения программа должна вывести в следующем формате:

<район>: <количество заведений>
<название сети>: <количество заведений>

Примечание 1. Гарантируется, что искомая сеть единственная.

Примечание 2. Пример вывода:

район Метрогородок: 456
Французская пекарня SeDelice: 144

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/food_services.json
https://stepik.org/media/attachments/lesson/623073/clue_food1.txt

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''
import json
from operator import itemgetter

# with open(file='037-food_services.json', mode='rt', encoding='utf-8', newline='') as file_opener:
with open(file='food_services.json', mode='rt', encoding='utf-8', newline='') as file_opener:
    district_dict = dict()
    name_dict = dict()
    for d in json.load(fp=file_opener):
        district_dict[d['District']] = district_dict.get(d['District'], 0) + 1
        if d['OperatingCompany']:
            name_dict[d['OperatingCompany']] = name_dict.get(d['OperatingCompany'], 0) + 1 

[print(f'{x[0]}: {x[1]}') for x in [max(district_dict.items(), key=itemgetter(1))]]
[print(f'{x[0]}: {x[1]}') for x in [max(name_dict.items(), key=itemgetter(1))]]
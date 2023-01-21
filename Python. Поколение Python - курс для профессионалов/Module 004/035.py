'''
Бассейны
Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, 
которые открыты в понедельник в период с 10:00 до 12:00. Также ему нравится плавать 
по длинным дорожкам, поэтому из всех работающих в это время бассейнов нужно 
выбрать бассейн с наибольшей длиной дорожки, при равных значениях — c наибольшей шириной.

Вам доступен файл pools.json, содержащий список JSON-объектов, 
которые представляют данные о крытых плавательных бассейнах:

[
   {
      "ObjectName": "Физкультурно-оздоровительный комплекс с бассейном «ГБУ «СШОР № 82» Москомспорта»",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Алтуфьевский район",
      "Address": "Инженерная улица, дом 5, корпус 1",
      "WorkingHoursSummer": {
         "Понедельник": "10:00-11:00",
         "Вторник": "10:00-11:00",
         "Среда": "10:00-11:00",
         "Четверг": "10:00-11:00",
         "Пятница": "10:00-11:00",
         "Суббота": "10:00-11:00",
         "Воскресенье": "09:00-15:00",
      },
      "DimensionsSummer": {
         "Square": 350,
         "Length": 25,
         "Width": 14,
         "Depth": 1.8
      }
   },
   ...
]

Под «бассейном» будем подразумевать один JSON-объект из этого списка. 
У бассейна имеются следующие атрибуты:

ObjectName — название, будь то фитнес клуб или спортивный комплекс
AdmArea — административный округ
District — название района
Address — адрес
WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина, 
Width — ширина, Depth — глубина

Напишите программу, которая определяет бассейн, подходящий Тимуру. 
Программа должна вывести его размеры и адрес в следующем формате:

<длина>x<ширина>
<адрес>

Примечание 1. Пример вывода:

25x16
Писцовая улица, дом 12, строение 1

Примечание 2. Бассейн должен быть открыт во время всего периода с 10:00 до 12:00. 
Например, если бассейн работает в 10:00, но не работает в 11:30, он не подходит.

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/pools.json
https://stepik.org/media/attachments/lesson/623073/clue_pools.txt

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''
import json
from datetime import datetime

pattern = '%H:%M'

# with open(file='035-pools.json', mode='rt', encoding='utf-8', newline='') as file_opener:
with open(file='pools.json', mode='rt', encoding='utf-8', newline='') as file_opener:
    pools_list_dicts = filter(
        lambda x: datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[0], pattern).time() <=\
            datetime.strptime('10:00', pattern).time() and\
            datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[1], pattern).time() >=\
            datetime.strptime('12:00', pattern).time(),
        json.load(fp=file_opener)
    )
# print(*pools_list_dicts) # test

pool = max(
    pools_list_dicts,
    key=lambda x: (int(x['DimensionsSummer']['Length']), int(x['DimensionsSummer']['Width']))
)
# print(pool) # test

print(f"{pool['DimensionsSummer']['Length']}x{pool['DimensionsSummer']['Width']}")
print(pool['Address'])
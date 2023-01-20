'''
Спортивные площадки
Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. 
В первом столбце записан тип площадки,  во втором — административный округ, 
в третьем — название района, в четвертом — адрес:

ObjectName;AdmArea;District;Address
Парк, озелененная городская территория «Лианозовский парк культуры и отдыха»;Северо-Восточный административный округ;район Лианозово;Угличская улица, дом 13
...

Напишите программу, создающую JSON-объект, ключом в котором является административный округ, 
а значением — JSON-объект, в котором, в свою очередь, ключом является название района, 
относящийся к этому административному округу, а значением — список адресов всех 
площадок в этом районе. Полученный JSON-объект программа должна записать в файл addresses.json.

Примечание 1. Адреса в списках должны располагаться в своем исходном порядке.

Примечание 2. Разделителем в файле playgrounds.csv является точка с запятой, 
при этом кавычки не используются.

Примечание 3. Начальная часть файла addresses.json выглядит так:

{
   "Северо-Восточный административный округ": {
      "район Лианозово": [
         "Угличская улица, дом 13",
         "Алтуфьевское шоссе, дом 147А"
      ],
      "район Отрадное": [
         "Алтуфьевское шоссе, дом 20А",
         "Юрловский проезд, дом 8, строение 1",
         "Юрловский проезд, дом 8, строение 1"
      ],
      ...
   },
   ...
}

Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/playgrounds.csv
https://stepik.org/media/attachments/lesson/623073/clue_playgrounds.txt

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''
import json, csv

# with open(file='033-playgrounds.csv', mode='rt', encoding='utf-8', newline='') as file_opener,\
with open(file='playgrounds.csv', mode='rt', encoding='utf-8', newline='') as file_opener,\
    open(file='addresses.json', mode='wt', encoding='utf-8', newline='') as file_writener:

    playgrounds_list_dicts = csv.DictReader(file_opener, delimiter=';', quoting=csv.QUOTE_NONE)
    fieldnames = playgrounds_list_dicts.fieldnames

    addresses_dict = dict()
    for d in playgrounds_list_dicts:
        addresses_dict.setdefault(
            d[fieldnames[1]], {}
            ).setdefault(
                d[fieldnames[2]] ,[]
                ).append(d[fieldnames[3]])

    # json.dump(addresses_dict, file_writener, indent=4, ensure_ascii=False)
    json.dump(addresses_dict, file_writener, indent=4, ensure_ascii=True)
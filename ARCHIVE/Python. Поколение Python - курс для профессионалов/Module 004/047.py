'''
Шахматы были лучше 🌶️
Вам доступен архив data.zip, содержащий различные папки и файлы. 
Среди них есть несколько JSON файлов, каждый из которых содержит 
информацию о каком-либо футболисте:

{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}

У футболиста имеются следующие атрибуты: 

first_name — имя
last_name — фамилия
team — название футбольного клуба
position — игровая позиция

Напишите программу, которая обрабатывает только данные JSON файлы 
и выводит имена и фамилии футболистов, выступающих за футбольный клуб Arsenal. 
Футболисты должны быть расположены в лексикографическом порядке имен, 
а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.

Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, 
что он является корректным текстовым файлом в формате JSON. Для того чтобы определить, 
является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь 
конструкцией try-except и функцией is_correct_json() из предыдущего урока.
https://stepik.org/lesson/623073/step/5?unit=618703

Примечание 2. Начальная часть ответа выглядит так:

Alex Iwobi
Alexis Sanchez
...

Примечание 3. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/data.zip
https://stepik.org/media/attachments/lesson/547172/clue_json.txt
'''
from zipfile import ZipFile
import json
from os import remove, rmdir
from os.path import basename, dirname, exists, getsize
from shutil import rmtree
from operator import itemgetter

# with ZipFile(file='047-data.zip', mode='r') as zip_opener:
with ZipFile(file='data.zip', mode='r') as zip_opener:
    files_list_zip = zip_opener.infolist()
    list_dicts = list()
    dir_lists = list()
    # zip_opener.printdir() # test

    for file in files_list_zip:
        if file.is_dir():
            dir_lists.append(file.filename)
        else:
            try:
                if file.filename.endswith('.json'):
                    filename_in_zip = file.filename
                    filename = basename(file.filename)
                    zip_opener.extract(filename_in_zip, dirname(__file__))             

                    with zip_opener.open(name=filename_in_zip, mode='r') as zip_file,\
                        open(file=filename, mode='wb') as json_file:
                        json_file.write(zip_file.read())
                        json_file.close()

                        with open(file=filename, mode='rt', encoding='utf-8', newline='') as file_opener:
                            try:
                                json_dict = json.load(fp=file_opener)
                            except UnicodeDecodeError:
                                pass

                        list_dicts.append(json_dict)                   
                        if exists(filename):
                            remove(filename)
                        if exists(filename_in_zip):
                            remove(filename_in_zip)
            except json.decoder.JSONDecodeError:
                pass

    # [print(dir) for dir in dir_lists] # test
    for dir in dir_lists:
        if exists(dir):
            if getsize(dir):
                rmtree(dir)
            else:
                rmdir(dir)
            

    # [print(l) for l in list_dicts] # test
    [print(d['first_name'], d['last_name']) for d in list(
        filter(
            lambda x: 'Arsenal' == x['team'],
            sorted(
                list_dicts,
                key=itemgetter('first_name', 'last_name') # or
                # key=lambda x: (x['first_name'], x['last_name']) # or
            )
        )
    )]
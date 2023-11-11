'''
Избранные
Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит названия файлов из этого архива, 
которые были созданы или изменены позднее 2021-11-30 14:22:00. 
Названия файлов должны быть расположены в лексикографическом порядке, 
каждое на отдельной строке.

Примечание 1. Если файл находится в папке, вывести следует 
только название без пути.

Примечание 2. Начальная часть ответа выглядит так:

countries.json
data_sample.csv
...

Примечание 3. Указанный архив доступен по ссылке. 
Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/workbook.zip
https://stepik.org/media/attachments/lesson/547172/clue_dragonborn.txt
'''
from zipfile import ZipFile
from datetime import datetime

pattern = '%Y-%m-%d %H:%M:%S'
dale_later = datetime.strptime('2021-11-30 14:22:00', pattern)

# with ZipFile(file='042-workbook.zip', mode='r') as zip_opener:
with ZipFile(file='workbook.zip', mode='r') as zip_opener:
    files_zip = zip_opener

    print(
        *sorted(
            map(
                # lambda x: x.filename.split('/')[-1] if x.filename.split('/')[-1] else x.filename.split('/')[-2],
                lambda x: x.filename.split('/')[-1],
                filter(
                    lambda x: datetime(*x.date_time) > dale_later and not x.is_dir(),
                    files_zip.infolist()
                )
            )
        ),
        sep='\n'
    )
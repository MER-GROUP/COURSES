'''
Структура архива 🌶️🌶️
Вам доступен архив desktop.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит его файловую структуру и объем каждого файла.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести файловую структуру архива desktop.zip 
и объем каждого файла в несжатом виде. Так как архив имеет собственную иерархию папок, 
каждый уровень вложенности должен быть выделен двумя пробелами.

Примечание 1. Вывод на примере архива test.zip из конспекта:
https://stepik.org/media/attachments/lesson/547172/test.zip

test
  Картинки
    1.jpg 88 KB
    avatar.png 19 KB
    certificate.png 43 KB
    py.png 33 KB
    World_Time_Zones_Map.png 2 MB
    Снимок экрана.png 11 KB
  Неравенства.djvu 5 MB
  Программы
    image_util.py 5 KB
    sort.py 61 B
  Разные файлы
    astros.json 505 B

Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.

Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB

Примечание 4. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/desktop.zip
https://stepik.org/media/attachments/lesson/547172/clue_archive_structure.txt
'''
from zipfile import ZipFile
from sys import platform

separator = '\\' if 'win32' == platform else '/'

def convert(n: int):
    unit = ['B', 'KB', 'MB', 'GB']
    step = 0
    while 1024 < n:
        n /= 1024
        step += 1
    return round(n), unit[step]

# with ZipFile(file='048-test.zip', mode='r') as zip_opener:
# with ZipFile(file='048-desktop.zip', mode='r') as zip_opener:
with ZipFile(file='desktop.zip', mode='r') as zip_opener:
    file_in_zip = zip_opener.infolist()

    for file in file_in_zip:
        filename = file.filename
        filename_len = len(filename.split(separator)) if not file.is_dir() else len(filename.split(separator))-1
        
        if 1 == filename_len and file.is_dir():
            print(filename[:-1], *convert(file.file_size) if not file.is_dir() else '')
        else:
            s = str()
            for i in range(filename_len - 1):
                s += '  '
            filename = s + filename.split(separator)[-2 if file.is_dir() else -1]
            print(filename, *convert(file.file_size) if not file.is_dir() else '')
'''
File names 2

Вам доступен набор различных файлов, названия которых представлены в списке file_names. 
Также вам доступен архив files.zip. Дополните приведенный ниже код, чтобы он добавил 
в архив files.zip только те файлы из списка file_names, объем которых не превышает 100 байт.

Примечание 1. Получить объем файла в байтах позволяет функция getsize() из модуля os.path. 
Данная функция принимает в качестве аргумента путь к файлу и возвращает 
размер указанного файла в байтах.

Например, вычислить объем архива files.zip в байтах и сохранить его в переменную size 
можно следующим образом:

import os.path

size = os.path.getsize('files.zip')

Примечание 2. Вычислить объем файла в байтах можно и вручную, не прибегая к 
использованию сторонних модулей. Подумайте, как 😉.
(Ответ: открываете файл в бинарном виде и считаете байты)

Примечание 3. Считайте, что файлы из списка file_names и архив files.zip 
находятся в папке с программой.

from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
'''
from zipfile import ZipFile
# from os.path import getsize

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

# with ZipFile(file='files.zip', mode='a') as zip_appender:
#     for file in file_names:
#         if 100 >= getsize(file):
#             zip_appender.write(file)

with ZipFile(file='files.zip', mode='a') as zip_appender:
    for file in file_names:
        with open(file=file, mode='rb') as file_opener:
            file_size = len(file_opener.read())
        if 100 >= file_size:
            zip_appender.write(file)
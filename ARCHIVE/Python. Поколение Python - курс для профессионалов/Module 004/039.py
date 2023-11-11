'''
Количество файлов
Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит единственное число — количество 
файлов в этом архиве.

Примечание 1. Обратите внимание, что папка не считается файлом.

Примечание 2. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/workbook.zip
https://stepik.org/media/attachments/lesson/547172/clue_files_num.txt
'''
from zipfile import ZipFile

# with ZipFile(file='039-workbook.zip', mode='r') as zip_opener:
with ZipFile(file='workbook.zip', mode='r') as zip_opener:
    # file_list = zip_opener.filelist # or
    file_list = zip_opener.infolist() # or
    # print(file_list) # test
    # print(len(file_list)) # test
    # print(zip_opener.printdir()) # test

    count_n = sum(
        map(
            lambda x: not x.is_dir(),
            file_list
        )
    )
    print(count_n)
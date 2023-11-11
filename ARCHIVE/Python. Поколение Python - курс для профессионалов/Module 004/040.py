'''
Объем файлов
Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит суммарный объем файлов 
этого архива в сжатом и не сжатом видах в байтах, в следующем формате:

Объем исходных файлов: <объем до сжатия> байт(а)
Объем сжатых файлов: <объем после сжатия> байт(а)

Примечание 1. Вывод на примере архива test.zip из конспекта:

Объем исходных файлов: 7810260 байт(а)
Объем сжатых файлов: 7798267 байт(а)

Примечание 2. Указанный архив доступен по ссылке. 
Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/workbook.zip
https://stepik.org/media/attachments/lesson/547172/clue_volumes.txt
'''
from zipfile import ZipFile

# with ZipFile(file='040-workbook.zip', mode='r') as zip_opener:
with ZipFile(file='workbook.zip', mode='r') as zip_opener:
    files = zip_opener.infolist()
    size, size_zip = 0, 0
    
    for file in files:
        if not file.is_dir():
            size += file.file_size
            size_zip += file.compress_size

    print(f'Объем исходных файлов: {size} байт(а)')
    print(f'Объем сжатых файлов: {size_zip} байт(а)')
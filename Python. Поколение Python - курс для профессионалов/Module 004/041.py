'''
Наилучший показатель
Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит название файла из этого архива, 
который имеет наилучший показатель степени сжатия.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Гарантируется, что в исходном архиве только один файл 
имеет наилучший показатель степени сжатия.

Примечание 3. Степень сжатия файла характеризуется коэффициентом K, 
определяемым как отношение объема сжатого файла V_c к объему исходного файла V_o, 
выраженным в процентах:

K = (V_c / V_o) * 100%

Примечание 4. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/workbook.zip
https://stepik.org/media/attachments/lesson/547172/clue_coef.txt
'''
from zipfile import ZipFile
from operator import attrgetter, itemgetter

# with ZipFile(file='041-workbook.zip', mode='r') as zip_opener:
with ZipFile(file='workbook.zip', mode='r') as zip_opener:
    files = zip_opener.infolist()
    dictonary = dict()

    for file in files:
        # print(attrgetter('filename' ,'file_size', 'compress_size')(file))
        # print(*map(attrgetter('file_size', 'compress_size'), [file]))
        # print(file.file_size, file.compress_size)
        tup = attrgetter('filename' ,'file_size', 'compress_size')(file)
        key = tup[0].split('/')[-1] if tup[0].split('/')[-1] else tup[0].split('/')[-2]
        # print(key) # test
        if not file.is_dir():
            dictonary[key] = dictonary.get(key, 0) + (tup[2] / tup[1]) * 100
    # print(dictonary) # test

    print(
        min(
            dictonary,
            key=dictonary.get
        )
    )

    # print(
    #     min(
    #         dictonary.items(),
    #         key=itemgetter(1)
    #     )
    # )
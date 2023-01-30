'''
File names

Вам доступен набор различных файлов, названия которых представлены в списке file_names. 
Дополните приведенный ниже код, чтобы он создал архив files.zip и 
добавил в него все файлы из данного списка.

Примечание. Считайте, что файлы из списка file_names находятся в папке с программой.

from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']
'''
from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']

# with ZipFile(file='044-files.zip', mode='w') as zip_writener:
with ZipFile(file='files.zip', mode='w') as zip_writener:
    for file in file_names:
        zip_writener.write(file)